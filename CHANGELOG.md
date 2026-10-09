# Changelog

## v9.9.9 — R1 negative control (auto-removed after test)

- Deliberate version-desync entry to prove lgd-ci-gate can fail. Reverted after test.

## [Unreleased]
- **Fixed — license metadata (machine-readable).** `CITATION.cff` had drifted from
  `LICENSE`: the human-readable license reserves all rights (ARR, since v1.6.0)
  while the machine-readable `CITATION.cff` still granted `CC-BY-4.0`. First fix
  replaced it with `license: LicenseRef-AllRightsReserved`, but independent
  review showed that value is **not** in the CFF 1.2.0 `license` enum (a strict
  list of ~459 SPDX ids) — so the file was semantically contradictory *and*
  schema-invalid. Corrected by **omitting `license:`** and declaring the license
  via `license-url:` (the CFF-sanctioned fallback when the license is not an
  SPDX id).
- **Added — `tools/lgd_gate_check.py` hardened.** New checks: license-family
  consistency with an offline CFF-enum validation, "newest = max heading"
  changelog parsing (code-fence aware, spacing-tolerant), and link resolution
  that rejects `..` escapes at any depth and enforces exact case. Selftest grew
  to **18 negative controls + 3 positive controls**. (See PR #7 for the six
  red-team bypass classes closed in the previous hardening pass.)

## v1.6.0 — 2026-09-28
- Current published version (Zenodo record 23019507; concept DOI `10.5281/zenodo.22456647` unchanged, auto-points to latest).
- Licensing aligned to **All Rights Reserved** (theory texts); matches the layered-licensing stance (code `uibc-core/lgd-core/` remains Apache-2.0). This is consistent with the published v1.6.0 Zenodo record (license "Other (closed)").
- Citation-facing files (`CITE.md` / `CITE-ALL.md` / README §Suggested citation) now cite v1.6.0. Prior snapshots v1.2–v1.5 are published on Zenodo but their per-version notes were not maintained in this file.
- Internal edition stamps on separate artifacts (e.g. book `LGD-Library-v1.1`) are intentionally unchanged — they are distinct editions, not the theory version.

## v1.1 — 2026-09-07
- Book (Appendix D) expanded into the full badge system: LGD-aligned reference badge (declaration), Laws badges — Registered / Evidenced / Gated (progress), LGD-Powered tool badge (mandatory for toolchain builds), and the lgd-certify certification line (register → evidence → gate, certification.json with cert_hash).
- Library version bumped to v1.1 across HTML / print / EPUB; EPUB regenerated (ch18.xhtml + opf title + toc).
- Badge assets are now self-hosted under the in-repo `badge/` directory; embed sources are documented in `badge/EMBEDS.md`.

## v1.0 — 2026-09-06
- Flagship paper first release-ready version: `docs/LGD-Lifecycle-Governance-Doctrine-v1.0.md`
- Repository scaffold: README (EN/CN), llms.txt, LICENSE (CC BY 4.0)
- Status: local release-ready; GitHub push pending token rotation + owner confirmation (see publication ledger).

## Planned
- v1.1: English full translation alongside the Chinese paper.
- Domain series: financial AI (FIN-001), electronic evidence chains (LAW-001), digital government trust (GOV-001), on-chain asset governance (CRYPT-001), autonomous driving, data-element lifecycle.
