---
title: "Catch an apple"
weight: 50
draft: false
learning_objectives: ["Make a catch return Apple to the top and play a sound."]
concepts: ["sensing", "conditions", "looks-sound"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Make the apple notice the bowl.

## Predict

If Apple stayed touching Bowl, how often could the forever loop notice the same catch?

## Build

1. Select **Apple → Sounds**.
2. Use **Choose a Sound** to add **Collect**.
3. Return to **Code**.
4. Add a second `if` inside Apple’s existing forever loop, below the bottom check.
5. From **Sensing**, put `touching [mouse-pointer]?` inside it and select **Bowl** from the dropdown.
6. From **Sound**, use `start sound [Collect]`. This starts the sound without pausing the falling script.
7. Check your whole Apple script matches this version.

```text
when green flag clicked
 go to [random position]
 set y to (180)
 forever
   change y by (-5)
   if <(y position) < (-170)> then
     go to [random position]
     set y to (180)
   end
   if <touching [Bowl]?> then
     start sound [Collect]
     go to [random position]
     set y to (180)
   end
 end
```

## Check it works

Click the flag. Move Bowl under Apple. When they touch, you hear Collect and Apple returns to the top. Move Bowl away for the next fall: Apple should return from the bottom without the catch sound.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Apple passes through Bowl | The touching menu may name the wrong object | Select Bowl in Apple’s touching block. |
| Apple pauses when caught | The sound block may wait | Use start sound, not play sound until done. |
| Apple catches from far away | The sprites may be very large | Restore Bowl size 100 and Apple size 60. |

## Why it works

Touching is a question about the sprites’ visible shapes. Returning Apple to the top separates them, so one catch triggers once. Why is the bottom check separate from the catch check?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=284s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../04-fall/) · [Next](../06-score/)
