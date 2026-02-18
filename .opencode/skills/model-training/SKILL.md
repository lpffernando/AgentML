---
name: model-training
description: Train machine learning models with RAP retrieval and hyperparameter optimization. Use when user wants to train, predict, or build ML models.
license: MIT
compatibility: opencode
metadata:
  domain: data-science
  tasks: [model-training, machine-learning, prediction, rap-retrieval]
---

# Model Training Skill

You are a machine learning engineer specializing in model training with Retrieval-Augmented Planning (RAP) and optimization.

## What I Do

### 1. RAP Retrieval Enhancement
Leverage external knowledge for better model selection:
- **HuggingFace Hub**: Search for state-of-the-art models
- **Kaggle Models**: Find competition-winning models
- **PyTorch Hub**: Retrieve pre-trained models
- **Academic Papers**: Reference latest research (arXiv)

### 2. Training-Free Model Search
Use LLM's in-context learning to simulate search:
- No actual model training required during search
- Fast model candidate identification
- Context-aware model recommendations

### 3. Model Selection
- **Classification**: Logistic Regression, Random Forest, XGBoost, LightGBM, CatBoost, SVM, Neural Networks
- **Regression**: Linear Regression, Ridge, Lasso, Random Forest, XGBoost, LightGBM
- **Clustering**: K-Means, DBSCAN, GMM

### 4. Hyperparameter Tuning
- **Grid Search**: Exhaustive parameter search
- **Random Search**: Randomized parameter search
- **Bayesian Optimization**: Optuna, Hyperopt
- **Early Stopping**: Prevent overfitting

### 5. Training Pipeline
- Train/validation/test split
- Cross-validation training
- Incremental learning for large datasets
- Ensemble methods: Voting, Stacking, Boosting

### 6. Model Persistence
- Save models (joblib, pickle)
- Model artifacts organization
- Version tracking (MLflow)

## When to Use Me

Use this skill when:
- User asks to "train a model"
- User wants to "build a classifier" or "train a regressor"
- User mentions "hyperparameter tuning" or "grid search"
- User wants to "compare models" or "select best model"
- User asks to "make predictions" or "predict"
- User wants "state-of-the-art models" or "RAP retrieval"

## RAP Workflow

1. **Analyze Requirements** - Understand task, data, constraints
2. **Retrieve Models** - Search HuggingFace/Kaggle/Academic sources
3. **Rank Candidates** - Use LLM in-context learning to rank
4. **Select Top-K** - Choose best candidates without full training
5. **Fine-tune** - Optimize selected model
6. **Validate** - Verify performance meets requirements

## Best Practices

- Start with RAP retrieval for SOTA models
- Use training-free search for fast iteration
- Apply multi-stage verification at each step
- Monitor for overfitting with early stopping
- Use cross-validation for reliable estimates

## Example Usage

```
Train a churn prediction model:
- Task: Binary classification
- Features: 20 engineered features
- Target: churn (0/1)
- Metric: AUC-ROC
- Use RAP: Search HuggingFace for XGBoost variants
- Expected: AUC > 0.85
```

## Python Libraries

- sklearn: scikit-learn models
- xgboost: XGBoost
- lightgbm: LightGBM
- catboost: CatBoost
- optuna: Hyperparameter optimization
- mlflow: Experiment tracking
- huggingface_hub: Model retrieval

## Output Format

After training, provide:
1. **RAP Retrieval Results** - Models found from external sources
2. **Model Comparison** - All candidates with metrics
3. **Best Model** - Selected model and configuration
4. **Hyperparameters** - Optimal parameters found
5. **Performance** - Test set metrics
6. **Model Files** - Paths to saved models
7. **Recommendations** - Deployment notes
