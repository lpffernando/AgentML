# AutoML-Agent → OpenCode 迁移计划

> 目标：将现有AutoML-Agent框架完整迁移到OpenCode，同时保留核心逻辑独立性，实现Skills标准化和MCP工具集成

---

## 一、项目概述

### 1.1 现状分析

**现有AutoML-Agent架构：**
- **核心层**：Manager → DataAgent → ModelAgent → OperationAgent
- **技术栈**：LangChain 0.2.1 + MetaGPT 0.8.1 + 自定义Agent
- **特点**：全自定义实现，缺乏标准化工具调用

**待解决问题：**
- ❌ 无原生Skills支持
- ❌ 无MCP工具集成
- ❌ 多模型切换需手动配置
- ❌ 能力无法跨平台复用

### 1.2 目标架构

**迁移后OpenCode架构：**
- **协调层**：Primary Agent (automl-coordinator)
- **执行层**：5个Subagents + 5个标准化Skills
- **工具层**：MCP服务器（Python执行器、文件系统等）
- **技术栈**：OpenCode + agentskills.io + MCP

**核心收益：**
- ✅ 原生Skills支持（agentskills.io标准）
- ✅ MCP工具生态（文件、数据库、代码执行）
- ✅ 75+模型provider支持
- ✅ 能力可跨14+ AI平台复用

---

## 二、迁移策略

### 2.1 核心原则

**装饰式迁移（Decorator Pattern）：**
- **保留核心**：现有AgentManager、DataAgent等核心逻辑不变
- **添加适配**：通过Adapter层包装为OpenCode格式
- **渐进增强**：逐步添加Skills和MCP能力
- **独立运行**：核心层可脱离OpenCode独立运行

**分层架构：**
```
Layer 1: OpenCode框架层 (新增)
  - Primary/Subagent定义
  - SKILL.md能力封装
  - MCP服务器配置

Layer 2: 适配层 (新增)
  - OpenCodeAgentAdapter
  - SkillGenerator
  - MCPBridge

Layer 3: 核心层 (保留)
  - agent_manager/
  - data_agent/
  - model_agent/
  - operation_agent/
  - prompt_agent/
```

### 2.2 迁移范围

**Phase 1: 核心迁移（必做）**
- [ ] Agent包装器开发
- [ ] 5个Subagent定义
- [ ] 5个Skills封装
- [ ] Python执行器MCP

**Phase 2: 能力增强（推荐）**
- [ ] 文件系统MCP
- [ ] 数据库MCP
- [ ] MLflow集成MCP
- [ ] 自定义工具MCP

**Phase 3: 高级功能（可选）**
- [ ] 多模型自动切换
- [ ] Agent自我优化
- [ ] 分布式执行
- [ ] Web界面集成

---

## 三、实施路线图

### Phase 1: 基础框架搭建 (Week 1)

#### Day 1-2: 项目结构初始化

**任务清单：**
- [ ] 创建`automl-opencode/`根目录
- [ ] 初始化`.opencode/`目录结构
  - `.opencode/agents/` - Agent定义
  - `.opencode/skills/` - Skills封装
- [ ] 创建`opencode.json`配置文件
- [ ] 设置`AGENTS.md`项目指令
- [ ] 创建`.gitignore`

**交付物：**
```
automl-opencode/
├── .opencode/
│   ├── agents/
│   └── skills/
├── opencode.json
├── AGENTS.md
└── .gitignore
```

**验收标准：**
- [ ] `opencode --version`可正常执行
- [ ] `opencode init`成功初始化项目
- [ ] 配置文件无语法错误

#### Day 3-4: 核心Agent定义

**任务清单：**
- [ ] 创建`automl-coordinator.md` (Primary Agent)
  - 定义协调器角色和职责
  - 编写系统prompt
  - 配置工具权限
- [ ] 创建5个Subagent定义
  - `data-processor.md`
  - `feature-engineer.md`
  - `model-selector.md`
  - `model-validator.md`
  - `explainability.md`

**交付物：**
- 6个Agent定义文件（`.opencode/agents/*.md`）
- Agent关系图
- 工具权限配置表

**验收标准：**
- [ ] 每个Agent有清晰的description
- [ ] Agent之间调用关系明确
- [ ] 工具权限配置合理（最小权限原则）

#### Day 5: MCP服务器配置

**任务清单：**
- [ ] 配置Python执行器MCP
  - 编写`mcp_server_python_executor.py`
  - 实现execute_python tool
  - 实现execute_script tool
  - 实现validate_code tool
- [ ] 测试MCP服务器连接
- [ ] 更新`opencode.json` MCP配置

**交付物：**
- `mcp_servers/python_executor/server.py`
- MCP配置更新（`opencode.json`）
- MCP测试报告

**验收标准：**
- [ ] MCP服务器可正常启动
- [ ] OpenCode可连接到MCP服务器
- [ ] execute_python tool工作正常

---

### Phase 2: SKILL.md能力封装 (Week 2-3)

#### Week 2: 核心Skills开发

**任务清单：**
- [ ] **data-cleaning SKILL.md**
  - 数据加载和检查
  - 缺失值处理
  - 异常值检测
  - 数据类型转换
  - 数据质量报告

