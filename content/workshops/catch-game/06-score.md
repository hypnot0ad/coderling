---
title: "Keep score"
weight: 60
draft: false
learning_objectives: ["Award one point per catch and reset the score when restarted."]
concepts: ["variables", "operators", "sequences"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Give every catch a point. A **variable** is a named place to keep a value that can change. Our value is a number called Score.

## Predict

Should a missed apple increase Score? Where should the point block go?

## Build

1. Select **Apple → Variables → Make a Variable**.
2. Name it exactly **Score**.
3. Choose **For all sprites**, then confirm. This is a shared variable. Keep the checkbox beside Score ticked so its monitor appears on the stage.
4. Add `set [Score] to (0)` just below Apple’s flag block, **before** forever.
5. Add `change [Score] by (1)` inside the touching-Bowl if, before the sound and return-to-top blocks.
6. Compare Apple with this complete final script. Replace the earlier version rather than keeping a second flag script.

```text
when green flag clicked
 set [Score] to (0)
 go to [random position]
 set y to (180)
 forever
   change y by (-5)
   if <(y position) < (-170)> then
     go to [random position]
     set y to (180)
   end
   if <touching [Bowl]?> then
     change [Score] by (1)
     start sound [Collect]
     go to [random position]
     set y to (180)
   end
 end
```

Keep Bowl’s script from Move the bowl. Apple owns score changes; Bowl only moves. `change Score by 1` adds one to its current value; `set Score to 0` replaces it.

## Check it works

Start at zero. Catch three apples: Score becomes 1, 2, then 3. Miss an apple: Score stays 3. Click the flag: Score becomes 0 and Bowl returns to the middle. Save your game.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Score keeps returning to zero | Reset may be inside forever | Move set Score to 0 above the loop. |
| A miss earns a point | The point block may be in the bottom if | Put it only inside touching Bowl. |
| Points rise continuously | Point block may be outside the catch if | Nest it beside the sound and move Apple away after catching. |

## Why it works

The flag resets once. The loop changes the value only for a catch. Explain the difference between “set” and “change” to a coding buddy.

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=322s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../05-catch/) · [Next](../07-challenges/)
