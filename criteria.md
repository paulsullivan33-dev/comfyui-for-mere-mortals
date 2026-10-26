# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab generated one invented teapot, and nothing else.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do and will not stop you doing: no guard rails of
   any kind, so judgment and consent sit entirely with the
   operator; hardware appetites that no setting repeals;
   workflows that rot as nodes change; consistency and text
   that must be earned rather than checked on; and an API with
   no authentication, safe only behind a perimeter the
   operator provides.
8. **The safety rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *a custom node is somebody
   else's program, running with your permissions* — before any
   chapter depends on it, and chapters 9 and 11 give it working
   form: audit a stranger's workflow before queueing it, and
   treat every node pack as a trust decision with named tests.
9. **Builds clean, and the ledger is honest.** The site builds
   with MkDocs in strict mode with no warnings, and a fresh
   reader following the chapters in order reaches the stated
   outcome of each. The verification notes below are the
   ledger: what was run for real on the lab machine, and what
   is documented-only, with nothing in the second list
   described anywhere as if it were in the first.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox with
no usable GPU. ComfyUI **0.42.0** was installed from the
project's source archive into a fresh virtual environment
(Python 3.12.3, PyTorch 2.14.1+cpu) and run with
`--cpu --listen 127.0.0.1 --port 8188`. All transcripts live in
`comfyui-lab/transcripts/`; the workflow the lab ran is
`comfyui-lab/workflows/first-workflow.json`, the runner is
`comfyui-lab/run-workflow.py`, and the metadata reader is
`comfyui-lab/read-embedded.py`.

Run for real, with transcripts as evidence:

- Versions of Python, PyTorch and ComfyUI (t00), and the
  server's startup log: CPU device, GUI address line (t01).
- The API answering a script: `/system_stats` reporting
  version 0.42.0 and device `cpu`, the web UI's page title,
  and `/object_info` counting **1,014 node types** on the
  stock install, with every node the guide's chapters rely on
  present (t02).
- Workflow validation before queueing: the first-workflow
  graph with an invented checkpoint name was refused with
  HTTP 400, `value_not_in_list`, naming the one checkpoint
  the machine did have (t03).
- End-to-end generation on CPU: the classic graph
  (CheckpointLoaderSimple, two CLIPTextEncode nodes,
  EmptyLatentImage 256×256, KSampler euler/normal at 4 steps,
  cfg 7.0, seed 42, VAEDecode, SaveImage) against
  `v1-5-pruned-emaonly.safetensors` (Stable Diffusion 1.5,
  4,265,146,304 bytes, from the public Hugging Face mirror),
  finishing successfully in about 112 s and saving
  `lab-first_00001_.png` (t04, t07).
- Reproducibility, both directions: the identical workflow
  returned in 5 s from the cache with the output file
  byte-identical by sha256 before and after; with only the
  seed changed to 43, a new, different file by hash, both
  outputs confirmed as real 256×256 PNGs (t05).
- The embedded-recipe promise of chapter 9: the output PNG's
  `prompt` chunk read back by a standard-library script,
  showing all 7 nodes with the lab's prompt text, checkpoint
  name and seed — and honestly showing no `workflow` chunk,
  because the run came through the API (t06).

What the generation actually looks like is stated in
chapter 5, not hidden: at 4 steps on CPU the picture is a
rough smudge that barely suggests its subject. The pipeline,
the caching, the seed behaviour and the metadata are the
verified claims; picture quality at real settings is not
among them.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything on a GPU, and ComfyUI's portable and desktop
  installers (the lab installed from source, on CPU).
- The browser canvas as a working surface (its page title
  and the server behind it were verified; no clicking was
  done, because clicks leave no transcript).
- Img2img, inpainting and the mask editor (chapter 7);
  ControlNet preprocessors and application (chapter 8);
  LoRA loading, split-model loaders and upscalers
  (chapter 4 describes their folders and wiring from the
  documentation and the server's own node list).
- Custom nodes and ComfyUI-Manager (chapter 11) — the lab
  deliberately ran a stock, zero-custom-node install, which
  is the state chapter 11 recommends starting from.
- `extra_model_paths.yaml` sharing of a model library
  (chapter 4 states the check a reader can run; the lab's
  single library never needed it).
- The comparison tools in chapter 12 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: one
invented still-life prompt ("a red teapot on a wooden table,
photograph"), one invented failure (a checkpoint name that
does not exist), and two small standard-library scripts. No
example is modelled on any real person, place, network or
organisation.
