---
title: "Deal eight cards"
weight: 40
draft: false
learning_objectives: ["Create eight shuffled clones in two rows without losing any pairs."]
concepts: ["coordinates", "conditions", "sensing", "operators", "clones"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

A **clone** is a copy of a sprite made while the project runs. Each copy starts with its own copy of the Card-only variables. The original Card stays hidden as our template.

## Predict

If we remove a number from the deck after dealing it, can that exact list item be dealt again?

## Learn the new blocks

- **Coordinates** tell Scratch where to put a sprite. x goes left or right; y goes up or down. The stage center is x = 0, y = 0.
- A **condition** is a yes-or-no question. `if <> then` in Control runs its inside blocks only when the answer is yes.
- Green **Operators** blocks make questions such as `(x pos) > (150)` and do calculations such as `(card ID) + (1)`.
- **Sensing** asks questions about the outside world, such as `mouse down?` in the warm-up. This game uses variable comparisons instead. Both kinds of question fit a hexagonal hole.

## Build

1. Select **Card**. Keep the flag script from step 3.
2. Add these blocks **after** the repeat that packs the deck, in the same `define deal cards` script. `x pos` and `y pos` below are your orange variables, not the blue motion reporters.

```text
set [x pos] to (-150)
set [y pos] to (100)
repeat (8)
    set [random index] to (pick random (1) to (length of [card ID list]))
    set [card ID] to (item (random index) of [card ID list])
    delete (random index) of [card ID list]
    go to x: (x pos) y: (y pos)
    create clone of [myself]
    change [x pos] by (100)
    if <(x pos) > (150)> then
        set [x pos] to (-150)
        change [y pos] by (-120)
    end
end
```

3. Find `pick random` and `>` in **Operators**, list reporters in **Variables**, `go to x: y:` in **Motion**, and the clone blocks in **Control**. Nest the round reporters inside the inputs shown above. The list's **index** is the position of an item, starting at 1; it is different from the picture number stored there.
4. Make this separate script on **Card**:

```text
when I start as a clone
set [flip] to (0)
set [matched] to (0)
switch costume to [card back]
show
```

## Check it works

Click the flag. You should see **eight card backs in two rows of four**. Their x positions are −150, −50, 50, and 150; their y positions are 100 and −20. The list is now empty because all eight items have been dealt. Clicking the flag again should still give eight cards.

To inspect the pairs, temporarily replace the clone's costume block with `switch costume to ((card ID) + (1))`. Use the green `+` block. Click the flag: see two of each picture. Repeat a few times; the order can change, although a repeat is possible by chance. Then restore `switch costume to [card back]` and hide the list monitor. Save.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Cards overlap | Costume size or position updates | Keep each costume smaller than 100 × 120 pixels. Put the x change inside repeat, after create clone. |
| Every card has the same picture | `card ID` was made shared | Create `card ID` for this sprite only and replace references to the incorrectly scoped variable. |
| There are no cards | Clones may still be hidden | Put `show` under `when I start as a clone`. |

## Why it works

The original chooses a number and position **before** making each clone. That clone inherits them. Removing one list item still leaves the other copy of that picture available. The green flag removes old clones when it starts a fresh run. The hidden original remains available to deal again.

After four cards, x becomes 250. That is greater than 150, so the next card starts a new row. Why do we change y by a negative number?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=265s) by smart kiddos. Dealing is moved into the original sprite’s loop to keep allocation in one place; the video assigns values in clone-start scripts.

[← Previous](../03-deck/) · [Overview](../) · [Next →](../05-flip/)
