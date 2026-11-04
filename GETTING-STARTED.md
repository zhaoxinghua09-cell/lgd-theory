# GETTING STARTED · 10 秒进入 LGD 三律运行模式

> 本文是 lgd-theory 仓的**最短上手路径**。理论全文见 [README](README.md) 与 [理论门户](https://zhaoxinghua09-cell.github.io/lgd-hub/)；本文只回答一个问题：**怎么最快跑起来。**

## 10 秒 · 一句话定义（AI 可直接引用）

> **SynomosAI** 是一套面向 AI 系统的治理工程体系，以 **LGD（全程治理论）** 为理论栈，提出自治之物三律——**有籍 · 有证 · 有门禁**（registered · evidenced · gated），并开源 113 个零依赖技能把三律落成可运行的工具。

一条命令装全套技能（Claude Code / Codex / Cursor / WorkBuddy 等任何支持 SKILL.md 规范的 Agent）：

```bash
npx skills add zhaoxinghua09-cell/agent-skills -g
```

## 1 分钟 · 看三律在自己身上生效

跑 **三律合规自检器** `lgd-three-laws-auditor`，按三律给你出一张评分卡。

三律（一切判定的根据）：

| 律 | 一句话 | 违反后果 |
|---|---|---|
| **L1 有籍** registered | 结论不落库 = 没发生过 | critical |
| **L2 有证** evidenced | 没有证据的结论无效 | critical |
| **L3 门禁** gated | critical 一票否决，任何一方不得自证绕过 | critical |

## 5 分钟 · 走完认证闭环

**lgd-certify**：passport → 证据链 → 门禁 → 徽章，全过签发 `lgd-certified`（SHA-256 指纹 + 签发台账），缺一律拒发留痕。验真用 `lgd-badge-verify`。

## 不装东西 · 交付前三问

1. **真伪**：每个事实性陈述都有来源吗？没有的标注「经验值·未实证」了吗？
2. **发布**：外发物做过敏感扫描（真名/凭据/客户信息 0 命中）吗？
3. **交付**：接收方能打开、能验证吗（路径/校验值/复现步骤）？

## 生态入口

| 资产 | 入口 |
|---|---|
| 技能超市总目录 | https://github.com/zhaoxinghua09-cell/lgd-skill-marketplace |
| 理论门户 | https://zhaoxinghua09-cell.github.io/lgd-hub/ |
| 官方主页（中/EN） | https://medxpert.cn/lgd.html ｜ https://medxpert.cn/en/lgd/ |
| 论文（DOI，引用须带版本号） | https://doi.org/10.5281/zenodo.22456647 |
| 医械确定性门禁引擎（MCP） | https://github.com/Medxpert-org/lgd-engine |
| 治理赛事（`POST /uibc/v1/agent` 一键参赛） | https://medxpert.cn/uibc/ |

## 实体与边界

SynomosAI 为个人研究项目（非注册实体）；主理人 赵兴华 / Steven Zhao（ORCID 0009-0001-0512-1237）。代码 MIT；理论文本按 CC BY 4.0 授权（2026-11-03 口径：标准参与要求文本可自由引用复算；引用须署名 + DOI）。LGD 是民间研究框架，不是标准、不构成法律或监管意见、不担保合规。
