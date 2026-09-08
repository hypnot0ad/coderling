# Coderling

A Scratch 3 workshop for ages 8–15, adapted from **How to make a memory game in scratch** by **smart kiddos**: https://www.youtube.com/watch?v=l0lIGWz4yKU.

The repository was inspected in a signed-in GitHub browser on 2026-09-08. It was private and empty: no files, theme, prerequisite catalog, or build workflow existed. This adds a small Hugo site with no external theme, fonts, JavaScript, or package dependencies. All card art is drawn by students.

## Workshop

Creator level; about 100 minutes, optionally split into two sessions. A 15-minute warm-up supports learners who need prerequisite practice. Eight stages cover setup, costumes, lists, dealing clones, choosing cards, matching and winning, optional challenges, and final tests. Each stage includes a prediction, checkpoint, troubleshooting, explanation, and visible source credit.

Editable lessons are in `content/workshops/memory-match/`. Source provenance, educational adaptations, and verification limits are in `author-notes.md`.

## Build and check locally

Install Hugo **0.150.1** from the official Hugo release, and Python 3. Then, from this directory:

```sh
hugo --minify --panicOnWarning
python3 scripts/check_site.py
```

Hugo writes to `docs/`. Keep that generated folder in the repository for branch-based GitHub Pages deployment. The file `static/.nojekyll` is copied into it automatically. Do not edit generated HTML directly.

For a local preview:

```sh
hugo server --baseURL http://localhost:1313/coderling/ --appendPort=false
```

Open http://localhost:1313/coderling/. The templates and all local links support the `/coderling/` project prefix. If the repository name or hostname changes, update `baseURL` in `hugo.toml`, the checker's `BASE`, and rebuild.

## GitHub Pages deployment

1. Commit the source and rebuilt `docs/` folder to `main`.
2. In **Settings → Pages**, choose **Deploy from a branch**.
3. Select **main** and **/docs**, then **Save**.
4. Wait for the Pages deployment to finish. GitHub will show the actual published URL; the intended URL is https://hypnot0ad.github.io/coderling/.

The repository owner made the repository public on 2026-09-08. GitHub Pages is now available. Students do not need to sign in.

No pre-existing workflow was available to run. This repository uses committed static output and GitHub's branch deployment, so no custom Actions workflow is required. After each content change, rebuild, run the checker, and commit the updated source and `docs/` together.

## Verification and limits

The Hugo production build and local link checker are the reproducible checks. The instructional scripts were reviewed for scope, nesting, pair allocation, click gating, broadcasts, victory, and restart behavior. The project was not executed inside Scratch, and no `.sb3` file is supplied. A teacher should run the final play checklist before teaching a group. Passing a site build does not test Scratch behavior.

The tutorial's automatic English transcript and selected video frames were reviewed. This is a documented educational adaptation, not a block-for-block transcript. No full transcript, video screenshot, audio, or creator artwork is distributed. See `author-notes.md` for evidence and corrections.

## Hosting status observed on 2026-09-08

The initial private-repository Pages restriction was resolved by the owner. The repository is now public and its Pages settings allow branch deployment. The site is configured for `main` → `/docs`.
