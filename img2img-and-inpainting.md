# Img2img and Inpainting

Outcome: instead of inventing a picture
from noise alone, you start from a
picture that already exists — either
letting the model reinterpret the whole
thing, or repainting one region while
the rest is held still. Both tricks from
chapter 5 survive; only the sampler's
starting point changes.

## Img2img: start from a picture

Chapter 6 left one field unexplained
until now: **denoise**. In text-to-image
there is nothing to preserve, so the
sampler starts from pure noise and
denoise is 1.0. **Img2img** swaps the
EmptyLatentImage node for two:

- **LoadImage** — picks a file from the
  `input/` folder, outputs an IMAGE.
- **VAEEncode** — takes that IMAGE and
  the loader's VAE, and outputs the
  LATENT version of it.

That latent goes into the sampler where
the empty one used to, everything else
is wired as before, and now denoise
does its work: the sampler adds noise
*up to* the denoise level and then
removes it, re-imagining as it goes.

- **Denoise 0.2–0.35** — a respectful
  pass: same composition, cleaned up,
  restyled at the edges.
- **0.5–0.65** — a reinterpretation: the
  layout survives, the details are the
  model's own.
- **0.8 and up** — a new picture that
  merely took your composition as a
  rumour.

The classic uses are restyling (a photo
in the manner of a watercolour prompt),
rescuing (a rough render or sketch
finished by the model), and consistency
work (variations on a picture you
already like). **Check:** with denoise
at 0, the output is your input re-encoded
— nearly identical, which proves the
wiring before you spend steps on it.

## Inpainting: repaint only this

**Inpainting** asks for one region to be
re-imagined while the rest is kept. Its
extra ingredient is a **MASK**: a
picture-sized map where white says
*repaint here* and black says *hands
off*. You make the mask in the browser
by right-clicking a LoadImage node and
opening the **mask editor** — a simple
paint-over tool — or by loading a mask
made elsewhere.

The wiring grows a little:

- The image still goes through
  **VAEEncode**, but the inpainting form
  of the node (VAEEncodeForInpaint) also
  takes the MASK and a *grow* value that
  softens the mask's edge.
- A **SetLatentNoiseMask** pattern, or
  the dedicated inpaint nodes in newer
  packs, ensures the sampler only lays
  fresh noise inside the mask.
- The prompt describes what should be
  *in the hole*, not the whole picture:
  for a masked-out bowl of fruit on the
  table, "a small vase of sunflowers",
  not the entire room's biography.

Denoise here is usually high — 0.85–1.0
inside the mask is normal, because the
region is meant to be invented whole.
Seams are the craft: a mask slightly
larger than the thing removed, a prompt
that respects the picture's light, and
the edge softening (grow/feather) are
what keep the repair invisible.

Both techniques are described from the
project's documentation and the
verified graph model of chapters 2 and
5; the lab did not run them — its CPU
budget went to the end-to-end proof in
chapter 5, and `criteria.md` says so.
The wiring, though, is only chapter 5's
graph with the starting latent swapped,
and reading it should by now feel like
exactly that.
