# Saving and Sharing Workflows

Outcome: you can save a workflow, hand
it to someone, receive one back, and
know the two ways a recipe travels — as
a file of its own, and hidden inside
every picture it makes.

## The two formats, again

Chapter 2 named them; here they earn
their keep.

- **Save** (from the canvas) writes the
  **UI format**: node positions, colours,
  your exact arrangement. This is the
  format for *people* — it reopens as
  the same picture of a graph.
- **Save (API Format)** — after enabling
  the developer option in settings —
  writes the **API format**: just the
  graph's meaning, numbered nodes and
  their inputs. This is the format for
  *programs* — chapter 10's scripts post
  exactly this, and the lab's
  `comfyui-lab/workflows/first-workflow.json`
  is one.

Both are **JSON**: plain text, braces
and lists, readable in any editor. That
readability is a security feature if you
use it, which brings us to receiving.

## The picture that carries its recipe

Every PNG the SaveImage node writes has
its workflow **embedded in its
metadata**: the **prompt chunk** holds
the API spelling of the graph — prompts,
seed, node list and all — and a run made
from the canvas adds a **workflow
chunk** with the UI spelling too. Drag
such a picture onto a ComfyUI canvas
and the graph rebuilds itself. This is
the feature that makes ComfyUI culture
what it is: pictures shared on model
sites arrive with their workings shown,
and "how was this made?" has a literal
answer.

The lab verified this rather than
admiring it: transcript
`t06-embedded.txt` reads the metadata
out of chapter 5's output file with a
script and finds the lab's own prompt,
seed and node list inside the prompt
chunk — the recipe, in the meal, as
advertised. (No workflow chunk: the
lab's run came through the API, which
is the chunk's absence explained, not
a promise broken.)

The mirror-image warning writes itself:
**a picture you share shares its prompts
too.** An embarrassing draft prompt, a
private name typed into a negative
prompt, travels with the file unless
you strip metadata first. Other tools'
outputs can also hide ComfyUI metadata
they never earned; trust, as ever, is
per-file.

## Receiving a workflow: the two-minute audit

A downloaded graph that will not run is
normal — models differ, nodes are
missing — and chapter 14 covers the
mechanics. Before the mechanics, the
audit, because chapter 1's rule needs
its practical form:

1. **Open it as text first.** JSON is
   readable. Look at the node kinds
   (`class_type` in API format). Loaders,
   encoders, samplers: expected. Anything
   that writes files, runs commands, or
   fetches from the network: that node is
   doing more than drawing, and chapter
   11's trust rule applies to *it*.
2. **Missing nodes are a question, not
   an errand.** The canvas marks nodes it
   cannot find in red and names the pack
   they came from. Installing that pack
   is installing its author's program.
   The two minutes to look the pack up
   are the cheapest security you will
   ever buy.
3. **Check the values, not just the
   boxes.** A workflow carries file paths
   and output prefixes; a saver pointing
   somewhere odd, or a loader naming a
   model you have never heard of, is
   worth a pause.

Workflows are data, and opening one runs
nothing — execution begins at Queue, and
Queue is your decision. Make it a
decision.
