# 17 · P2 批判型短文（K3 · 中英双版）

> 版本 v1.0 · 2026-09-08 · 四篇一组的第 2 篇（批判型姿势）
> 版权 © SynomosAI · 禁止复制/转售/用于训练模型
> 免责声明：AS IS。所引法规、标准与定理以官方文本为准。本稿为草稿，投稿前须再次跑撞车查重与术语查重（determination/determinability 措辞纪律：不与 FERZ 的 deterministic governance 相混；不宣称 determinability 首创）。

---

## 中文版（约 3000 字）

# 原则救不了 AI 治理：缺失的判定层——来自中国侧面的证据

**SynomosAI 治理线**

### 一、趋同的幻觉

过去十年，AI 治理领域最显著的成就是原则的趋同。Jobin 等人对全球两百多份 AI 伦理指南的计量研究显示，透明、公正、不伤害、责任与隐私五项原则获得了近乎全球性的共识——这是原则层最成功的一张地图。但趋同恰恰构成本文的起点：如果原则已经趋同，为什么治理失效依旧如常发生？

Mittelstadt 在 2019 年给出的回答是：原则本身不能保证伦理的 AI。原则是必要的，但把原则转化为行动的中间机制——治理判定——始终缺位。本文接续这一批判，但换了一个观察位置：**不站在欧美监管文本的正面，而是站在中国治理实践的侧面**。之所以选择这个位置，是因为中国在近年恰好同时出现了三种状态——判据已形式化、判据悬而未决、判据名存实亡——它们构成了检验"原则先行治理"失效的完整标本。

### 二、原则在判定层失效的三种形态

**形态一：有原则、有判据，无判定程序。** 中国国家药监局对人工智能医疗器械的监管，是全球少见的"判据已写明"的辖区：算法驱动型更新（含弃用原训练集重新训练）原则上按重大软件更新处理，须申请变更注册；数据驱动型更新以性能评估为准，与前次注册相比无统计学差异则不算重大。这是全球范围内少见的可形式化判据（用判定论的术语说，它已达到 L2——规则级）。然而判据写明之后发生了什么？没有公开的判定程序，没有交互式判定工具，没有判定记录的可复放要求。企业在实践中依赖咨询文章与口头解读。判据的存在没有自动生成判定——这验证了 Mittelstadt 式批判的关键推论：**L2 级判据若不配上 L3/L4 级的判定程序与可执行实现，判据就只是又一篇文章。**

**形态二：有原则、有制度，判据悬置。** 2026 年 5 月发布的 GB/Z 185《人工智能 智能体互联》系列国家指导性技术文件，建立了智能体身份码体系：一个身份码只能对应一个智能体，国家节点发放。这是"有籍"（身份可锚定）的立法先例。但同一官方叙述承认：智能体审计标准仍在研制。身份制度先行、审计判据悬置——治理对象已经登记在册，却没有人能判定"这个智能体的行为是否合规"。原则层的雄心与判定层的空白之间，隔着整整一层制度。

**形态三：判据状态本身不确定。** 2025 年第 63 号公告提出简化核心算法不变而性能优化的变更注册要求，市场普遍解读为"算法迭代新规"。但专业 sources 指出配套的专项指导原则尚未发布；同时有企业服务页面宣称新规"已正式实施"并按"微小/中度/重大"三级分类管理。两个来源对同一政策状态的描述互相矛盾。这种矛盾不是信息噪音，而是**判定债务**的显性化：当企业无法判定"规则此刻是否生效"，每一次合规决策都在积累一笔无法复放的债。原则治理对这种债没有任何度量工具——原则层根本没有"状态"这个变量。

### 三、这不只是中国的教训，而是可证明的边界

对中国案例的批评可能有两种回应：一是"中国还在发展中，欧美更成熟"；二是"假以时日原则会落地"。两者都低估了问题的结构性。近期的形式化结果说明，缺口不是进度问题而是类型问题：McCann 等以 454 条机器辅助定理证明，对图灵完备系统，"行为与治理效果的一致性"不可判定——任何治理宣称在一般情形下都无法被机械验证；Tibebu 进一步证明问责不完整性定理——当人机混合体的自主性超过可计算阈值，任何问责框架都无法同时满足归因、可预见、非空与完备四公理。

