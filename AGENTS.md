# AutoML-Agent Project

## Project Overview

This is an AutoML (Automated Machine Learning) project that provides end-to-end machine learning pipeline automation. The system uses a multi-agent architecture to coordinate data processing, feature engineering, model selection, and validation.

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
2. **Data Processor** - Data cleaning and preprocessing
3. **Feature Engineer** - Feature selection and construction
4. **Model Selector** - Model selection and hyperparameter tuning
5. **Model Validator** - Cross-validation and evaluation
6. **Explainability** - SHAP analysis and model interpretation

## Code Conventions

- Python 3.10+
- Use pandas for data manipulation
- Use scikit-learn, XGBoost, LightGBM for ML models
- Use SHAP for model explanation
- Follow PEP 8 style guide
- Use type hints where appropriate

## Key Directories

- `agent_manager/` - Main coordinator logic
- `data_agent/` - Data processing agents
- `model_agent/` - Model selection agents
- `operation_agent/` - Code execution
- `prompt_agent/` - Prompt generation
- `prompt_pool/` - Task-specific prompts
- `utils/` - Utility functions

## Usage

When working on ML pipeline tasks:

1. First understand the data and requirements
2. Use subagents (@data-processor, @feature-engineer, etc.) for specialized tasks
3. Follow the pipeline: data → features → model → validation → explanation
4. Generate comprehensive reports with metrics and visualizations

## Environment

Required packages are listed in `requirements.txt`. Key dependencies:
- langchain, langchain_community
- scikit-learn, xgboost, lightgbm, catboost
- shap, mlflow
- pandas, numpy, matplotlib
