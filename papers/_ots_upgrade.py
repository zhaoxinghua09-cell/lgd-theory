#!/usr/bin/env python3
"""Upgrade OpenTimestamps .ots from PendingAttestation to BitcoinBlockHeaderAttestation.
Self-contained (no otsclient/bitcoinlib) — companion to _ots_stamp.py."""
import sys, os
sys.path.insert(0, r"D:\Workbuddy\2026-09-06-08-06-50\_conv\ots\pylibs")
from opentimestamps.core.timestamp import DetachedTimestampFile
from opentimestamps.core.notary import PendingAttestation, BitcoinBlockHeaderAttestation
from opentimestamps.core.serialize import StreamDeserializationContext, StreamSerializationContext
from opentimestamps.calendar import RemoteCalendar


def walk(node, pending_nodes, seen):
    if id(node) in seen:
        return
    seen.add(id(node))
    if any(isinstance(a, PendingAttestation) for a in node.attestations):
        pending_nodes.append(node)
    for sub in node.ops.values():
        walk(sub, pending_nodes, seen)


def has_bitcoin(node, seen):
    if id(node) in seen:
        return False
    seen.add(id(node))
    if any(isinstance(a, BitcoinBlockHeaderAttestation) for a in node.attestations):
        return True
    return any(has_bitcoin(sub, seen) for sub in node.ops.values())


def main():
    for path in sys.argv[1:]:
        name = os.path.basename(path)
        with open(path, "rb") as f:
            dt = DetachedTimestampFile.deserialize(StreamDeserializationContext(f))
        if has_bitcoin(dt.timestamp, set()):
            print("SKIP (already bitcoin-anchored):", name)
            continue
        nodes = []
        walk(dt.timestamp, nodes, set())
        ok = fail = 0
        uris_tried = set()
        for node in nodes:
            for a in node.attestations:
                if isinstance(a, PendingAttestation) and a.uri not in uris_tried:
                    uris_tried.add(a.uri)
        for node in nodes:
            for uri in sorted(uris_tried):
                try:
                    cal = RemoteCalendar(uri)
                    upgraded = cal.get_timestamp(node.msg, timeout=25)
                    node.merge(upgraded)
                    ok += 1
                    print("  upgraded node %s via %s" % (node.msg.hex()[:12], uri))
                except Exception as e:
                    fail += 1
                    print("  calendar miss %s -> %s" % (uri, repr(e)[:110]))
        anchored = has_bitcoin(dt.timestamp, set())
        if ok:
            with open(path, "wb") as f:
                dt.serialize(StreamSerializationContext(f))
        print("%s %s | upgrades=%d misses=%d | bitcoin_anchored=%s"
              % ("DONE " if anchored else "PENDING", name, ok, fail, anchored))


if __name__ == "__main__":
    main()
