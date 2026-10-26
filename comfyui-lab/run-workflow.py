#!/usr/bin/env python3
"""Queue a ComfyUI workflow (API format) and wait for its output.

Usage:
    python3 run-workflow.py WORKFLOW.json [--seed N] [--base URL]

Posts the workflow to the server's /prompt endpoint, polls
/history/<prompt_id> until the job finishes, then prints the
saved output filename(s). Standard library only.

Exit codes: 0 = job completed and outputs listed,
1 = the server refused the workflow (its reasons are printed),
2 = timed out waiting.
"""

import json
import sys
import time
import urllib.request

DEFAULT_BASE = "http://127.0.0.1:8188"
TIMEOUT_SECONDS = 1800
POLL_SECONDS = 5


def post_json(url, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", "replace")
        try:
            return err.code, json.loads(body)
        except json.JSONDecodeError:
            return err.code, {"raw": body}


def get_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    workflow_path = argv[1]
    seed = None
    base = DEFAULT_BASE
    rest = argv[2:]
    while rest:
        if rest[0] == "--seed" and len(rest) > 1:
            seed = int(rest[1])
            rest = rest[2:]
        elif rest[0] == "--base" and len(rest) > 1:
            base = rest[1]
            rest = rest[2:]
        else:
            print(f"unknown argument: {rest[0]}")
            return 2

    with open(workflow_path, encoding="utf-8") as fh:
        workflow = json.load(fh)

    if seed is not None:
        for node in workflow.values():
            if node.get("class_type") == "KSampler":
                node["inputs"]["seed"] = seed
        print(f"seed overridden to {seed}")

    status, answer = post_json(base + "/prompt", {"prompt": workflow})
    print(f"POST /prompt -> {status}")
    print(json.dumps(answer, indent=2))
    if status != 200:
        print("the server refused this workflow; see its reasons above")
        return 1

    prompt_id = answer["prompt_id"]
    print(f"queued as prompt_id {prompt_id}; polling /history ...")
    waited = 0
    while waited < TIMEOUT_SECONDS:
        time.sleep(POLL_SECONDS)
        waited += POLL_SECONDS
        history = get_json(f"{base}/history/{prompt_id}")
        if prompt_id not in history:
            continue
        entry = history[prompt_id]
        state = entry.get("status", {})
        print(f"after {waited}s: status = {state.get('status_str')}")
        if not state.get("completed"):
            continue
        outputs = entry.get("outputs", {})
        for node_id, node_out in outputs.items():
            for image in node_out.get("images", []):
                print(
                    "output image: "
                    f"{image['filename']} (node {node_id}, "
                    f"type {image.get('type')})"
                )
        return 0
    print("timed out waiting for the job to finish")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
