#!/usr/bin/env python3
"""OpenTimestamps stamping without otsclient CLI (Windows OpenSSL-free path).

Uses the installed opentimestamps core library only:
  - DetachedTimestampFile.from_fd(OpSHA256(), fd) -> per-file stamp
  - nonce OpAppend(os.urandom(16)) -> OpSHA256 -> merkle root
  - make_merkle_tree([roots]) -> tip; RemoteCalendar.submit(tip.msg) x N; merge
  - StreamSerializationContext -> <file>.ots
Result: .ots proof with PendingAttestation(s); upgrades to Bitcoin-anchored
via `ots upgrade` later (any OTS client, e.g. WSL/Linux) once block lands.
"""
import sys, os

# 依赖路径不写死本机绝对路径（公开仓红线）：环境变量 OTS_PYLIBS 优先，其次仓内同目录 _ots_pylibs/
PYLIBS = os.environ.get("OTS_PYLIBS") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_ots_pylibs")
if os.path.isdir(PYLIBS) and PYLIBS not in sys.path:
    sys.path.insert(0, PYLIBS)

from opentimestamps.core.notary import *          # noqa: F401,F403
from opentimestamps.core.timestamp import *        # noqa: F401,F403
from opentimestamps.core.op import *               # noqa: F401,F403
from opentimestamps.core.serialize import *        # noqa: F401,F403
from opentimestamps.core.timestamp import make_merkle_tree
import opentimestamps.calendar

CALENDARS = [
    "https://a.pool.opentimestamps.org",
    "https://b.pool.opentimestamps.org",
    "https://ots.btc.catallaxy.com",
]


def stamp_file(path):
    with open(path, "rb") as fd:
        ft = DetachedTimestampFile.from_fd(OpSHA256(), fd)
    nonce_appended = ft.timestamp.ops.add(OpAppend(os.urandom(16)))
    root = nonce_appended.ops.add(OpSHA256())
    tip = make_merkle_tree([root])
    ok = []
    for url in CALENDARS:
        try:
            cal = opentimestamps.calendar.RemoteCalendar(url, user_agent="lgd-theory/0.1")
            remote_ts = cal.submit(tip.msg, timeout=30)
            tip.merge(remote_ts)
            ok.append(url)
        except Exception as e:  # noqa: BLE001
            print("   cal-fail %s %s" % (url, repr(e)[:140]))
    mode = "xb" if not os.path.exists(path + ".ots") else "wb"
    with open(path + ".ots", mode) as out:
        ctx = StreamSerializationContext(out)
        ft.serialize(ctx)
    atts = list(ft.timestamp.all_attestations())
    return ok, atts


def main():
    rc = 0
    for p in sys.argv[1:]:
        try:
            ok, atts = stamp_file(p)
            kinds = ",".join(a.__class__.__name__ for a in atts)
            print("STAMPED %s | calendars_ok=%d/%d | attestations=%s"
                  % (os.path.basename(p), len(ok), len(CALENDARS), kinds or "NONE"))
            if not ok:
                rc = 2
        except Exception as e:  # noqa: BLE001
            print("ERROR   %s %s" % (os.path.basename(p), repr(e)[:200]))
            rc = 1
    sys.exit(rc)


if __name__ == "__main__":
    main()
