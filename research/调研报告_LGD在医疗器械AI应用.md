---
title: LGD 在医疗器械 AI 应用的全面调研报告
summary: 把 LGD 三律（有籍 · 有证 · 有门禁）映射到医疗器械 AI 全生命周期，用真实监管案例定位其落点、所补空白与差异化价值；v1.1 撞车审查修订版。
domain: LGD 理论体系
source: SynomosAI × MedXpert
version: v1.1
updated: 2026-09-13
tags: [LGD, 三律, 医疗器械, 医疗AI, 全生命周期]
type: research
---
# LGD 在医疗器械 AI 应用的全面调研报告

> **作者署名**：赵兴华 / Steven Zhao·China（ORCID 0009-0001-0512-1237 ｜ GitHub: zhaoxinghua09-cell/lgd-theory ｜ https://medxpert.cn）
> **品牌**：MedXpert × SynomosAI
> **版本**：v1.1（2026-09-13 撞车审查修订版）｜ **许可**：CC BY 4.0
> **理论上游**：TH-META-006（LGD 母版 v1.0）｜ TH-MED-002（医械注册方法论 v1.0）
> **本件定位**：硕士论文 LGD 题"医械实证素材四件套"之第三件——把 LGD 三律从"注册方法论"扩到"全生命周期方法论"，并以真实医械 AI 案例做参照映射。
> **诚实边界**：本件为方法论调研，非监管申报材料；法规条目为稳定公开名称，具体条款版本以监管官网原文为准。
> **⚠️ v1.1 修订说明**：依中立撞车审查报告（`论文线/撞车审查/撞车审查报告_CVG_20260913.md`，结论=退回修改）执行 5 条差异化指令——核心修订：①"空白"口径收窄为"无逐次授权门禁"（IMDRF N93 草案已占据"持续治理"表述）②PCCP/PMS 缺口观察让渡优先权予 B-46/B-47/B-48 ③差异化落点改为"变更区间概念化 + 逐次授权门禁（签发权属人）"，并明确"持续验证≠逐次授权"（对照 B-50）。新增引用编号 B-45~B-52（见 120 篇池 B6 节）。

---

## 0. 执行摘要

本调研回答一个问题：**Steven 自研的全程治理论（Lifecycle Governance Doctrine, LGD），在医疗器械 AI 这一受监管实业中，究竟能落在何处、补什么空白、有何独特价值。**

结论先行——四条核心发现：

1. **同构母版铁证**：医疗器械全生命周期监管（RRM）是 LGD 母版 §2 明示的"同构参照母版"。LGD 三律（有籍/有证/有门禁）在医械域**每个生命周期节点都有现成对应物**——这给理论提供了全球最成熟的真实参照场，远超金融、自动驾驶等其它域。

2. **LGD-MED-002 已落"注册"环节，但 SaMD TPLC 全周期映射仍是空白**：Steven 自己的医械方法论只覆盖了"注册 = 文档化承诺"这单一环节。本调研首次把 LGD 三律**完整映射到 SaMD 全生命周期（TPLC）五阶段**：Concept→Discovery & Prototyping→Design & Development→Validation→Post-market。映射矩阵见 §4。

3. **国际监管框架正向 LGD 收敛但尚未咬合成链**：FDA 的 TPLC/PCCP/GMLP、EU 的 AI Act + MDR 双重符合性、ISO/IEC 13485+42001+14971、NIST AI RMF——单点都对，**但缺一条贯穿主轴**。LGD 母版 §6 自陈"收口层不替代既有理论"——它的独特贡献是把上述散点咬合成一条从生到退不可断裂的链。

4. **LGD 独特价值定位**：**持续核验门禁（Continuous Verification Gate, CVG）**。FDA PCCP 允许预设变更控制计划（事前授权），EU MDR 强调上市后监督（事后发现），2026 年 IMDRF N93 草案更把"持续治理"立为监管方向 [B-45]——但**现有持续治理以监测与质量体系承载，所有框架均未要求"每次演化通过签发权属人的逐次授权门禁"**（验证结果不构成逐次放行决定）。LGD-III 有门禁的主张比 PCCP 更严——它要求**每次**能力升级、改版、扩权、行为变更都过触发评估—评分放行—事后复盘三段式门禁，签发权属人。**"逐次授权门禁 + 签发权属人"这一规范位置，是 PCCP/PMS/N93 等现有框架尚未占据的**，是 LGD 的差异化贡献（详见 §7.2，注意"持续验证≠逐次授权"的划界 [B-50]）。

**对硕士论文的支撑**：本调研是 v1.1 规划中医工交叉类章节框架第 3 章"LGD 三律与既有医械治理框架的对齐"的一手实证素材底稿；也是"立即可启动 5 项"中第 1 项（文献综述 120 篇池）和第 3 项（LGD 三律→SaMD TPLC 映射图）的直接依据。

---

## 1. 调研背景与目标

### 1.1 为什么选医疗器械 AI 做 LGD 实证场

Steven 在 LGD 母版 §2 明示：**"受监管的世界早已拥有'全程治理'的成熟样板，其中最具代表性的是医疗器械全生命周期监管。"** 这一选择不是偶然：

| 维度 | 医疗器械 AI 的优势 |
|------|---------------------|
| 监管成熟度 | 1976 年《医疗器械修正案》至今 50 年，ISO/IEC/AAMI/MDR/FDA 多套标准稳定运行 |
| 全周期覆盖 | 从分类、设计开发、风险管理、注册、临床评价、生产质量、上市后监督到退役处置——8 个环节全部有强制监管要求 |
| AI 特化 | 2017 年 IMDRF SaMD 工作组、2021 年 FDA AI/ML SaMD Action Plan、2025 年 PCCP 最终指南——AI 医械治理框架已成独立子领域 |
| 公开案例 | IDx-DR（首个无医生判读自主 AI 诊断设备，DEN180001）、EyeArt（K200667）、HeartFlow FFRct（P150023）等公开授权案例 |
| 学术活跃 | Nature Medicine、NEJM AI、Lancet Digital Health 持续发布 AI 医械临床验证研究 |
| Steven 自身背景 | 国际医疗器械业务，LGD-MED-002 已立医械注册方法论，理论现场感强 |

相比之下，金融、自动驾驶、机器人等域要么监管尚未成熟（自动驾驶）、要么 AI 治理框架仍在演进（金融）、要么公开案例稀缺（机器人）。**医疗器械 AI 是 LGD 实证的最优母版。**

### 1.2 本调研与既有 LGD 医械线文档的关系

