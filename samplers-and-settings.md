# Samplers and Settings

Outcome: the six fields on the KSampler
stop being runes. In a panel tool these
are sliders; here they are fields on one
node, and that is the only difference
that matters — each can be wired,
varied, and saved as part of the
recipe.

## What the sampler is doing

The model does not draw a picture in one
pass. The sampler starts from **noise** —
television static shaped like a latent —
and asks the model, repeatedly, "what
picture is this almost a picture of?"
Each answer removes a little noise. A
**step** is one such round. What remains
at the end is decoded into the image.
Every setting below is a knob on that
one process.

## The six fields

- **seed** — the number the noise is
  grown from. Same seed, same everything
  else: same picture, on the same machine
  and model. Change only the seed and
  everything re-rolls. Beside it, a
  **control after generate** setting
  decides what happens to the seed after
  each run: leave it (*fixed*), add one
  (*increment*), or roll fresh dice
  (*randomize*) — the setting behind a
  thousand "it changed my picture!"
  mysteries, and why careful workflows
  set it to fixed while exploring.
- **steps** — how many noise-removing
  rounds. Too few: a picture still
  dissolving out of static. Enough: the
  picture settles. Beyond enough: time
  spent polishing nothing, and with some
  samplers, worse. 20 is the classic
  starting point for the model family in
  chapter 5; quick modern "turbo" models
  are built for 4–8.
- **cfg** — classifier-free guidance:
  how hard the model must listen to the
  prompt. Low (3–5): loose, dreamy,
  prompt taken as a suggestion. The
  classic 7–8: obedient. High (12+):
  the prompt shouted — colours burn,
  edges harden, pictures can look
  fried. **CFG is a volume knob, not a
  quality knob.**
- **sampler_name** — *which* noise-removal
  algorithm walks the steps: `euler`,
  `euler_ancestral`, `dpmpp_2m`, `ddim`,
  and dozens more. They differ in speed,
  smoothness and flavour, not in moral
  worth. `euler` is the plain, predictable
  starting point this guide's lab used;
  ancestral variants inject fresh noise
  each step and never quite settle (which
  some prompts love); dpmpp family are
  the efficient modern defaults.
- **scheduler** — the *schedule* of how
  much noise each step expects: `normal`,
  `karras`, `exponential`, `sgm_uniform`.
  It partners with the sampler; `karras`
  is the common recommendation with the
  dpmpp samplers. When a shared workflow
  specifies a pair, keep the pair
  together until you know why it works.
- **denoise** — how much of the starting
  latent the sampler is allowed to
  replace. At 1.0 (this chapter's
  setting) the start is pure noise and
  everything is invented. Below 1.0 the
  sampler starts from an existing latent
  and keeps some of it — the entire
  trick of chapter 7, hiding in one
  field.

## Exploring without drowning

The canvas rewards a method panel tools
make awkward: **duplicate and branch.**
Wire one loader and one prompt into two
samplers with different settings, decode
both, save both. One queue press, an
honest A/B, same seed — the comparison
every settings argument needs and
seldom gets. **Check:** the two output
files differ only where the setting
differed; if the seed rolled between
them (set it fixed!), you compared dice,
not settings.

What the lab verified, cheaply, is the
seed's promise: transcript
`t05-reproduce.txt`, chapter 5's
workflow with a different seed,
everything else identical — a different
picture from the same recipe, and the
same-seed run before it reproduced the
original file exactly. Settings are
science only when the dice are pinned.