- [ ] **feature-engineering SKILL.md**
  - 特征选择
  - 特征构造
  - 特征转换
  - 降维
  - 特征重要性分析

- [ ] **model-training SKILL.md**
  - 模型选择
  - 超参调优
  - 交叉验证
  - 模型保存

**交付物：**
- 3个SKILL.md文件
- 每个Skill的使用示例
- Skill测试用例

**验收标准：**
- [ ] 每个Skill有清晰的description
- [ ] YAML frontmatter格式正确
- [ ] Markdown instructions详细且可执行
- [ ] 通过Skill验证工具检查

#### Week 3: 高级Skills开发

**任务清单：**
- [ ] **model-validation SKILL.md**
  - 交叉验证策略
  - 性能指标计算
  - 过拟合检测
  - 模型对比

- [ ] **shap-analysis SKILL.md**
  - SHAP值计算
  - 特征重要性可视化
  - 单样本解释
  - 全局解释

- [ ] **AutoML pipeline SKILL.md**（综合Skill）
  - 端到端pipeline编排
  - 步骤依赖管理
  - 结果汇总
  - 报告生成

**交付物：**
- 3个新增SKILL.md文件
- 综合pipeline示例
- Skill间调用关系图

---

### Phase 3: 适配层开发 (Week 3-4)

#### Week 3: 核心适配器

**任务清单：**
- [ ] **OpenCodeAgentAdapter类**
  - `__init__()`: 初始化配置
  - `initialize_manager()`: 初始化AgentManager
  - `execute_full_pipeline()`: 执行完整pipeline
  - `get_status()`: 获取执行状态

- [ ] **Subagent调用包装**
  - `execute_data_processing()`: 包装DataAgent
  - `execute_feature_engineering()`: 包装FeatureAgent
  - `execute_model_selection()`: 包装ModelAgent
  - `execute_model_validation()`: 包装ValidationAgent
  - `execute_shap_analysis()`: 包装ExplanationAgent

**交付物：**
- `adapter/agent_wrapper.py`
- 适配器类图
- 调用关系文档

**验收标准：**
- [ ] 适配器可正常初始化
- [ ] 能调用核心层Agent
- [ ] 结果格式符合OpenCode预期
- [ ] 错误处理完善

#### Week 4: 工具与集成

**任务清单：**
- [ ] **SkillGenerator工具**
  - 从Prompt模板生成SKILL.md
  - 版本管理和diff
  - 批量生成工具

- [ ] **MCPBridge工具**
  - 调用MCP服务器
  - 结果解析和转换
  - 错误处理和重试

- [ ] **OpenCode集成**
  - `opencode.json`完整配置
  - Agent和Skill自动注册
  - 命令行工具集成

**交付物：**
- `adapter/skill_generator.py`
- `adapter/mcp_bridge.py`
- 完整配置包
- CLI工具

---

### Phase 4: 测试与优化 (Week 4-5)

#### Week 4: 测试

**任务清单：**
- [ ] **单元测试**
  - Adapter类测试
  - Skill生成测试
  - MCP桥接测试
  - 边界条件测试

- [ ] **集成测试**
  - 端到端pipeline测试
  - 多Agent协作测试
  - MCP服务器集成测试
  - 错误恢复测试

- [ ] **性能测试**
  - 与原始AutoML-Agent对比
  - 延迟和吞吐量测试
  - 资源消耗分析

**交付物：**
- `tests/`目录完整测试套件
- 测试覆盖率报告
- 性能基准报告

#### Week 5: 优化与文档

**任务清单：**
- [ ] **性能优化**
  - 识别瓶颈
  - 缓存机制优化
  - 并行执行优化

- [ ] **用户体验优化**
  - 错误信息改进
  - 进度展示优化
  - 交互流程简化

- [ ] **文档完善**
  - 架构设计文档
  - 用户指南
  - API文档
  - 开发者指南
  - 故障排查手册

**交付物：**
- 性能优化报告
- 完整文档集
- 用户手册
- 视频教程（可选）

---

### Phase 5: 部署与发布 (Week 5-6)

#### Week 5: 部署准备

**任务清单：**
- [ ] **打包与发布**
  - Python包打包（setup.py/pyproject.toml）
  - Docker镜像构建
  - npm包发布（如需要）

- [ ] **CI/CD设置**
  - GitHub Actions工作流
  - 自动化测试
  - 自动发布流程

- [ ] **环境配置**
  - 开发环境配置脚本
  - 生产环境配置指南
  - 环境变量模板

**交付物：**
- 发布包
- Docker镜像
- CI/CD配置
- 部署脚本

#### Week 6: 发布与推广

**任务清单：**
- [ ] **正式发布**
  - GitHub Release
  - PyPI发布
  - 文档站点上线

- [ ] **社区推广**
  - 技术博客文章
  - 社交媒体宣传
  - 技术社区分享

- [ ] **用户支持**
  - 问题跟踪系统
  - 用户反馈收集
  - 持续改进计划

**交付物：**
- 正式发布版本
- 推广材料
- 用户支持渠道

---

## 四、预期成果

