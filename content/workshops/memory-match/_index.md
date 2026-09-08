---
title: "Make a memory-match game"
description: "Build a shuffled, eight-card Scratch game with four matching pairs."
weight: 10
draft: false
status: "ready"
level: "Creator"
level_reason: "Coordinate clones using local and shared variables, lists, custom blocks, and broadcasts."
age_range: "8–15"
duration_minutes: 100
scratch_version: "3"
concepts_used: ["coordinates", "looks-sound", "loops", "conditions", "variables", "broadcasts", "clones", "custom-blocks", "lists", "game-state"]
concepts_taught: ["coordinates", "looks-sound", "loops", "sensing", "operators", "conditions", "variables", "broadcasts", "clones", "custom-blocks", "lists", "game-state"]
prerequisite_concepts: ["editor", "sprites", "events", "sequences", "motion"]
prerequisite_workshops: []
curriculum_version: "1.0"
learning_objectives: ["Deal eight shuffled cards containing four pairs.", "Use local state to reveal only two unmatched cards at a time.", "Keep matching pairs visible and turn other pairs back over.", "Show a win message and restart with a clean board."]
source: {"url": "https://www.youtube.com/watch?v=l0lIGWz4yKU", "video_id": "l0lIGWz4yKU", "title": "How to make a memory game in scratch", "creator": "smart kiddos", "published_date": null, "accessed_date": "2026-09-08", "transcript_origin": "auto-captions", "transcript_language": "en", "license": null, "adaptation": "Educational adaptation with reordered stages, explicit initialization, and serialized dealing."}
asset_credits: ["Students draw their own card costumes. No video art, music, or screenshots are redistributed."]
inspired_by: "https://splunk.github.io/observability-workshop/en/"
---


Make eight cards with four pairs of pictures. Hide the pictures, turn over two cards, and see if they match. Find every pair to win!

**Level: Creator.** This means the project combines several coding ideas. It does not mean you need to be a fast coder. We will introduce lists, clones, and messages one step at a time.

**Time: about 100 minutes.** Try steps 1–4 in one session and steps 5–8 in another. Allow another 15 minutes if you need the warm-up.

## Before you start

You should be able to find the Code and Costumes tabs, select a sprite, join blocks under `when green flag clicked`, and use `move (10) steps`.

There are no earlier workshops in this repository yet. [Try the readiness check and warm-up](01-setup/) if any of those ideas are new. You do not need to know lists or clones already.

## What you will learn

- Make eight shuffled cards using a list and clones.
- Allow two different cards to turn over each turn.
- Keep matching pairs visible and hide pairs that do not match.
- Show a win message, then restart with a fresh board.

## Your workshop

1. [Get ready](01-setup/) — open Scratch and try a warm-up.
2. [Draw the cards](02-costumes/) — make a back and four faces.
3. [Pack a deck](03-deck/) — learn variables, lists, and a custom block.
4. [Deal eight cards](04-deal/) — make a shuffled board with clones.
5. [Turn over two](05-flip/) — remember which cards you chose.
6. [Find a match](06-match/) — keep pairs and celebrate a win.
7. [Make it yours](07-challenges/) — optional challenges with hints.
8. [Play, test, and save](08-wrap-up/) — check your finished game.

## Reading the scripts

The dark boxes show Scratch blocks from top to bottom. Indented lines go **inside** the block above them. `end` marks the bottom of a C-shaped block; it is not a block to drag. Round brackets show inputs or round reporters. Square brackets show menu choices or text. Angle brackets show a hexagonal true-or-false question.

## Credits

Adapted from [How to make a memory game in scratch](https://www.youtube.com/watch?v=l0lIGWz4yKU) by [smart kiddos](https://www.youtube.com/@smartkiddos6473).

The game idea and core approach come from the tutorial. This workshop adds smaller exercises, test cases, complete resets, and a dealing sequence that gives each clone its own values before the next card is made. Variable names use spaces for readability. You will draw your own pictures; no video images or music are needed.

Workshop organization is inspired by [Splunk Observability Workshops](https://splunk.github.io/observability-workshop/en/). No endorsement is implied.
