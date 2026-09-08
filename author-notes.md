# Author notes: Memory match

## Source and repository evidence

- Canonical video: https://www.youtube.com/watch?v=l0lIGWz4yKU
- Title: **How to make a memory game in scratch**.
- Creator: **smart kiddos**, https://www.youtube.com/@smartkiddos6473.
- Runtime observed: 14:51. Publication date and license remain unverified (`null` in metadata).
- Accessed: 2026-09-08. Title and creator verified through YouTube oEmbed and visible watch page.
- Captions: English, auto-generated, successfully exported using the browser's YouTube transcript export. Direct timedtext retrieval returned an empty body. The complete transcript is retained only in task scratch storage, not distributed here. No audio transcription was claimed.
- Video frames inspected at approximately 7:25 (clone initialization), 8:54 (click handler), and 13:27 (Win sprite). Frame updates after seeking can lag; only clearly loaded frames were used as evidence.
- Repository: https://github.com/hypnot0ad/coderling was visibly **Private** and empty in the authenticated browser. Public API returned 404, HTTPS cloning required unavailable authentication, and SSH connection timed out. There was no existing structure/style, catalog, AGENTS.md, or build workflow to preserve.

## Evidence map

| Workshop stage | Source time | Observed content | Teaching adaptation |
|---|---|---|---|
| Get ready | 0:16–0:26 establishes project | Memory game in Scratch | Editor and Builder warm-ups, local saving, account-free instructions |
| Draw the cards | 1:56–2:53 | Card back plus four ordered face costumes | Student-drawn shapes, centered 70 × 90 sizing guidance, explicit costume table |
| Pack a deck | 0:29–1:52; 2:56–6:02 | Three local and seven global variables; deal custom block; list filled 1–4 twice | Spaced variable names; numeric flags; complete resets; isolated eight-item test |
| Deal eight cards | 5:31–8:49; frame ~7:25 | x −150, y 100; x increment 100, row threshold 150, y change −120; random list index and deletion; clones show back | Allocation and position handled sequentially by original before clone creation; inherited local card ID; temporary reveal test |
| Turn over two | 8:52–10:53; frame ~8:54 | Flip count under 2, not already flipped; costume card ID + 1; first and second IDs | Extra matched guard, explicit nested conditions, intermediate stopping point |
| Find a match | 10:57–13:10 | 1.5-second wait; equality; match count; matched and flip-back messages; unmatched closure | `broadcast and wait` to finish receivers before reopening turn; renamed messages; complete script |
| Win | 13:13–14:14; frame ~13:27 | Win sprite flag hides; receive Win shows; matches reset; victory at four pairs | Check victory after second-card resolution instead of separate polling loop; explicit Win position/front layer |
| Challenges | Not in source | None claimed | Original customization, longer delay, turn counter, six-pair extension |
| Final checks | 14:27–14:34 shows completed game | Working shuffled game described | Edge-case test matrix, reflection, local saving |

## Corrections and deliberate differences

1. At 3:55–4:09, the narration says `delete this clone` deletes the original template. It does not delete the original sprite. This workshop leaves the original hidden and does not use that ineffective block there.
2. A card ID is a picture/pair identifier, not a unique instance ID: there must be two copies of each ID. At 8:19–8:29 the narration says deletion prevents duplicates; more precisely, removing one selected list entry preserves the intended two-per-picture distribution.
3. The video assigns shared position and deck state in clone-start handlers. The workshop moves allocation into the original's deal loop. A clone inherits the original's local ID and position at creation; clone handlers only initialize their own flags, back costume, and visibility. No clone mutates the shared deck/position state.
4. `True`/`False` text flags become numeric 1/0, explicitly taught. Broadcast names become `pair found`, `turn back`, and `win` so variable/message names do not collide visually.
5. Every shared turn/score value resets on the flag. Old clones are removed by Scratch on a new green-flag run. The Win sprite also hides on the flag. Victory is checked after pair resolution. The shorter wait remains 0.2 seconds in the nonmatch branch.
6. `broadcast … and wait` ensures pair receivers complete before flip count returns to 0. No receiver contains a wait. Click gating blocks reselecting the same card, a matched card, and a third card during the reveal pause.

## Curriculum

Graph version: **1.0**, from the Scratch YouTube Workshops skill. Level: **Creator**, because the core combines variables, lists, clones, broadcasts, custom blocks, and coordinated game state. No age-based override.

Core used: coordinates, looks-sound, loops, conditions, variables, broadcasts, clones, custom-blocks, lists, game-state.

Closure in prerequisite order: editor → sprites → events → sequences → motion → coordinates; looks-sound; loops; sensing; operators; conditions; variables; broadcasts; clones; custom-blocks; lists; game-state. This is a topological list, not a claim that every neighboring concept is a direct dependency.

Taught: coordinates, looks-sound, loops, sensing, operators, conditions, variables, broadcasts, clones, custom-blocks, lists, game-state. Entry concepts: editor, sprites, events, sequences, motion. Setup includes an optional bridge for these entry skills and introduces Builder dependencies before later state/list lessons. Variables follow operators; lists follow variables and loops; clones follow events/loops; broadcasts precede coordinated match resolution.

The skill's curriculum resolver was run with the used/taught sets above and returned Creator plus these five entry concepts. No prerequisite workshops exist in the empty repository, so `prerequisite_workshops` is an empty list. Preparation links point only to the real setup page; no catalog links were invented.

Time estimate: 100 minutes hands-on, roughly 5 setup + 15 costumes + 20 deck + 20 dealing + 15 flipping + 20 matching/win + 5 final tests. Optional warm-up adds about 15 minutes; challenges are outside core duration. Younger learners may benefit from two sessions and an adult/coding buddy.

## Script review and verification

- Trace reviewed: flag resets → eight-entry deck → choose index in current list bounds → inherit ID/position → delete selected item → eight clones → two different choices → delayed pair comparison → receiver updates → reopen turn → victory at four pairs.
- Scope checked: card ID, flip, matched are per-sprite; seven others and list shared.
- Geometry checked: four columns at −150/−50/50/150; rows 100/−20; student cards under 100 × 120. Win at y −130.
- Costumes checked: back is #1, faces #2–#5, reveal is ID + 1.
- Repeated clicks, third clicks during pause, locked matches, mismatch closure, full win, and restart during pause reviewed logically.
- No Scratch runtime execution or `.sb3` playback performed. These checks are a logical review, not an execution test.
- Hugo 0.150.1 production build executed locally with `--minify --panicOnWarning`.
- `scripts/check_site.py` checks generated local links, assets, fragment targets, stage count, credits, and navigation. See the task delivery report for final command results.
- No prior build workflow existed. A private-repository Pages restriction may prevent public hosting; deployment must be confirmed in GitHub rather than inferred from a build.

## Rights and design provenance

No creator screenshots, video, audio, full transcript, or card artwork are redistributed. Source license is unknown; attribution is not permission to reuse assets. Students draw their own replacements. Site layout/CSS and workshop prose are newly authored; no third-party font or image dependency is included. No broad license has been chosen on the repository owner's behalf.

Guided multi-page organization is inspired by https://splunk.github.io/observability-workshop/en/ . No text, branding, or endorsement is borrowed.

## Hosting status observed on 2026-09-08

The repository’s Settings → Pages screen explicitly displayed “Upgrade or make this repository public to enable Pages.” Hosting is currently blocked by the account/repository eligibility setting. No visibility or billing change was made.

## Follow-up repository status

After the owner’s update, the repository was observed as Public and Pages allowed branch deployment. The initial restriction recorded above is historical. The owner also enabled browser file uploads.
