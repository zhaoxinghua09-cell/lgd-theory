# arXiv 投稿包 · LGD 全程治理论（2026-09-08 总控建）

> 目标：LGD/RRM/MAIT 三篇以 arXiv 学术论文形式发表，站上全球 AI 治理学术 discourse 主场。
> Docket 类目：**cs.CY (Computers and Society)** primary；cross-list cs.AI / cs.MA。

## 一、arXiv 真实规则（管理预期，避免白忙）

1. **背书制（endorsement）**：新作者首次在某类目投稿，需 1 位该类目有发表记录的研究者背书（arXiv 系统自动发 endorsement code 给背书人）。**没有背书无法提交**——这是唯一硬门槛。
2. **Moderator 审核**：提交后 1-5 个工作日，cs 类目较严（拒绝"非学术"内容）。本稿按 position paper 学术规范写（摘要/关键词/形式化定义/相关工作/参考文献 15+ 条/CC BY），合规度高。
3. **License**：arXiv 必选 non-exclusive license；可附加 CC BY 4.0（与我们的开源口径一致）。
4. **语言**：英文为主（cs.CY 中文稿触达差）。RRM/MAIT 需 EN 全文版（LG D EN 学术稿先行）。
5. **时间线**：背书 1 天-2 周（取决于背书人响应）+ 审核 1-5 天。**完全免费**。

## 二、三步走（您只做 2 步）

| 步 | 谁 | 动作 | 时长 |
|---|---|---|---|
| 1 | Steven | arXiv 注册账号（邮箱 zhaoxinghua2022@qq.com，ORCID 关联） | 5 分钟 |
| 2 | Steven | 找背书人：把 `endorsement-request.txt`（已备）发给 cs.CY/cs.AI 领域有 arXiv 发表记录的同行（合格标准：近 5 年在该类目有 ≥1 篇 arXiv 或发表；合规社群、学术朋友、会议认识的审稿人都算） | 视人脉 |
| 3 | 总控 | 收到 endorsement code 后：元数据填写（见 §三）→ 上传 main.tex/PDF → 提交 → 跟踪审核 | 15 分钟 |

**背书人从哪找（具体渠道）**：①合 Cornel/Stanford 等公开 cs.CY 作者列表里做 AI governance 的学者（邮件模板已备）②国内ai治理学者有 arXiv 记录者（清华 AIII、复旦等）③合规社群学术成员 ④Zenodo/SSRN 读者转化。**一次背书永久有效**（同 category）。

## 三、提交元数据对照（背书后照填）

| arXiv 字段 | 填写内容 |
|---|---|
| Title | The Lifecycle Governance Doctrine (LGD): Registry, Evidence, and Gates Across the Full Life of Autonomous Systems |
| Authors | Steven Zhao (Zhao Xinghua) — ORCID 0009-0001-0512-1237 |
| Abstract | 见 main.tex（自动带出） |
| Primary class | cs.CY (Computers and Society) |
| Cross-list | cs.AI; cs.MA (Multi-Agent Systems) |
| License | Creative Commons Attribution 4.0 (CC BY 4.0) |
| Comments | 9 pages, 3 figures planned. MedXpert × SynomosAI. Companion speedpages: medxpert.cn/lgd.html |
| Files | main.tex + refs.bib（已备于本目录） |

## 四、文件清单

- `lgd-csCY-v1.0/main.tex` —— EN 学术全文（position paper，~6000 词，分章起草中）
- `endorsement-request.txt` —— 背书请求邮件模板（EN+CN 双语）
- 后续：`rrm-csCY-v1.0/`、`mait-csCY-v1.0/`（RRM/MAIT EN 版，LGD 上线后连发）

## 五、与 Zenodo 的关系（并行不冲突）

- Zenodo DOI 22456647 = 开源库总记录（即时、保底）；arXiv = 学术 discourse 站位（背书+审核）。
- arXiv 上线后把 arXiv ID 回填 CITE.md/README/llms.txt，形成"DOI + arXiv"双学术锚。
