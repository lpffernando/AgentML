# agentML Project

## Project Overview

This is an agentML (Automated Machine Learning) project built on OpenCode platform. The system uses a multi-agent architecture to coordinate data processing, feature engineering, model selection, and validation.

## Supported ML Tasks

- **Image Classification** - CNN-based models for image recognition
- **Text Classification** - NLP models for text categorization
- **Tabular Classification** - Classification for tabular data (binary/multiclass)
- **Tabular Regression** - Regression for tabular data
- **Tabular Clustering** - Unsupervised clustering for tabular data
- **Node Classification** - Graph neural networks for node classification
- **Time-Series Forecasting** - Time series prediction

## Agent Architecture

The project uses a multi-agent system:

1. **Coordinator** - Orchestrates the entire pipeline
2. **Data Processor / EDA** - EDA and data preprocessing
3. **Feature Engineer** - Feature selection and construction
4. **Model Selector** - Model selection and hyperparameter tuning
5. **Model Validator** - Cross-validation and evaluation
6. **Explainability** - SHAP analysis and model interpretation
7. **Viz Agent** - Visualization and charting

## Code Conventions

- Python 3.10+
- Use pandas for data manipulation
- Use scikit-learn, XGBoost, LightGBM for ML models
- Use SHAP for model explanation
- Follow PEP 8 style guide
- Use type hints where appropriate

## Key Directories

- `.opencode/agents/` - Agent definitions (7 agents)
- `.opencode/skills/` - Standardized skills (8 skills)
- `adapter/` - Agent wrapper utilities
- `mcp_servers/` - MCP tool implementations
- `tests/` - Test cases

## Usage

When working on ML pipeline tasks:

1. First understand the data and requirements
2. Use subagents (@data-processor/@eda, @feature-engineer, etc.) for specialized tasks
3. Use skills via `skill` tool (e.g., `skill(name="eda")`, `skill(name="data-visualization")`)
4. Follow the pipeline: data → features → model → validation → explanation
5. Generate comprehensive reports with metrics and visualizations

## Environment

Required packages are listed in `requirements-opencode.txt`. Key dependencies:
- langchain, langchain_community
- scikit-learn, xgboost, lightgbm, catboost
- shap, mlflow
- pandas, numpy, matplotlib
