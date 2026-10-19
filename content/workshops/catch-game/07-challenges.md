---
title: "Make it your own"
weight: 70
draft: false
learning_objectives: ["Customize the game and test an optional change."]
concepts: ["looks-sound", "conditions", "coordinates"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Save a copy before trying an extra challenge. These are optional and outside the 65-minute core.

## Predict

If the apple moves twice as far each loop, will catching it feel easier or harder?

## Build

Choose one challenge at a time:

1. **New theme — Starter looks skills.** Change the backdrop or paint a new Apple costume. Keep the Apple sprite and name so its scripts still work. Hint: use the Costumes tab rather than deleting the coded sprite. This follows the video’s invitation to change the theme.
2. **Change the pace — Builder motion and loops.** Try `change y by (-3)` for a gentler game or `(-7)` for a harder one. Hint: change only Apple’s falling block. Very large jumps can skip over Bowl between checks. Restore −5 if catches stop working.
3. **Keep Bowl on stage — Builder coordinates, operators, conditions.** This is a Coderling extension. Add the two if blocks below at the bottom of Bowl’s forever loop, after the arrow checks. Hint: positive x is the right side.

```text
if <(x position) > (190)> then
  set x to (190)
end
if <(x position) < (-190)> then
  set x to (-190)
end
```

## Check it works

For a theme change, catch two apples and check Score. For a pace change, compare five falls before and after. For the boundary extension, hold each arrow for five seconds: Bowl stops at x 190 or −190 and still moves back the other way.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| The new falling object has no code | You may have added a new sprite | Paint a costume on Apple or copy the script and update references deliberately. |
| Bowl sticks at one side | A comparison sign may be reversed | Check right is x greater than 190; left is x less than −190. |

## Why it works

Changing one thing makes it easier to tell what caused the result. Which change made the game more fun, and how did you test it?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=359s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../06-score/) · [Next](../08-wrap-up/)
