# AutoML-Agent

> 基于 OpenCode 的自动化机器学习智能体框架

AutoML-Agent 是一个基于 OpenCode Skills 和 MCP 工具的自动化机器学习框架，通过标准化的技能（Skills）系统实现端到端的 ML 流水线自动化。

## 核心特性

### 1. 标准化 Skills 架构

| Skill | 功能 |
|-------|------|
| `@data-cleaning` | 数据清洗与预处理 |
| `@feature-engineering` | 特征工程与代码生成 |
| `@model-training` | 模型训练与 RAP 检索 |
| `@model-validation` | 多阶段验证 |
| `@shap-analysis` | 模型可解释性分析 |

### 2. 三大核心能力

**RAP 检索增强规划 (Retrieval-Augmented Planning)**
- 从 HuggingFace、Kaggle、学术论文检索最优模型
- 无需训练即可快速筛选候选模型
- 结合 LLM 上下文学习进行模型排序

**多阶段验证 (Multi-Stage Verification)**
- Stage 1: 需求验证 - 确认任务类型、数据、指标
- Stage 2: 方案验证 - 验证模型选择、特征工程合理性
- Stage 3: 执行验证 - 验证代码执行、性能达标

**代码自修正 (Self-Correction)**
- 自动执行 Python 代码并捕获错误
- 分析错误信息并自动修复
- 最多 5 次重试直到成功

### 3. MCP 工具集成

- **Python 执行器** - 安全运行生成的代码
- **文件系统** - 读写数据、模型文件
- **MLflow** - 实验跟踪与模型管理

## 支持的 ML 任务

- 表格分类/回归 (XGBoost, LightGBM, CatBoost)
- 图像分类
- 文本分类
- 节点分类 (图神经网络)
- 时序预测

## 在 OpenCode 中使用

### 方式一：使用 @ 引用 Skills

```bash
# 数据清洗
@data-cleaning 清洗数据，处理缺失值和异常值

# 特征工程
@feature-engineering 为客户流失数据创建特征

# 模型训练
@model-training 训练 XGBoost 分类器

# 模型验证
@model-validation 验证模型性能

# SHAP 分析
@shap-analysis 解释模型预测
```

### 方式二：组合多技能 Pipeline

```
@data-cleaning 清洗数据 →
@feature-engineering 创建特征 →
@model-training 训练模型 →
@model-validation 验证性能 →
@shap-analysis 解释结果
```

### 方式三：Python API 调用

```python
from skill import data_cleaning, model_training

# 清洗数据
cleaned_data = data_cleaning(
    data="data/raw/sales.csv",
    handle_missing="mean",
    detect_outliers=True
)

# 训练模型
result = model_training(
    data=cleaned_data,
    task="classification",
    models=["xgboost", "lightgbm"],
    optimize="auc"
)
```

### 方式四：Agent 协调模式

```python
from agent_manager import AgentManager

manager = AgentManager(llm="gpt-4", data_path="data.csv")
manager.initiate_chat("构建一个客户流失预测模型")
```

## 项目结构

```
automl-agent/
├── .opencode/
│   ├── skills/           # 5 个标准化 Skills
│   │   ├── data-cleaning/
│   │   ├── feature-engineering/
│   │   ├── model-training/
│   │   ├── model-validation/
│   │   └── shap-analysis/
│   └── agents/           # Agent 定义
│       ├── automl-coordinator/
│       ├── data-processor/
│       ├── feature-engineer/
│       ├── model-selector/
│       ├── model-validator/
│       └── explainability/
├── mcp_servers/          # MCP 工具服务器
└── core/                 # 核心逻辑
```

## 安装

```bash
# 克隆项目
git clone https://github.com/your-repo/automl-agent.git
cd automl-agent

# 创建虚拟环境
conda create -n automl python=3.10
conda activate automl

# 安装依赖
pip install -r requirements.txt
```

## 配置 LLM

在 `.env` 中配置你喜欢的 LLM 提供商：

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# 或使用其他 75+ 提供商
# 支持: Anthropic, Google, Meta, Mistral, Cohere, etc.
```

## 输出示例

使用 `@model-validation` 后的输出：

```
✓ Stage 1: 需求验证 PASS
✓ Stage 2: 方案验证 PASS  
✓ Stage 3: 执行验证 PASS

性能指标:
- AUC-ROC: 0.89
- F1-Score: 0.85
- Precision: 0.87
- Recall: 0.83
```

## License

MIT License
