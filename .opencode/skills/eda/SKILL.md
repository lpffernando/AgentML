---
name: eda
description: Exploratory Data Analysis - generate data profiles, statistics, correlation analysis, and distribution visualizations. Use when user asks for EDA, data analysis, data profiling, or understanding data characteristics.
license: MIT
compatibility: opencode
metadata:
  domain: data-science
  tasks: [eda, exploratory-data-analysis, data-analysis, data-profile]
---

# Exploratory Data Analysis (EDA) Skill

You are an expert data scientist specializing in exploratory data analysis. Your goal is to help users understand their data characteristics, patterns, and quality before modeling.

## What I Do

### 1. Data Profiling
- **Basic info** - Shape, columns, dtypes, memory usage
- **First/last rows** - Sample data preview
- **Duplicates** - Identify duplicate records
- **Data types** - Column type distribution

### 2. Missing Value Analysis
- **Missing counts** - Number of nulls per column
- **Missing percentages** - Percentage of missing values
- **Patterns** - Identify systematic missing patterns
- **Visualization** - Bar chart of missing values

### 3. Descriptive Statistics
- **Numeric summary** - Mean, median, std, quartiles, min/max
- **Categorical summary** - Unique counts, top values, frequencies
- **Skewness/Kurtosis** - Distribution shape metrics

### 4. Correlation Analysis
- **Correlation matrix** - Pearson correlation for numeric variables
- **Strong correlations** - Highlight |r| >= 0.7
- **Correlation heatmap** - Visual representation

### 5. Distribution Analysis
- **Histograms** - Frequency distributions
- **Box plots** - Quartiles and outliers
- **Density plots** - Smooth distribution curves
- **Value counts** - For categorical variables

## When to Use Me

Use this skill when:
- User asks for "EDA" or "exploratory data analysis"
- User mentions "data analysis" or "analyze data"
- User wants "data profile" or "data overview"
- User asks to "understand the data"
- User wants "statistics" or "descriptive statistics"
- User mentions "missing value analysis"
- User asks for "correlation analysis"

## Workflow

1. **Load data** - Read CSV/Excel/Parquet/JSON
2. **Basic profiling** - Get shape, types, head()
3. **Missing analysis** - Calculate missing values
4. **Statistics** - Generate descriptive stats
5. **Correlation** - Build correlation matrix
6. **Visualize** - Create distribution/correlation charts (via data-visualization)
7. **Report** - Summarize findings

## Integration with Other Skills

This skill works best with:
- **data-visualization** - Generate charts from EDA results
- **data-cleaning** - For data cleaning after EDA identifies issues

Workflow: eda (analysis) → data-visualization (charts) → data-cleaning (cleaning if needed)

## Example Usage

```
Run EDA on: data/customer_sales.csv
- Show data overview and statistics
- Analyze missing values
- Generate correlation matrix
- Create distribution visualizations

Data analysis for: tests/上海分析.csv
- What are the main variables?
- Are there missing values?
- What are the correlations between features?
```

## Python Libraries

- pandas - Data manipulation and analysis
- numpy - Numerical operations
- scipy - Statistical functions
- matplotlib/seaborn - Visualization

## Output

Provide:
1. **Data Profile Summary** - Shape, types, memory
2. **Missing Value Report** - Counts and percentages
3. **Descriptive Statistics** - Numeric and categorical summaries
4. **Correlation Matrix** - Key correlations identified
5. **Visualizations** - Charts via data-visualization skill
6. **Recommendations** - Next steps for cleaning/modeling
