# Installing ComfyUI

Outcome: ComfyUI running on your machine,
its page open in a browser, and you able
to say which folder everything landed
in. ComfyUI runs on Windows, macOS and
Linux. It is happiest with an **NVIDIA
graphics card** (a **GPU**), works on
recent Apple-silicon Macs and on AMD and
Intel graphics with more effort, and can
run on the plain **CPU** — slowly, which
is fine for learning and is exactly what
this guide's lab did.

## The three ways in

**The portable build (Windows).** The
project publishes a self-contained
package for Windows with an NVIDIA card:
download, unzip, double-click the batch
file. Python and every library ride
inside the folder, so nothing else on
the machine is touched and deleting the
folder uninstalls it. For a first
machine this is the kindest door, and
the one the documentation leads with.
There is also a desktop application in
the same spirit.

**From source (everywhere).** Clone the
repository (or download its archive),
install **PyTorch** — the engine room
library the models run on — for your
hardware, install the listed
requirements, and start the program with
Python. More moving parts, but every
part is visible, and it is the only door
on Linux and the one this guide's lab
used. The shape of it:

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python -m venv venv
venv/bin/pip install torch torchvision torchaudio
venv/bin/pip install -r requirements.txt
venv/bin/python main.py
```

The PyTorch line is the one that varies:
its website offers a selector that writes
the exact command for your card and
operating system, including the plain-CPU
variant. Copy it from there rather than
from memory — the right wheel for the
wrong hardware is the commonest install
failure in this corner of computing.

**A package manager or a pinokio-style
installer** exists for some platforms;
the advice is the same as everywhere in
this guide: prefer the project's own
documented routes.

## The first launch

Starting the program prints a short log
and ends with an address:

```bash
venv/bin/python main.py --cpu --listen 127.0.0.1 --port 8188
```

Open `http://127.0.0.1:8188` in a browser
and the canvas appears, with a starter
workflow drawn. The flags the lab used
deserve a sentence each, because you will
meet them again:

- `--cpu` — do not look for a GPU; run
  on the processor. Slow, honest, and
  the reason the lab's generation in
  chapter 5 is small and short.
- `--listen 127.0.0.1` — answer only
  this machine. ComfyUI has **no login
  and no password**; anything that can
  reach the port can run workflows and
  read your outputs. On your own machine
  that is fine. `--listen 0.0.0.0` opens
  it to the whole local network, which
  is a decision to make on purpose,
  never by default (chapter 13 returns
  to this).
- `--port 8188` — the usual port; change
  it only if something else holds it.

**Check:** the console prints the
version and a line like `To see the GUI
go to: http://127.0.0.1:8188`, and the
browser shows the canvas. The lab's
transcript `comfyui-lab/transcripts/t01-startup.txt`
shows its own first launch, and
`t02-api.txt` shows the server answering
a script with its version and device —
the same server, two callers.

## What landed where

Inside the ComfyUI folder:

- `main.py` — the program.
- `models/` — where your model files go,
  in named subfolders. Empty at birth.
  Chapter 4 is the tour.
- `custom_nodes/` — extensions live
  here. Empty at birth too, and
  chapter 11 argues it should grow
  slowly.
- `input/` and `output/` — pictures you
  feed in (chapter 7) and pictures the
  machine saves.
- `user/` — your saved workflows and
  settings.
- `temp/` — previews and passing work.

Nothing here phones home to ask
permission; the program runs entirely
on your machine once installed. Updating
is a `git pull` plus re-installing the
requirements — and chapter 13 has an
honest word about updates breaking
yesterday's workflows, because in this
fast-moving project, sometimes they do.
