#!/usr/bin/env python3
"""Read the workflow ComfyUI embedded in an output PNG.

Usage:
    python3 read-embedded.py IMAGE.png

Parses the PNG's text chunks with the standard library only
and prints what it finds: the 'prompt' chunk (the API-format
workflow that made the picture) summarised node by node, and
whether a 'workflow' chunk (the UI format) is present.
"""

import json
import struct
import sys
import zlib


def text_chunks(path):
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"{path} is not a PNG")
    pos = 8
    chunks = {}
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos : pos + 4])
        ctype = data[pos + 4 : pos + 8].decode("ascii", "replace")
        body = data[pos + 8 : pos + 8 + length]
        if ctype in ("tEXt", "iTXt", "zTXt"):
            if ctype == "tEXt":
                key, _, value = body.partition(b"\x00")
                chunks[key.decode("latin-1")] = value.decode(
                    "latin-1"
                )
            elif ctype == "zTXt":
                key, _, rest = body.partition(b"\x00")
                chunks[key.decode("latin-1")] = zlib.decompress(
                    rest[1:]
                ).decode("utf-8", "replace")
            else:  # iTXt, simplified: fields are nul-separated
                parts = body.split(b"\x00")
                key = parts[0].decode("latin-1")
                chunks[key] = parts[-1].decode("utf-8", "replace")
        pos += 12 + length
        if ctype == "IEND":
            break
    return chunks


def main(argv):
    chunks = text_chunks(argv[1])
    print(f"text chunks found: {sorted(chunks)}")
    if "prompt" not in chunks:
        print("no 'prompt' chunk: this PNG carries no workflow")
        return 1
    prompt = json.loads(chunks["prompt"])
    print(f"'prompt' chunk: {len(prompt)} nodes")
    for node_id in sorted(prompt, key=lambda x: int(x)):
        node = prompt[node_id]
        print(f"  node {node_id}: {node['class_type']}")
        inputs = node.get("inputs", {})
        for key in ("text", "seed", "ckpt_name", "filename_prefix"):
            if key in inputs and not isinstance(inputs[key], list):
                print(f"      {key} = {inputs[key]!r}")
    print(f"'workflow' chunk present: {'workflow' in chunks}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
