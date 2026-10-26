# Troubleshooting

Symptom first, cause second, in the
order the lab and the documentation
suggest you check them.

## The node is red and the queue stops

*A workflow is offered and refused,
with one node outlined in red.*

1. **The error text names the field.**
   The console and the API's refusal both
   say which node's which input is
   unhappy — in the lab's transcript
   `t03-validation.txt`, a checkpoint
   name "not in list", because the file
   was not on the machine yet. Read the
   refusal before touching the graph;
   nine times in ten it is literal.
2. **The value is a file that moved.**
   Loaders go stale when models are
   renamed or ComfyUI was started before
   the file arrived. Refresh or restart,
   then re-pick from the dropdown rather
   than trusting the text in the box.
3. **A custom node is missing.** The
   node draws as an unknown block and
   the canvas names its pack. Chapter
   11's rule applies *now*, while you
   are impatient: look the pack up
   before installing it.

## "Checkpoint not in list" and empty dropdowns

The loader's list is the folder's
contents (chapter 4) as of the last
refresh. File in the wrong subfolder —
a LoRA among the checkpoints is the
classic — wrong extension, or a restart
owed. If the dropdown is empty for
*every* loader, ComfyUI is looking at a
different `models/` tree than you are:
check for an `extra_model_paths.yaml`
pointing elsewhere, or a second install
being launched from a shortcut.

## It runs, but the picture is noise or mush

- **Steps too low or CFG astray**
  (chapter 6): a picture still in static
  at step 4 of 4 is arithmetic, not a
  fault — the lab's own short run is
  rougher than a 20-step picture for
  exactly this reason.
- **Size far from the model's native
  size**: doubled subjects and smeared
  geometry — return to 512×512 (SD 1.5)
  or 1024×1024 (SDXL) and change one
  thing at a time.
- **The wrong VAE or a mismatched
  LoRA family** gives washed-out or
  scorched colours: check the family
  match (chapter 4) before the settings.

## CUDA out of memory (or the machine crawls)

The model, the picture size and the
batch all eat VRAM at once. Shrink in
that order of likelihood: batch to 1,
size to native, then reach for the
flags — `--lowvram`, tiled VAE decoding,
or a smaller (fp16, pruned) checkpoint.
On CPU-only runs the same wall is time:
fewer steps and smaller pictures are
not a failure of the exercise, they
*are* the exercise (chapter 5).

## Nothing at the address

The browser cannot reach
`127.0.0.1:8188`: the console window
behind it holds the answer. Still
printing imports means wait; a traceback
means read it; `Address already in use`
means an earlier ComfyUI — perhaps one
you forgot — holds the port, and the
cure is to close it or choose
`--port 8189` and remember you did.
A machine that reboots into a helpful
"optimisation" that reaps background
consoles will kill the server with no
error at all; the log simply ends.

## The picture changed and I changed nothing

The seed's control-after-generate was
set to randomize (chapter 6), or a node
in the graph reads the time, a folder,
or the network. Reproduce before you
investigate: queue twice, untouched,
and compare — with caching, a truly
unchanged graph returns the same file,
and a mismatch means something in the
graph is itself a dice roll wearing a
node's clothes.
