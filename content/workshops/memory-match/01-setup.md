---
title: "Get ready"
weight: 10
draft: false
learning_objectives: ["Save a Scratch project and make a sprite move when the flag is clicked."]
concepts: ["editor", "sprites", "events", "sequences", "motion", "coordinates", "loops", "operators", "sensing", "conditions"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

You can build this project in Scratch 3 without signing in.

## Predict

If two motion blocks are joined together, will Scratch run the top one or the bottom one first?

## Build

1. Open the [Scratch editor](https://scratch.mit.edu/projects/editor/). If a welcome tutorial covers the stage, close it. The **stage** is where your project runs.
2. Select the cat below the stage. A **sprite** is an object you can code.
3. Open **Code**. Choose **Events**, then drag `when green flag clicked` into the coding area.
4. Choose **Motion**. Join `move (10) steps` under the event block.
5. Join another `move (10) steps` underneath it.
6. Click the green flag. The cat should move 20 steps to the right. The joined blocks are a **sequence**: Scratch runs them from top to bottom.
7. Select **File → Save to your computer**. Save as `memory-match.sb3`. Keep the `.sb3` ending. You can choose the name in the save window if there is no project-name field.

## Quick Builder warm-up

Try these on the practice cat before you delete it in the next step. Replace its script each time.

1. **Coordinates:** use `when green flag clicked` → `go to x: (0) y: (0)`. The cat goes to the middle. Change x to 100: it moves right. Change y to −50: it moves down.
2. **Loops:** use `when green flag clicked` → `repeat (2)` with `move (10) steps` inside. Predict the distance, then run it: 20 steps. A loop repeats the blocks inside it.
3. **Operators:** drag the green `( ) + ( )` block into the number hole of `move (10) steps`. Enter 10 and 5. Under a flag event, this moves 15 steps. Green `=` and `>` blocks ask true-or-false questions instead of doing sums.
4. **Sensing and conditions:** build the script below. `if` is in Control; `mouse down?` is in Sensing. Click the flag, then hold the mouse button down over an empty part of the stage within two seconds. Repeat without holding it: the cat should stay still. On a touchscreen, try holding a finger on the empty stage instead.

```text
when green flag clicked
wait (2) seconds
if <mouse down?> then
    move (10) steps
end
```

An `if` block runs its inside blocks only when its question is true. **Checkpoint:** explain why the final script sometimes moves and sometimes does not. If it always stays still, hold the mouse button until after the two-second wait. If these tests feel new, take an extra 15 minutes to practise them.

## Check it works

Find the Code tab, Costumes tab, and sprite list. Click the flag twice and explain why the cat moves again. Save your file. Later, **File → Load from your computer** lets you open it again; save any current work before loading another file.

If you can do all of this, you are ready. If it feels new, repeat this tiny exercise before continuing. Ask a coding buddy to help find a block if you get stuck.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| The cat stays still | A motion block is not joined to the event | Drag it up until it snaps under the flag block. |
| You cannot see the cat | It has moved off the stage | Drag the cat back to the middle. |

## Why it works

The green flag starts the script. Scratch runs each connected block in order. Which block starts your script?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=0s) by smart kiddos. This warm-up and local saving guidance are teaching additions.

[← Previous](../) · [Overview](../) · [Next →](../02-costumes/)
