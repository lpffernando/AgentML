# agentML

> 基于 OpenCode 的多智能体自动化机器学习框架

agentML 是一个构建在 OpenCode 平台上的自动化机器学习框架，通过**多智能体（Multi-Agent）**架构 + **标准化 Skills** + **MCP 工具**实现端到端的 ML 流水线。

---

## 核心架构

agentML 由三层架构组成：

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

agentML 定义了 **6 个专业化智能体**，分工协作：

| Agent | 类型 | 职责 |
|-------|------|------|
| `@automl-coordinator` | **Primary** | 统筹协调整个 ML 项目，调度子 Agent |
| `@data-processor` | Subagent | 数据加载、清洗、缺失值处理、异常值检测 |
| `@feature-engineer` | Subagent | 特征选择、构造、转换、降维 |
| `@model-selector` | Subagent | 模型选型、超参数优化、训练 |
| `@model-validator` | Subagent | 交叉验证、性能评估、模型比较 |
| `@explainability` | Subagent | SHAP 分析、模型可解释性 |

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
| `@data-cleaning` | 数据清洗与预处理 |
| `@feature-engineering` | 特征工程与代码生成 |
| `@model-training` | 模型训练与超参数优化 |
| `@model-validation` | 交叉验证与性能评估 |
| `@shap-analysis` | SHAP 可解释性分析 |

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

### MCP 扩展

可按需添加更多 MCP 工具：
- 文件系统操作
- 数据库连接
- MLflow 实验跟踪
- 模型部署

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
├── .opencode/
│   ├── agents/              # 6 个 Agent 定义
│   │   ├── automl-coordinator.md
│   │   ├── data-processor.md
│   │   ├── feature-engineer.md
│   │   ├── model-selector.md
│   │   ├── model-validator.md
│   │   └── explainability.md
│   ├── skills/             # 5 个标准化 Skills
│   │   ├── data-cleaning/
│   │   ├── feature-engineering/
│   │   ├── model-training/
│   │   ├── model-validation/
│   │   └── shap-analysis/
│   ├── mcp_servers/        # MCP 工具实现
│   │   └── python_executor/
│   └── opencode.json        # OpenCode 配置
│
├── core/                   # 核心逻辑（可选使用）
│   ├── agent_manager/
│   ├── data_agent/
│   ├── model_agent/
│   └── operation_agent/
│
└── tests/                  # 测试用例
```

---

## 安装

### 前置要求

- Python 3.10+
- OpenCode CLI (`npm install -g opencode-ai`)

### 步骤

```bash
# 1. 克隆项目
git clone https://github.com/lpffernando/agentML.git
cd agentML

# 2. 创建虚拟环境
conda create -n agentml python=3.11
conda activate agentml

# 3. 安装依赖
pip install -r requirements.txt

# 4. 安装 OpenCode 依赖
pip install -r requirements-opencode.txt

# 5. 配置环境变量
cp .env.example .env
# 编辑 .env 添加你的 API Key

# 6. 启动 OpenCode
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
```

---

## 快速开始

### 1. 启动 OpenCode

```bash
# 在项目目录运行
opencode
```

### 2. 基本使用

```bash
# 方式1: 让 coordinator 自动处理
@automl-coordinator 使用 data/churn.csv 构建客户流失预测模型

# 方式2: 分步处理
@data-processor 加载并清洗数据
@model-selector 训练模型
@model-validator 验证结果
```

### 3. 配置 LLM

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

## 与原 AutoML-Agent 的关系

agentML 是基于原 [AutoML-Agent](https://github.com/your-repo/AutoML-Agent) (ICML 2025) 的**重新架构**版本：

| 对比 | 原 AutoML-Agent | agentML (OpenCode 版) |
|------|-----------------|---------------------|
| Agent 定义 | 自定义实现 | OpenCode 标准 |
| Skills | 无 | 5 个标准化 Skills |
| 工具调用 | 硬编码 | MCP 协议 |
| 扩展性 | 有限 | 插件式扩展 |
| 模型支持 | 固定 | 75+ 提供商 |

---

## License

MIT License