| 既有文档 | 覆盖范围 | 本调研的关系 |
|---------|---------|-------------|
| LGD 母版 v1.0 §2 | 给出医械监管作为"同构母版"的总论 | 提供总论锚点；本调研展开实证 |
| LGD-MED-002 注册方法论 v1.0 | 只覆盖"注册 = 文档化承诺"单一环节 | 本调研是它的"全周期扩展"——把三律从注册扩到 TPLC 五阶段 |
| LGD-MED-001（反编造 AFG）| 注册资料反编造纪律 | 本调研在 §6 案例研究中调用 AFG 标准 |

**本调研不重复既有内容，只补"全周期映射 + 真实案例 + LGD 独特价值"这一空白。**

### 1.3 调研方法

1. **一手标准与监管文献**：FDA 官网（SaMD Pre-Cert TPLC、PCCP Final Guidance 2025、GMLP 2021）、EU 官网（AI Act 全文、MDCG 2025-6、MDR 2017/745）、ISO/IEC 标准（13485:2016、42001:2023、14971:2019、IEC 62304:2015）、NIST AI RMF 1.0（2023）+ 医疗剖面。
2. **公开授权案例**：FDA 510(k) 数据库、De Novo 数据库、PMA 数据库直接查询 IDx-DR / EyeArt / HeartFlow 授权文件。
3. **学术文献**：Nature Medicine、NEJM AI、Lancet Digital Health 关于 AI 糖网筛查、骨科 AI 的临床验证论文。
4. **LGD 母版自身映射方法**：把三律按"出生—演化—退场"映射到 SaMD TPLC 每一阶段，每阶段填一个公开母版依据，得到完整映射矩阵。

---

## 2. LGD 三律与医械治理映射理论基础

### 2.1 LGD 三律正式定义（来自母版 v1.0）

| 律 | 名称 | 核心 |
|----|------|------|
| LGD-I | 有籍（Registry）| 凡自治之物，出生即登户籍。身份、创造者、治理归属与档案登记于统一户籍层；**凡造必登**，登记不因规模小或用途私而豁免。 |
| LGD-II | 有证（Evidence）| 凡所行必有证据。关键决策留证据工件——决策日志、风险登记、模型/产品档案、变更记录、人类监督证明、事件台账；业务侧结论须带"依据—来源—签字"的可溯源链条。 |
| LGD-III | 有门禁（Gate）| 凡演化必经门禁。能力升级、改版、扩权、行为变更，须过触发评估—评分放行—事后复盘；**签发权与高利害决定权属人**，机器只请求，人可授权。 |

### 2.2 三律的"贯穿性"主张（LGD 区别于单点治理的关键）

LGD 母版 §1 推论指出："治理不是一次注册，也不是一纸政策，而是一条**从出生到退役不可断裂的链条**。" 这是 LGD 与市面多数 AI 治理框架的根本区别：

- **单点治理框架**：UBIC 解决身份（"它是谁"），XCGS 解决证据（"凭什么"），A³ 解决门禁（"谁允许它变强"）——但都各自独立成立。
- **LGD 的贯穿主张**：三律不是三个独立工具，而是**贯穿生命周期每个节点的主轴**。每个节点都要回答"有籍吗—有证吗—有门禁吗"三问；任一不过，链条在此断裂。

### 2.3 医械监管对三律的天然支撑

医械监管本身就是按"全程"组织——监管要求覆盖分类→设计→风险→注册→临床→生产→PMS→退役八个环节，每个环节都有：
- 身份信息（对应 LGD-I）：产品定义、分类、注册单元、UDI
- 证据要求（对应 LGD-II）：设计开发记录、风险登记、临床评价报告、检验报告
- 放行门禁（对应 LGD-III）：体系核查、注册审评、变更控制、延续注册、注销

**结论**：医械监管结构天然契合 LGD 三律，是 LGD 在受监管实业中**最容易做实证映射**的领域。

---

## 3. SaMD TPLC 全生命周期阶段模型

### 3.1 IMDRF SaMD 框架与 FDA TPLC

**IMDRF（International Medical Device Regulators Forum）** 2013 年发布《Software as a Medical Device: Key Definitions》，把 SaMD 定义为"用于一种或多种医疗目的，但并非必需作为硬件医疗器械一部分的软件"。FDA 在 IMDRF 工作基础上，于 2018-2021 年提出**TPLC（Total Product Lifecycle）** 框架，并在 2023 年《Artificial Intelligence-Enabled Software as a Medical Device》指南中明确 AI-DSF（AI-Enabled Device Software Function）定义。

**FDA 已授权 AI 医械设备**：截至 2025 年 9 月，FDA 已累计授权 1100+ 个 AI/ML 医械设备（CDRH 公开数据库），其中影像类占 75%+、放射治疗类占 10%+、心血管类占 5%。

### 3.2 SaMD TPLC 五阶段模型

FDA TPLC 把 SaMD 生命周期分为五个阶段（与 IMDRF 框架对齐）：

| 阶段 | 中文名 | 核心活动 | 公开母版依据 |
|------|--------|---------|--------------|
| **S1 Concept** | 概念期 | 临床需求识别、预期用途定义、风险等级初判、产品定义 | ISO 14971 风险分析；FDA Pre-Sub 咨询 |
| **S2 Discovery & Prototyping** | 发现与原型期 | 数据集构建、模型架构选型、原型验证、数据治理计划 | GMLP 原则 1-3（数据与训练治理）|
| **S3 Design & Development** | 设计开发期 | 详细设计、软件工程（IEC 62304）、设计控制（21 CFR 820.30）、风险管理持续、性能验证 | ISO 13485 7.3；21 CFR 820.30；IEC 62304；GMLP 原则 4-7 |
| **S4 Validation** | 验证期 | 分析验证（Analytical Validation）、临床验证（Clinical Validation）、临床试验或真实世界证据 | FDA Clinical Study Design Guidance；MDR 临床评价 |
| **S5 Post-market** | 上市后期 | PMS、PMSR、PSUR、CAPA、变更控制（PCCP）、警戒上报、退役处置 | FDA Postmarket Surveillance；EU MDR Article 83-86；UDI 注销 |

### 3.3 现有 TPLC 框架的"缺口"信号

FDA 自身在 2021 年《Artificial Intelligence/Machine Learning-Based Software as a Medical Device Action Plan》中坦承，传统医械监管的"一次性注册 + 偶发变更申报"模式，对 AI 这种"模型持续学习、行为持续漂移"的新型产品存在治理缺口，故提出 PCCP（Predetermined Change Control Plan）作为应对。但 PCCP 本身只覆盖**事先可预期的变更**，对**事后才能识别的漂移**仍依赖传统 PMS。

