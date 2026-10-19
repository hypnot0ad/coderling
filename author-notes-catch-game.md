# Author notes: Catch the apples

## Skill and repository

Requested name: “build github workshop”. No separate SKILL.md with that name or phrase was found in the local skill directories or projects. The actual installed user skill at `/Users/nistone/.codex/skills/scratch-youtube-workshops/SKILL.md` provides the requested YouTube-to-Coderling workflow. Its source-handling, curriculum, concept graph, templates, and output contract were followed. The same skill also exists in a previous Coderling deliverable.

Current repository cloned from https://github.com/hypnot0ad/coderling on 19 October 2026. Base commit: f1671828442aea230c8349cf1e6c99a034a2bfa8. The project is Hugo with committed docs/ output and branch-based GitHub Pages. The existing memory-match lesson content and feedback feature are retained. Shared templates now list both workshops and identify the current workshop. CONTRIBUTING.md and LICENSE were read; no AGENTS.md was found in the checkout. No push, issue, PR, hosting change, or publication was performed.

## Source provenance

- Canonical video: https://www.youtube.com/watch?v=7NN5v2wSL4U
- Title: How to Make a Catch Game in Scratch | Tutorial
- Channel: Scratch Team, https://www.youtube.com/@ScratchTeam
- Presenter: Zoë, also known as Zinnea (intro 0:00–0:03).
- Published: 2021-01-26, verified in the expanded YouTube description.
- Runtime observed: 6:34.
- Accessed: 2026-10-19.
- English captions retrieved through the browser’s YouTube transcript export. Export labels them “authored or unspecified”; manual authorship is not independently established. This value is recorded explicitly instead of assuming auto-captions or inventing speech transcription.
- Full timestamped transcript retained only in task work storage; not redistributed in the site or archive.
- A loaded frame at 5:54 was inspected: Apple selected; touching Bowl branch contains change Score by 1, start sound Collect, go to random position, set y to 180. At that frame the presenter was still editing the reset dropdown. The final Score reset is supported by narration at 5:52–5:56. No claim is made that every block was visually inspected.
- Video license unverified: null. The music’s separate CC credit in the description is not treated as a license for the entire video.

## Evidence map

| Stage | Source range | Observed or narrated behavior | Coderling adaptation |
|---|---|---|---|
| Setup | 0:26–0:39; 2:14–2:20 | Choose Bowl, Boardwalk, Apple | Editor bridge, local saving, explicit sprite sizes |
| Move | 0:41–2:12 | Key sensing, if, forever, x ±10 | Reset Bowl to x 0 y −130; operator practice before later comparisons |
| Top | 2:22–3:00 | Random position then y 180 | Isolated repeated-start checkpoint |
| Fall | 3:02–4:42 | Fall by −5; y less than −170 returns to top | Full replacement script and three-fall test |
| Catch | 4:44–5:22; frame 5:54 | Touch Bowl, return to top, Collect sound | One Apple loop containing fall, miss, catch, rather than separate polling stacks |
| Score | 5:25–5:58; frame 5:54 | Score variable, +1 on catch, reset on start | Explicit shared variable scope; score reset in same Apple script |
| Challenges | 5:59–6:17 | Theme ideas and customization | Pace experiment and bowl boundary extension are newly designed |
| Wrap-up | 5:58; 6:18–6:20 | Completed catch game | Original replay, miss, save/reopen and restart checklist |

All prose, checkpoints, troubleshooting, and explanations are original educational writing. Source code behavior is adapted, not claimed as a frame-perfect reconstruction. Transcript “ball” at 0:49–0:51 means the selected Bowl in context. Coordinates are explained relative to the stage center, rather than as distance from its bottom. Falling is −5, consistent with narration at 4:35, despite earlier exploratory +10 examples.

## Script decisions and logical review

Bowl has one flag script, resets position, then checks each arrow inside forever. Apple has one flag script: reset Score → choose random position → set y 180 → forever: fall −5 → miss test → catch test. A miss returns to the top without scoring. A catch increments once, starts sound without waiting, and returns to the top. That move separates the objects before the next catch test. Only Apple writes Score, avoiding cross-sprite score-reset races. No clones, broadcasts, parallel Apple loops, timers, life counters, or win condition are introduced.

Bowl y −130 and sizes Bowl 100%, Apple 60% are teaching choices to keep collision above the miss boundary. The optional x clamp uses ±190 with these sizes. Green flag resets both scripts for repeated play. A finite random number of repeated x positions is normal; “random” does not promise a different position every time. The apple’s default size and library artwork determine its visible shape; a teacher should run the published play checklist in Scratch before class.

The core scripts were traced for startup, holding and releasing each key, fall/miss repetition, catch separation, +1 scoring, and restart. Scratch execution was not performed. No .sb3 project or gameplay execution claim is included.

## Curriculum

Graph version 1.0 from the installed skill. Used: input-control, coordinates, loops, conditions, variables, looks-sound. Taught: coordinates, loops, sensing, operators, conditions, input-control, variables, looks-sound. Closure in resolver order: editor, sprites, events, sensing, sequences, operators, conditions, motion, input-control, coordinates, loops, variables, looks-sound. This is a valid dependency order, not a linear dependency chain.

Entry concepts: editor, sprites, events, sequences, motion. The optional setup warm-up bridges these five concepts. Coordinates follow motion; sensing and true/false operator practice precede conditions and input-control in Move the bowl; loops are introduced before repeated checking; numeric comparison returns in Fall; the variable follows sequence/operator practice in Keep score. Sound is introduced before score. No cyclic or invented prerequisite links.

Level is Creator because the core uses a variable. Earlier movement/catch stages are Builder. Age 8–15 is the skill’s default audience, not evidence about a particular learner. No age-based level override is applied. The existing memory-match workshop teaches more advanced concepts and is offered only as a possible next project; it is not necessary preparation. No simpler prerequisite workshop exists in this catalog, so prerequisite_workshops remains empty and the setup bridge supplies missing practice.

Estimated core time: setup 10 + move 15 + top 5 + fall 10 + catch 10 + score 10 + final tests 5 = 65 minutes. Optional warm-up adds 10 minutes; optional challenges are excluded. Pace is an instructional estimate, not video runtime.

## Rights and structural inspiration

No video frames, music, full transcript, or creator artwork are distributed. Learners select Scratch library assets in their own editor. No new asset files are bundled. The tutorial’s third-party music and example projects are not used. Existing repository license is retained without making claims about third-party rights. The guided overview/stage structure follows the skill’s structural inspiration, https://splunk.github.io/observability-workshop/en/ ; no endorsement is implied.

## Validation performed

- Curriculum resolver executed with the used/taught sets above: Creator; five entry concepts; valid graph.
- Hugo 0.150.1 production build with --minify --panicOnWarning: PASS, 20 HTML pages.
- Current installed Hugo 0.166.0 initially rejected the existing languageCode configuration as deprecated under --panicOnWarning. Used the project’s documented 0.150.1 binary instead, preserving its configuration.
- Existing checker extended to cover both eight-stage workshops. All local links, asset references, fragment IDs, stage counts, source credits, navigation and feedback controls: PASS across 20 generated HTML pages.
- Browser inspected the generated catch-game overview and score lesson. Local preview uses the actual /coderling/ project prefix. See validation report for final visual observations.
- No remote deployment or Scratch runtime execution was performed.
