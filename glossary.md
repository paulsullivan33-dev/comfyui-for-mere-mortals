# Glossary

**API** — the set of web addresses the
ComfyUI server answers, so scripts can
do everything the mouse can (chapter
10). API format is the workflow spelling
those addresses accept.

**Checkpoint** — one file holding a
whole image model: diffusion model, CLIP
and VAE together (chapter 4).

**CFG** — classifier-free guidance; how
hard the model must obey the prompt
(chapter 6).

**CLIP** — the text-reading part of a
model; turns prompt words into numbers
the sampler can use (chapters 2, 4).

**Conditioning** — a prompt after CLIP
has read it; what the sampler is
actually handed (chapter 2).

**ControlNet** — a second model that
steers generation to fit a map — pose,
depth, edges (chapter 8).

**Custom node** — a node written by
someone other than the core project,
installed as code into `custom_nodes/`
(chapter 11).

**Denoise** — how much of a starting
latent the sampler may replace; 1.0
invents everything, lower values keep
some of the start (chapters 6, 7).

**Diffusion** — the generation method:
start from noise and remove it in
steps, guided by the model, until a
picture remains (chapter 6).

**Embedding** (textual inversion) — a
tiny file teaching the prompt-reader a
new word (chapter 4).

**GPU / VRAM** — the graphics card, and
its own memory; where the models want
to live, and the resource chapter 13
counts (chapters 3, 13).

**Headless** — running the server with
no browser, as an engine other programs
call (chapter 10).

**Img2img** — generation starting from
an existing picture's latent instead of
pure noise (chapter 7).

**Inpainting** — regenerating only the
masked region of a picture (chapter 7).

**KSampler** — the core node that runs
the sampling; the engine room of every
generation graph (chapters 5, 6).

**Latent** — a picture in the model's
compressed inner space, before the VAE
decodes it to pixels (chapter 2).

**LoRA** — a small adapter file that
nudges a big model toward a style or
subject; needs its matching checkpoint
family (chapter 4).

**Manager (ComfyUI-Manager)** — the
best-known custom pack, adding an
in-app browser and installer for other
packs (chapter 11).

**Mask** — a picture-sized map of where
an operation may act (chapters 2, 7).

**Node** — one box on the canvas, one
job, inputs on the left and outputs on
the right (chapter 2).

**Prompt** — the text describing the
picture wanted (positive), or unwanted
(negative) (chapter 5).

**PyTorch** — the library the models
run on; the install step that depends
on your hardware (chapter 3).

**Queue** — the act of submitting a
workflow to run, and the list of jobs
waiting (chapters 2, 10).

**Safetensors** — a model file format
that is data only and cannot carry code;
preferred over `.ckpt` (chapter 4).

**Sampler / Scheduler** — the algorithm
that removes noise step by step, and
the schedule saying how much noise each
step expects (chapter 6).

**Seed** — the number the starting
noise is grown from; pin it and runs
reproduce (chapter 6).

**VAE** — variational autoencoder; the
translator between pixels and latent
space (chapter 2).

**Workflow** — a complete graph of
nodes and wires: one recipe, saved as
JSON or inside a PNG (chapters 2, 9).