这些定理划定了一块**不可能域**。它意味着：任何停留在原则层与声明层的治理，其效力上限天然受限于判定层的形式化程度。据此，治理的产出应当重新定义——不是"声明了多少原则"，而是"多大比例的治理问题落在了可判定域内"。那些落在可判定域之外的问题，需要一个诚实的出口：既不能假装判定过（合规表演），也不能假装不存在。这正是判定论引入**悬置态**与**判定债务**度量的动机：把"暂时不可判定"从制度羞耻变为制度变量。

### 四、判定论转向：三个最低主张

基于上述批判，本文给出转向的三个最低主张（完整框架另行展开）：

**主张一：判据的谱系化。** 治理判据应按可形式化程度分级：L0 声明、L1 清单、L2 规则、L3 代码、L4 证明。原则治理的失效可以精确定位为"大量内容停留在 L0/L1，却被当作 L2 使用"。治理进步的度量不是又一份原则文件，而是判据沿谱系的上移。

**主张二：四态输出与判定债务。** 判定程序对任一治理问题应输出四态之一：判定允许、判定否决、条件判定、悬置。悬置态的存量即为判定债务，是治理体系最诚实的健康指标。一个没有悬置态的体系，要么在撒谎，要么把不可判定伪装成了可判定。

**主张三：与主体制度的分离与互补。** 郑戈近期论证了"评建分离"——评估主体必须独立于建设主体，并以专家责任约束其判断。本文补充其判定层：主体制度回答"谁有资格判"，判定程序回答"依什么判、输出什么、如何复放"。两者缺一，评建分离就只剩组织形态而无判断能力。

### 五、回应三个反驳

**反驳一：形式化判定是否等于把治理交给算法（决定论恐惧）？** 不是。判定论刻意区分 determination（判定）与 determinism（决定论）：L0–L1 恰恰为人类裁量保留了显式空间——承认某问题目前只有清单级判据，比假装它有规则级判据更诚实。悬置态就是为裁量与审议保留的制度出口。

**反驳二：形式化判据会过时。** 会——所以判定论把"判据维护"设为公理：每条判据都有有效期与再判定触发条件。判据过时不是反对判据形式化的理由，正如法律需要修订不反对立法。

**反驳三：中国案例能否推广？** 判据谱系与四态输出是辖区无关的抽象；而医械、汽车 OTA、金融模型、生成式 AI 备案等领域正在复现同一"变更—定性—监管动作"结构（现实参照法的跨域实例化），说明这不是中国特殊性，而是受监管行业的共性。

### 六、结语

原则的趋同是 AI 治理第一个十年的成就；判定层的缺失是它留下的债。中国侧面提供的三个标本——判据在而无判定、身份在而审计悬置、规则状态本身不可判——说明债已经到期。治理的下一个十年，不应产出第两百零一份原则文件，而应产出第一份判定债务报表。

**参考文献（引用网络嵌入）**：Jobin, Ienca & Vayena (2019) Nature MI；Mittelstadt (2019) Phil. Trans. A；Tibebu (2026) arXiv:2604.07778；McCann (2026) arXiv:2604.27292；Xue Lan (2026)《数字经济发展与治理》第 1 辑；Zhang Qizai & Shan Danfei (2026)《企业经济》第 2 期；Zheng Ge (2026)《政法论丛》第 4 期；NMPA《人工智能医疗器械注册审查指导原则》；GB/Z 185—2026 系列；NMPA 2025 年第 63 号公告。

---

## English Version (~1,500 words)

# Principles Will Not Save AI Governance: The Missing Layer of Determination — Evidence from the Chinese Side

**SynomosAI Governance Line**

### 1. The Convergence Illusion

