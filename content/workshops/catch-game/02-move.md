---
title: "Move the bowl"
weight: 20
draft: false
learning_objectives: ["Hold each arrow key to move the bowl in the matching direction."]
concepts: ["sensing", "operators", "conditions", "loops", "input-control"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Give the player control of Bowl.

## Predict

What will happen if Scratch checks a key only once, just as you click the flag?

## Build

1. Select **Bowl → Code**.
2. From **Sensing**, drag `key [space] pressed?` and choose `right arrow`. This is a **condition**: a question with a true-or-false answer.
3. From **Operators**, try the green `(1) < (2)` block by clicking it. It reports true. Change 2 to 0 and click again: false. Operators can compare numbers. Remove this loose practice block afterwards.
4. From **Control**, drag `if <> then`. Put the key question in its hexagonal hole. The blocks inside run only when the answer is true.
5. Build this complete script. Both `if` blocks go **inside** `forever`, one after the other. The indents show nesting. The lines marked `end` show where a Control block closes; you do not add an end block.

```text
when green flag clicked
 go to x: (0) y: (-130)
 forever
   if <key [right arrow] pressed?> then
     change x by (10)
   end
   if <key [left arrow] pressed?> then
     change x by (-10)
   end
 end
```

`when green flag clicked` is in Events. `go to x: y:` and `change x by` are in Motion. A **loop** repeats its inside blocks. `forever` keeps asking about the keys until you stop the project.

## Check it works

Click the flag. Hold right, release it, then hold left. Bowl moves right, stops, then moves left. Click the flag again: it returns to `(0, -130)`.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Bowl moves only when you start | The if blocks may be outside forever | Put both if blocks inside the loop. |
| Both keys move right | The left movement may be positive | Set the left branch to change x by −10. |
| Bowl is at the side | It reached the edge | Hold the other arrow or click the flag to reset. |

## Why it works

Positive x changes move right. Negative x changes move left. Which part keeps checking after you release a key?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=41s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../01-setup/) · [Next](../03-top/)
