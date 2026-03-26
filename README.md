# AgentML

> 基于 OpenCode 的多智能体自动化机器学习框架

AgentML 是一个构建在 OpenCode 平台上的自动化机器学习框架，通过**多智能体（Multi-Agent）**架构 + **标准化 Skills** + **MCP 工具**实现端到端的 ML 流水线。

---

## 核心架构

AgentML 由三层架构组成：

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenCode 平台                            │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │    Agent    │  │   Skills    │  │      MCP Tools      │ │
│  │   (角色层)   │  │  (能力层)   │  │     (工具层)        │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                    ML 流水线                                │
│   Data → Features → Model → Validation → Explanation       │
└─────────────────────────────────────────────────────────────┘
```

---

## Agent 体系

AgentML 定义了 **7 个专业化智能体**，分工协作：

| Agent | 类型 | 职责 |
|-------|------|------|
| `@automl-coordinator` | **Primary** | 统筹协调整个 ML 项目，调度子 Agent |
| `@data-processor` / `@eda` | Subagent | EDA数据分析、数据加载、清洗、缺失值处理 |
| `@feature-engineering` | Subagent | 特征选择、构造、转换、降维 |
| `@model-selector` | Subagent | 模型选型、超参数优化、训练 |
| `@model-validator` | Subagent | 交叉验证，性能评估、模型比较 |
| `@explainability` | Subagent | SHAP 分析、模型可解释性 |
| `@viz-agent` | Subagent | 可视化、图表生成、地图绑定 |

### Agent 协作流程

```
用户请求
    ↓
@automl-coordinator (主智能体)
    ↓
┌─────────────────────────────────────────┐
│  @data-processor   →   数据清洗         │
│  @feature-engineer →   特征工程         │
│  @model-selector   →   模型训练         │
│  @model-validator  →   模型验证         │
│  @explainability   →   模型解释         │
└─────────────────────────────────────────┘
    ↓
返回结果 + 报告
```

---

## Skills 体系

每个 Agent 可以调用标准化的 **Skills**（技能），实现能力复用：

| Skill | 功能 |
|-------|------|
| `eda` | 探索性数据分析、数据概览、统计描述、相关性分析 |
| `data-cleaning` | 数据清洗与预处理、缺失值、异常值处理 |
| `data-visualization` | 统计图表、相关性热力图、ML可视化 |
| `geospatial-analysis` | 地图可视化、距离计算、聚类分析 |
| `feature-engineering` | 特征工程与代码生成 |
| `model-training` | 模型训练与超参数优化 |
| `model-validation` | 交叉验证与性能评估 |
| `shap-analysis` | SHAP 可解释性分析 |

> **使用方式**: 通过 `skill(name="xxx")` 调用，如 `skill(name="eda")`

### Skill 特点

- **标准化** - 统一接口定义，可跨 Agent 调用
- **可组合** - 多个 Skill 可串联形成完整 Pipeline
- **可扩展** - 易于添加新的 Skill

---

## MCP 工具

通过 MCP (Model Context Protocol) 集成外部工具：

| MCP Tool | 功能 |
|----------|------|
| `python-executor` | 安全执行生成的 Python 代码 |
| `atlas-gis-tools` | 地图/GIS 分析工具（需配置 ATLAS_TOKEN） |

### MCP 扩展

可按需添加更多 MCP 工具：
- 文件系统操作
- 数据库连接
- MLflow 实验跟踪
- 模型部署

---

---

## 快速开始

### 1. 安装 OpenCode

```bash
npm i -g opencode-ai
```

### 2. 导入项目配置

```bash
# 方式一：拷贝 .opencode 到全局配置目录
# 方式二：直接在项目目录下运行 opencode
```

### 3. 开始使用

```bash
opencode
```

---

## 在 OpenCode 中使用

### 方式一：使用 @ 引用 Agent

```bash
# 直接调用专业 Agent
@data-processor 清洗客户流失数据，处理缺失值
@feature-engineer 创建客户行为特征
@model-selector 训练 XGBoost 分类器
@model-validator 评估模型性能
@explainability 分析特征重要性
```

### 方式二：使用 @ 引用 Skill

```bash
# 直接调用标准化 Skill
@data-cleaning 清洗数据
@feature-engineering 特征选择
@model-training 训练模型
@model-validation 交叉验证
@shap-analysis 解释预测
```

### 方式三：主智能体协调（推荐）

```bash
# 让 coordinator 自动调度
@automl-coordinator 构建一个客户流失预测模型，数据在 data/churn.csv
```

### 方式四：组合 Pipeline

```bash
# 串联多个 Agent/Skill
@data-processor 清洗数据 →
@feature-engineer 创建特征 →
@model-selector 训练模型 →
@model-validator 验证性能 →
@explainability 解释结果
```

---

## 支持的 ML 任务

- **表格分类** - 二分类、多分类（XGBoost, LightGBM, CatBoost）
- **表格回归** - 连续值预测
- **图像分类** - CNN 模型
- **文本分类** - NLP 模型
- **时序预测** - 时间序列预测
- **聚类** - 无监督 clustering

---

## 项目结构

```
agentML/
├── .opencode/              # OpenCode 配置
│   ├── agents/             # 7 个 Agent 定义
│   │   ├── automl-coordinator.md
│   │   ├── data-processor.md
│   │   ├── feature-engineer.md
│   │   ├── model-selector.md
│   │   ├── model-validator.md
│   │   ├── explainability.md
│   │   └── viz-agent.md
│   ├── skills/             # 8 个标准化 Skills
│   │   ├── eda/
│   │   ├── data-cleaning/
│   │   ├── data-visualization/
│   │   ├── geospatial-analysis/
│   │   ├── feature-engineering/
│   │   ├── model-training/
│   │   ├── model-validation/
│   │   └── shap-analysis/
│   └── opencode.json       # OpenCode 配置
│
├── mcp_servers/            # MCP 工具实现
│   └── python_executor/
├── .env                    # 环境变量
├── LICENSE
├── CHANGELOG.md
├── README.md
└── pyproject.toml
```

---

## 安装

### 前置要求

- Python 3.10+
- OpenCode CLI (`npm install -g opencode-ai`)

### 步骤

```bash
# 1. 安装 OpenCode
npm i -g opencode-ai

# 2. 配置 .opencode（全局或项目目录）

# 3. 启动
opencode
```

### 环境变量配置

在 `.env` 中配置 LLM 提供商：

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# 或 Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# 或使用其他 75+ 提供商

# Atlas GIS Tools (可选，用于地图/GIS 分析)
ATLAS_TOKEN=pk.eyJ...
```

---

## 快速开始

在 `opencode.json` 中配置模型：

```json
{
  "agent": {
    "automl-coordinator": {
      "model": "anthropic/claude-sonnet-4-20250514"
    }
  }
}
```

支持 75+ LLM 提供商（OpenAI, Anthropic, Google, Meta 等）。

---

## 扩展 agentML

### 添加新 Agent

1. 在 `.opencode/agents/` 创建 `new-agent.md`
2. 定义 Agent 角色和能力
3. 在 `opencode.json` 注册

### 添加新 Skill

1. 在 `.opencode/skills/` 创建目录
2. 编写 `SKILL.md` 定义技能
3. Agent 即可调用

### 添加新 MCP

1. 实现 MCP 服务器
2. 在 `opencode.json` 配置

---

---

## License

MIT License
