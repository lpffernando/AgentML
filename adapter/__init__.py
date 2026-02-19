"""
agentML Adapter Package

This package provides integration between agentML (OpenCode-based AutoML)
and the optional legacy core components.

Usage:
    from adapter import OpenCodeAgentAdapter, create_adapter
    from adapter.agent_wrapper import train_model, clean_data
"""

from .agent_wrapper import (
    OpenCodeAgentAdapter,
    PipelineConfig,
    PipelineResult,
    TaskType,
    create_adapter,
    clean_data,
    train_model,
)

__version__ = "0.1.0"

__all__ = [
    "OpenCodeAgentAdapter",
    "PipelineConfig",
    "PipelineResult",
    "TaskType",
    "create_adapter",
    "clean_data",
    "train_model",
]