EU 在 2024 年 AI Act + 2025 年 MDCG 2025-6 把 AI 医械定为"高风险 AI"，要求与 MDR 双重符合性评估，但同样未明确要求"每次演化都过门禁"。

**这正是 LGD 的切入点——三律贯穿要求每个阶段都过门禁，覆盖了 PCCP 与 PMS 都未明确要求的部分。**

---

## 4. LGD 三律 × SaMD TPLC 五阶段映射矩阵（核心创新）

### 4.1 映射矩阵总表

下表把 LGD 三律按"行"展开，SaMD TPLC 五阶段按"列"展开，每格填一个公开母版依据与 LGD 落地点。这是本调研的核心创新——把 LGD-MED-002（只覆盖注册）扩展到 TPLC 全周期。

| LGD 律 ↓ / TPLC 阶段 → | S1 概念期 | S2 发现与原型期 | S3 设计开发期 | S4 验证期 | S5 上市后期 |
|--------|---------|----------------|--------------|---------|-----------|
| **LGD-I 有籍** | 产品定义、预期用途、分类判定、注册单元划分（FDA 产品分类、CN 分类目录、MDR 分类规则）| 数据来源登记、数据治理计划、数据集身份证（GMLP 原则 1-2）| 软件配置项登记、模型卡（Model Card）、训练数据快照冻结、版本号管理（IEC 62304 配置管理）| 临床试验注册号（ClinicalTrials.gov / EU CTR）、验证数据集冻结、性能基线快照 | UDI 发放与维持、PMS 计划登记、PSUR 提交编号、退役日期与销号登记 |
| **LGD-II 有证** | 风险分析文档（ISO 14971）、预期用途声明、临床需求文档 | 数据集证明（来源/质量/代表性/偏见审计）、训练日志、原型验证报告 | 设计开发文档（21 CFR 820.30 i-viii）、设计评审记录、设计变更历史文件（DHCF）、风险管理持续更新、模型卡 v2 | 分析验证报告、临床验证报告（CER）、统计性能（敏感度/特异度/AUC）、真实世界证据 | PMS 报告、不良事件台账、CAPA 记录、PSUR、警戒上报（MDR/PMSR）|
| **LGD-III 有门禁** | 风险等级初判门禁、Pre-Sub 咨询放行 | 数据冻结门禁（数据集一旦冻结不可追溯改）、原型→进入设计开发的放行评审 | 设计评审门禁（DHR）、设计变更门禁（变更控制委员会 CCB）、风险管理复审门禁 | 注册审评门禁（FDA De Novo/510(k)/PMA；MDR 符合性评估）、临床数据完整性门禁（21 CFR Part 11）| **变更控制门禁（PCCP / SCF）**、CAPA 闭环门禁、PSUR 接受门禁、退役销号门禁 |

### 4.2 映射矩阵的三个关键洞察

**洞察一：每阶段都有"门禁"，不止"注册"和"退役"两端的门禁**

传统医械监管倾向于把门禁集中在两端——准入门禁（注册审评）+ 退役门禁（注销）。但 LGD-III 要求**每个演化节点都过门禁**。映射矩阵显示，TPLC 五个阶段每个阶段都有至少一个"门禁"机制：
- S1：风险等级初判门禁（决定走哪条注册路径）
- S2：数据冻结门禁（数据集一旦冻结即"封档"，后续不可追溯改）
- S3：设计评审门禁、CCB 变更门禁
- S4：注册审评门禁
- S5：PCCP/SCF 变更门禁、CAPA 闭环门禁、PSUR 接受门禁

**这是 LGD 对 PCCP 的扩展**：PCCP 只覆盖事先声明的变更，但 LGD 要求所有变更都过门禁，包括事先未声明的应急变更（如安全补丁）。

**洞察二：LGD-II 有证 的"证据工件清单"是市面多数 AI 治理框架未充分枚举的部分**

市面 AI 治理框架多提"可审计"（auditability），但少有完整枚举"关键决策的证据工件清单"。LGD 母版明确列了六类证据工件：决策日志、风险登记、模型/产品档案、变更记录、人类监督证明、事件台账。映射矩阵显示这六类在 SaMD TPLC 每个阶段都有具体落地点，且每类都有现成标准（ISO 14971 风险登记、IEC 62304 软件配置、21 CFR 820.30 设计控制、21 CFR Part 11 电子记录、ISO 13485 不良事件台账）。

**LGD 在医械域的贡献是"枚举完整 + 贯穿要求"，而非发明新证据类型**——这契合母版 §6 的"收口层"定位。

**洞察三：LGD-I 有籍 在 AI 域的"籍"远比传统医械复杂**

传统医械的"籍"是产品定义 + UDI。但 AI 模型有三类"籍"必须分别登记：
- **产品籍**（模型作为产品的身份）：UDI、注册证号、预期用途
- **数据籍**（训练数据的身份）：数据集身份证、来源、代表性、偏见审计
- **模型籍**（模型本身的身份）：架构、参数、版本号、性能基线、训练配置

LGD 母版对"籍"的定义是"身份、创造者、治理归属与档案"——三类籍都能归入这个统一户籍层。**数据籍和模型籍是 AI 域特有的新增籍**，传统医械监管框架只覆盖产品籍，数据籍和模型籍是 PCCP、GMLP 等新指南才开始覆盖的，LGD 把它们一并纳入"凡造必登"。

### 4.3 与 LGD-MED-002 注册方法论的衔接

LGD-MED-002 把"注册 = 文档化承诺"映射到 LGD 三律：
- 身份（有籍）：产品定义、预期用途、分类
- 证据（有证）：风险/性能/临床/质量证据卷宗
- 门禁（有门禁）：体系核查、注册检验、审评发补、变更控制、延续注册
- 延续（链条闭合）：PMS、警戒、飞行检查、退役与注销

**本调研的扩展点**：LGD-MED-002 的"注册"对应 TPLC 的 S4 验证期门禁 + S5 上市后门禁。本矩阵进一步把三律扩到 S1-S3——即"注册前"的设计开发期和原型期，也要过三律。这填补了 LGD-MED-002 没覆盖的"注册前阶段"空白，使 LGD 在医械域成为真正的"全周期方法论"。

---

## 5. 国际监管框架对齐分析

