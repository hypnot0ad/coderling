---
title: "Find a match"
weight: 60
draft: false
learning_objectives: ["Resolve a pair, lock matched cards, show a win, and restart cleanly."]
concepts: ["broadcasts", "game-state"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

A **broadcast** sends a named message to every sprite and clone. Each can have a `when I receive` script that responds.

## Predict

When two pictures do not match, should cards matched on an earlier turn close too?

## Build: compare the pair

1. Select **Card**. In Events, drag a `broadcast [message1] and wait` block. Open its message menu and choose **New message**. Create `pair found`. Do the same to create `turn back` and `win`. The names must match in senders and receivers.
2. Replace the click script from step 5 with this complete version. The comparison, wait, broadcasts, and reset all belong in the **else** branch for the second choice.

```text
when this sprite clicked
if <<(flip count) < (2)> and <<(flip) = (0)> and <(matched) = (0)>>> then
    set [flip] to (1)
    switch costume to ((card ID) + (1))
    change [flip count] by (1)
    if <(flip count) = (1)> then
        set [first card] to (card ID)
    else
        set [second card] to (card ID)
        wait (1.5) seconds
        if <(first card) = (second card)> then
            change [matches] by (1)
            broadcast [pair found] and wait
        else
            wait (0.2) seconds
            broadcast [turn back] and wait
        end
        set [flip count] to (0)
        if <(matches) = (4)> then
            broadcast [win]
        end
    end
end
```

Use `broadcast … and wait` for the two pair messages. It lets the cards finish responding before the next turn opens. `flip count` stays 2 during the pause, which stops a third card opening.

## Build: tell the cards what to do

3. Still on **Card**, add these two separate scripts:

```text
when I receive [pair found]
if <(flip) = (1)> then
    set [matched] to (1)
end
```

```text
when I receive [turn back]
if <<(flip) = (1)> and <(matched) = (0)>> then
    set [flip] to (0)
    switch costume to [card back]
end
```

A matched card keeps `flip = 1` and `matched = 1`. It stays visible and will not count as a new choice. The hidden original has `flip = 0`, so it ignores both messages.

4. Test one matching pair and one different pair now. Matches should stay open. Different pictures should close after about 1.7 seconds. `matches` increases only for a new pair.

## Build: celebrate

5. Paint a new sprite named **Win**. Use the text tool to write `You found all four pairs!`. Keep the text about 300 pixels wide.
6. On **Win**, add these two scripts. Find `go to [front] layer` in Looks.

```text
when green flag clicked
hide
go to x: (0) y: (-130)
```

```text
when I receive [win]
go to [front] layer
show
```

7. Hide the test monitors except `matches`. Save.

## Check it works

- Reveal two different pictures. Try a third card during the pause: it stays closed. The first two close and you can choose again.
- Find a pair. It stays face up and `matches` increases by 1. Clicking it again does nothing.
- Find all four pairs. The Win text appears and `matches` is 4.
- Press the flag. Win hides, matches returns to 0, and eight card backs appear. Restart once more while a pair is waiting; the old turn must not affect the new board.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Old matches turn back over | The receiver does not check matched | Put both `flip = 1` and `matched = 0` inside the turn-back condition. |
| The first card closes before you choose a second | The wait and comparison are outside else | Move them into the second-choice else branch, as shown. |
| Win never appears | The message name or total is wrong | Use `win` on both sprites and test `matches = 4` after resolving a pair. |
| A third card opens during the pause | Flip count resets too early | Reset it after both message branches have finished. |

## Why it works

Shared values describe the turn. Local values describe each card. Broadcasts let each card update itself. Why does the turn-back receiver need to ask two questions?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=657s) by smart kiddos. Messages are renamed for clarity; waiting for receivers and checking victory after each resolved turn are reliability adaptations.

[← Previous](../05-flip/) · [Overview](../) · [Next →](../07-challenges/)
