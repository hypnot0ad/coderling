---
title: "Get ready"
weight: 10
draft: false
learning_objectives: ["Save a project and place two sprites on the stage."]
concepts: ["editor", "sprites", "events", "sequences", "motion", "coordinates"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Make a game where a bowl catches apples. You only need Scratch 3, a keyboard with arrow keys, and somewhere to save a file. You do not need an account.

## Predict

Which number changes when an object moves sideways: x or y?

## Build

1. Open the [Scratch editor](https://scratch.mit.edu/projects/editor/).
2. Close the welcome tutorial if it covers the stage. The **stage** is where your game runs. A **sprite** is an object you can code.
3. Try the readiness check below on the cat.
4. Delete the practice cat using its trash button below the stage.
5. Use **Choose a Sprite** to add **Bowl**.
6. Select Bowl and set its size to `100` in the sprite information below the stage.
7. Use **Choose a Sprite** to add **Apple**.
8. Select Apple and set its size to `60`. These sizes are teaching choices; keep them while testing.
9. Use **Choose a Backdrop** to add **Boardwalk**. Any backdrop will work.
10. Select **File → Save to your computer**. Save as `catch-the-apples.sb3`.

### Readiness check and optional 10-minute warm-up

Can you select a sprite, join blocks, and make a flag script move it? If yes, continue. If not, practice with the cat before step 4:

1. Select the cat and open **Code → Events**.
2. Drag `when green flag clicked` into the coding area. An **event** starts a script.
3. From **Motion**, attach two `move (10) steps` blocks beneath it. A **sequence** runs from top to bottom.
4. Click the green flag. The cat moves 20 steps.
5. Replace the two move blocks with `go to x: (0) y: (0)`. This places the cat in the middle.
6. Try x `100` and y `-50`. The cat moves right and down.

**Coordinates** describe position. x increases to the right and y increases upwards. The middle is `(0, 0)`. Negative numbers sit left of or below the middle. Scratch’s stage runs from x −240 to 240 and y −180 to 180.

No earlier workshop is required if you can pass this check. The existing memory-match workshop uses harder concepts and is not required preparation.

## Check it works

Bowl and Apple appear below the stage. You can select each one. Save the file, then use **File → Load from your computer** to reopen it before continuing. Loading replaces the current project, so save first.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| New code appears on the wrong object | Which sprite is selected? | Click its thumbnail before adding blocks. |
| You cannot save online | You are not signed in | Use File → Save to your computer. |

## Why it works

Each sprite owns its own scripts. The backdrop belongs to the stage. Why will we need different scripts for the bowl and the apple?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=26s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../) · [Next](../02-move/)