### 5.1 FDA：TPLC + PCCP + GMLP + AI-DSF

**5.1.1 TPLC（Total Product Lifecycle）框架**
- 来源：FDA CDRH，2018 年起基于 IMDRF SaMD 框架演进
- 核心：把 SaMD 监管从"一次注册"扩展到"全周期持续监管"
- 对齐 LGD：TPLC 是 LGD 三律的"骨架"——LGD 把 TPLC 五阶段作为"贯穿主轴"，三律在每阶段填实

**5.1.2 PCCP（Predetermined Change Control Plan）**
- 来源：FDA 2025 年 1 月最终指南（最初 2019 年讨论，2023 年 12 月草案，2025 年最终版）
- 三组件：
  1. Description of Modifications（变更描述：事先声明哪些类型的变更允许走 PCCP）
  2. Modification Protocol（变更协议：变更触发条件、评估方法、性能基线、验收判据）
  3. Impact Assessment（影响评估：变更对安全/有效性的预期影响）
- 对齐 LGD：PCCP 是 LGD-III 有门禁 在 S5 阶段的具体落地之一，但**PCCP 只覆盖事先声明的变更**——LGD 要求所有变更都过门禁，覆盖范围更广

**5.1.3 GMLP（Good Machine Learning Practice）10 原则**
- 来源：FDA / Health Canada / MHRA 联合，2021 年 10 月发布
- 10 原则：① 多学科专家参与 ② 良好数据卫生 ③ 培训/测试独立 ④ 代表性训练集 ⑤ 参照基准 ⑥ 用户清晰理解 ⑦ 临床表现与提交资料一致 ⑧ 持续监控 ⑨ 退役与更新受控 ⑩ 安全网（向 FDA 上报重大变更）
- 对齐 LGD：GMLP 原则 1-3 关联 S2 期"有籍"（数据籍）；原则 4-7 关联 S3 期"有证"（设计与验证证据）；原则 8-10 关联 S5 期"有门禁"（持续监控 + 变更门禁 + 退役门禁）。**LGD 把 GMLP 10 原则按 TPLC 阶段重新组织为三律贯穿**，是结构而非内容创新。

**5.1.4 AI-DSF（AI-Enabled Device Software Function）**
- 来源：FDA 2023 年《Artificial Intelligence-Enabled Software as a Medical Device》指南
- 定义：医疗器械中包含 AI/ML 的软件功能组件
- 对齐 LGD：AI-DSF 是 LGD-I 有籍 在 FDA 域的官方登记对象——AI 模型作为 SaMD 的特化形态

### 5.2 EU：AI Act + MDR 双重符合性

**5.2.1 EU AI Act（2024）**
- 高风险 AI 系统定义：Annex III #5 明示"用于医疗器械（MDR/IVDR 监管）的安全组件或 AI 系统"自动归为高风险
- 义务：风险评估、数据治理、技术文档、记录保存、人类监督、准确性/稳健性/网络安全、投放市场后监控、严重事件上报、注册（在 EU 数据库）
- 对齐 LGD：AI Act 多数义务（风险评估、数据治理、技术文档、记录保存、监控、注册）可归入 LGD-I 有籍或 LGD-II 有证；但 AI Act 同样未明确要求"每次演化都过门禁"，LGD-III 比 AI Act 更严

**5.2.2 MDR 2017/745**
- 高风险医械分类：Class IIa/IIb/III（按 Rule 6 等）
- PMS、PSUR、警戒（MIR）要求：MDR Article 83-86
- UDI：MDR Article 27、Annex VI（产品籍的强制登记）
- 对齐 LGD：MDR PMS/PSUR 是 LGD-III 在 S5 的现有落地；UDI 是 LGD-I 有籍 的成熟实现

**5.2.3 MDCG 2025-6（MDAI 定义与符合性评估）**
- 来源：欧盟医械协调组 2025 年发布
- 核心：定义 MDAI（Medical Device AI），与 AI Act 互动关系
- 对齐 LGD：MDAI 是 LGD-I 有籍 在 EU 域的官方登记对象

**5.2.4 Digital Omnibus 推迟**
- 2025 年 EU 通过 Digital Omnibus 简化包，把 AI Act 高风险义务对医械的适用日期从 2026 年 8 月推迟到 2027 年 8 月（高风险非医疗 AI 系统）和 2028 年 8 月（高风险通用 AI 模型 + 高风险 AI 系统）
- 影响：EU 医械 AI 双重符合性的强制时点有所后延，但 MDR 仍按原有时点要求；Steven 的硕士论文答辩（2027-03）恰在过渡期，可在论文中讨论"过渡期双重符合性操作难题"作为应用章节

### 5.3 ISO/IEC：13485 + 42001 + 14971 + 62304

| 标准 | 范围 | 对齐 LGD |
|------|------|---------|
| ISO 13485:2016 | 医械 QMS | 全 QMS 是 LGD-I/II/III 的过程载体；设计开发（7.3）、风险管理（7.1.2）、CAPA（8.5.2/3）、不良事件（8.2.2/3）每个都有对应 LGD 律 |
| ISO/IEC 42001:2023 | AI 管理体系 | AI-IMS 是 AI 域的 ISO 13485 等价物；LGD 可作为 ISO 42001 的"贯穿性叙事"——ISO 42001 条款 5/6/7/8/9/10 与 LGD 三律在 TPLC 各阶段都有交集 |
| ISO 14971:2019 | 医械风险管理 | 风险登记随生命演进持续更新——LGD-II 有证 在风险维度的具体落地 |
| IEC 62304:2015 | 医械软件生命周期 | 软件开发 5 个安全等级 A/B/C 各有流程要求——LGD-III 有门禁 在 S3 设计开发期软件维度的落地 |
| IEC 62366-1:2015 | 可用性工程 | 用户界面验证——LGD-II 在 S4 验证期可用性维度 |
| AAMI CR34971:2023 | AI 医械风险管理应用指南 | 把 ISO 14971 应用到 AI/ML 特定风险（数据漂移、性能衰减、偏见）——LGD-II 在 AI 维度的风险特化 |

**关键观察**：ISO/IEC 体系已基本覆盖 LGD 三律所需的过程要求，但**没有一条主轴把它们咬合**。ISO 13485 不涉及 AI 特定治理，ISO 42001 不涉及医械特化，ISO 14971 不涉及 AI 漂移。LGD 母版 §6 自陈"收口层不替代既有理论"——在医械域，LGD 把 ISO 13485+42001+14971+AAMI CR34971 咬合成一条贯穿 TPLC 五阶段的主轴。

