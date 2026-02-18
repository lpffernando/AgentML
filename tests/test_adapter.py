"""
Unit tests for OpenCodeAgentAdapter
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock


class TestPipelineConfig:
    """Test PipelineConfig dataclass"""

    def test_default_config(self):
        from adapter.agent_wrapper import PipelineConfig

        config = PipelineConfig()

        assert config.task == "classification"
        assert config.metric == "auto"
        assert config.time_budget == 3600
        assert config.cv_folds == 5

    def test_custom_config(self):
        from adapter.agent_wrapper import PipelineConfig

        config = PipelineConfig(
            task="regression", metric="rmse", time_budget=1800, cv_folds=3
        )

        assert config.task == "regression"
        assert config.metric == "rmse"
        assert config.time_budget == 1800
        assert config.cv_folds == 3


class TestTaskType:
    """Test TaskType enum"""

    def test_task_types_exist(self):
        from adapter.agent_wrapper import TaskType

        assert TaskType.BINARY_CLASSIFICATION.value == "binary_classification"
        assert TaskType.REGRESSION.value == "regression"
        assert TaskType.CLUSTERING.value == "clustering"


class TestOpenCodeAgentAdapter:
    """Test OpenCodeAgentAdapter class"""

    @pytest.fixture
    def temp_workspace(self):
        """Create temporary workspace"""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir, ignore_errors=True)

    def test_adapter_initialization(self, temp_workspace):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter(
            agent_type="coordinator", llm="gpt-4", workspace=temp_workspace
        )

        assert adapter.agent_type == "coordinator"
        assert adapter.llm == "gpt-4"
        assert adapter.workspace == Path(temp_workspace)

    def test_adapter_with_config(self, temp_workspace):
        from adapter.agent_wrapper import OpenCodeAgentAdapter, PipelineConfig

        config = PipelineConfig(task="regression", cv_folds=10)

        adapter = OpenCodeAgentAdapter(
            agent_type="model-selector", workspace=temp_workspace, config=config
        )

        assert adapter.config.task == "regression"
        assert adapter.config.cv_folds == 10

    def test_get_status(self, temp_workspace):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter(
            agent_type="coordinator", workspace=temp_workspace
        )

        status = adapter.get_status()

        assert "agent_type" in status
        assert "llm" in status
        assert "workspace" in status
        assert "config" in status
        assert "components" in status

    def test_infer_task_type_churn(self):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter()

        task = adapter._infer_task_type("Predict customer churn")
        assert task == "binary_classification"

    def test_infer_task_type_regression(self):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter()

        task = adapter._infer_task_type("Predict house prices")
        assert task == "regression"

    def test_infer_task_type_clustering(self):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter()

        task = adapter._infer_task_type("Cluster customers by behavior")
        assert task == "clustering"

    def test_infer_task_type_forecast(self):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter()

        task = adapter._infer_task_type("Forecast quarterly sales")
        assert task == "time_series_forecasting"

    def test_infer_task_type_default(self):
        from adapter.agent_wrapper import OpenCodeAgentAdapter

        adapter = OpenCodeAgentAdapter()

        task = adapter._infer_task_type("Build a model")
        assert task == "classification"


class TestPipelineResult:
    """Test PipelineResult dataclass"""

    def test_default_result(self):
        from adapter.agent_wrapper import PipelineResult

        result = PipelineResult(status="initiated")

        assert result.status == "initiated"
        assert result.steps == []
        assert result.best_model is None
        assert result.metrics == {}
        assert result.artifacts == {}
        assert result.errors == []

    def test_result_with_data(self):
        from adapter.agent_wrapper import PipelineResult

        result = PipelineResult(
            status="completed",
            best_model={"name": "XGBoost", "score": 0.9},
            metrics={"accuracy": 0.89, "f1": 0.87},
        )

        assert result.status == "completed"
        assert result.best_model["name"] == "XGBoost"
        assert result.metrics["accuracy"] == 0.89


class TestCreateAdapter:
    """Test create_adapter factory function"""

    def test_create_adapter_default(self):
        from adapter.agent_wrapper import create_adapter

        adapter = create_adapter("coordinator")

        assert adapter.agent_type == "coordinator"

    def test_create_adapter_with_kwargs(self):
        from adapter.agent_wrapper import create_adapter

        adapter = create_adapter(
            "data-processor", llm="claude-3", workspace="/tmp/test"
        )

        assert adapter.agent_type == "data-processor"
        assert adapter.llm == "claude-3"


class TestConvenienceFunctions:
    """Test convenience functions"""

    @patch("adapter.agent_wrapper.OpenCodeAgentAdapter")
    def test_clean_data(self, mock_adapter_class):
        from adapter.agent_wrapper import clean_data

        mock_adapter = MagicMock()
        mock_adapter.execute_full_pipeline.return_value = MagicMock(status="completed")
        mock_adapter_class.return_value = mock_adapter

        result = clean_data("data/test.csv")

        mock_adapter.execute_full_pipeline.assert_called_once()

    @patch("adapter.agent_wrapper.OpenCodeAgentAdapter")
    def test_train_model(self, mock_adapter_class):
        from adapter.agent_wrapper import train_model

        mock_adapter = MagicMock()
        mock_adapter.execute_full_pipeline.return_value = MagicMock(status="completed")
        mock_adapter_class.return_value = mock_adapter

        result = train_model("data/train.csv", "target")

        mock_adapter.execute_full_pipeline.assert_called_once()
