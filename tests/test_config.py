"""
Tests for OpenCode Agent configurations
"""

import pytest
import json
import yaml
from pathlib import Path


class TestOpenCodeConfig:
    """Test opencode.json configuration"""

    @pytest.fixture
    def config_path(self):
        return Path(__file__).parent.parent / ".opencode" / "opencode.json"

    def test_config_exists(self, config_path):
        assert config_path.exists(), "opencode.json should exist"

    def test_config_valid_json(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        assert config is not None

    def test_config_has_schema(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        assert "$schema" in config
        assert "opencode.ai/config.json" in config["$schema"]

    def test_config_has_agents(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        assert "agent" in config
        assert "automl-coordinator" in config["agent"]

    def test_coordinator_is_primary(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        coordinator = config["agent"]["automl-coordinator"]
        assert coordinator["mode"] == "primary"

    def test_subagents_correct_mode(self, config_path):
        with open(config_path) as f:
            config = json.load(f)

        subagents = [
            "data-processor",
            "feature-engineer",
            "model-selector",
            "model-validator",
            "explainability",
        ]

        for agent_name in subagents:
            assert agent_name in config["agent"]
            assert config["agent"][agent_name]["mode"] == "subagent"

    def test_all_agents_have_description(self, config_path):
        with open(config_path) as f:
            config = json.load(f)

        for agent_name, agent_config in config["agent"].items():
            assert "description" in agent_config, f"{agent_name} missing description"
            assert len(agent_config["description"]) > 0

    def test_all_agents_have_model(self, config_path):
        with open(config_path) as f:
            config = json.load(f)

        for agent_name, agent_config in config["agent"].items():
            assert "model" in agent_config, f"{agent_name} missing model"

    def test_mcp_configured(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        assert "mcp" in config
        assert "python-executor" in config["mcp"]


class TestAgentDefinitionFiles:
    """Test agent definition markdown files"""

    @pytest.fixture
    def agents_dir(self):
        return Path(__file__).parent.parent / ".opencode" / "agents"

    def test_agents_directory_exists(self, agents_dir):
        assert agents_dir.exists(), "agents directory should exist"

    def test_all_agents_exist(self, agents_dir):
        expected_agents = [
            "automl-coordinator.md",
            "data-processor.md",
            "feature-engineer.md",
            "model-selector.md",
            "model-validator.md",
            "explainability.md",
        ]

        for agent_file in expected_agents:
            agent_path = agents_dir / agent_file
            assert agent_path.exists(), f"{agent_file} should exist"

    def test_coordinator_has_correct_frontmatter(self, agents_dir):
        agent_path = agents_dir / "automl-coordinator.md"
        content = agent_path.read_text()

        assert "---" in content
        assert "name:" in content
        assert "mode:" in content

    def test_coordinator_is_primary_mode(self, agents_dir):
        agent_path = agents_dir / "automl-coordinator.md"
        content = agent_path.read_text()

        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.strip() == "mode: primary":
                break
        else:
            pytest.fail("Coordinator should have mode: primary")

    def test_subagents_have_subagent_mode(self, agents_dir):
        subagent_files = [
            "data-processor.md",
            "feature-engineer.md",
            "model-selector.md",
            "model-validator.md",
            "explainability.md",
        ]

        for agent_file in subagent_files:
            agent_path = agents_dir / agent_file
            content = agent_path.read_text()
            assert "mode: subagent" in content, (
                f"{agent_file} should have mode: subagent"
            )


class TestSkillsDirectory:
    """Test skills directory structure"""

    @pytest.fixture
    def skills_dir(self):
        return Path(__file__).parent.parent / ".opencode" / "skills"

    def test_skills_directory_exists(self, skills_dir):
        assert skills_dir.exists(), "skills directory should exist"

    def test_all_skills_exist(self, skills_dir):
        expected_skills = [
            "data-cleaning",
            "feature-engineering",
            "model-training",
            "model-validation",
            "shap-analysis",
        ]

        for skill_name in expected_skills:
            skill_dir = skills_dir / skill_name
            assert skill_dir.exists(), f"{skill_name} directory should exist"

            skill_file = skill_dir / "SKILL.md"
            assert skill_file.exists(), f"{skill_name}/SKILL.md should exist"


class TestSkillFiles:
    """Test individual SKILL.md files"""

    @pytest.fixture
    def skills_dir(self):
        return Path(__file__).parent.parent / ".opencode" / "skills"

    def test_skill_has_frontmatter(self, skills_dir):
        skill_file = skills_dir / "data-cleaning" / "SKILL.md"
        content = skill_file.read_text()

        assert content.startswith("---")
        assert "name:" in content
        assert "description:" in content

    def test_skill_has_name(self, skills_dir):
        skill_file = skills_dir / "data-cleaning" / "SKILL.md"
        content = skill_file.read_text()

        assert "name: data-cleaning" in content

    def test_skill_has_capabilities(self, skills_dir):
        skill_file = skills_dir / "data-cleaning" / "SKILL.md"
        content = skill_file.read_text()

        assert "## What I Do" in content or "## Capabilities" in content

    def test_skill_has_examples(self, skills_dir):
        skill_file = skills_dir / "data-cleaning" / "SKILL.md"
        content = skill_file.read_text()

        assert "## Example" in content or "example" in content.lower()

    def test_all_skills_valid(self, skills_dir):
        skill_names = [
            "data-cleaning",
            "feature-engineering",
            "model-training",
            "model-validation",
            "shap-analysis",
        ]

        for skill_name in skill_names:
            skill_file = skills_dir / skill_name / "SKILL.md"
            content = skill_file.read_text()

            # Check basic structure
            assert content.startswith("---"), (
                f"{skill_name}: should start with frontmatter"
            )
            assert content.count("---") >= 2, (
                f"{skill_name}: should have opening and closing ---"
            )
            assert "name:" in content, f"{skill_name}: should have name"
            assert "description:" in content, f"{skill_name}: should have description"


class TestAGENTSFile:
    """Test AGENTS.md project file"""

    @pytest.fixture
    def agents_md_path(self):
        return Path(__file__).parent.parent / "AGENTS.md"

    def test_agents_md_exists(self, agents_md_path):
        assert agents_md_path.exists(), "AGENTS.md should exist"

    def test_agents_md_has_content(self, agents_md_path):
        content = agents_md_path.read_text()
        assert len(content) > 100, "AGENTS.md should have substantial content"

    def test_agents_md_mentions_agents(self, agents_md_path):
        content = agents_md_path.read_text()

        assert "Coordinator" in content or "coordinator" in content
        assert "Agent" in content
