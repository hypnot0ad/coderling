---
title: "Make it yours"
weight: 70
draft: false
learning_objectives: ["Customize the finished game and test that four pairs still work."]
concepts: []
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

These challenges are optional. Finish the working game first.

## Predict

Which changes affect only how the game looks? Which ones need new rules?

## Build: choose a challenge

### A new theme · Creator, no new core concepts

Change the four face costumes into things you like: fruit, planets, or your own symbols. Keep the same costume order and card sizes.

**Hint:** Change the picture inside the border. Leave `card back` first. Use shapes or words as well as color.

**Checkpoint:** Reveal all the cards using the temporary test from step 4. There should still be two of each picture. Restore the card-back block afterwards.

### A little more thinking time · Creator, no new core concepts

Change the 1.5-second pause to 3 seconds. Ask a coding buddy which feels more comfortable.

**Hint:** Change only the wait in the second-choice branch. Keep flip count at 2 until the pair has been handled.

**Checkpoint:** Try to open a third card during the longer pause. It must stay closed.

### Count your turns · Creator extension: another shared variable

Add a shared variable called `turns`. Show it on the stage. Reset it to 0 in the Card flag script. Increase it once each time the player chooses a second card.

**Hint:** Put `change [turns] by (1)` directly after `set [second card] to (card ID)`. Do not count each click: one turn uses two cards.

**Checkpoint:** A repeated click on the first card must not add a turn. One matching pair or one different pair adds exactly 1. Restart resets it to 0.

### Six pairs · Creator extension: generalizing a list and layout

Add `card 5` and `card 6` costumes, then make a 12-card board.

**Hints:** Pack numbers 1–6 twice, create 12 clones, and win at 6 matches. Design a layout that still fits. One option is four columns at x = −150, −50, 50, 150 and three rows starting at y = 110 with a row change of −90. Shrink costumes below 100 × 90 pixels. Keep the Win message small and below the last row.

**Checkpoint:** Temporarily reveal the board to count two of each of the six faces. Play all six pairs, then restart. A new costume alone is not enough: check the deck, clone count, and win condition too.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Your new pictures never appear | Deck numbers and costume order disagree | For four pairs, keep only face IDs 1–4 and costumes 2–5. |
| Your extension breaks the game | Several rules changed at once | Save extensions under a new filename and return to your working copy to compare. |

## Why it works

Small changes are easier to test than many changes at once. Which checkpoint helped you find a mistake fastest?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=0s) by smart kiddos. All challenges are original teaching additions, not claimed as steps in the video.

[← Previous](../06-match/) · [Overview](../) · [Next →](../08-wrap-up/)
