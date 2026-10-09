#!/usr/bin/env python3
"""lgd_gate_check — the real check behind the lgd-ci-gate required status check.

History: the gate job used to be `echo x3 + exit 0`. A required status check
that cannot fail proves nothing (the green checkmark existed, the check did
not). This script is the replacement: it runs falsifiable checks against a
checkout, and its selftest proves on every CI run that it can fail.

Checks (check mode):
  1. Required files exist and are non-empty.
  2. CITATION.cff carries title / version / date-released / authors.
  3. CITATION.cff version == newest CHANGELOG.md entry (normalized numeric
     compare, "v1.6.0" == "1.6.0"). This exact defect existed for real:
     CITATION said 1.1.0 while the CHANGELOG head was v1.6.0, and the old
     echo-gate could never catch it.
  4. Relative markdown links in README.md / TLDR.md resolve inside the tree
     (anchors #, external http(s), mailto: are skipped; dir links need the dir).
  5. License consistency: the license family declared in CITATION.cff (`license:`
     field) must match the license family of LICENSE. This exact defect existed
     for real (2026-10-09): LICENSE said All-Rights-Reserved while CITATION.cff
     still declared CC-BY-4.0 — machine-readable metadata granted what the
     human-readable license withheld. Historical released snapshots (<= v1.5.0,
     CC BY 4.0) are immutable by design and are NOT touched; the gate enforces
     the CURRENT tree only.

Selftest mode: builds a known-good fixture (must PASS) and a known-broken
fixture (missing LICENSE, stale version, dead link, license conflict — each
must FAIL). If the checker fails to reject the broken fixture, selftest exits
non-zero: the gate has gone decorative again and the run must be red.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "CHANGELOG.md",
    "SECURITY.md",
    "NOTICE.md",
]

CFF_REQUIRED_KEYS = ["title", "version", "date-released", "authors"]

LINK_FILES = ["README.md", "TLDR.md"]

# `## v1.6.0`, `## 1.6.0`, `## [0.2.1] — 2026-09-17`, `##[v1.6.0]` (no space) ;
# NOT `## [Unreleased]`, and NOT headings inside a ``` / ~~~ code fence.
CHANGELOG_VER_RE = re.compile(r"^##(?!#)\s*\[?\s*[vV]?(\d+\.\d+(?:\.\d+)?)\s*\]?")


def _unfenced_lines(text: str) -> list[str]:
    """Drop lines inside ``` / ~~~ code fences (a fenced `## v9.9.9` is docs,
    not a release heading — treating it as one is a false red)."""
    out: list[str] = []
    fenced = False
    for line in text.splitlines():
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else line)
    return out


class Report:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.failed: list[str] = []

    def ok(self, msg: str) -> None:
        self.passed.append(msg)
        print(f"  PASS  {msg}")

    def bad(self, msg: str) -> None:
        self.failed.append(msg)
        print(f"  FAIL  {msg}")


def norm_ver(v: str) -> str:
    v = v.strip().strip('"').lstrip("vV")
    parts = v.split(".")
    try:
        return ".".join(str(int(p)) for p in parts)
    except ValueError:
        return v


def cff_value(text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}\s*:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def cff_value_status(text: str, key: str) -> tuple[str | None, str]:
    """Return (value, status) with status in {'missing','empty','ok'}.

    An inline empty value (`version: ""`) is 'empty' (a failure), while a YAML
    block scalar (value on following indented lines, e.g. `authors:`) is 'ok'.
    """
    m = re.search(rf"^{re.escape(key)}\s*:(.*)$", text, re.M)
    if not m:
        return None, "missing"
    inline = m.group(1).strip()
    if inline and inline not in ('""', "''"):
        return inline, "ok"
    for line in text[m.end():].splitlines():
        if not line.strip():
            continue
        if line[:1] in (" ", "\t"):
            return "<block>", "ok"
        break
    return inline, "empty"


def _ver_key(v: str) -> tuple:
    try:
        return tuple(int(x) for x in norm_ver(v).split("."))
    except ValueError:
        return (0,)


def changelog_newest(text: str) -> str | None:
    """The MAXIMUM released version heading (not merely the first one)."""
    vers: list[str] = []
    for line in _unfenced_lines(text):
        m = CHANGELOG_VER_RE.match(line)
        if m:
            vers.append(norm_ver(m.group(1)))
    return max(vers, key=_ver_key) if vers else None


def check_required_files(root: Path, rep: Report) -> None:
    for rel in REQUIRED_FILES:
        p = root / rel
        if p.is_file() and p.stat().st_size > 0:
            rep.ok(f"required file present: {rel}")
        else:
            rep.bad(f"required file missing or empty: {rel}")


def check_cff_keys(root: Path, rep: Report) -> None:
    cff = root / "CITATION.cff"
    if not cff.is_file():
        rep.bad("CITATION.cff unreadable (skip key check)")
        return
    text = cff.read_text(encoding="utf-8")
    for key in CFF_REQUIRED_KEYS:
        _val, status = cff_value_status(text, key)
        if status == "ok":
            rep.ok(f"CITATION.cff has non-empty {key}")
        elif status == "empty":
            rep.bad(f"CITATION.cff key is empty: {key}")
        else:
            rep.bad(f"CITATION.cff missing key: {key}")


def check_version_sync(root: Path, rep: Report) -> None:
    cff = root / "CITATION.cff"
    chlog = root / "CHANGELOG.md"
    if not (cff.is_file() and chlog.is_file()):
        rep.bad("version sync unverifiable (CITATION.cff/CHANGELOG.md missing)")
        return
    cff_ver = cff_value(cff.read_text(encoding="utf-8"), "version")
    newest = changelog_newest(chlog.read_text(encoding="utf-8"))
    if not cff_ver or not newest:
        rep.bad(f"version parse failed (cff={cff_ver!r}, changelog newest={newest!r})")
        return
    if norm_ver(cff_ver) == newest:
        rep.ok(f"CITATION.cff version {cff_ver} matches CHANGELOG newest {newest}")
    else:
        rep.bad(
            f"CITATION.cff version {cff_ver} != CHANGELOG newest {newest} "
            "(citation metadata is stale; the echo-gate could never catch this)"
        )


def _inline_targets(text: str) -> list[str]:
    """Destinations of inline links `]( … )`.

    Tolerates a `<...>` wrapped destination (may contain spaces) and an optional
    `"title"` / `'title'` / `(title)` suffix; a bare destination containing
    spaces is kept whole rather than dropped.
    """
    out: list[str] = []
    for m in re.finditer(r"\]\(", text):
        start = m.end()
        end = text.find(")", start)
        if end == -1:
            continue
        inner = text[start:end].strip()
        if inner.startswith("<"):
            close = inner.find(">")
            if close != -1:
                out.append(inner[1:close].strip())
                continue
        titled = re.match(r"(\S+)(?:\s+[\"'(].*[\"')])?$", inner)
        out.append(titled.group(1) if titled else inner)
    return out


def _reference_targets(text: str) -> list[str]:
    """Destinations of reference-style definitions `[label]: url`."""
    return [m.group(1) for m in re.finditer(r"^\s*\[[^\]]+\]:\s*(\S+)", text, re.M)]


def _resolve_inside(root: Path, path_part: str) -> tuple[bool, bool]:
    """Return (escapes, exists).

    `escapes` is True if the link leaves the tree at ANY point on the way down —
    closes the "escape-and-return" bypass `../<this-repo>/docs/x.md`, which
    resolves back inside yet 404s on GitHub. `exists` is checked
    segment-by-segment with exact-case listing so the verdict does not depend on
    the host filesystem's case sensitivity.
    """
    segs = [s for s in path_part.replace("\\", "/").split("/") if s not in ("", ".")]
    depth = 0
    cur = root
    for s in segs:
        if s == "..":
            if depth == 0:
                return True, False
            depth -= 1
            cur = cur.parent
            continue
        depth += 1
        try:
            names = {e.name for e in os.scandir(cur)}
        except OSError:
            return False, False
        if s not in names:
            return False, False
        cur = cur / s
    return False, True


def check_links(root: Path, rep: Report) -> None:
    seen_dead = 0
    seen_live = 0
    checked: list[str] = []
    for rel in LINK_FILES:
        f = root / rel
        if not f.is_file():
            continue
        checked.append(rel)
        text = f.read_text(encoding="utf-8")
        for target in _inline_targets(text) + _reference_targets(text):
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0].strip()
            if not path_part:
                continue
            escapes, exists = _resolve_inside(root, path_part)
            if escapes:
                seen_dead += 1
                rep.bad(f"{rel}: relative link escapes the tree -> {target}")
            elif exists:
                seen_live += 1
            else:
                seen_dead += 1
                rep.bad(f"{rel}: dead relative link -> {target}")
    if seen_dead == 0:
        rep.ok(f"all relative links resolve ({seen_live} checked in {', '.join(checked) or 'n/a'})")


# --- license logic -------------------------------------------------------
# (i) "All rights reserved" is *boilerplate* inside many MIT/Apache LICENSE
#     files. Reading it first made the gate false-red a genuine MIT license
#     and false-green a LICENSE granting MIT while CITATION claims ARR. Fix: an
#     explicit standard-license marker always wins.
# (ii) CFF 1.2.0 `license` is a strict enum of SPDX ids; `LicenseRef-*`,
#     `All Rights Reserved`, `NONE` and `NOASSERTION` are NOT members. The
#     spec's fallback is to omit `license:` and provide `license-url:`.
_STANDARD_MARKERS = [
    ("apache-2.0", r"apache\s+license[^\n]{0,40}2\.0"),
    ("mit", r"\bmit\s+license\b"),
    ("bsd-3-clause", r"bsd\s+3-?clause"),
    ("bsd-2-clause", r"bsd\s+2-?clause"),
    ("gpl-3.0", r"gnu\s+general\s+public\s+license[^\n]{0,40}(version\s*3|v3)"),
    ("lgpl-3.0", r"gnu\s+lesser\s+general\s+public\s+license"),
    ("mpl-2.0", r"mozilla\s+public\s+license[^\n]{0,40}(2\.0|version\s*2)"),
    ("isc", r"\bisc\s+license\b"),
    ("unlicense", r"\bthe\s+unlicense\b|this\s+is\s+free\s+and\s+unencumbered"),
    ("cc0-1.0", r"cc0[\s\-]1\.0|creative\s+commons\s+zero"),
    ("cc-by-4.0", r"creative\s+commons\s+attribution[^\n]{0,40}4\.0|cc[-\s]by[-\s]4\.0"),
]

# Curated subset of the CFF 1.2.0 `license-enum` (SPDX ids); the authoritative
# check is the schema-validation CI step, this is the offline-deterministic one.
_CFF_ENUM: set[str] = {
    x.lower() for x in [
        "0BSD", "AFL-3.0", "AGPL-3.0-only", "AGPL-3.0-or-later", "Apache-1.1",
        "Apache-2.0", "Artistic-2.0", "Beerware", "BSD-2-Clause", "BSD-3-Clause",
        "BSD-3-Clause-Clear", "BSD-4-Clause", "BSL-1.0", "CC-BY-3.0", "CC-BY-4.0",
        "CC-BY-NC-4.0", "CC-BY-NC-ND-4.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0",
        "CC-BY-SA-4.0", "CC0-1.0", "CECILL-2.1", "EPL-1.0", "EPL-2.0", "EUPL-1.1",
        "EUPL-1.2", "GPL-2.0-only", "GPL-2.0-or-later", "GPL-3.0-only",
        "GPL-3.0-or-later", "ISC", "LGPL-2.1-only", "LGPL-2.1-or-later",
        "LGPL-3.0-only", "LGPL-3.0-or-later", "MIT", "MIT-0", "MPL-1.1", "MPL-2.0",
        "MS-PL", "MS-RL", "NCSA", "ODbL-1.0", "OFL-1.1", "OSL-3.0", "PostgreSQL",
        "Python-2.0", "Unlicense", "UPL-1.0", "Vim", "WTFPL", "X11", "Zlib",
    ]
}


def license_family_from_text(text: str) -> str | None:
    """Classify a LICENSE document into a comparable family, or None if unknown.

    An explicit standard-license marker always wins; the "All rights reserved"
    phrase is only consulted when no standard header is present.
    """
    t = text.lower()
    for fam, pat in _STANDARD_MARKERS:
        if re.search(pat, t):
            return fam
    if "all rights reserved" in t or "保留所有权利" in text:
        return "arr"
    return None


def license_family_from_spdx(expr: str) -> str | None:
    """Map a CITATION.cff license expression to a family (or 'multi')."""
    parts = re.split(r"\s+(?:OR|AND)\s+", expr.strip().strip('"'), flags=re.I)
    fams: set[str] = set()
    for p in parts:
        pl = p.strip().strip("()").lower()
        if not pl:
            continue
        if "allrightsreserved" in pl or "all rights reserved" in pl or pl == "arr":
            fams.add("arr")
        elif pl.startswith("licenseref-") or pl in {"none", "noassertion"}:
            fams.add(f"?{pl}")
        else:
            got = next((f for f, pat in _STANDARD_MARKERS
                        if re.search(pat, pl) or pl == f or pl.startswith(f + "-")), None)
            fams.add(got or f"?{pl}")
    if len(fams) == 1:
        return next(iter(fams))
    if len(fams) > 1:
        return "multi"
    return None


def check_license_sync(root: Path, rep: Report) -> None:
    lic = root / "LICENSE"
    cff = root / "CITATION.cff"
    if not (lic.is_file() and cff.is_file()):
        rep.bad("license sync unverifiable (LICENSE/CITATION.cff missing)")
        return
    text = cff.read_text(encoding="utf-8")
    expr, status = cff_value_status(text, "license")
    fam_lic = license_family_from_text(lic.read_text(encoding="utf-8"))
    if status == "missing":
        url = cff_value_status(text, "license-url")[0]
        if url:
            rep.ok("license declared by URL only (license-url) — correct CFF 1.2.0 "
                   "fallback when the license is not an SPDX enum id")
        else:
            rep.bad("CITATION.cff declares neither `license:` nor `license-url:`")
        return
    if status == "empty":
        rep.bad("CITATION.cff `license:` is empty")
        return
    assert expr is not None
    _tokens = re.split(r"\s+(?:OR|AND)\s+", expr.strip().strip('"'), flags=re.I)
    if not all(t.strip().strip("()").lower() in _CFF_ENUM for t in _tokens):
        rep.bad(f"CITATION.cff license {expr!r} is not a valid CFF 1.2.0 value "
                "(strict SPDX enum; LicenseRef-*, free text and 'All Rights "
                "Reserved' are NOT members); omit `license:` and use "
                "`license-url:` instead")
        return
    fam_cff = license_family_from_spdx(expr)
    if fam_lic is None:
        rep.bad(
            "LICENSE family unrecognized — add a recognizable marker "
            "(All Rights Reserved / Apache 2.0 / MIT / Creative Commons Attribution)"
        )
        return
    if fam_cff == "multi":
        rep.bad(f"CITATION.cff license {expr!r} spans multiple families — "
                "ambiguous, resolve to a single SPDX expression")
        return
    if fam_cff is None or (fam_cff or "").startswith("?"):
        rep.bad(f"CITATION.cff license {expr!r} is not a CFF 1.2.0 enum value")
        return
    if fam_lic == fam_cff:
        rep.ok(f"license family consistent: {fam_lic} (LICENSE == CITATION.cff {expr})")
    else:
        rep.bad(
            f"LICENSE METADATA CONFLICT: LICENSE says {fam_lic} but CITATION.cff "
            f"declares {expr} ({fam_cff}) — machine metadata grants what the "
            "license text may withhold"
        )


def run_checks(root: Path) -> Report:
    rep = Report()
    print(f"lgd-gate: checking {root}")
    check_required_files(root, rep)
    check_cff_keys(root, rep)
    check_version_sync(root, rep)
    check_license_sync(root, rep)
    check_links(root, rep)
    print(f"lgd-gate: {len(rep.passed)} passed, {len(rep.failed)} failed")
    return rep


# ---------------------------------------------------------------- selftest --

GOOD_FIXTURE: dict[str, str] = {
    "README.md": ("# T\n\nSee [LICENSE](LICENSE), [DETAILS](docs/details.md), "
                  "[TITLED](docs/details.md \"t\"), [REF][ref] and "
                  "[WRAPPED](<docs/details.md>).\n\n[ref]: docs/details.md\n"),
    "LICENSE": "MIT License\n",
    "CITATION.cff": (
        'cff-version: 1.2.0\ntitle: "T"\nversion: "1.6.0"\n'
        'date-released: "2026-09-28"\nlicense: MIT\nauthors:\n  - family-names: Z\n'
    ),
    "CHANGELOG.md": "# Changelog\n\n## v1.6.0 — 2026-09-28\n- latest\n\n## v1.0 — old\n",
    "SECURITY.md": "s\n",
    "NOTICE.md": "n\n",
    "docs/details.md": "d\n",
}

# each entry: (mutated files, expected-to-catch check label)
BROKEN_CASES = [
    ("missing LICENSE", {"LICENSE": None}, "required file"),
    ("stale CITATION version", {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace('"1.6.0"', '"1.1.0"')}, "version"),
    ("dead link", {"README.md": "# T\n\nSee [GONE](docs/gone.md).\n"}, "dead relative link"),
    ("missing CHANGELOG", {"CHANGELOG.md": None}, "required file"),
    # the real 2026-10-09 defect: machine metadata grants CC-BY-4.0 while the
    # license text reserves all rights
    (
        "license metadata conflict",
        {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace("license: MIT", "license: CC-BY-4.0")},
        "LICENSE METADATA CONFLICT",
    ),
    (
        "license field dropped from CITATION",
        {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace("license: MIT\n", "")},
        "neither `license:` nor `license-url:`",
    ),
    # --- B1..B6: six bypass classes found by an independent red-team seat ---
    ("B1 dead link whose path contains spaces",
     {"README.md": "# T\n\nSee [GONE](docs/gone file.md).\n"}, "dead relative link"),
    ("B2 dead link with a title suffix",
     {"README.md": "# T\n\nSee [GONE](docs/gone.md \"T\").\n"}, "dead relative link"),
    ("B3 dead reference-style link",
     {"README.md": "# T\n\nSee [GONE][g].\n\n[g]: docs/gone.md\n"}, "dead relative link"),
    ("B4 link escapes the tree via ..",
     {"README.md": "# T\n\nSee [OUT](../outside.md).\n"}, "escapes the tree"),
    ("B5 newer CHANGELOG heading lower down",
     {"CHANGELOG.md": "# Changelog\n\n## v1.6.0 — old\n\n## v9.9.9 — future\n"},
     "newest 9.9.9"),
    ("B6 empty CITATION value",
     {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace('"1.6.0"', '""')},
     "is empty"),
    # --- round-3: findings from the independent license/IP auditor ---
    ("CITATION license is a LicenseRef (not a CFF enum id)",
     {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace(
         "license: MIT", "license: LicenseRef-AllRightsReserved")},
     "CFF 1.2.0"),
    ("MIT LICENSE with ARR boilerplate must not be misread as ARR",
     {"LICENSE": "MIT License\n\nCopyright (c) 2026 X. All rights reserved.\n",
      "CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace("license: MIT",
                                                           "license: CC-BY-4.0")},
     "LICENSE METADATA CONFLICT"),
    ("ambiguous OR license expression",
     {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace(
         "license: MIT", "license: MIT OR CC-BY-4.0")},
     "spans multiple families"),
    ("spacing-less CHANGELOG heading must not fail-open to SKIP",
     {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace('"1.6.0"', '"1.1.0"'),
      "CHANGELOG.md": "# Changelog\n\n##[v1.6.0] — 2026-09-28\n- latest\n"},
     "version"),
]

# fixture variants that MUST pass (positive controls)
GOOD_VARIANTS = [
    ("license declared by URL only (no enum id) — the CFF-sanctioned fallback",
     {"CITATION.cff": GOOD_FIXTURE["CITATION.cff"].replace(
         "license: MIT\n", "license-url: \"https://example.invalid/LICENSE\"\n")}),
    ("MIT LICENSE with ARR boilerplate + CITATION MIT (must NOT false-red)",
     {"LICENSE": "MIT License\n\nCopyright (c) 2026 X. All rights reserved.\n"}),
    ("version-looking heading inside a code fence must NOT be read as a release",
     {"CHANGELOG.md": "# Changelog\n\n## v1.6.0 — 2026-09-28\n- latest\n\n"
                       "```\n## v9.9.9\n```\n"}),
]


def build_fixture(mutations: dict[str, str | None]) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="lgd-gate-fixture-"))
    for rel, content in GOOD_FIXTURE.items():
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    for rel, content in mutations.items():
        p = tmp / rel
        if content is None:
            p.unlink()
        else:
            p.write_text(content, encoding="utf-8")
    return tmp


def selftest() -> int:
    print("selftest: proving the gate can fail (and can pass)")
    rc = 0

    good = build_fixture({})
    if not run_checks(good).failed:
        print("  PASS  good fixture passes")
    else:
        print("  FAIL  good fixture did NOT pass — checker is broken")
        rc = 1
    shutil.rmtree(good, ignore_errors=True)

    for label, mutations, expect in BROKEN_CASES:
        bad = build_fixture(mutations)
        rep = run_checks(bad)
        if any(expect in f for f in rep.failed):
            print(f"  PASS  broken fixture rejected: {label}")
        else:
            print(f"  FAIL  broken fixture NOT rejected ({label}) — gate is decorative")
            rc = 1
        shutil.rmtree(bad, ignore_errors=True)

    for label, mutations in GOOD_VARIANTS:
        okv = build_fixture(mutations)
        rep = run_checks(okv)
        if not rep.failed:
            print(f"  PASS  good variant accepted: {label}")
        else:
            print(f"  FAIL  good variant FALSELY rejected ({label}) — gate over-reds")
            rc = 1
        shutil.rmtree(okv, ignore_errors=True)

    # N6 (red-team round 2): escape-and-return `../<this-repo>/docs/details.md`
    n6 = build_fixture({})
    (n6 / "README.md").write_text(
        f"# T\n\nSee [SELF](../{n6.name}/docs/details.md).\n", encoding="utf-8")
    rep = run_checks(n6)
    if any("escapes the tree" in f for f in rep.failed):
        print("  PASS  broken fixture rejected: N6 escape-and-return via ../<repo>/")
    else:
        print("  FAIL  broken fixture NOT rejected (N6 escape-and-return) — gate is decorative")
        rc = 1
    shutil.rmtree(n6, ignore_errors=True)

    # case-only mismatch must red on every host (Windows/macOS are otherwise blind)
    cm = build_fixture({})
    (cm / "README.md").write_text("# T\n\nSee [U](DOCS/details.md).\n", encoding="utf-8")
    rep = run_checks(cm)
    if any("dead relative link" in f for f in rep.failed):
        print("  PASS  broken fixture rejected: case-only path mismatch")
    else:
        print("  FAIL  broken fixture NOT rejected (case-only mismatch) — host-dependent")
        rc = 1
    shutil.rmtree(cm, ignore_errors=True)

    print("selftest:", "OK — gate can fail and can pass" if rc == 0 else "BROKEN")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--root", default=".")
    sub.add_parser("selftest")
    args = ap.parse_args()

    if args.cmd == "selftest":
        return selftest()
    rep = run_checks(Path(args.root).resolve())
    if rep.failed:
        print("lgd-gate: RED — " + str(len(rep.failed)) + " defect(s)")
        return 1
    print("lgd-gate: GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
