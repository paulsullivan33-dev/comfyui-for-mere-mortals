# What ComfyUI Is

An **AI image model** takes a written
description — a **prompt** — and produces
a picture. Every tool for driving one has
to answer the same practical questions:
which model, what prompt, how large, how
many attempts, with what settings? Most
tools answer them the way a microwave
does: a fixed panel of controls, one
button, and the machinery out of sight.

**ComfyUI refuses the panel.** It is a
program, written by the developer known
as comfyanonymous and now maintained
with a wide community, that shows you
the machinery itself. The main window is
a **graph**: a canvas of **nodes** —
small boxes, each doing one job — joined
by **wires**. One node loads the model.
Two nodes turn your positive and negative
prompts into **conditioning**, the form a
model can actually read. A node called
**KSampler** does the generation. A node
decodes the result into pixels, and a
node saves it. You press **Queue**, the
program walks the wires, and the picture
appears.

The graph a set of nodes and wires forms
is called a **workflow**, and the workflow
is the heart of the tool. Chapter 2 gives
the mental model properly; this chapter
is about what the choice buys, and what
it costs.

## Why anyone would do this

- **Nothing is hidden.** On a panel, the
  order of operations is the program's
  secret — did the upscale happen before
  or after the face fix? In a graph, the
  order is drawn on the screen. If a step
  exists, you can point at it.
- **The recipe travels with the meal.**
  Every picture ComfyUI saves carries its
  whole workflow inside the file
  (chapter 9). A panel tool's settings
  vanish into a screenshot or a settings
  file; a ComfyUI picture *is* its own
  documentation.
- **Anything can be rearranged.** Want
  the picture upscaled, then passed to a
  second sampler with a different prompt?
  On a panel, you hope the author added
  that mode. On the canvas, you wire it.
- **It can be driven without hands.**
  The same graph the mouse builds can be
  sent to ComfyUI as data, by a script
  (chapter 10). Batch jobs, other
  programs, a button on a web page of
  your own — all become possible because
  the workflow is a file, not a gesture.

## What it costs

Honesty requires the other column. A
beginner's first hour in ComfyUI is
harder than a beginner's first hour with
a panel: there are more things on the
screen, most of them unexplained, and
the graph can be *wrong* in ways a panel
cannot — wires unconnected, a model fed
into the wrong socket. Graphs shared by
experts can be enormous, hundreds of
nodes in coloured thickets, and reading
one is a skill this guide starts but
does not finish. And ComfyUI trusts you
completely, which chapter 13 will show
is a limit as much as a feature: it has
no opinion about what you ask for, no
guard rails, and no undo worth the name.

## The rule, stated before everything else

One hazard in this tool is bigger than
a confusing first hour, and it is not
the models. ComfyUI can be extended with
**custom nodes**: extra boxes written by
anyone, installed into the program, that
run whenever your workflow uses them.
In the eyes of your computer there is no
difference between a custom node and any
other program you choose to run:

> **A custom node is somebody else's
> program, running with your permissions,
> on your machine. Install only ones you
> have reason to trust.**

"Reason to trust" is ordinary, not
paranoid: a named author whose other
work you know, a project page with real
history and other users, code you or
someone you trust has read. Chapter 11
gives the full rules and shows where the
line sits. The rule is stated here, in
chapter 1, because the temptation to
install first and think later arrives
the moment a downloaded workflow lights
up with missing-node errors — and by
then it is a decision made in a hurry,
which is the worst kind.

A smaller rule rides with it: **a
workflow is data, but check it anyway.**
Opening a stranger's workflow file does
not run anything by itself — it only
draws boxes. Running it asks every node
in it to do its job, including any node
whose job you did not look at. Chapter 9
shows how to read a workflow before you
queue it.

## A familiar shape

Under the canvas, ComfyUI is a **server**:
a program that waits on an address (on
your own machine, `127.0.0.1:8188`) and a
**front end** in your browser talking to
it. That split sounds like trivia and is
actually the key to chapter 10: anything
the browser can ask the server for, a
script can ask for too. The lab in this
guide mostly talked to the server
directly, through its **API** — the set
of web addresses the server answers —
because an API call leaves a transcript
you can keep, and a mouse click does not.

A first taste, after installing
(chapter 3): open the page, and the
starter graph is already drawn. Press
Queue Prompt with a model loaded and the
sampler counts its steps in the console;
seconds or minutes later the picture sits
in the output panel and in the `output`
folder on disk, carrying its recipe with
it.

## Who it is for

The person who outgrew the panel: the
settings they need are behind a mode
that does not exist, or the process they
invented takes eleven steps by hand,
every time. The person who learns by
seeing the machine, not the microwave.
The person building something — a small
service, a batch job — that needs
pictures made without a human at the
mouse. If a panel still does everything
you want, chapter 12 says so kindly and
points at the neighbours without a
trace of shame.

## What it is not

ComfyUI is not a model: it ships with
none, and chapter 4 is about feeding it.
It is not an editor: it does not retouch
with brushes the way a photo program
does — it *generates*, and editing means
regenerating with more instructions
(chapter 7). It is not a gallery or a
social network: pictures stay on your
machine unless you carry them somewhere.
And it is not safe-by-default in the way
a curated app is: it will run the graph
you drew, the model you loaded and the
nodes you installed, and its opinion of
all three is that they were your choices.
The rest of this guide is about making
them good ones.
