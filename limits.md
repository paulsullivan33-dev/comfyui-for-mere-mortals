# Limits

What ComfyUI cannot do, and what it will
not stop you doing — the chapter the
rest of the guide has been pointing at.

## It has no guard rails, on purpose

ComfyUI contains no opinion about what
pictures should exist. There is no
filter on prompts, no review of outputs,
no account to ban. For research, art,
and private work on your own machine
that absence is the point of local
tools — and it transfers the whole
weight of judgment to the person at the
keyboard. Some of that judgment is
legal, not just tasteful: a generated
picture can defame a real person,
imitate a living artist's livelihood,
or counterfeit evidence, and "the tool
let me" is not a defence anywhere.
Consent does not become optional
because the camera became imaginary.
Chapter 8's steering and chapter 7's
repainting make *specific* imitations
easy; that is precisely where the
operator's rules have to exist, because
the software has none.

## Hardware is the real licence

The tool is free; the arithmetic is
not. Models want **VRAM** — the graphics
card's own memory — and time. Below a
model's appetite, ComfyUI does not
refuse so much as crawl: offloading to
system memory, splitting work, taking
ten minutes over a picture a bigger
card finishes in seconds. The lab ran
on two CPU cores and produced its
256×256 picture in about two minutes
(chapter 5); that is a proof, not a
practice. A
reader whose machine cannot hold a
modern model has honest options — older
smaller models, hosted services
(chapter 12), patience — but no setting
in this guide repeals the arithmetic.

## Graphs rot

A workflow is a snapshot of an
ecosystem in a hurry. Core nodes gain
fields and rename them; packs release
breaking versions; a graph saved last
spring can light up red this autumn
(chapter 14) because three of its nodes
changed their minds. Panel tools hide
this by owning the whole pipeline;
ComfyUI exposes it as the price of
owning yours. The mitigations are
habits, not features: note versions
with shared workflows, update at chosen
moments, keep the last-known-good
graph beside the experiment.

## The canvas is not the whole craft

- **It generates; it does not compose.**
  Layout beyond what control maps can
  dictate (chapter 8), text spelled
  right (models still fumble letters,
  though newer families fumble less),
  and the last retouching mile belong to
  editors and patience.
- **Consistency is earned, not given.**
  The same character across twenty
  pictures is a project — seeds, LoRAs,
  control maps, curation — not a
  checkbox.
- **Serendipity is rationed by seed.**
  The dice are pinned only if you pin
  them (chapter 6); a workflow that
  relies on a lucky roll is a workflow
  that will change its mind on a
  different machine, driver, or version,
  because bitwise sameness across
  hardware is not promised.

## The open door

Chapter 10 said it as a feature;
chapter 13 says it as a limit: the
server has no authentication, sees
workflows as instructions, and executes
the nodes it is given. On a loopback
address, alone, that is a reasonable
design. Exposed to a network — by a
careless `--listen`, a forwarded port,
a tunnel opened for a demo and
forgotten — it is a remote control for
your machine wearing a picture tool's
coat. The limit is not that ComfyUI is
careless; it is that it assumes *you*
are the perimeter. Be one.

And the meta-limit, which the whole
guide has tried to honour: **ComfyUI
cannot make the picture in your head.**
It can be wired, steered, seeded and
re-run until the dice agree with you.
Taste — knowing which output is the one,
and when to stop — remains, stubbornly
and happily, the operator's job.
