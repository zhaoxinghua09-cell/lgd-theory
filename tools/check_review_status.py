# -*- coding: utf-8 -*-
"""
发布闸门校验器（Review Gate Checker）

用途
   扫描目标目录下的 markdown 文档，检查是否带合法的 REVIEW-GATE 审查标记，
   并检出「文档自称可发布但无审查背书」这类矛盾。

依据
   `11-研究成果/发布闸门/发布闸门规范_v1.md`（闸门规则 G-1 ~ G-6）

用法
   python check_review_status.py <目录> [更多目录...]
   python check_review_status.py D:/Workbuddy/08-理论体系/发布/lgd-theory/docs
   python check_review_status.py docs/ --json out.json
   python check_review_status.py docs/ --quiet      # 只输出汇总与失败项

退出码
   0 = 全部通过
   1 = 存在 FAIL（CI 用此判定失败）
   2 = 参数或环境错误

规则
   G-1 无标记不得发布       缺 REVIEW-GATE 块            → FAIL
   G-2 自称无效             正文有自我"可发布"宣称，但标记非 verified → FAIL
   G-3 verdict/status 一致  rejected 却 verified        → FAIL
   G-4 独立席位             reviewed-by 与作者同线       → WARN（需人工核对）
   G-5 时效复核             review-date 距今 > 180 天    → WARN
   G-6 争议件标红           conditional/rejected 但无 ⚠️ 待修订区块 → FAIL
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime

MARKER_RE = re.compile(r"<!--\s*REVIEW-GATE(.*?)-->", re.S | re.I)
FIELD_RE = re.compile(r"^\s*([A-Za-z_\-]+)\s*[:：]\s*(.+?)\s*$", re.M)

VALID_STATUS = {"unverified", "in-review", "verified", "contested"}
VALID_VERDICT = {"pass", "conditional", "rejected"}

# 自我宣称"可发布"的形态（中文/英文/emoji）
SELF_CLAIM_RE = re.compile(
    r"(状态\s*[:：].{0,20}(可发布|已发布|可对外))"
    r"|(\U0001F7E2\s*可发布)"
    r"|(\bready\s+to\s+publish\b)",
    re.I,
)

# 争议件必须出现的告警区块
CONTEST_BANNER_RE = re.compile(r"⚠️\s*\*{0,2}\s*(待修订|修订说明)")

STALE_DAYS = 180


def parse_marker(text):
    """从正文中解析 REVIEW-GATE 块；返回 dict 或 None。"""
    m = MARKER_RE.search(text)
    if not m:
        return None
    fields = {}
    for k, v in FIELD_RE.findall(m.group(1)):
        fields[k.strip().lower()] = v.strip()
    return fields


def days_since(datestr):
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"):
        try:
            d = datetime.strptime(datestr.strip(), fmt).date()
            return (date.today() - d).days
        except ValueError:
            continue
    return None


def check_file(path):
    """检查单个文件，返回 (findings, info)。findings: [(level, rule, msg)]"""
    findings = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as exc:
        return [("FAIL", "IO", "读取失败: %s" % exc)], {}

    marker = parse_marker(text)
    info = {"path": path, "has_marker": marker is not None}

    if marker is None:
        # G-1
        if SELF_CLAIM_RE.search(text):
            findings.append(("FAIL", "G-2",
                             "文档自称『可发布』但完全没有 REVIEW-GATE 审查标记"))
            info["self_claim"] = True
        else:
            findings.append(("FAIL", "G-1", "缺少 REVIEW-GATE 审查标记"))
        return findings, info

    status = (marker.get("review-status") or "").lower()
    verdict = (marker.get("verdict") or "").lower()
    info.update({"review_status": status, "verdict": verdict,
                 "reviewed_by": marker.get("reviewed-by", ""),
                 "review_date": marker.get("review-date", ""),
                 "review_ref": marker.get("review-ref", "")})

    # 必填字段
    for req in ("review-status", "reviewed-by", "review-date", "verdict"):
        if not marker.get(req):
            findings.append(("FAIL", "G-1", "标记缺少必填字段 `%s`" % req))

    if status and status not in VALID_STATUS:
        findings.append(("FAIL", "G-1", "review-status 取值非法: %s" % status))
    if verdict and verdict not in VALID_VERDICT:
        findings.append(("FAIL", "G-1", "verdict 取值非法: %s" % verdict))

    # G-2 自称与标记矛盾
    if SELF_CLAIM_RE.search(text) and status != "verified":
        findings.append(("FAIL", "G-2",
                         "文档自称『可发布』，但 review-status=%s（非 verified）" % (status or "空")))
        info["self_claim"] = True

    # G-3 结论矛盾
    if verdict == "rejected" and status == "verified":
        findings.append(("FAIL", "G-3", "verdict=rejected 却 review-status=verified，自相矛盾"))

    # G-6 争议件须标红
    if verdict in ("conditional", "rejected") and not CONTEST_BANNER_RE.search(text):
        findings.append(("FAIL", "G-6",
                         "verdict=%s 但正文无『⚠️ 待修订 / 修订说明』区块" % verdict))

    # G-5 时效
    d = days_since(marker.get("review-date", ""))
    if d is not None and d > STALE_DAYS:
        findings.append(("WARN", "G-5", "审查日期距今 %d 天（> %d），建议重新核验引用时效"
                         % (d, STALE_DAYS)))

    # G-4 独立性（只能做粗判：提示人工核）
    if marker.get("reviewed-by"):
        findings.append(("INFO", "G-4",
                         "reviewed-by=%s —— 请人工确认其与文档作者不同线（工具无法判定）"
                         % marker["reviewed-by"]))

    return findings, info


def iter_markdown(targets):
    for t in targets:
        if os.path.isfile(t):
            if t.lower().endswith((".md", ".markdown")):
                yield t
            continue
        for root, dirs, files in os.walk(t):
            dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
            for fn in sorted(files):
                if fn.lower().endswith((".md", ".markdown")):
                    yield os.path.join(root, fn)


def main():
    ap = argparse.ArgumentParser(description="发布闸门校验器")
    ap.add_argument("targets", nargs="+", help="要扫描的目录或文件")
    ap.add_argument("--json", help="把结果写入 JSON 文件")
    ap.add_argument("--quiet", action="store_true", help="只输出汇总与 FAIL 项")
    ap.add_argument("--baseline",
                    help="基线豁免文件：列在其中的文件属『已登记的历史问题』，"
                         "只警告不阻断；退出码仅反映『新增问题』")
    ap.add_argument("--strict", action="store_true",
                    help="配合 --baseline：即使问题都在基线内也返回 1")
    args = ap.parse_args()

    # 载入基线（按文件名匹配，避免路径分隔符差异）
    baseline = set()
    if args.baseline:
        try:
            with open(args.baseline, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        baseline.add(os.path.basename(line))
        except Exception as exc:
            print("基线文件读取失败：%s" % exc)
            return 2

    files = list(iter_markdown(args.targets))
    if not files:
        print("未找到任何 markdown 文件：%s" % ", ".join(args.targets))
        return 2

    results = []
    n_fail = n_warn = n_pass = 0
    known_fail = new_fail = 0
    baseline_used = set()
    scanned_basenames = set()
    for path in files:
        findings, info = check_file(path)
        fails = [f for f in findings if f[0] == "FAIL"]
        warns = [f for f in findings if f[0] == "WARN"]
        base = os.path.basename(path)
        scanned_basenames.add(base)
        if fails:
            if base in baseline:
                known_fail += 1
                baseline_used.add(base)
                info["baseline"] = True
            else:
                new_fail += 1
            n_fail += 1
        elif warns:
            n_warn += 1
        else:
            n_pass += 1
        results.append({"file": path, "info": info, "findings": findings})

    baseline_stale = sorted(
        b for b in baseline
        if b in scanned_basenames and b not in baseline_used
    )

    # 输出
    for r in results:
        fails = [f for f in r["findings"] if f[0] == "FAIL"]
        warns = [f for f in r["findings"] if f[0] == "WARN"]
        if args.quiet and not fails:
            continue
        if fails:
            flag = "已知" if r["info"].get("baseline") else "新增"
        else:
            flag = "WARN" if warns else "PASS"
        print("[%s] %s" % (flag, r["file"]))
        for lv, rule, msg in r["findings"]:
            if args.quiet and lv != "FAIL":
                continue
            print("       %-4s %-4s %s" % (lv, rule, msg))

    print("\n—— 汇总 ——")
    print("扫描 %d 份 ｜ PASS %d ｜ WARN %d ｜ FAIL %d（新增 %d / 已知 %d）"
          % (len(results), n_pass, n_warn, n_fail, new_fail, known_fail))
    if baseline:
        print("基线登记 %d 份 ｜ 本轮命中 %d 份" % (len(baseline), len(baseline_used)))
    if baseline_stale:
        print("\n⚠️ 以下基线条目本轮已不再 FAIL，可从基线中移除：")
        for b in baseline_stale:
            print("   - %s" % b)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({"summary": {"total": len(results), "pass": n_pass,
                                   "warn": n_warn, "fail": n_fail,
                                   "new_fail": new_fail, "known_fail": known_fail,
                                   "baseline_total": len(baseline),
                                   "baseline_stale": baseline_stale},
                       "results": results}, f, ensure_ascii=False, indent=2)
        print("JSON 已写入：%s" % args.json)

    # 退出码：有新增问题 → 1；--strict 时任何问题 → 1
    if new_fail:
        return 1
    if args.strict and n_fail:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