### 5.4 NIST AI RMF 1.0 + 医疗剖面

**5.4.1 NIST AI RMF 1.0（2023）**
- 四功能：Govern（治理）/ Map（映射）/ Measure（度量）/ Manage（管理）
- 核心：贯穿 AI 全生命周期的"风险治理"框架
- 对齐 LGD：
  - Govern = LGD-I 有籍 + LGD-III 有门禁（治理结构、责任分配、政策、门禁）
  - Map = LGD-I 有籍 在 S1-S2 阶段（识别 AI 系统的预期用途、上下文、潜在影响）
  - Measure = LGD-II 有证 在 S3-S4 阶段（性能、稳健性、可解释性的度量）
  - Manage = LGD-III 有门禁 在 S5 阶段（风险缓解、变更管理、事件响应）

**5.4.2 NIST AI RMF 医疗剖面（2024 草案）**
- 来源：NIST AI Safety Institute Consortium Healthcare Profile
- 核心：把 AI RMF 1.0 特化到医疗场景
- 对齐 LGD：医疗剖面提供了"医械特化"的视角，但仍是单点工具，LGD 把它与 SaMD TPLC 主轴咬合

### 5.5 中国 GB-Z 185 + AI 医械指南

**5.5.1 GB/T 42062（等同 ISO 14971）+ GB-Z 185 系列人工智能医疗器械标准**
- GB-Z 185 系列是中国 AI 医械推荐性标准，包括分类、风险、数据集、性能评估等
- 对齐 LGD：GB-Z 185 是中国本土的 LGD 落地参照；Steven 的硕士论文可在中国章节用 GB-Z 185 做"本土实证"

**5.5.2 NMPA AI 医械指南**
- 2022 年《人工智能医用软件产品分类界定指导原则》
- 2023 年《人工智能医疗器械注册审查指导原则（2023）》
- 对齐 LGD：NMPA 已要求 AI 医械做算法版本管理、数据集登记、性能验证、上市后追溯——LGD 三律在中国已有监管对接

### 5.6 框架对齐总览（一表速览）

| 框架 | 国别/组织 | 阶段覆盖 | 主要对齐 LGD 律 |
|------|----------|---------|-----------------|
| IMDRF SaMD 框架 | 国际 | S1-S5 全周期 | I+II+III 全律 |
| FDA TPLC | 美国 | S1-S5 全周期 | I+II+III 全律（骨架）|
| FDA PCCP | 美国 | S5 局部 | III 局部 |
| FDA GMLP | 美加英 | S2-S5 部分 | II+III |
| FDA AI-DSF | 美国 | S1-S5 全周期 | I |
| EU AI Act | 欧盟 | S1-S5 全周期 | I+II+III |
| EU MDR | 欧盟 | S1-S5 全周期 | I+II+III |
| EU MDCG 2025-6 | 欧盟 | S1（分类）| I |
| ISO 13485 | 国际 | S3+S5（QMS）| II+III |
| ISO/IEC 42001 | 国际 | S1-S5 全周期 | I+II+III（AI 域）|
| ISO 14971 | 国际 | S1-S5 全周期 | II（风险）|
| AAMI CR34971 | 国际 | S1-S5 全周期 | II（AI 风险）|
| IEC 62304 | 国际 | S3 | III（软件门禁）|
| NIST AI RMF 1.0 | 美国 | S1-S5 全周期 | I+II+III |
| NIST AI RMF 医疗剖面 | 美国 | S1-S5 全周期 | I+II+III |
| GB-Z 185 系列 | 中国 | S1-S5 全周期 | I+II+III |
| NMPA AI 指南 | 中国 | S1-S5 全周期 | I+II+III |
| **IMDRF N93 AILCM 草案** [B-45] | 国际 | S1-S5 全周期 | I+II+III（持续治理方向）——**未见逐次授权门禁要求** |

**总结论**（v1.1 修订）：所有主流监管框架都在朝"持续治理/全生命周期"方向收敛，IMDRF N93 草案（2026）已把持续治理立为国际监管方向——但**没有任何框架要求"每次演化通过签发权属人的逐次授权门禁"作为基线**（N93 的持续治理以监测与体系承载，验证结果不构成逐次放行决定；另见撞车审查证据 B-46/B-47/B-48 证实的 PCCP 覆盖缺口观察，其观察优先权归原发现者）。LGD-III 的"逐次授权门禁（签发权属人）"主张，是 LGD 在这些框架之上的差异化贡献点。

---

## 6. 案例研究

### 6.1 AI 糖网筛查：IDx-DR + EyeArt + 13 个 CE 系统

#### 6.1.1 IDx-DR（首个自主 AI 诊断设备）

| 维度 | 内容 |
|------|------|
| 授权路径 | FDA De Novo DEN180001（2018-04-11，首个无医生判读自主 AI 诊断设备）|
| 预期用途 | 自主检测 22 岁以上糖尿病患者的糖尿病视网膜病变（DR），轻度及以上水平 |
| 临床验证 | pivotal 试验（IDx-DR pivotal study, Gulshan et al., JAMA 2016 → IDX-200 pivotal, IDx-DR Multi-Reader Multi-Case）|
| 关键性能 | 敏感度 87.2%（>slight DR），特异度 90.7%（< mild），AUC 0.91 |
| LGD-III 门禁 | IDx-DR 是"locked model"——训练后模型参数冻结，无持续学习，每次变更需新申报 |
| LGD-I 籍 | 已在 FDA De Novo 数据库、UDI 数据库登记 |
| LGD-II 证 | pivotal 临床试验数据、性能基线、PMS 计划、真实世界数据收集（EyePACS）|
| LGD-III 门禁 | 因是 locked，无需 PCCP；但任何变更（即使算法微调）需重新走 De Novo 或 510(k) |

#### 6.1.2 EyeArt（510(k) 路径，已在多市场授权）

| 维度 | 内容 |
|------|------|
| 授权路径 | FDA 510(k) K200667（2020-08）；CE Mark（Class IIa）；英国 UKCA；加拿大 MDL |
| 预期用途 | 检测 DR（≥ moderate level），用于 22 岁以上糖尿病患者 |
| 临床验证 | EyeArt AI System Pivotal Trial（Multi-Reader Multi-Case Trial, Abramoff et al., Eye 2023）|
| 关键性能 | 敏感度 91.7%，特异度 67.0%，但 referable DR（≥ moderate）检测敏感度 95%+ |
| LGD-III 门禁 | 同为 locked model；变更需 510(k) special |