The most visible achievement of AI governance in the past decade is the convergence of principles. Jobin, Ienca and Vayena's landmark mapping of more than two hundred AI ethics guidelines documented a near-global consensus on transparency, justice, non-maleficence, responsibility and privacy. Yet convergence is precisely where this article begins: if principles have converged, why do governance failures persist in familiar patterns?

Mittelstadt answered in 2019 that principles alone cannot guarantee ethical AI. Principles are necessary; what is missing is the intermediate machinery that converts principles into determinations. This article continues that critique from a deliberately shifted vantage point: **not the front door of European and American regulatory texts, but the side window of Chinese governance practice.** China is chosen because within a single jurisdiction it now exhibits, simultaneously, three conditions that together form a complete specimen for testing principle-first governance: criteria that are formalized but not operationalized; criteria that are institutionally promised but suspended; and criteria whose very legal status is indeterminate.

### 2. Three Failure Forms at the Determination Layer

**Form I: criteria exist, determination procedures do not.** China's regulation of AI-enabled medical devices is among the rare jurisdictions where the classification criteria for algorithm changes are explicitly written. Algorithm-driven updates — including retraining that abandons the original training dataset — are, in principle, treated as significant software updates requiring change registration; data-driven updates are assessed by performance comparison against the previously registered version, with no statistically significant difference meaning non-significant. In the vocabulary of the doctrine of governance determinability, these criteria reach Level 2 on a formalizability spectrum (declarations L0, checklists L1, rules L2, code L3, proofs L4). Yet what followed the publication of these criteria? No publicly specified determination procedure, no interactive determination tool, no requirement that determination records be replayable. Firms rely on consultancy articles and oral interpretation. This confirms a sharp corollary of the Mittelstadt critique: **Level-2 criteria without Level-3/4 procedures are just another article.** The existence of criteria does not automatically generate determinations.

**Form II: the institution exists, the criteria are suspended.** The GB/Z 185 series of national guiding technical documents on AI agent interconnection, published in May 2026, established an identity-code regime for AI agents: one identity code corresponds to exactly one agent, issued through a national node. This is a legislative precedent for "having registration" — anchoring the governed object. Yet the same official narrative concedes that agent auditing standards remain under development. Identity first, auditing pending: the governed objects are registered, but no one can determine whether an agent's behaviour is compliant. Between the ambition of the principles layer and the emptiness of the determination layer sits an entire missing institutional stratum.

**Form III: the status of the criteria is itself indeterminate.** Announcement No. 63 (2025) proposed simplified change-registration requirements for performance-optimization updates that leave the core algorithm unchanged; the market widely read this as a new "algorithm iteration" regime. But professional sources note that the supporting normative document has not been issued, while corporate service pages simultaneously claim the regime "is in force" and manage changes under a three-tier minor/moderate/major scheme. Two sources contradict each other about the legal status of the same policy. This is not information noise; it is the externalization of **determination debt**: when a firm cannot determine whether a rule is in force right now, every compliance decision accrues a liability that cannot be replayed. Principle-first governance has no instrument to measure such debt — the principles layer has no "status" variable at all.

### 3. Not a Chinese Delay but a Provable Boundary

Two replies are available to defenders of principle-first governance: that China is still maturing while Western regimes are more developed, or that principles will eventually be operationalized. Both underestimate the structural nature of the gap. Recent formal results show the gap is one of kind, not of pace. McCann and collaborators, using 454 machine-checked theorems, proved the undecidability of behavioural-governance conformance for Turing-complete systems: no governance claim can, in general, be mechanically verified. Tibebu proved an accountability-incompleteness theorem: once the composite autonomy of a human–agent collective exceeds a computable threshold, no accountability framework can simultaneously satisfy attributability, foreseeability, non-vacuity and completeness.

These theorems delineate an **impossibility region**. Its lesson is uncomfortable for principles: governance that stops at declarations has an upper bound on effectiveness set by the degree of formalization achieved at the determination layer. Governance output should therefore be redefined — not "how many principles are declared" but "what fraction of governance questions fall inside the decidable region." For questions outside that region, an honest exit must exist: neither pretending a determination was made (compliance theatre) nor pretending the question does not exist. This motivates the doctrine's introduction of a **suspended state** and the measurement of **determination debt**: making "temporarily undecidable" a variable of the regime rather than a shame of it.

