---
title: "Draw the cards"
weight: 20
draft: false
learning_objectives: ["Create five centered costumes in the correct order."]
concepts: ["looks-sound"]
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

A **costume** changes how a sprite looks. Our Card sprite will have one hidden back and four different faces.

## Predict

Why should every card have the same picture on its back?

## Build

1. Delete the practice cat using its trash button in the sprite list.
2. Hover over **Choose a Sprite**, then select **Paint**. Rename the sprite `Card` in the sprite-name box.
3. Open **Costumes**. Use the rectangle tool to draw a card about **70 pixels wide and 90 pixels tall**. Keep it centered on the costume crosshair. The exact size is not important, but it must fit in a 100-by-120-pixel space.
4. Name this costume `card back`. Give it a thick outline and a plain back. You could put a question mark in the middle.
5. Right-click its costume thumbnail and choose **duplicate**. Name the copy `card 1`. Replace the question mark with a circle.
6. Duplicate again to make `card 2`, `card 3`, and `card 4`. Use a triangle, square, and star, or four pictures of your own. Use different shapes as well as colors so the pairs are easy to tell apart.
7. Drag the thumbnails into this exact order:

| Costume number | Costume name | Picture |
|---|---|---|
| 1 | card back | Hidden back |
| 2 | card 1 | Circle |
| 3 | card 2 | Triangle |
| 4 | card 3 | Square |
| 5 | card 4 | Star |

8. Select **Code → Looks**. Build this short script on **Card**:

```text
when green flag clicked
switch costume to [card back]
```

## Check it works

Click each costume thumbnail. All five pictures should stay in the same place and have the same card outline. Click the flag: only the back should show. Save your project.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| The card jumps when its picture changes | Costumes have different centers | Move each whole drawing to the costume crosshair. |
| There are five sprites | You duplicated the sprite instead of its costume | Keep one Card sprite. Make the five pictures inside its Costumes tab. |

## Why it works

Costume 1 is the back. Picture 1 will therefore need costume 2. What costume number will picture 4 need?


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=124s) by smart kiddos. The simple shape designs and dimensions are teaching additions.

[← Previous](../01-setup/) · [Overview](../) · [Next →](../03-deck/)
