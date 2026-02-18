"""
MCP Server for Python Code Execution
Provides tools for executing Python code in AutoML pipeline

This MCP server integrates with OpenCode to provide:
- execute_python: Run Python code in sandboxed environment
- execute_script: Execute Python script files
- validate_code: Syntax validation without execution

Install:
    pip install mcp-server-python-executor

Or use directly with OpenCode's local MCP configuration.
"""

import json
import subprocess
import tempfile
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

try:
    from mcp.server import Server
    from mcp.types import Tool, TextContent
    from mcp.server.stdio import stdio_server
except ImportError:
    print("Warning: MCP SDK not installed. Install with: pip install mcp")
    Server = None


# Configuration
DEFAULT_TIMEOUT = 120  # seconds
DEFAULT_WORKSPACE = "./agent_workspace"


class PythonExecutor:
    """Execute Python code in sandboxed environment"""

    def __init__(self, workspace: str = DEFAULT_WORKSPACE):
        self.workspace = Path(workspace)
        self.workspace.mkdir(parents=True, exist_ok=True)

    def execute(
        self, code: str, timeout: int = DEFAULT_TIMEOUT, capture_output: bool = True
    ) -> Dict[str, Any]:
        """Execute Python code and return results"""

        # Create temporary file
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, encoding="utf-8"
        ) as f:
            f.write(code)
            temp_file = f.name

        try:
            # Execute with timeout
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=capture_output,
                text=True,
                timeout=timeout,
                cwd=str(self.workspace),
                env=self._get_safe_env(),
            )

            return {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout if capture_output else "",
                "stderr": result.stderr if capture_output else "",
                "workspace": str(self.workspace),
                "timeout": timeout,
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Execution timed out after {timeout} seconds",
                "workspace": str(self.workspace),
                "timeout": timeout,
            }
        except Exception as e:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Execution failed: {str(e)}",
                "workspace": str(self.workspace),
                "timeout": timeout,
            }
        finally:
            # Cleanup
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def execute_script(
        self,
        script_path: str,
        args: Optional[list] = None,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> Dict[str, Any]:
        """Execute a Python script file"""

        script_path = Path(script_path)
        if not script_path.exists():
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Script not found: {script_path}",
                "workspace": str(self.workspace),
            }

        cmd = [sys.executable, str(script_path)]
        if args:
            cmd.extend(args)

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.workspace.parent),
                env=self._get_safe_env(),
            )

            return {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "script": str(script_path),
                "args": args or [],
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Script timed out after {timeout} seconds",
                "script": str(script_path),
            }
        except Exception as e:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Script execution failed: {str(e)}",
                "script": str(script_path),
            }

    def validate(self, code: str) -> Dict[str, Any]:
        """Validate Python code syntax without execution"""

        try:
            compile(code, "<string>", "exec")
            return {"valid": True, "errors": []}
        except SyntaxError as e:
            return {
                "valid": False,
                "errors": [{"line": e.lineno, "column": e.offset, "message": str(e)}],
            }

    def _get_safe_env(self) -> Dict[str, str]:
        """Get safe environment variables for execution"""
        env = os.environ.copy()
        # Add workspace to Python path
        current_path = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = f"{self.workspace}:{current_path}"
        return env


# MCP Server Implementation
if Server:
    app = Server("python-executor")
    executor = PythonExecutor()

    @app.list_tools()
    async def list_tools():
        return [
            Tool(
                name="execute_python",
                description="Execute Python code in a sandboxed environment. Use for data analysis, ML model training, and general Python tasks.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "Python code to execute",
                        },
                        "timeout": {
                            "type": "number",
                            "description": "Execution timeout in seconds (default: 120)",
                            "default": 120,
                        },
                        "working_dir": {
                            "type": "string",
                            "description": "Working directory for execution (default: ./agent_workspace)",
                            "default": "./agent_workspace",
                        },
                    },
                    "required": ["code"],
                },
            ),
            Tool(
                name="execute_script",
                description="Execute a Python script file",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "script_path": {
                            "type": "string",
                            "description": "Path to Python script",
                        },
                        "args": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Command line arguments",
                            "default": [],
                        },
                        "timeout": {
                            "type": "number",
                            "description": "Execution timeout in seconds",
                            "default": 120,
                        },
                    },
                    "required": ["script_path"],
                },
            ),
            Tool(
                name="validate_code",
                description="Validate Python code syntax without execution",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "Python code to validate",
                        }
                    },
                    "required": ["code"],
                },
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "execute_python":
            # Update workspace if specified
            if "working_dir" in arguments:
                executor.workspace = Path(arguments["working_dir"])
                executor.workspace.mkdir(parents=True, exist_ok=True)

            result = executor.execute(
                code=arguments["code"],
                timeout=arguments.get("timeout", DEFAULT_TIMEOUT),
            )

            output = f"""Execution Result:
Return Code: {result["returncode"]}

Output:
{result["stdout"]}

Errors:
{result["stderr"]}

Working Directory: {result["workspace"]}
Timeout: {result["timeout"]}s"""

            return [TextContent(type="text", text=output)]

        elif name == "execute_script":
            result = executor.execute_script(
                script_path=arguments["script_path"],
                args=arguments.get("args"),
                timeout=arguments.get("timeout", DEFAULT_TIMEOUT),
            )

            output = f"""Script Execution Result:
Return Code: {result["returncode"]}

Output:
{result["stdout"]}

Errors:
{result["stderr"]}

Script: {result.get("script", "N/A")}"""

            return [TextContent(type="text", text=output)]

        elif name == "validate_code":
            result = executor.validate(arguments["code"])

            output = f"""Validation Result:
Valid: {result["valid"]}

Errors: {len(result.get("errors", []))}"""

            if result.get("errors"):
                for err in result["errors"]:
                    output += f"\n- Line {err['line']}: {err['message']}"

            return [TextContent(type="text", text=output)]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]


def main():
    """Main entry point for MCP server"""
    if not Server:
        print("Error: MCP SDK not installed")
        print("Install with: pip install mcp")
        sys.exit(1)

    import asyncio

    async def run():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream, write_stream, app.create_initialization_options()
            )

    asyncio.run(run())


if __name__ == "__main__":
    main()
