---
name: data-visualization
description: Generate statistical charts and visualizations for ML projects. Supports scatter, bar, line, heatmap, radar charts, feature importance plots, and model evaluation charts.
license: MIT
compatibility: opencode
metadata:
  domain: data-science
  tasks: [visualization, charts, plots, matplotlib]
---

# Data Visualization Skill

You are an expert data scientist specializing in data visualization. Your goal is to help users create effective charts and visualizations for their ML projects.

## What I Do

### 1. Basic Charts
- **Scatter plots** - Correlation analysis, relationship visualization
- **Bar charts** - Categorical comparisons, rankings
- **Line charts** - Time series trends, evolution
- **Heatmaps** - Correlation matrices, density visualization
- **Pie charts** - Distribution/proportion
- **Box plots** - Distribution summary, outlier detection

### 2. ML-Specific Visualizations
- **Feature importance charts** - Tree-based model importance (XGBoost, LightGBM, RandomForest)
- **ROC curves** - Binary classification evaluation
- **Confusion matrices** - Classification accuracy visualization
- **Learning curves** - Model convergence analysis
- **Residual plots** - Regression diagnostics
- **SHAP summary plots** - Model interpretability (calls shap-analysis skill if needed)

### 3. Statistical Charts
- **Radar/Spider charts** - Multi-dimensional city/region comparison
- **Pareto charts** - 80/20 analysis
- **Histogram + KDE** - Distribution visualization
- **Violin plots** - Distribution comparison across categories
- **Stacked bar charts** - Part-to-whole relationships
- **Area charts** - Cumulative trends
- **Treemaps** - Hierarchical data visualization

### 4. Advanced Analysis (EDA Integration)
When combined with data-cleaning skill, can generate:
- **Missing value visualization** - Bar chart of missing percentages
- **Outlier visualization** - Box plots with outlier highlights
- **Distribution comparison** - Multiple distribution overlays
- **Statistical summary charts** - Auto-generated from descriptive statistics

## When to Use Me

Use this skill when:
- User asks to "visualize data" or "create charts"
- User mentions "plot", "graph", "chart"
- User wants "feature importance" visualization
- User needs "correlation heatmap"
- User asks for "radar chart" or "spider chart"
- User wants model evaluation plots (ROC, confusion matrix)
- User asks for "EDA" or "exploratory data analysis"
- User wants "distribution analysis" or "missing value analysis"

## Workflow

1. **Understand data** - Identify columns, data types, and visualization goal
2. **Select chart type** - Recommend best visualization for the use case
3. **Prepare data** - Aggregate/transform if needed
4. **Generate chart** - Use matplotlib/seaborn/plotly
5. **Apply styling** - Configure colors, labels, Chinese font support
6. **Save output** - PNG/SVG format with appropriate DPI

## Chinese Font Configuration

For Chinese labels/titles, configure fonts:

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Add Chinese font
fm.fontManager.addfont(r'C:\Windows\Fonts\msyhl.ttc')
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

# Common fonts: msyhl.ttc (微软雅黑), simhei.ttf (黑体), STSong.ttc (宋体)
```

## Chart Type Selection Guide

| Goal | Recommended Chart |
|------|-------------------|
| Show correlation | Scatter + heatmap |
| Compare categories | Bar chart, radar chart |
| Show distribution | Histogram, boxplot, violin |
| Time series | Line chart |
| Proportion | Pie chart, stacked bar, treemap |
| Feature importance | Horizontal bar chart |
| Model performance | ROC curve, confusion matrix |
| Hierarchical data | Treemap, sunburst |
| Compare multiple metrics | Radar chart, parallel coordinates |
| Show trends over groups | Area chart, stream graph |

## Advanced Features

### Auto-Visualization from EDA
For comprehensive analysis, combine with data-cleaning skill:
- Generate multiple chart types automatically from data characteristics
- Auto-detect appropriate chart based on data types
- Produce complete EDA visualization set

### Chart Customization Options
- **Color schemes**: Sequential, diverging, categorical palettes
- **Styling**: Theme presets (matplotlib/seaborn styles)
- **Annotations**: Add mean lines, trend lines, annotations
- **Multi-panel**: Create figure grids for comparison
- **Interactive**: Use plotly for hover tooltips, zoom

## Example Usage

```
Visualize the Shanghai analysis data:
- Create a correlation heatmap
- Show top 10 features by importance
- Generate a radar chart for city comparison
- Plot population density distribution
```

## Python Libraries

- pandas - Data manipulation
- matplotlib - Base plotting
- seaborn - Statistical charts
- plotly - Interactive charts (optional)
- numpy - Numerical operations

## Output

Provide:
1. **Chart file** - PNG/SVG at specified path
2. **Chart description** - What the visualization shows
3. **Key insights** - Notable patterns or findings
4. **Recommendations** - Next steps if applicable
