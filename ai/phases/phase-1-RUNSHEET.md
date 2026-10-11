# PHASE 1 RUN SHEET
Build and launch
MP4 to MP3 Converter: a free installable tool from Your AV Department

> SOURCE OF TRUTH: this file, `ai/phases/phase-1-RUNSHEET.md`. Disposable: delete at phase close.

> READ THIS FIRST: Sessions 1.1 to 1.7 are already done. Mark ran them in one go on 2026-10-11 at Michael's request. Only 1.8 and the close remain.

| STEP | WHAT | OUTPUT |
|---|---|---|
| 1 | Plan | `ai/phases/phase-1-build.md` (done) |
| 2 | Build | Sessions 1.1 to 1.7 (done), 1.8 (open) |
| 3 | Close | Verify, calibrate, hand off |

Each step is a new conversation. Connect `C:\01_AppDevelopment\19_mp4-mp3_converter` first. Attach nothing: every prompt reads the repo itself.

## The sessions
- ☑ 1.1 Spike: prove the engine · M
- ☑ 1.2 Contracts and queue logic · S
- ☑ 1.3 Converter screen · L
- ☑ 1.4 Folder saving, cancel, warnings · M
- ☑ 1.5 Install and offline · M
- ☑ 1.6 Usage counter and stats · M
- ☑ 1.7 Landing page, deploy, full test · L
- ☐ 1.8 Connect to youravdept.com, push to GitHub, real-file run · S · ~15 min of Michael's time

## Step 2: run Session 1.8
Inputs needed BEFORE the session: (a) GitHub reconnected in Claude settings, or the push block below already run; (b) the main youravdept.com site's repo folder connected, or its GitHub name.

```
Mark, run Session 1.8 from ai/phases/phase-1-build.md.

BOOT: report in 5 lines or fewer: what DIRECTIVES and DECLARATIONS constrain, where CONTEXT says
the last session ended, the MAP in BUILD_NOTES, this session's goal, and the inputs you need from me.
The code wins over the documents. Ask only what blocks you, all at once.

EXECUTE: add the proxy rule for /mp3-converter to the main site (Hard Limit: show me the exact
change and wait for my yes before touching the main site). Confirm the install button and offline
use work at youravdept.com/mp3-converter. Push the repo to GitHub.

VERIFY: paste real output. Then archive CONTEXT, write a new one-page CONTEXT, update BUILD_NOTES
only with what a future session would waste time rediscovering, and tell me what is next.
```

## Step 3: close the phase
```
Mark, close Phase 1. Verify the goal with real output, compare estimates to actuals, curate
BUILD_NOTES, audit DECLARATIONS against the code line by line, review the five objectives,
write CONTEXT as a phase-boundary handoff, and tell me honestly what is next.
```

## Standing reminders
- Start the app locally: `npm run serve` in the app folder, then http://localhost:8080/
- Every release: bump VERSION in `public/sw.js`, or installed copies keep the old files.
- If conversion fails only in an automated test browser, read the Engine notes in BUILD_NOTES first.
- There is no user data, so no backup points in this phase. Git is the backup.
