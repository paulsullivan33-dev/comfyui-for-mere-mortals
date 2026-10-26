# ComfyUI for Mere Mortals

Most tools for making pictures with an
**AI image model** give you a panel: a
box for the prompt, sliders for the
settings, a button. **ComfyUI** gives you
a **canvas** instead. On the canvas sit
**nodes** — small labelled boxes, one
for loading a model, one for turning a
prompt into numbers, one for the actual
generation — and you join them with
**wires** that carry the work from one
node to the next. Press Queue, and the
machine walks your wiring and makes the
picture.

That sounds like more work than a panel,
and for a single picture it is. The
payoff comes later: the wiring *is* the
recipe. Nothing is hidden behind a
settings page. A workflow someone hands
you shows you every step it takes, in
order, with the values in plain sight —
and the picture it produces carries the
whole recipe inside it, so you can open
it, learn from it, and run it yourself.

This guide explains the model behind
the canvas, how to install ComfyUI, where
the model files live and why there are
so many folders, and how to build and
read the standard first workflow node by
node. Then come the sampler settings in
node terms, starting from an existing
picture (img2img and inpainting), steering
a picture with ControlNet, saving and
sharing workflows, driving ComfyUI from
a script through its API, and adding
**custom nodes** — with the safety rule
that matters most in this tool stated
early and repeated where it belongs:
**a custom node is somebody else's
program, running with your permissions,
on your machine.** Only install ones you
have reason to trust.

The lab behind this guide ran the real
thing: **ComfyUI 0.42.0**, installed from
source on a small Linux machine with no
graphics card worth the name, run
entirely on the **CPU**. Against it the
lab started the server and checked the
interface answered, asked the API for
its list of nodes, offered it a workflow
naming a model the machine did not have
and kept the honest error, then
downloaded a real checkpoint and ran the
classic first workflow end to end
through the API — prompt in, picture
out, and the picture's embedded recipe
read back and checked against the
workflow that made it. The identical
workflow ran again and returned the
identical file in seconds, from the
cache; with only the seed changed, it
returned a different picture from the
same recipe.

What the lab could not do, it did not
fake. With two CPU cores and no GPU,
everything graphical beyond that first
small, short run — ControlNet, big
models, inpainting at real sizes,
animation — is taught from the
project's documentation and labelled as
such wherever it appears. `criteria.md`
keeps the full ledger of what was run
and what was only read.

## What this guide covers

- [**What ComfyUI is**](what-comfyui-is.md) —
  the node graph against the panel
  interfaces, what you gain and what it
  costs, and the one safety rule
- [**The mental model**](the-mental-model.md) —
  nodes, wires, the types that travel
  along them, execution order, and why
  ComfyUI only re-runs what changed
- [**Installing ComfyUI**](installing-comfyui.md) —
  the portable build, installing from
  source with pip, and the first launch
- [**Models and folders**](models-and-folders.md) —
  checkpoints, VAEs, LoRAs, embeddings
  and ControlNet models: what each is
  and which folder it belongs in
- [**Your first workflow**](your-first-workflow.md) —
  the standard text-to-image graph,
  taken apart node by node
- [**Samplers and settings**](samplers-and-settings.md) —
  steps, CFG, seed, sampler and
  scheduler, denoise — as nodes and
  fields, not panel sliders
- [**Img2img and inpainting**](img2img-and-inpainting.md) —
  starting from a picture you already
  have, and repainting only the part
  under a mask
- [**ControlNet — steering the picture**](controlnet.md) —
  poses, edges and depth maps as a
  second set of instructions the model
  must obey
- [**Saving and sharing workflows**](saving-and-sharing-workflows.md) —
  workflow JSON, the recipe hidden
  inside every PNG, and what to check
  before running a stranger's graph
- [**The API and headless running**](the-api-and-headless.md) —
  queueing workflows from a script, the
  queue and history endpoints, and
  ComfyUI as a back end with no browser
- [**Custom nodes and the Manager**](custom-nodes.md) —
  extending the toolbox, the Manager
  that installs extensions, and why
  every custom node is a trust decision
- [**The neighbours**](the-neighbours.md) —
  SD.Next, A1111 and DiffusionBee: the
  panel tools, honestly compared
- [**Limits**](limits.md) — no guard
  rails, real hardware appetites, graphs
  that rot, and what the canvas cannot
  do for you
- [**Troubleshooting**](troubleshooting.md) —
  the red node, the model that is not
  in the list, the out-of-memory wall,
  and the traps this guide's lab fell
  into so you don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Making the models themselves — training
and fine-tuning are a different craft,
pointed at once and left there. Running
ComfyUI as a public multi-user service,
with accounts and queues of strangers,
is likewise out; this guide stays with
one person and their own machine.
Workflows built to imitate a real
person, or to strip the credit and
consent out of somebody else's art, are
not a harder chapter of this book; the
limits chapter says why, briefly.

## How to use this guide

Read chapter 1 for the idea and the
rule, and chapter 2 before installing
anything — once nodes, wires and
execution order make sense, the rest of
the guide is vocabulary. Chapters 3 to
5 take you from a bare machine to a
finished picture in one sitting. Chapter
11 is not the optional chapter: read it
before your first custom node, because
installing one is running a stranger's
code, and the time to decide your rules
is before the interesting extension
appears. The lab's transcripts live in
`comfyui-lab/transcripts/`; its workflow
and runner script are `comfyui-lab/`;
its notes are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Local AI for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)
- [AI for Mere Mortals](https://paulsullivan33-dev.github.io/ai-for-mere-mortals/)
- [Open WebUI for Mere Mortals](https://paulsullivan33-dev.github.io/open-webui-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/comfyui-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/comfyui-for-mere-mortals/blob/main/LICENSE-CODE).