#### 6.1.3 13 个 CE 认证 AI 糖网系统

截至 2025 年 9 月，欧盟已有 13 个 AI 糖网筛查系统通过 CE Mark，代表系统包括 Retmarker（PT）、EyeArt（EU）、IDx-DR（EU 自 2013 年起在荷兰部署）、RetinaRisk 等。这一规模证明 AI 糖网筛查已从"先驱性个案"转为"成熟产品类"。

#### 6.1.4 LGD 三律在 AI 糖网筛查案例的实证

- **LGD-I 有籍**：每个系统都有 UDI、CE/FDA/NMPA 注册号、模型版本、训练数据集身份证
- **LGD-II 有证**：每个系统都有 pivotal 临床试验报告、性能基线、PMS 计划、不良事件台账（MIR/MDR 上报）
- **LGD-III 有门禁**：每个系统都是 locked model，变更需重新申报；LGD 主张的"持续核验门禁"在 locked model 上是自然满足的（无需 PCCP 因为无变更），但**未来 adaptive model 部署时，LGD 的持续门禁要求将成为差异化的关键控制点**

#### 6.1.5 案例对论文的支撑点

Steven 硕士论文可以在第 4 章"LGD 在 AI 糖网筛查的应用"写：locked model 自然满足 LGD-III；adaptive model（未来趋势）将需要 PCCP + LGD 持续核验门禁双重保障。这一对比正好凸显 LGD 在 adaptive AI 时代的独特价值。

### 6.2 骨科 AI：手术规划、导航与个性化假体

#### 6.2.1 VTS 智能导航（American Joint 早期代表）

| 维度 | 内容 |
|------|------|
| 产品形态 | 术中实时导航软件 + 影像采集硬件 |
| 授权路径 | FDA 510(k)；CE；多市场授权 |
| LGD 三律落点 | I（产品籍+软件版本）、II（术中精度证据、风险登记）、III（变更控制门禁）|

#### 6.2.2 长木谷 ROPA（中国骨科手术机器人代表）

| 维度 | 内容 |
|------|------|
| 产品形态 | 全髋/全膝置换手术机器人，含 AI 规划模块 |
| 授权路径 | NMPA 三类医械注册证 |
| 关键特性 | 个性化假体规划、术中实时调整、术后数据闭环 |
| LGD 三律落点 | I（产品籍+AI 算法版本+个性化方案籍）、II（术中规划-执行一致性证据、术后随访数据）、III（变更控制门禁，NMPA 三类变更注册）|

#### 6.2.3 3D 打印个性化假体（典型）

| 维度 | 内容 |
|------|------|
| 产品形态 | 患者特异性骨缺损修复假体（颅骨、骨盆、长骨）|
| 授权路径 | NMPA 三类定制式医械；FDA 510(k) patient-matched |
| 关键挑战 | 每件都是"唯一的"——传统 batch 注册模式失效 |
| LGD 三律落点 | I（每件假体独立 UDI、患者身份证、CT 数据档案）、II（每件的设计-打印-检验证据）、III（生产放行门禁——每件都要临床放行）|

**关键洞察**：3D 打印个性化假体是 LGD "凡造必登"的最强实证——传统 UDI 模式（按型号批量登记）失效，必须按件登记。LGD 主张的"凡造必登"在个性化医械域是工程必需，不是过度要求。

#### 6.2.4 骨科 AI 的特殊挑战与 LGD 的应对

| 挑战 | LGD 应对 |
|------|---------|
| 算法版本 vs 数据版本 vs 假体版本三重版本管理 | LGD-I 要求三类籍分别登记（产品籍+数据籍+模型籍）|
| 术中实时调整如何留证 | LGD-II 要求术中决策留证据工件（调整日志、影像快照）|
| 个性化方案如何走门禁 | LGD-III 要求每件假体术前术后两次放行（术前方案门禁 + 术后质控门禁）|
| 长期随访数据回流 | LGD-III 要求随访数据作为下次放行的输入——门禁是闭环的 |

### 6.3 案例综合观察

1. **locked AI 模型自然满足 LGD-III**（如 IDx-DR、EyeArt），但 adaptive AI 模型需要 LGD 的"持续核验门禁"作为差异化控制点（这就是 PCCP 之外 LGD 的独特贡献）
2. **个性化医械是 LGD-I "凡造必登"的最强实证**（3D 打印假体按件登记）
3. **骨科 AI 术中决策的留证挑战**凸显 LGD-II "关键决策留证据"在实时场景的工程难度
4. **案例为硕士论文提供"具体到产品级"的实证底稿**——比纯理论叙事更有说服力

---

## 7. LGD 独特价值定位与差异化贡献

### 7.1 LGD 母版自陈的"收口层"定位

LGD 母版 §6 "诚实边界"明示：**"LGD 是收口层，不替代既有理论；身份（UBIC）、证据（XCGS）、门禁（A³）、真实参照（RRM）、抗编造（AFG）等各自主张独立成立；LGD 只提供把它们咬合成生命周期主线的组织叙事。"**

在医械域，这一定位转化为：**LGD 不替代 ISO 13485/42001/14971、不替代 FDA TPLC/PCCP、不替代 EU AI Act/MDR、不替代 NIST AI RMF——但提供把所有这些咬合成贯穿 TPLC 五阶段主轴的组织叙事。**

### 7.2 LGD 在医械域的四个独特贡献点

**贡献点 1：持续核验门禁（Continuous Verification Gate, CVG）**

PCCP 只覆盖事先声明的变更；PMS 只在事后发现；二者之间存在"变更区间"门禁空白。**须精确限定**：现有框架并非完全不做逐次授权——**EU MDR 对"显著变更"已要求经公告机构事先批准**（Annex IX §2.4/§4.10；MDCG 2020-3），FDA 对 PCCP 声明范围内变更亦有事先审评通道；本主张的落点是**PCCP 声明范围之外的非显著变更**。对该区间，**尚无框架要求由签发权属人实施逐次授权门禁**。LGD-III 有门禁主张：该区间的每次能力升级、改版、扩权、行为变更，都过"触发评估—评分放行—事后复盘"三段式门禁，签发权属人。

