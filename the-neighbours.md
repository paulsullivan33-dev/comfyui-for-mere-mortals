# The Neighbours

ComfyUI is not the only way to drive an
image model, and for many people it is
not the right first way. An honest map
of the tools a beginner will meet,
including the one this guide keeps
comparing itself to.

## A1111 — the original panel

**Stable Diffusion WebUI**, universally
called **A1111** after its repository's
author (AUTOMATIC1111), is the interface
that taught the world this craft: prompt
box at the top, sliders under it, tabs
for text-to-image, image-to-image, and
extras. Everything ComfyUI draws as a
graph, A1111 arranges as panels and
checkboxes. For making a picture the way
you made the last one, it is faster to
drive; its extension ecosystem is old
and deep. The graph tools win when the
process itself is the thing being built
— A1111's pipeline order is fixed by
its author, ComfyUI's by you. Its
development pace has slowed while
forks and successors (below) carry the
panel tradition on.

## SD.Next — the panel, modernised

**SD.Next** is the panel lineage's
engineering-minded descendant: the same
arrangement of prompt, settings and
gallery, rewritten over a modern engine,
with broad hardware support (including
graphics cards the others treat as
afterthoughts), several model families
behind one interface, and a choice of
*backends* under the hood. Where
ComfyUI's answer to "can it do X?" is
"wire it", SD.Next's is "there is a
setting, and it is probably already
there". Readers who want pictures first
and machinery later are well served by
it; readers who found this guide because
a panel would not bend are in the right
place already. The two share model
files happily — the folders of chapter
4 and SD.Next's library describe the
same `.safetensors` world, and pointing
both at one library is a normal life.

## DiffusionBee — the appliance

**DiffusionBee** is a Mac application:
download it, open it, type a prompt.
No Python, no folders of models to
curate, no graph, almost no settings —
and that is a feature, honestly aimed at
people who want *a picture*, not a
practice. Its ceiling is its floor's
price: when you outgrow the appliance
there is nothing to adjust, only
somewhere to move to. As a first-ever
five minutes with image models on a
Mac, it has no rival here; as a tool to
grow in, it is a doorway, not a room.

## The rest of the street

**InvokeAI** splits the difference: a
polished, opinionated panel with a
unified canvas for inpainting work,
favoured by people doing illustration
professionally. **Fooocus** hides
nearly everything — a prompt and a
style, in the Midjourney manner — and
produces handsome defaults. **Forge**
is A1111's faster, better-memory-mannered
fork. The hosted services (Midjourney
and its kin) are neighbours of a
different kind: no machine of yours at
all, a subscription, their models and
their rules — including rules about
what may be pictured, which local tools
do not impose and chapter 13 discusses
as freedom with its own weight.

The comparisons in this chapter are
characterised, not benchmarked — the
lab ran ComfyUI alone, and picking a
daily tool deserves your own afternoon
with two of them, not this page's
verdict.
