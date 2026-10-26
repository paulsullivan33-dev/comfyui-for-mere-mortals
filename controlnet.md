# ControlNet — Steering the Picture

Outcome: you understand how to give the
model instructions words cannot carry —
a pose, a floor plan, the exact edges of
a face — and where those instructions
plug into the graph you already know.

## The problem prompts cannot solve

Prompts are eloquent about *what* and
helpless about *where precisely*. "A
dancer, arms raised" gives you a dancer;
which way the arms bend is dice. If the
pose matters — because the picture must
match a product shot, a storyboard frame,
another picture — language runs out.

**ControlNet** is the answer built for
this: a second, smaller model trained to
watch one *kind of map* — a stick-figure
pose, a depth map, a line drawing — and
to steer the main model's generation so
the result fits the map. You supply the
map; the main model still supplies the
art. Pose from a stick figure, room from
its edges, face lit the way the depth
map says: that is the division of
labour.

## The wiring

ControlNet enters chapter 5's graph
between the prompts and the sampler:

- A **Load ControlNet Model** node picks
  the steering file from
  `models/controlnet/` — one per kind of
  map, and matched to the model family
  (an SD 1.5 ControlNet steers SD 1.5
  checkpoints; chapter 4's rule about
  families applies again).
- Your source picture (LoadImage) usually
  passes through a **preprocessor** — a
  node that extracts the map: OpenPose
  finds the stick figure, Canny finds the
  edges, a depth node estimates the
  depth. The map it draws is itself an
  image you can preview, and you should:
  a bad map steers faithfully to the
  wrong place.
- A **ControlNetApply** (in current
  versions, Apply ControlNet with start
  and end points) takes the positive and
  negative CONDITIONING, the ControlNet
  and the map, and hands the sampler
  conditioning that now carries the
  extra instruction, at a **strength**
  you set. Strength is CFG's cousin:
  0.6 is guidance, 1.0 is law, and above
  that the map can start showing through
  the art.

The two conditionings both pass through
the apply node; wire only the positive
and the negative will outvote the map
in places you did not expect. Start and
end points let the steering act for only
part of the sampling — pose matters
early, while the broad shapes form, so
ending the control at 0.8 of the steps
often frees the model's hand for the
finish.

## Stacking and honesty

ControlNets **stack**: pose *and* depth
*and* edges, each applied in turn, for
pictures that must obey several maps at
once. Each adds time and obedience, and
together they can over-constrain a small
model into mush; add one, look, then
decide.

This chapter is documented-only in the
lab's ledger: the nodes, folders and
fields above are as the project's
documentation and the server's own node
list describe them, but the lab ran no
ControlNet generation — its two CPU
cores spent themselves proving chapter
5, and a pose-steered run at honest sizes
was beyond the sitting. `criteria.md`
records the boundary exactly, and
chapter 13 records the limit that is
not technical: a pose copied from a real
person's photograph is still that
person's, and steering does not launder
consent.