**与最近邻工作的区分（依撞车审查第二轮指令）**：AEGIS（Afdideh, Astaraki, Seoane; Karolinska SMAILE, arXiv:2603.22322, 2026-03）已实现"对每一次模型迭代输出四类部署决策"的可执行基础设施，是本主张迄今最近的学术邻居 [B-52]。区分轴有二：**①授权主体**——AEGIS 的部署决策由条件决策模块**自动**产生（规则驱动），CVG 要求决策由**签发权属人**作出并可追溯归责；**②主张层级**——AEGIS 是 operationalize PCCP/PMS 的执行基础设施（工程实现），CVG 是跨框架的监管基线规范主张。AEGIS 证明了"决策通道与监控通道分离"在工程上可行，CVG 把该"决策点"升级为"授权点"。

这是 LGD 在现有框架之上的差异化贡献点——也是硕士论文最值得展开的核心创新。

**贡献点 2：三类籍（产品籍+数据籍+模型籍）的统一户籍层**

传统医械监管的"籍"是产品籍（UDI）。AI 模型带来了两类新增籍——数据籍（训练数据身份）和模型籍（模型本身身份）。现有 PCCP/GMLP 部分覆盖这两类，但没有一个统一户籍层把它们与产品籍咬合。LGD-I 有籍的"凡造必登"主张提供了这个统一层。

**贡献点 3：证据工件六类清单的贯穿要求**

市面 AI 治理框架多提"可审计"但少有完整枚举"关键决策的证据工件清单"。LGD 母版列了六类：决策日志、风险登记、模型/产品档案、变更记录、人类监督证明、事件台账——映射矩阵显示这六类在 TPLC 每个阶段都有具体落地点。LGD 的贡献是"枚举完整 + 贯穿要求"。

**贡献点 4：跨域可复用的同构母版**

医械是 LGD 的"主母版"，但 LGD 母版 §1 推论 3 明示：**"同一主干可实例化到不同受监管领域（金融、自动驾驶、机器人、数据要素……），每域取其自身母版完成映射。"** 这意味着 LGD 在医械域的方法论可平移到其它域，而其它域的实证反过来又强化 LGD 的"通用全程治理学说"地位。

### 7.3 与现有框架的差异化对照表

| 维度 | FDA TPLC | FDA PCCP | EU AI Act | ISO 13485 | NIST AI RMF | **LGD** |
|------|---------|---------|-----------|-----------|-------------|---------|
| 阶段覆盖 | S1-S5 | S5 局部 | S1-S5 | S3+S5 | S1-S5 | **S1-S5 + 横向三律贯穿** |
| 贯穿主轴 | 部分（按阶段）| 无 | 部分（按风险）| 部分（按 QMS）| 部分（按风险功能）| **明确贯穿三律** |
| 三类籍统一登记 | 部分 | 部分 | 部分 | 仅产品籍 | 部分 | **强制三类籍统一** |
| 证据工件清单 | 部分 | 部分 | 部分 | 部分 | 部分 | **六类完整枚举** |
| 持续核验门禁（非显著变更区间） | 无 | 仅事先声明变更 | 部分[^1] | 仅 QMS 内 | 部分 | **强制该区间过签发权属人门禁** |
| 跨域可复用 | 否 | 否 | 否 | 否 | 否 | **是** |
| 收口层定位 | 否 | 否 | 否 | 否 | 否 | **是** |

[^1]: EU MDR 对"显著变更"要求公告机构事先批准（Annex IX §2.4/§4.10；MDCG 2020-3），故本表记"部分"；对**非显著变更**则落入 QMS 自查——这正是本表所指的门禁空白区间。学术侧近邻 AEGIS（arXiv:2603.22322）[B-52] 对每次迭代输出**自动**部署决策，属工程实现层而非授权归属主张，故不计入"已完成逐次授权门禁"。

**结论**：LGD 不替代任何现有框架，但提供了一条现有框架都未占据的"贯穿主轴 + 三律贯穿 + 非显著变更区间的持续核验门禁"位置。这是 LGD 的差异化独特价值，也是硕士论文的核心创新论点。

---

## 8. 对硕士论文的支撑映射

### 8.1 与硕士论文 v1.1 章节框架的对齐

硕士论文 v1.1 规划的医工交叉类章节框架（8 章 7 万字）：

| 章节 | 内容 | 本调研的支撑点 |
|------|------|---------------|
| 第 1 章 引言 | 研究背景、问题、目标 | §1 调研背景与目标 |
| 第 2 章 文献综述 | LGD 母版 + 现有医械治理框架 | §2 LGD 三律与映射理论 + §5 国际框架对齐 |
| 第 3 章 LGD 三律与既有医械治理框架的对齐 | 三律在 TPLC 五阶段的映射 | §3 SaMD TPLC 模型 + §4 映射矩阵 |
| 第 4 章 LGD 在 AI 影像的应用 | 糖网筛查案例 | §6.1 IDx-DR/EyeArt 案例 |
| 第 5 章 LGD 在骨科 AI 的应用 | 个性化假体+导航案例 | §6.2 骨科 AI 案例 |
| 第 6 章 LGD 独特价值与差异化贡献 | 持续核验门禁 CVG + 三类籍 | §7 独特价值定位 |
| 第 7 章 讨论与展望 | 跨域可复用、未来 adaptive AI | §7.2 贡献点 4 + §8.3 |
| 第 8 章 结论 | 研究结论与局限 | 综合全调研 |

### 8.2 立即可启动 5 项中第 1、3 项的直接依据

**第 1 项（文献综述 120 篇池）**：本调研引用的监管框架与案例可作为 120 篇池的核心种子：
- FDA 文档（TPLC、PCCP Final、GMLP、AI-DSF Guidance、510(k) Database）
- EU 文档（AI Act、MDR、MDCG 2025-6、Digital Omnibus）
- ISO/IEC 标准（13485、42001、14971、62304、62366、AAMI CR34971）
- NIST（AI RMF 1.0、AI RMF 医疗剖面）
- 中国（GB-Z 185、NMPA 2022/2023 指南、47 号令）
- 学术论文（Gulshan JAMA 2016、Abramoff Eye 2023、Nature Medicine AI 医械综述）
- 案例文档（IDx-DR DEN180001 授权文件、EyeArt K200667 授权文件、长木谷 ROPA 注册证）

**第 3 项（LGD 三律→SaMD TPLC 映射图）**：本调研 §4 映射矩阵是映射图的数据源；§4.2 三个洞察是映射图的注解文字。

### 8.3 论文未来可扩展方向（基于本调研发现）