### 4.1 核心能力

| 能力 | 迁移前 | 迁移后 | 提升 |
|------|--------|--------|------|
| Skills标准化 | ❌ | ✅ 5个标准化Skills | 可跨14+平台复用 |
| MCP工具集成 | ❌ | ✅ 3+ MCP服务器 | 文件/DB/代码执行 |
| 多模型支持 | ⚠️ 手动配置 | ✅ 75+ providers | 一键切换 |
| 社区生态 | ❌ | ✅ OpenCode社区 | 100K+ stars |

### 4.2 性能指标

| 指标 | 目标 | 测量方法 |
|------|------|---------|
| 适配层开销 | < 20% | Benchmark对比测试 |
| MCP调用延迟 | < 500ms | 工具响应时间测试 |
| Skill加载时间 | < 100ms | 首次调用耗时测试 |
| 测试覆盖率 | > 80% | 单元+集成测试 |

### 4.3 用户价值

**对于开发者：**
- 标准化能力封装，一次开发多处复用
- 丰富的MCP工具生态，开箱即用
- 灵活的模型切换，适应不同场景

**对于团队：**
- Skills可在14+ AI平台共享
- 统一的Agent协作标准
- 降低多Agent系统开发门槛

**对于生态：**
- 贡献标准化Skills到社区
- 推动Agent互操作性标准
- 丰富OpenCode生态

---

## 五、风险评估与应对

### 5.1 风险清单

| 风险 | 概率 | 影响 | 应对策略 |
|------|------|------|---------|
| 适配层性能开销超标 | 中 | 高 | 实现多级缓存；优化调用链；benchmark持续监控 |
| OpenCode版本兼容性 | 低 | 中 | 锁定版本；定期更新测试；使用稳定API |
| MCP服务器稳定性 | 中 | 中 | 实现fallback机制；本地MCP优先；健康检查 |
| Skills维护成本 | 中 | 中 | 自动化生成；版本化管理；社区贡献 |
| 团队学习曲线 | 高 | 低 | 完善文档；培训计划；渐进式迁移 |

### 5.2 应急预案

**性能问题：**
1. 立即启用性能分析工具，定位瓶颈
2. 临时降级：跳过非关键Skills
3. 启用备用方案：直接调用核心层

**兼容性问题：**
1. 回滚到上一个稳定版本
2. 使用容器化隔离环境
3. 联系OpenCode社区获取支持

**功能缺陷：**
1. 启用功能开关，禁用问题功能
2. 切换到备用实现
3. 提供手动workaround文档

---

## 六、下一步行动

### 6.1 待确认事项

**需要你确认：**
1. **优先级确认**：Phase 1-3是否按顺序执行？还是优先某个特定模块？
2. **资源投入**：计划投入多少人/周？需要我调整时间表吗？
3. **技术确认**：当前的OpenCode版本和Python版本是什么？
4. **迁移范围**：完整迁移还是先从某个模块（如data-cleaning）开始POC？
5. **发布策略**：私有使用还是开源贡献？需要特定合规要求吗？

### 6.2 立即可以开始的工作

**无需等待确认即可开始：**
1. **环境准备**：
   - 安装OpenCode CLI
   - 验证Python环境
   - 准备测试数据集

2. **原型验证**：
   - 创建第一个SKILL.md（data-cleaning）
   - 测试在OpenCode中加载
   - 验证核心功能正常

3. **文档准备**：
   - 整理现有AutoML-Agent文档
   - 提取关键Prompt模板
   - 准备迁移对照表

### 6.3 沟通计划

**定期同步：**
- **每日**：快速进展更新（5分钟）
- **每周**：详细进度review（30分钟）
- **每阶段**：里程碑验收和计划调整（1小时）

**沟通渠道：**
- 技术问题：GitHub Issues
- 紧急事项：即时通讯
- 文档协作：共享文档

---

## 七、总结

本迁移计划提供了一个**完整、可行、渐进式**的AutoML-Agent到OpenCode的迁移方案。通过**装饰式迁移策略**，我们：

1. **保留核心价值**：现有AutoML-Agent核心逻辑100%保留
2. **添加标准能力**：获得Skills、MCP、多模型支持
3. **渐进式交付**：分阶段实施，降低风险
4. **生态兼容**：遵循开放标准，能力可跨平台复用

**关键成功因素：**
- 清晰的架构分层
- 完善的测试覆盖
- 持续的性能监控
- 积极的社区参与

**预期成果：**
- 5个标准化Skills，可在14+ AI平台复用
- 3+ MCP服务器集成，扩展工具生态
- 75+模型provider支持，灵活切换
- 100K+ stars社区生态接入

---

**现在，请告诉我你的决策：**

1. **确认优先级**：Phase 1-3是否按顺序执行？还是优先某个特定模块？
2. **资源投入**：计划投入多少人/周？需要我调整时间表吗？
3. **技术确认**：当前的OpenCode版本和Python版本是什么？
4. **迁移范围**：完整迁移还是先从某个模块（如data-cleaning）开始POC？
5. **发布策略**：私有使用还是开源贡献？需要特定合规要求吗？

我根据你的确认，立即开始实施！
