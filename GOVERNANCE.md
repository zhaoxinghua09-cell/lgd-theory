# GOVERNANCE.md v1.0 — Lifecycle Governance for the Three-Account System

> **Status**: PROPOSAL / self-reported. This document is not a legal instrument, certification, or claim of external recognition. It governs internal operation of the three GitHub accounts described below, per the LGD (Lifecycle Governance Doctrine) framework.

> 中文摘要：本文件定义三号账号体系（理论号/产品号/评测号）的治理结构——**三权闭环**（决策权/执行权/审计权分离）、**tiebreaker=Steven**（冲突终裁）、**变更程序**（提案→公示→终裁）、以及无终裁人时的默认冻结兜底。本文件为自报级治理文本，不构成法律承诺或认证主张。

---

## 1. Scope (适用范围)

This governance applies to the account system operated under three GitHub accounts:

| Account | Line | Primary scope |
|---|---|---|
| `zhaoxinghua09-cell` | Theory & Governance (理论号) | LGD doctrine, skill index, flagship spec repos (SSOT) |
| `stevenzhao07` | Product (产品号) | Product-facing delivery, `.github` shared host, AGENTS.md rollout |
| `LGD-Eval` | Evaluation (评测号) | Evaluation protocol, evaluation reports, skill-audit gates |

Write operations are account-isolated: no account writes to another account's repositories beyond its assigned line; the evaluation account never holds write access to the other two accounts.

## 2. Separation of Powers (三权闭环)

### 2.1 Decision Power — Governance (决策权)
- **Owner**: Steven (tiebreaker).
- **Scope (final approval required)**:
  - External publishing / public releases;
  - New repository creation (any account);
  - License or permission changes;
  - Specification releases (e.g., GOVERNANCE itself, doctrine versions);
  - Any action with external-facing impact beyond routine repository-internal changes.
- **Delegation**: routine in-repo changes (documents, code, templates, gates) may proceed without prior approval; any of the items above require explicit approval.

### 2.2 Execution Power (执行权)
- **Theory account**: owns specs, templates, SSOT documents (e.g., AGENTS.md six-area template, GOVERNANCE.md, doctrine).
- **Product account**: owns product-facing repositories and delivery tooling.
- **Evaluation account**: owns evaluation protocol, reports, skill-audit, evidence chains; runs gates independently.
- Each account executes within its line and does not substitute for another line's judgment.

### 2.3 Audit Power (审计权)
- **Owner**: Evaluation line (LGD-Eval) + external-perspective audit.
- **Principle**: audit does **not** report to execution power. Evaluation reports and gates are independent of the code/repos they evaluate.
- **Evidence**: rerun quadruple (commit SHA / tool version / evaluation date / rerun command) is required for evaluation reports (G-17); an external-perspective audit of the three accounts has been run (2026-10-18) and is retained as baseline evidence.

## 3. Tiebreaker (终裁)

- **Tiebreaker**: Steven, for all decision-power items in §2.1.
- **Fallback freeze**: if no tiebreaker is available (e.g., unresponsive), the default is **freeze** — no external publishing, no new repositories, no license changes — until the tiebreaker decides. This prevents single-point-of-decision from becoming a single point of failure in the opposite direction (unchecked motion).

## 4. Change Procedure (变更程序)

This document, and any governance-level document, changes as follows:

1. **Proposal**: draft the change (file/PR/issue) with rationale and impact;
2. **Notice (公示)**: at least 7 days public notice on the repository;
3. **Decision (终裁)**: Steven approves, rejects, or requests revision;
4. **Record**: the change is merged with the decision recorded in commit message / changelog.

The procedure applies to GOVERNANCE.md itself. Routine, non-governance repository changes do not need this procedure.

## 5. Dispute Escalation (争议升级)

1. Discuss in the repository (issue/PR) with the executing line;
2. If unresolved, escalate to the evaluation line for an independent audit note;
3. Final: Steven (tiebreaker). If unavailable → freeze per §3.

## 6. Contributor Roles (贡献者角色)

Role definitions follow the existing contributor-roles catalog (12 roles, maintained by the evaluation line). This document does not duplicate or replace it; role assignments and review rights reference that catalog.

## 7. Relation to Other Governance Artifacts (衔接)

- **AGENTS.md** (six areas: persona / commands / structure / style / git workflow / boundaries): operational guidance per repository; GOVERNANCE.md is the account-level governing text.
- **urgy (17 methodology booklets)**: maintained under a dedicated host with editorial-board rules (P0-7); GOVERNANCE.md tiebreaker applies to booklet-level decisions too.
- **Community health files** (CONTRIBUTING / CODE_OF_CONDUCT / SECURITY): per-account `.github` host; SECURITY.md encodes the credential discipline (vault-only, no secrets in chat/files).

## 8. Boundaries (边界)

- This document is **self-reported**; it does not claim certification, regulatory recognition, or legal personality.
- "SynomosAI" / "MedXpert" remain unregistered entity names (no trademark registration) — see NOTICE.md.
- Any external-facing statement derived from governance must retain the self-reported limitation.

---

*Version 1.0 · 2026-10-19 · Drafted by the theory line, approved by Steven. License layering: code MIT where stated; doctrine/theory text All Rights Reserved per NOTICE.md.*
