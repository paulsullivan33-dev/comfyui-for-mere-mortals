# Models and Folders

Outcome: a model file in your hand and
no doubt about which folder it belongs
in — because ComfyUI is strict about
this in a way panel tools are not. A
panel loads "a model". ComfyUI's graph
has different *kinds* of node eating
different kinds of file, and each kind
has its own folder under `models/`. A
file in the wrong folder is, to the
node that wants it, simply not there.

## The checkpoint: the whole kitchen

A **checkpoint** is a single file
(usually `.safetensors`) containing a
complete image model: the **diffusion
model** that imagines, the **CLIP** text
reader that understands prompts, and the
**VAE** that decodes the result to
pixels — the three outputs of chapter
2's loader, from one file. Checkpoints
live in `models/checkpoints/`.

They are big: roughly 2 GB for an older
SD 1.5 model in half precision, 6–7 GB
for SDXL, more for the newest families.
Half precision (**fp16**) files hold
each number in half the space, run
faster, and are what nearly everyone
uses; a file named `-fp16` or *pruned*
is the same model trimmed for use rather
than for further training. Download from
the model's own page — Hugging Face and
Civitai are the two big libraries — and
prefer `.safetensors` over the older
`.ckpt` format: a safetensors file is
data only, while a `.ckpt` can carry
executable code, which is chapter 1's
rule wearing a different hat.

The lab's checkpoint, for the record, is
`v1-5-pruned-emaonly.safetensors` — the
original Stable Diffusion 1.5, old and
honest: a good first model precisely
because it is undemanding and every
tool knows it, even though newer models
draw better.

## The split models: parts, separately

Newer model families arrive in pieces,
and ComfyUI has loader nodes for each
piece:

- `models/diffusion_models/` (older name
  `unet`) — the imagining engine alone.
- `models/text_encoders/` (older name
  `clip`) — the prompt reader, sometimes
  two of them.
- `models/vae/` — a standalone VAE. A
  checkpoint's built-in VAE is usually
  fine; a separate one is loaded when a
  model ships without, or when a sharper
  decoder is recommended for it.

Current ComfyUI's own starter workflow
uses these split loaders, because the
model it starts with ships in pieces.
The classic workflow in chapter 5 uses
one checkpoint instead. Both are the
same skeleton from chapter 2; only the
loading differs.

## The seasoning shelf

- **LoRA** — `models/loras/`. A small
  file (tens to a few hundred MB) that
  nudges a big model toward a style, a
  character, a subject. It is an adapter,
  not a model: useless alone, powerful
  clipped onto the checkpoint it was
  made for — and only that family of
  checkpoint. A LoRA node sits between
  loader and sampler, passing MODEL and
  CLIP through with the nudge applied,
  at a **strength** you set.
- **Embeddings** (textual inversions) —
  `models/embeddings/`. Tiny files that
  teach the prompt-reader a new word:
  put one in the folder and typing its
  name in a prompt invokes it.
- **ControlNet models** — `models/controlnet/`.
  Chapter 8's steering machinery; one
  file per kind of steering (pose,
  depth, edges).
- **Upscalers** — `models/upscale_models/`.
  Models that enlarge a finished image
  more cleverly than stretching it.
- **VAE approximations** and others —
  folders you may never open; they exist
  because some node, somewhere, wants
  them.

## Making ComfyUI look elsewhere

Models are large and multiply quickly;
keeping a second library — shared with
another tool, or on a bigger disk — is
common. Copy `extra_model_paths.yaml.example`
to `extra_model_paths.yaml`, uncomment
and edit a block naming the other
folder tree, and restart. ComfyUI then
offers the files from both places in
every loader's list. **Check:** a file
you placed in the second library appears
in the checkpoint dropdown after a
restart — if it does not, the path in
the YAML is wrong, not the file.

And the dropdown is the everyday check
for this whole chapter: **if a loader
does not list your file, the file is in
the wrong folder, has the wrong
extension, or ComfyUI was already
running when it arrived** (click the
refresh, or restart). The lab hit the
same wall from the other side in
transcript `t03-validation.txt`: a
workflow politely refused, with names,
because the checkpoint it asked for —
a name the lab invented for the test —
was not on the machine.