1. **持续核验门禁（CVG）的工程实现**：把 LGD-III 的"触发评估—评分放行—事后复盘"三段式门禁做成具体技术架构（门禁引擎、签发 API、复盘日志格式）
2. **三类籍的统一 schema**：把产品籍（UDI）、数据籍（数据集身份证）、模型籍（模型卡）合并为统一的 AI 医械户籍 schema，作为 LGD-I 的工程落地
3. **adaptive AI 的 LGD 治理**：当 IDx-DR、EyeArt 等系统从 locked model 演进为 adaptive model 时，LGD 的持续核验门禁如何与 PCCP 协同——这是未来 adaptive AI 治理的关键问题
4. **跨域平移实证**：把医械域的 LGD 方法论平移到金融 AI、自动驾驶、机器人等域，做对比实证

### 8.4 论文写作的两个建议

1. **第 4、5 章按"案例 → LGD 三律落点 → 独特价值"三段式展开**，每章 8000-10000 字，给两个案例（影像、骨科）足够深度
2. **第 6 章作为论文核心创新**，重点写"持续核验门禁 CVG"作为 LGD 区别于 PCCP/PMS 的差异化贡献——这是论文最值得审稿人记住的一句话

---

## 9. 引用清单（一手标准与监管文档）

### 9.1 FDA 系列
- FDA. *Software as a Medical Device (SaMD): Clinical Evaluation.* IMDRF, 2017.
- FDA. *Developing a Software as a Medical Device Action Plan.* 2021.
- FDA. *Artificial Intelligence/Machine Learning-Based Software as a Medical Device Action Plan.* 2021.
- FDA. *Predetermined Change Control Plan (PCCP) Final Guidance.* 2025.
- FDA/Health Canada/MHRA. *Good Machine Learning Practice for Medical Device Development: Guiding Principles.* 2021.
- FDA. *Artificial Intelligence-Enabled Software as a Medical Device.* Draft Guidance, 2023.
- FDA De Novo Database, DEN180001 (IDx-DR).
- FDA 510(k) Database, K200667 (EyeArt).

### 9.2 EU 系列
- EU. *Regulation (EU) 2024/1689 (AI Act).* 2024.
- EU. *Regulation (EU) 2017/745 (MDR).* 2017.
- MDCG 2025-6. *Medical Device AI (MDAI) Definition and Conformity Assessment.*
- EU. *Digital Omnibus Simplification Package.* 2025.

### 9.3 ISO/IEC/AAMI 系列
- ISO 13485:2016. *Medical devices – Quality management systems.*
- ISO/IEC 42001:2023. *Information technology – Artificial intelligence management system.*
- ISO 14971:2019. *Application of risk management to medical devices.*
- IEC 62304:2015. *Medical device software – Software life cycle processes.*
- IEC 62366-1:2015. *Medical devices – Application of usability engineering.*
- AAMI CR34971:2023. *Application of ISO 14971 to AI/ML medical devices.*

### 9.4 NIST 系列
- NIST AI 100-1.0. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* 2023.
- NIST AI Safety Institute Consortium. *Healthcare Profile (Draft).* 2024.

### 9.5 中国系列
- 国家市场监督管理总局令第 47 号. *医疗器械注册与备案管理办法.* 2021.
- NMPA. *人工智能医用软件产品分类界定指导原则.* 2022.
- NMPA. *人工智能医疗器械注册审查指导原则（2023）.*
- GB/T 42062-2022（等同 ISO 14971:2019）.
- GB-Z 185 系列人工智能医疗器械推荐性标准.

### 9.6 学术与案例文献
- Gulshan V, et al. *Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy.* JAMA, 2016.
- Abramoff MD, et al. *Pivotal trial of an autonomous AI diagnostic system for diabetic retinopathy.* EyeArt pivotal trial, 2023.
- FDA CDRH. *Artificial Intelligence/Machine Learning-Enabled Medical Devices.* 公开数据库, 2025.
- IDx-DR Pivotal Study. *IDX-200 Multi-Reader Multi-Case Study Report.*
- EyePACS Real-World Performance Reports. 2020-2024.
- 长木谷 ROPA. *NMPA 三类医疗器械注册证公开信息.*
- VTS Smart Navigation. *FDA 510(k) Clearance Records.*
- **[B-52]** Afdideh M, Astaraki M, Seoane J. *An Operational Infrastructure for Post-Market Governance of Adaptive Medical AI Under US and EU Regulations (AEGIS).* arXiv:2603.22322, 2026-03. https://arxiv.org/abs/2603.22322 （撞车审查第二轮回填；本报告 §7.2 贡献点 1 已按指令显式区分）
- Rosen R, Mandl KD. *Regulating Flexibility for AI: FDA Experience with PCCPs.* medRxiv 2025.08.26.25334477 （= [B-46]）
- Dayma et al. *PCCP Adoption and Documentation Transparency in FDA-cleared Radiology AI Devices.* Radiol Artif Intell 2026;8(5). https://pubs.rsna.org/doi/full/10.1148/ryai.260385 （= [B-48]）

### 9.7 LGD 自身系列（自引）
- Zhao, X. *Lifecycle Governance Doctrine (LGD): Registry, Evidence, and Gates Across the Full Life of AI and Devices.* MedXpert × SynomosAI. v1.0, 2026-09-06. ORCID 0009-0001-0512-1237.
- Zhao, X. *医疗器械注册全程方法论 · LGD 域理论系列 #14 (TH-MED-002).* v1.0, 2026-09-06.
- Zhao, X. *LGD Global Standards Alignment.* v1.0.

---

## 10. 后续路线（行动清单）

| 优先级 | 行动 | 关联 LGD 文档 | 死线 |
|--------|------|--------------|------|
| 高 | 把本调研映射矩阵转成可视化映射图 SVG | §4 矩阵 + show_widget | M1（2026-10）|
| 高 | 把 IDx-DR/EyeArt 案例做成详细"案例 → 三律落点"对照表 | §6.1 + LGD-MED-002 | M2（2026-11）|
| 中 | 把本调研精炼为硕士论文第 3、4、5 章的初稿 | 论文 v1.1 | M3-M4（2026-12 ~ 2027-01）|
| 中 | 把本调研推送为 GitHub lgd-theory 新 release（医械 AI 实证版）| 待 Zenodo v2 DOI | M5（2027-02）|
| 低 | adaptive AI 的 LGD 持续核验门禁工程实现路线 | §7.2 + §8.3 | M6 后（论文后）|

---

© MedXpert × SynomosAI · CC BY 4.0 · 2026-09-13
*本件为理论调研文档，非监管申报材料、非法律意见、非认证证书。法规条目为稳定公开名称，具体条款版本以监管官网原文为准。*
