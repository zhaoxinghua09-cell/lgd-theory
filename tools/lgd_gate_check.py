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
    for line in text.splitlines():
        m = re.match(r"^##\s+\[?\s*[vV]?(\d+\.\d+(?:\.\d+)?)\s*\]?", line)
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


def check_links(root: Path, rep: Report) -> None:
    root_res = root.resolve()
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
            resolved = (root / path_part).resolve()
            try:
                resolved.relative_to(root_res)
            except ValueError:
                seen_dead += 1
                rep.bad(f"{rel}: relative link escapes the tree -> {target}")
                continue
            if resolved.exists():
                seen_live += 1
            else:
                seen_dead += 1
                rep.bad(f"{rel}: dead relative link -> {target}")
    if seen_dead == 0:
        rep.ok(f"all relative links resolve ({seen_live} checked in {', '.join(checked) or 'n/a'})")


def license_family_from_text(text: str) -> str | None:
    """Classify a LICENSE document into a comparable family, or None if unknown."""
    t = text.lower()
    if "all rights reserved" in t or "保留所有权利" in text:
        return "arr"
    if "apache license" in t or ("apache" in t and "2.0" in t):
        return "apache-2.0"
    if ("creative commons" in t and "attribution" in t) or "cc-by-4.0" in t or "cc by 4.0" in t:
        return "cc-by-4.0"
    if re.search(r"\bmit license\b", t):
        return "mit"
    return None


def license_family_from_spdx(expr: str) -> str | None:
    """Map a CITATION.cff `license:` SPDX expression to the same family space."""
    s = expr.strip().strip('"').lower()
    if "allrightsreserved" in s or "arr" in s.split("-"):
        return "arr"
    if "cc-by-4.0" in s or "cc-by-4" in s:
        return "cc-by-4.0"
    if "apache-2.0" in s:
        return "apache-2.0"
    if s == "mit" or "mit" in re.split(r"[\s()+&]", s):
        return "mit"
    return None


def check_license_sync(root: Path, rep: Report) -> None:
    lic = root / "LICENSE"
    cff = root / "CITATION.cff"
    if not (lic.is_file() and cff.is_file()):
        rep.bad("license sync unverifiable (LICENSE/CITATION.cff missing)")
        return
    fam_lic = license_family_from_text(lic.read_text(encoding="utf-8"))
    cff_text = cff.read_text(encoding="utf-8")
    expr = cff_value(cff_text, "license")
    if not expr:
        rep.bad(
            "CITATION.cff has no `license:` field — machine-readable metadata "
            "must state the license (or its absence) explicitly"
        )
        return
    fam_cff = license_family_from_spdx(expr)
    if fam_lic is None:
        rep.bad(
            "LICENSE family unrecognized — add a recognizable marker "
            "(All Rights Reserved / Apache 2.0 / MIT / Creative Commons Attribution)"
        )
        return
    if fam_cff is None:
        rep.bad(f"CITATION.cff license {expr!r} does not map to a known family")
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
        "no `license:` field",
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
