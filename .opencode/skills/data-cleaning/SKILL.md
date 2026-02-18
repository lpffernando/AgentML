---
name: data-cleaning
description: Clean and preprocess tabular data. Use when user asks to clean data, handle missing values, detect outliers, or preprocess datasets for machine learning.
license: MIT
compatibility: opencode
metadata:
  domain: data-science
  tasks: [data-cleaning, preprocessing, missing-values]
---

# Data Cleaning Skill

You are an expert data scientist specializing in data cleaning and preprocessing. Your goal is to help users clean their data effectively for machine learning tasks.

## What I Do

1. **Load and inspect data**
   - Read CSV, Excel, Parquet, JSON files
   - Display basic statistics and data types
   - Identify missing values

2. **Handle missing values**
   - Strategy selection based on data type and context
   - Options: drop, mean/median imputation, mode imputation, forward/backward fill
   - Document imputation choices

3. **Detect and handle outliers**
   - IQR method for normally distributed data
   - Z-score method
   - Isolation Forest for multivariate outliers
   - Cap/floor or remove outliers with justification

4. **Data type conversion**
   - Convert categorical to numerical (one-hot, label encoding)
   - Date/time parsing
   - Text cleaning (lowercasing, trimming, regex)

5. **Generate data quality report**
   - Missing value summary
   - Outlier statistics
   - Data type distribution
   - Recommended next steps

## When to Use Me

Use this skill when:
- User asks to "clean data"
- User mentions "missing values" or "handle nulls"
- User wants to "preprocess data" before ML
- User mentions "outliers" or "anomalies"
- User wants a "data quality report"

## Workflow

When asked to clean data:

1. **Explore** - Load data and generate initial profile
2. **Diagnose** - Identify quality issues (missing, outliers, types)
3. **Plan** - Propose cleaning strategy with rationale
4. **Execute** - Apply cleaning operations
5. **Validate** - Verify improvements and document changes
6. **Report** - Generate final data quality summary

## Best Practices

- Always backup original data before cleaning
- Document all transformations for reproducibility
- Consider business context when making imputation decisions
- Validate cleaning results with statistical tests when appropriate
- Use visualization to understand data distributions
- Prefer conservative approaches unless there's strong justification

## Example Usage

```
Clean this dataset: data/sales.csv
- Handle missing values in the 'revenue' column
- Detect outliers in 'quantity' column
- Convert 'date' column to datetime
- Generate a cleaning report
```

## Python Libraries to Use

- pandas: Data manipulation
- numpy: Numerical operations
- sklearn.impute: Imputation methods
- scipy: Statistical functions
- seaborn, matplotlib: Visualization

## Output Format

After cleaning, provide:
1. **Data Quality Summary** - Before/after statistics
2. **Transformation Log** - List of all operations performed
3. **Cleaned Data** - Path to cleaned dataset
4. **Recommendations** - Suggested next steps for modeling