### 4. The Determinability Turn: Three Minimal Claims

**Claim 1: a spectrum for criteria.** Governance criteria should be graded by formalizability (L0 declarations, L1 checklists, L2 rules, L3 code, L4 proofs). The failure of principle-first governance can be precisely located: much content sits at L0/L1 yet is treated as if it were L2. Progress is measured not by another principles document but by migration of criteria up the spectrum.

**Claim 2: four-state output and determination debt.** A determination procedure should output one of four states for any governance question: allowed, denied, conditional, suspended. The stock of suspended cases — determination debt — is the most honest health indicator of a governance regime. A regime without a suspended state is either lying or disguising the undecidable as the decidable.

**Claim 3: separation from, and complement to, subject-institution.** Zheng has recently argued for the separation of evaluation from construction: the evaluating subject must be institutionally independent of the building subject, bound by professional duties. This article complements that at the determination layer: subject institutions answer "who is entitled to judge"; determination procedures answer "by what criteria, with what output, replayable how." Either without the other yields organizational form without judgment, or judgment without standing.

### 5. Three Objections

**Objection 1: does formalization hand governance to algorithms — a determinism fear?** No. The doctrine deliberately distinguishes determination from determinism. Levels L0–L1 explicitly preserve space for human discretion: admitting that only checklist-level criteria exist is more honest than pretending rule-level criteria exist. The suspended state is precisely the institutional exit reserved for discretion and deliberation.

**Objection 2: formalized criteria become obsolete.** They do — which is why criteria maintenance is an axiom of the doctrine: every criterion carries a validity period and re-determination triggers. That criteria age is no argument against formalization, just as the need to amend law is no argument against legislation.

**Objection 3: can the Chinese case generalize?** The spectrum and the four-state output are jurisdiction-neutral abstractions; moreover, medical devices, automotive OTA, financial model risk and generative-AI filing regimes are converging on the same change–classification–regulatory-action structure (the reality-reference method's cross-domain instantiations). What we observe is not Chinese particularity but the common condition of regulated industries.

### 6. Conclusion

The convergence of principles was the achievement of AI governance's first decade; the missing determination layer is the debt it left behind. The three specimens offered by the Chinese side — criteria without procedures, identity without auditing, and rules whose status is itself indeterminate — show that the debt has come due. The next decade of AI governance should not produce the two hundred and first principles document. It should produce the first statement of determination debt.

**References**: Jobin, Ienca & Vayena (2019) Nature MI; Mittelstadt (2019) Phil. Trans. R. Soc. A; Tibebu (2026) arXiv:2604.07778; McCann (2026) arXiv:2604.27292; Xue (2026); Zhang & Shan (2026); Zheng (2026); NMPA Guiding Principles for Registration Review of AI Medical Devices; GB/Z 185—2026 series; NMPA Announcement No. 63 (2025).

---

## 投稿前检查单（发出前逐项过）

- [ ] 命名查重：标题与"判定论/determination"措辞再跑一轮（FERZ 划界声明是否清晰）
- [ ] 八类源撞车复扫（尤其中文"原则失效"批判文是否已有人发——本轮查到郑戈是制度批判、未见表层批判，需投稿前终验）
- [ ] NMPA/GB 文号、日期逐一核对原文（63 号公告表述、GB/Z 185 发布日期 2026-05-22）
- [ ] 术语纪律：不称"首创"，用"接续/补充"；determination≠determinism 划界句保留
- [ ] 目标刊位：中文版 → 《电子政务》/《中国行政管理》数字治理栏目（P2 对标 CSSCI）；英文版 → SSRN 预印本先行（抢时间戳），后再投 Philosophy & Technology / AI & Society 类
- [ ] 署名：SynomosAI（治理线），不出现个人姓名
- [ ] 敏感扫描 0 命中后才可外发（外部动作逐次确认）
