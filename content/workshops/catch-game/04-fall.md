---
title: "Fall and try again"
weight: 40
draft: false
learning_objectives: ["Make Apple fall and return to the top after a miss."]
concepts: ["loops", "motion", "operators", "conditions"]
source_url: "https://www.youtube.com/watch?v=7NN5v2wSL4U"
---

Let Apple fall again and again.

## Predict

Will changing y by `5` make Apple fall or rise?

## Build

1. Select **Apple**.
2. Replace its flag script with the complete version below. Keep only one copy of this script.
3. Find `y position` in **Motion** and the green `<` comparison in **Operators**.
4. Put `y position` into the **left** input of `<` and type `-170` in the right input.
5. Put that question inside `if <> then`. Put both return-to-top blocks inside this if. Put the if inside forever after `change y by`.

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
 end
```

## Check it works

Click the flag. Keep Bowl away from Apple. Apple falls past the middle and reaches the bottom, then appears at the top and falls again. Let it repeat three times. Catching does not work yet.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Apple goes up | The y change has the wrong sign | Use −5, including the minus sign. |
| Apple gets stuck at the bottom | The comparison or nesting is wrong | Check y position is less than −170 inside forever. |
| Apple keeps jumping at the top | The comparison may be greater than | Use the green less-than block. |

## Why it works

Each trip through the loop moves Apple down, then asks whether it has missed. −175 is less than −170. Should y equal to −170 pass the test?

Source: [How to Make a Catch Game in Scratch | Tutorial](https://www.youtube.com/watch?v=7NN5v2wSL4U&t=182s) by **Scratch Team**, presented by Zoë (Zinnea). Coderling adds checkpoints, explicit resets, and consolidated scripts.

[Previous](../03-top/) · [Next](../05-catch/)
