# Custom Nodes and the Manager

Outcome: you know how ComfyUI grows new
abilities, how the tool that installs
them works, and — the point of the
chapter — how to decide what earns a
place in your `custom_nodes/` folder.

## What custom nodes are

The core nodes are a good general
toolbox, but the field invents a new
technique monthly, and ComfyUI's answer
is not to wait for releases. A **custom
node pack** is a folder of Python code
placed in `custom_nodes/`; at startup,
ComfyUI runs it, and the nodes it
defines appear in the canvas beside the
core ones — indistinguishable in the
menu, which is convenient and is also
the whole problem, addressed below.

Packs exist for everything: face
restoration and detailing, extra
samplers, video pipelines, batch
managers, nodes that read and write
files, nodes that call other services.
A large fraction of the workflows
circulating online need at least one
pack the core does not have.

## The Manager

Installing by hand means cloning a
repository into `custom_nodes/` and
installing its requirements — visible,
copyable, and fussy. **ComfyUI-Manager**
is itself a custom node pack that adds
a Manager button to the interface:
browse a catalogue of packs, install,
update, and uninstall them from inside
the tool, and — its kindest feature —
when a loaded workflow is missing
nodes, **Install Missing Custom Nodes**
offers the packs they came from.

Use it with your eyes open:

- The Manager makes installing *easy*,
  not *safe*. The catalogue is a
  directory, not a guarantee; entries
  are community projects of every age
  and level of care.
- A pack can declare Python
  **dependencies**, and installing the
  pack installs those too.
- Updates are whole-pack: the code you
  audited last month is not necessarily
  the code running this month, which
  argues for updating on purpose, at a
  quiet moment — never because a
  workflow is impatient.

## The trust rules, spelled out

Chapter 1 gave the rule; here is the
practice. A custom node executes when a
workflow containing it runs, with the
permissions of the user who started
ComfyUI. Nothing sandboxes it. Assume
any pack *could* read your files, use
your network, and change your outputs —
then decide:

1. **Named author, real history.** A
   project page with a history of
   commits, other users, and issues
   answered beats a fresh upload with a
   eager description, every time.
2. **Popularity is evidence, not proof.**
   Widely used packs are widely looked
   at; that raises the cost of mischief
   but does not audit the code for you.
3. **Small and single-purpose beats
   kitchen-sink.** A pack that adds one
   node exposes one node's worth of
   code to your trust.
4. **Install the fewest packs that do
   the job.** Every pack is a standing
   permission. The lab's machine ran
   with **zero** custom nodes — the
   whole verification in this guide is
   core-only — which is the right default
   to depart from deliberately, not a
   purity to perform.
5. **When a workflow demands a pack**,
   the two-minute audit of chapter 9
   happens *before* the Manager's
   install button, not after the first
   mysterious behaviour.

The same scepticism, scaled down,
applies to model files from strangers:
`.safetensors` cannot execute (chapter
4), which is one more reason to prefer
the format — but a model still decides
what your pictures look like, and a
packaged workflow-plus-model bundle
from an unknown source deserves the
full audit, both halves.
