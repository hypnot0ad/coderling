---
title: "Pack a deck"
weight: 30
draft: false
learning_objectives: ["Fill a shared list with exactly two of each picture number."]
concepts: ["operators", "loops", "variables", "lists", "custom-blocks"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

A **variable** is a named box that remembers one value. A **list** remembers several values in order. Our deck will hold `1, 2, 3, 4, 1, 2, 3, 4`.

## Predict

If you put four numbers into a list twice, how many items will it contain?

## Build: make the memory boxes

1. Select **Card → Code → Variables → Make a Variable**.
2. Create the names in this table, one at a time. Choose the scope before clicking **OK**. **For this sprite only** gives each clone its own box. **For all sprites** shares one box across the game.

| Scope | Names to create | What they remember |
|---|---|---|
| For this sprite only | `card ID`, `flip`, `matched` | This card's picture number, face-up state, and matched state |
| For all sprites | `flip count`, `first card`, `second card`, `matches` | This turn's choices and total pairs found |
| For all sprites | `random index`, `x pos`, `y pos` | Which list item to take and where to place the next card |

Use exactly these names. For `flip` and `matched`, we will use **0 = no** and **1 = yes**. A card ID is a **picture number**, so two cards share each ID.

3. In **Variables**, select **Make a List**. Name it `card ID list` and choose **For all sprites**.
4. Show its checkbox so you can watch the list on the stage. Hide the variable monitors except `matches`.

## Build: pack the deck

5. Open **My Blocks → Make a Block**. Name it `deal cards`. Leave **Run without screen refresh** unchecked. A custom block gives a group of instructions a name.
6. Replace the Card flag script from step 2 with this script. `deal cards` comes from My Blocks.

```text
when green flag clicked
hide
set [flip count] to (0)
set [first card] to (0)
set [second card] to (0)
set [matches] to (0)
set [random index] to (0)
set [card ID] to (0)
set [flip] to (0)
set [matched] to (0)
switch costume to [card back]
deal cards
```

7. Under the pink `define deal cards` block, build:

```text
define deal cards
delete all of [card ID list]
repeat (2)
    add (1) to [card ID list]
    add (2) to [card ID list]
    add (3) to [card ID list]
    add (4) to [card ID list]
end
```

The four `add` blocks go inside `repeat`. A **loop** runs the blocks inside it more than once. The `repeat` block is in Control. List blocks are in Variables.

## Check it works

Click the flag. The list should contain exactly eight items: `1, 2, 3, 4, 1, 2, 3, 4`. Click again: still eight. Card will be hidden; that is expected. Save.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| The list grows to 16 items on restart | The old deck was not cleared | Put `delete all of [card ID list]` before the repeat. |
| The list has only four items | The repeat count or nesting is wrong | Set repeat to 2 and place all four add blocks inside it. |

## Why it works

We reset the game before packing the deck. The `deal cards` block calls the instructions below its `define` block. Later we will use Operators such as `+`, `>`, and `=` to do sums and ask questions about these values. Why does clearing the list belong outside the repeat?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=24s) by smart kiddos. Resets and numeric state flags are teaching adaptations. Lists and custom blocks are explained at 3:25–6:02.

[← Previous](../02-costumes/) · [Overview](../) · [Next →](../04-deal/)
