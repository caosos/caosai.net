#!/usr/bin/env python3
import argparse, json, os, sys, time
from typing import List, Tuple

def normalize_backslash_n_outside_strings(s: str) -> str:
    """
    Converts literal two-char sequences \\n into real newlines ONLY when outside JSON strings.
    This fixes files where multiple JSON objects were concatenated with literal \\n delimiters.
    It will NOT touch \\n inside JSON strings.
    """
    out = []
    in_str = False
    esc = False
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if in_str:
            out.append(ch)
            if esc:
                esc = False
            else:
                if ch == '\\':
                    esc = True
                elif ch == '"':
                    in_str = False
            i += 1
            continue

        # outside string
        if ch == '"':
            in_str = True
            out.append(ch)
            i += 1
            continue

        # convert literal \n delimiter outside string to real newline
        if ch == '\\' and i + 1 < n and s[i + 1] == 'n':
            out.append('\n')
            i += 2
            continue

        out.append(ch)
        i += 1

    return ''.join(out)

def iter_json_objects(text: str) -> List[dict]:
    dec = json.JSONDecoder()
    i = 0
    L = len(text)
    objs = []
    while True:
        # skip whitespace
        while i < L and text[i].isspace():
            i += 1
        if i >= L:
            break
        obj, j = dec.raw_decode(text, i)
        objs.append(obj)
        i = j
    return objs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="path to *.jsonl session file")
    ap.add_argument("--out", default="", help="output path (default: <input>.fixed.jsonl)")
    ap.add_argument("--backup", action="store_true", help="write a timestamped .bak copy of input")
    args = ap.parse_args()

    inp = args.input
    if not os.path.isfile(inp):
        print(f"ERROR: input_missing: {inp}", file=sys.stderr)
        return 2

    with open(inp, "rb") as f:
        raw = f.read()

    # decode as utf-8 with replacement (never crash)
    text = raw.decode("utf-8", errors="replace")

    # normalize only delimiter-style \\n outside strings
    norm = normalize_backslash_n_outside_strings(text)

    try:
        objs = iter_json_objects(norm)
    except Exception as e:
        print("ERROR: json_parse_failed", file=sys.stderr)
        print(str(e), file=sys.stderr)
        return 3

    out_path = args.out.strip() or (inp + ".fixed.jsonl")

    if args.backup:
        ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        bak = inp + f".bak_{ts}"
        with open(bak, "wb") as f:
            f.write(raw)
        print(f"BACKUP_WRITTEN -> {bak}")

    # write strict JSONL: 1 object per line
    with open(out_path, "w", encoding="utf-8") as f:
        for obj in objs:
            f.write(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))
            f.write("\n")

    print(f"FIXED_WRITTEN -> {out_path}")
    print(f"OBJECTS -> {len(objs)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
