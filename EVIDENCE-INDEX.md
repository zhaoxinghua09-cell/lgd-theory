# EVIDENCE-INDEX — lgd-theory

## 现状

| 级 | 结果 | 证据位置 | 说明 |
|---|---|---|---|
| L1 自我复现 | **有** | `_tools/verify_generated.py`、`_tools/sync_meta.py`、`_tools/check_remote.py`、`tools/check_review_status.py`、`tools/lgd_gate_check.py`、`.github/workflows/{lgd-ci-gate,review-gate,lgd-ai-review}.yml` | 生成物可校验、评审状态可查、门禁在跑 |
| L2 异体审查 | **有限** | `papers/*.ots`（OpenTimestamps 锚）、`.github/workflows/lgd-itu-review.yml`、`.review-gate-baseline` | 有第三方时间锚与评审流水线；**但"谁审的、结论是什么"未落成可指认回执**，暂记有限 |
| L3 第二实现 | **0** | — | 理论文本无第二实现（本不需实现，故此级不适用，记 0 而非"满分"） |
| L3.5 外部语料 | **0** | `cases/LGD三律落点案例对照表_AI糖网+骨科.md` 为自有案例 | 非外部独立案例 |
| L4 外部节点 | **0** | — | 未见第三方引用/采用的可指认证据 |

## 已知不硬的地方

1. **`Trust Score 98/100 A+` 徽章指向 `skillgate` 自评。** 理论仓的"分数"由自家工具打出，这不是外部评审；引用必须写明"自评"。
2. **`.ots` 只证明"某时刻存在"，不证明"内容被谁审过"。** 时间锚与外部评审是两回事，不能混用。
3. **13 个分域文档体量大，但缺对照表。** `docs/LGD-*-001-*.md` 与 `docs/theories/` 中各框架之间的引用关系没有机器可查的映射，读者难以确认"三律"在各域如何落点。
4. **中英双版并行。** `LGD-Lifecycle-Governance-Doctrine-v1.0.md` 与 `-EN-v1.0.md` 需人工同步，易漂移。

## 维护约定

- 改理论文本 → 重生成 `book/` 与 `*_print.html` → 更新 `.ots`。
- 声称"被评审"必须附回执；否则只写"有评审流水线"。
- 等级只降不升。
