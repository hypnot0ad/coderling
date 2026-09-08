---
title: "Play, test, and save"
weight: 80
draft: false
learning_objectives: ["Demonstrate the finished rules and save a working project."]
concepts: []
source_url: "https://www.youtube.com/watch?v=l0lIGWz4yKU"
---

You have built a game that remembers the cards and the player's choices.

## Predict

What should happen if you press the green flag halfway through a turn?

## Play your final checks

1. Start a new game. Count eight card backs, and check that matches is 0.
2. Click one card twice. Only one choice should count.
3. Choose a second, different picture. A third card must not open during the pause. The two pictures should turn back over.
4. Find a matching pair. Both cards should stay face up. Clicking them again must not increase matches.
5. Find all four pairs. Look for the win message and a total of 4.
6. Restart during a pause and after a win. Both times, expect eight card backs, no win text, and matches = 0.
7. Choose **File → Save to your computer**. Keep a working copy as `memory-match.sb3`. Save experiments with a different name.

## If something goes wrong

| What you see | What to check | Try this |
|---|---|---|
| Restart keeps the score | The flag script does not reset matches | Compare your Card flag script with step 3. |
| One test fails | A later step may have changed a working script | Return to that step's checkpoint and compare one block at a time. |

## Explain your game

- Why does each clone need its own `flip` variable?
- Why do we remove an item from the list after dealing it?
- What does `broadcast [turn back] and wait` let the cards do before the next turn starts?

You have finished when your game passes the checks and you can explain one of those ideas in your own words. It is fine to look back at your blocks.

## What next?

Try the turn counter or six-pair challenge. These are extra Creator-level practice. No later workshop is available in this repository yet.

You do not need to publish your project or create an account. You can show someone your game on your own device.


---
Source: [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU&t=869s) by smart kiddos. The final test matrix, reflection prompts, and saving guidance are teaching additions.

[← Previous](../07-challenges/) · [Overview](../) · [Next →](../)
