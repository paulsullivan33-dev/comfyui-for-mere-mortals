# The API and Headless Running

Outcome: you can make a picture without
touching the mouse — post a workflow to
the server, learn its number in the
queue, and collect the finished file —
and you know what **headless** running
(the server with no browser at all) is
for.

## Why the split matters

Chapter 1 said ComfyUI is a **server**
with a browser front end. Everything the
browser does arrives as ordinary web
requests to addresses on the server —
the **API**. That means a script can do
everything a mouse can, and this guide's
lab did exactly that: not one picture in
its transcripts was made by clicking.

The addresses you will actually use:

- `POST /prompt` — hand over a workflow
  in API format (chapter 9), plus a
  client id. The answer names your job:
  a **prompt_id**, and its place in the
  queue. A workflow the server cannot
  accept is refused here, with reasons —
  transcript `t03-validation.txt` is the
  lab offering a graph naming a checkpoint
  the machine did not have, and the
  server naming the missing value in its
  reply. Validation before queueing is
  the API's good manners; learn to read
  its refusals before your users meet
  them.
- `GET /queue` — what is running and
  what is waiting.
- `GET /history/<prompt_id>` — a job's
  record once finished, including the
  output filenames. This is how a script
  knows the picture exists and where.
- `GET /view?filename=...` — fetch the
  picture itself.
- `GET /object_info` — every node the
  server knows, with its inputs, outputs
  and choices: the machine-readable
  version of the whole toolbox.
  Transcript `t02-api.txt` counts them:
  1,014 node types on the lab's stock
  install, before a single custom node
  is added.
- `GET /system_stats` — version, device,
  memory: the server's identity card.
- A **websocket** at `/ws` streams live
  progress — the channel the browser's
  progress bar drinks from. Scripts that
  need patience with feedback use it;
  scripts that can poll `/history` do
  not need it.

## A run, as the lab did it

`comfyui-lab/run-workflow.py` is the
whole pattern in a page of Python: read
the workflow JSON, post it to `/prompt`,
take the prompt_id, ask `/history`
every few seconds until the job
appears, print the output filename.
Transcript `t04-generation.txt` is its
output on chapter 5's workflow. Swap the
JSON file and the same script runs any
graph — including graphs no human will
ever draw twice, built by another
program on the fly. **Parameters are
just JSON edits:** the runner's seed
experiment (transcript `t05-reproduce.txt`)
changed one number in the loaded JSON
before posting, which is precisely how
batch tools sweep seeds, prompts, or
sizes over a template workflow.

## Headless, and the honest reasons

Run the server and never open the
browser, and ComfyUI becomes a picture
engine other software calls: a chat bot
that illustrates, a catalogue job that
renders a thousand variants overnight,
a test harness proving a workflow still
runs after an update. The flags from
chapter 3 decide its manners in that
life: `--output-directory` and friends
place the results; `--listen` decides
who may ask — and chapter 13's warning
bears repeating here, because headless
servers drift toward networks: **the API
has no authentication.** Anyone who can
reach the port can queue workflows, and
a workflow can contain any node you have
installed. Bind it to localhost, put it
behind something that does authenticate,
or keep it on a network you trust
entirely. The tool assumes the network
is friendly; make sure it is right.
