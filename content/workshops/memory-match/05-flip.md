---
title: "Turn over two"
weight: 50
draft: false
learning_objectives: ["Reveal at most two different cards in one turn."]
concepts: ["conditions", "operators", "variables", "game-state"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

Now a click will reveal a card. We will remember its picture number so the next step can compare the pair.

## Predict

If you click the same face-up card twice, should that count as two choices?

## Build

1. Select **Card**. Keep its existing scripts.
2. Add a new `when this sprite clicked` block from **Events**.
3. Build this complete script. The outer question uses two green `and` blocks. Build the smaller comparisons first, then place them in the `and` inputs.

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
    end
end
```

`and` says that both questions must be true. Here, all three checks must pass: fewer than two choices, this card face down, and this card not already matched.

4. Show the `flip count`, `first card`, and `second card` monitors for this test. These are shared boxes, so both cards can use them.

## Check it works

Click the flag, then one card. Its picture appears and `flip count` becomes 1. Click the same card again: the count stays 1. Click another card: the count becomes 2. A third card must stay hidden.

**The two cards stay open at this stage.** We have not added the match check yet. Use the green flag to start another test. Save.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| The back appears instead of a picture | Costume number has no offset | Use `card ID + 1`, not just `card ID`. |
| Clicking the same card counts twice | The face-up check is missing | Check `flip = 0` before setting flip to 1. |
| A third card opens | The outer condition is wrong | Check that `flip count < 2` is inside the outer if question. |

## Why it works

Each clone remembers whether it is face up. The shared flip count remembers how many choices the player has made. Why do those two variables need different scopes?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=532s) by smart kiddos. The matched guard and intermediate two-card test are additions; the core click logic follows 8:52–10:53.

[← Previous](../04-deal/) · [Overview](../) · [Next →](../06-match/)
