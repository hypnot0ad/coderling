---
title: "Play, test, and save"
weight: 80
draft: false
learning_objectives: ["Demonstrate the completed game and save a working local copy."]
concepts: ["events", "variables", "conditions"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

You made a game with controls, falling objects, catches, and points.

## Predict

What should happen if you click the green flag after scoring five points?

## Build

1. Run the play checklist below.
2. Fix one problem at a time using the earlier pages.
3. Use **File → Save to your computer** to save your finished `.sb3` file.
4. Stop the game, then use **File → Load from your computer** to reopen the saved copy.
5. Click the flag and play again. You can show someone on your device without publishing or making an account.

## Check it works

| Test | Success looks like |
|---|---|
| Start and restart | Bowl is at x 0, y −130; Score is 0; Apple starts at y 180. |
| Hold right, then left | Bowl follows the chosen arrow. |
| Release both arrows | Bowl stops moving. |
| Miss three apples | Each returns to the top; none adds points or catch sounds. |
| Catch five apples | Each adds exactly one point and returns to the top. |
| Restart during a fall | The game resets and continues with one falling Apple. |
| Open the saved file | The same scripts, sprites, and sound are present. |

The core game runs until you press Scratch’s red stop button. There is no timer, life counter, or win screen in this workshop.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Apple falls unusually fast or scores twice | Old flag scripts may still be attached | Keep one complete Apple flag script from Keep score. |
| Reopened game is an older version | You may have opened an earlier download | Save a new file and check its name and date. |

## Why it works

A complete game needs a clear starting state as well as rules during play. Without looking, name the block that repeats, the block that asks a question, and the variable that remembers points.

Want to explore more? [Memory match](../../memory-match/) is an existing Coderling Creator workshop with lists, clones, and messages. It is a larger next project, not a prerequisite. Revisit its setup warm-up before beginning.

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=358s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../07-challenges/) · [Next](../)
