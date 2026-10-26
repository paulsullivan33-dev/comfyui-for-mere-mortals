# Your First Workflow

Outcome: one finished picture, made by a
graph you can explain out loud. This is
the classic text-to-image workflow — the
one this guide's lab ran for real — and
nearly every fancier graph is this one
with extra limbs.

## The cast, in the order data flows

1. **CheckpointLoaderSimple.** One field:
  the checkpoint's name. Three outputs:
  MODEL, CLIP, VAE — the whole kitchen
  from chapter 4, unpacked. Everything
  downstream drinks from these three
  sockets.

2. **CLIPTextEncode (positive).** Fed by
  the loader's CLIP. You type what you
  *do* want: the lab's run used "a red
  teapot on a wooden table, photograph".
  Its output is CONDITIONING — the
  prompt in the model's own language.

3. **CLIPTextEncode (negative).** Same
  node, second copy, fed by the same
  CLIP. You type what you want *less*
  of: "blurry, low quality" in the lab's
  run. Negative prompting is not an
  insult list; it is steering away from
  failure modes the model knows by name.

4. **EmptyLatentImage.** Width, height,
  batch size. This is the blank canvas in
  latent space (chapter 2): pure
  potential, sized 512×512 for SD 1.5 —
  models have a **native size** they were
  trained at, and wandering far from it
  gives doubled faces and strange
  geometry. The lab, on CPU, used
  256×256 to keep the run short.

5. **KSampler.** The engine room, and
  chapter 6's whole subject. It takes
  MODEL, both CONDITIONINGs and the
  LATENT, adds **noise** according to its
  **seed**, and removes noise step by
  step until a picture's latent remains.
  For the first run, its defaults are
  fine — and the lab's run used fewer
  steps (4) than the usual 20 for the
  same CPU reason. Fewer steps, rougher
  picture, same lesson.

6. **VAEDecode.** Takes the sampler's
  LATENT and the loader's VAE, and
  produces an IMAGE: the translation out
  of latent space into pixels.

7. **SaveImage.** A filename prefix —
  the lab used `lab-first` — and the
  picture lands in `output/`, named with
  a counter, carrying the whole workflow
  inside it (chapter 9).

## Running it

In the browser: draw or load the graph,
choose the checkpoint in the loader,
type the prompts, press **Queue Prompt**.
The nodes light up as they execute —
chapter 2's backwards walk made visible
— and the picture appears under the
saver. **Check:** the console records
each job as it runs — the lab's is
transcript `t07-server-log.txt`, first
generation 112 seconds, the seed-changed
run 61 with the model already loaded —
and the output file exists. The progress bar on the sampler
counts steps; on a GPU, seconds — on
the lab's CPU, a slower, more patient
count, which is why its picture is
small.

By script, the same graph is the file
`comfyui-lab/workflows/first-workflow.json`,
posted to the API by
`comfyui-lab/run-workflow.py`. The
transcript `t04-generation.txt` is the
lab's complete run: the queue's answer,
the history entry naming the saved
file, and the file itself identified —
a real PNG, 256×256, with the workflow
embedded. And the picture itself? At
four steps, honesty wins: a dark,
rounded smudge on a table-ish surface
under smears of pink and green — the
teapot's ghost, not the teapot. That is
chapter 6's first lesson arriving
early: too few steps leaves a picture
still dissolving out of its noise. The
pipeline is proven; the polish costs
steps the lab's CPU was rationing.

Transcript `t05-reproduce.txt` then ran
the workflow twice more. Untouched, it
came back in five seconds with the
identical file, byte for byte — chapter
2's cache, caught in the act. With only
the seed changed in the JSON, it
produced a different picture: same
recipe, different roll of the dice.

Two first-run courtesies that save real
grief:

- **One change at a time.** Because of
  caching (chapter 2), changing the
  negative prompt alone re-runs almost
  nothing but the sampler. Fiddling with
  five fields at once teaches you none
  of them.
- **Name your prefixes.** `output/`
  fills with `ComfyUI_00001_.png` by
  default. A prefix per experiment —
  `teapot-seed-test` — turns the folder
  into a lab notebook instead of a junk
  drawer.
