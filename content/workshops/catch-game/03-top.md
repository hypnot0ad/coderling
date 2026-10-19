---
title: "Start at the top"
weight: 30
draft: false
learning_objectives: ["Restart Apple at a new horizontal position along the top."]
concepts: ["coordinates", "sequences"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Start Apple high above Bowl.

## Predict

If you choose a random position after setting y, will Apple still always be at the top?

## Build

1. Select **Apple → Code**.
2. Add the script below. Find both blue blocks in **Motion**. For `go to [random position]`, use its dropdown.

```text
when green flag clicked
 go to [random position]
 set y to (180)
```

3. Click the flag five times and watch where Apple appears.
4. Save your project to your computer again. Repeat this save at every checkpoint.

## Check it works

Apple starts at y `180` each time. Its x position usually changes. The top of Apple may be clipped by the stage edge; that is expected.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Apple starts halfway down | The block order may be reversed | Put set y to 180 after go to random position. |
| Bowl jumps to the top | The script belongs to Bowl | Move it to Apple and remove it from Bowl. |

## Why it works

The first block chooses x and y. The second replaces only y, leaving a random x. What would setting x to 0 afterwards do?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=134s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../02-move/) · [Next](../04-fall/)
