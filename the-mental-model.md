# The Mental Model

Outcome first: by the end of this short
chapter you will be able to look at any
ComfyUI graph and say what will happen,
in what order, and why changing one
number does not mean starting the whole
job again. Everything after this chapter
is vocabulary on top of that.

## Nodes: one box, one job

A **node** is a box on the canvas with a
job, some **inputs** on its left edge,
some **outputs** on its right edge, and
usually a few **fields** — numbers and
words you type directly into the box. A
loader node has a field naming the file
to load and outputs for what it found
inside. The KSampler has fields for its
settings and inputs for everything it
must be handed: model, prompts, and a
starting canvas of noise.

Nodes come from the program itself — the
**core nodes** — or from **custom node**
packs other people wrote (chapter 11).
The canvas does not care which; a node
is a node. That indifference is exactly
why chapter 1's rule exists.

## Wires carry typed things

A **wire** joins one node's output to
another node's input. Wires are fussy
about what they carry: each socket has a
**type**, shown by its colour, and a wire
only lands where the type matches. The
types you will meet first:

- **MODEL** — the image model itself,
  loaded and ready.
- **CLIP** — the text-reading half of the
  model; prompts go through it.
- **VAE** — the part that translates
  between pictures and the model's inner
  working space.
- **CONDITIONING** — a prompt after CLIP
  has read it: instructions in the form
  the sampler uses.
- **LATENT** — a picture in the model's
  inner space: compressed, unfinished,
  not yet pixels.
- **IMAGE** — actual pixels: a finished
  or loaded picture.
- **MASK** — a picture-sized instruction
  about *where*: paint here, not there.

That inner working space has a name:
**latent space**. Models do their
imagining there because it is small and
fast; the **VAE** (variational
autoencoder) decodes a latent into an
image at the end and encodes images into
latents when you start from one
(chapter 7). Half of ComfyUI literacy is
simply noticing, before you wire, whether
a socket wants a latent or an image.

## Execution: the graph walks itself

When you press Queue, you are not
running the nodes left to right like
reading. ComfyUI starts from the **output
nodes** — the ones that end a chain, like
Save Image or Preview Image — and asks:
*what do you need?* Each unanswered need
traces a wire backwards: Save Image needs
an image, so VAEDecode must run; it needs
a latent and a VAE, so the sampler and
the loader must run; and so on back to
the sources. This demand-driven walk is
called **execution order**, and it has
two consequences worth memorising:

- **Unconnected branches do not run.** A
  node whose output leads nowhere is
  decoration. (It can also be your
  mistake: the classic first-day bug is a
  beautiful graph whose sampler was never
  wired to a saver.)
- **Only what changed runs again.** The
  server remembers each node's result.
  Queue the same graph twice and the
  second run is nearly instant — every
  answer is already known. Change the
  prompt and only the text encoding, the
  sampler, and everything downstream of
  them re-run; the loader sits it out.
  This **caching** is why exploring in
  ComfyUI feels quick despite the heavy
  machinery, and why chapter 6's seed
  experiments cost seconds, not minutes.

Check: the console window behind the
browser prints each node as it executes.
Queue a graph, then queue it again
untouched, and the second log is a
whisper of the first.

## Widgets, fields, and the two formats

Values typed into a node are stored in
the workflow itself. That makes a
workflow a complete, portable recipe —
and makes chapter 9's warning real: a
shared workflow carries its author's
settings, sizes, and file names into
your machine, where most will be
harmless and some may point at files you
do not have.

Workflows exist in two forms. The **UI
format** is what the canvas saves from
the Save button: it knows where each box
sits on the screen, its colour, the zoom.
The **API format** is the same graph
stripped to what the engine needs — node
number, kind, inputs, values — and it is
what scripts send (chapter 10). The
browser can produce either (a developer
setting turns on "Save (API Format)").
Same graph, two spellings; the lab's
workflow in `comfyui-lab/workflows/` is
the API spelling, because that is the
one a script can post.

## The shape of nearly every graph

Strip any text-to-image workflow down
and the skeleton is always:

**load → describe → imagine → decode →
keep.**

Chapter 5 builds that skeleton node by
node. ControlNet (chapter 8) adds a
second describer; img2img (chapter 7)
changes where the imagining starts.
But the skeleton holds, and when a
stranger's graph confuses you, finding
its KSampler and walking the wires
backwards is the way to read it.
