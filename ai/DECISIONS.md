# DECISIONS: why, and what was rejected (append-only)

## 2026-10-11
- **Runs in the browser, installable (PWA).** Michael chose "installable web app only". Rejected: a signed Windows/Mac installer (yearly signing fees, security warnings without them, two builds) and a single downloadable HTML file (feels less like an app, large files unproven).
- **Engine: Mediabunny with the browser's audio decoder and a LAME MP3 encoder.** Rejected: ffmpeg compiled for the browser. It loads the whole file into memory (unreliable from 500 MB up), is about 30 MB to download, and its GPL terms would have required publishing the app's source.
- **No build step.** The libraries ship as ready-made modules, so a bundler would add dependencies without benefit. One line of the vendored MP3 encoder was changed to import `./mediabunny.min.mjs` by relative path.
- **Sequential conversion.** One file at a time, for stability and honest progress.
- **192 kbps fixed.** No settings. Quality selector deferred.
- **Public promo, Your AV Department brand.** Raised the UX tier to Polished and added the landing page.
- **Usage counting with our own counter.** One tiny record per event in Netlify Blobs, counted by listing. Rejected: Google Analytics (third-party script would break the "nothing leaves this computer" promise) and a single shared counter (simultaneous visitors would overwrite each other).
- **Landing page and app on their own Netlify project,** to be shown at youravdept.com/mp3-converter through one proxy rule on the main site. Rejected: adding the files to the main site's repo (mixes two codebases and risks the live site).
- **Error rows use navy with a dashed outline,** not red. Andy's call: red is off-palette, and status is carried by text and icon.
- **Buttons are Signal Teal with navy text.** White on teal fails contrast.
- **Phase 1 was run as one continuous build** at Michael's request ("build without my assistance"), not one conversation per session.

## 2026-10-11 (afternoon): moved into youravdept.com
- **The converter now lives inside the main website** at youravdept.com/mp3-converter (landing page) and /mp3-converter/app/ (the converter). Michael's call: one site to own. This reverses the morning's "own Netlify project" decision. The `yavd-mp3-converter` project is retired once the main site is deployed.
- **This repo stays the source of truth.** `mp3-mp4_app/public/` mirrors the website's `mp3-converter/` folder exactly and is copied over it to release.
- **The landing page is generated from the site's own library page** (`tools/build-landing.py`), so header, footer, styles and site map are the site's. Rejected: hand-copying the look, which drifts.
- **The converter page matches the site's tokens:** Inter body, Montserrat 800 headings, white ground, the site's gradient buttons. Open Sans is gone (the site uses Inter).
- **The strict content security policy covers /mp3-converter/app/* only.** The landing page uses the site template's inline CSS and JS and Google Fonts, like every other page on the site. It handles no files.
- **Counter moved to /api/mp3-converter/count and /stats,** stores `mp3-usage` (live) and `mp3-usage-test`, key in MP3_STATS_KEY on the main site.

## 2026-10-11: MOV input added (version 1.2.0)
- **MOV files are accepted alongside MP4.** Michael's call, and only MOV: M4A, WebM, MKV, WAV and extra output formats stay deferred to keep the tool settings-free. The product name stays "MP4 to MP3 Converter".

## 2026-10-11: M4A input added (version 1.3.0)
- **M4A files are accepted alongside MP4 and MOV** (Zoom audio-only recordings, phone voice memos). Michael's call. WebM, MKV, WAV and extra output formats stay deferred. The product name stays "MP4 to MP3 Converter".

## 2026-10-11: renamed to "Just the Audio" (version 2.0.0)
- **The product is "Just the Audio".** Alex's shortlist, Michael's pick: it names the outcome a planner wants, in the words they already use, and stays true as formats are added. Rejected: Session Audio, Session to Audio, Recording to MP3, The Audio Puller.
- **Address is youravdept.com/just-the-audio/**, tool at /just-the-audio/app/. Functions, stores, the stats key (JUST_THE_AUDIO_STATS_KEY) and the offline cache name all follow the new name.
- **"MP4, MOV and M4A to MP3" stays in the page title and subtitle** so the page still describes itself to search and to first-time visitors.
- **The landing page explains every format** it takes and the one it produces (section id `formats`), plus what it will not take.
- **Not renamed:** the project folder (19_mp4-mp3_converter), the app folder (mp3-mp4_app) and the GitHub repo (mp4-mp3_converter). Renaming them is Michael's call and breaks nothing if left.
- The trademark and prior-use check on the name has not been done.

## 2026-10-12: page copy broadened (version 2.1.0)
- **Copy from the "Just the Audio: Page Copy" doc, approved by Michael by asking to deploy.** Session recordings are one use among nine, not the theme; "a whole conference at once" removed. The doc's open choices were left as drafted (nine uses, byline kept, "kept needing it" line).

## 2026-10-12: private activity page
- **youravdept.com/just-the-audio-activity**, listed in the hidden site map on every page that has one. Live visits, installs and files converted (today, last 7 days, all time, by day), refreshed every 30 seconds while open.
- **Protected by the same key as the stats function.** The page and site map are public files, so the key is never in them: the page asks once per browser and remembers it there. Rejected: a key in the page or link (anyone opening the site map would have it).
- "Machine" changed to "device" in the landing page privacy passage, and the usage-counting line removed from it (Michael: that is for him only).
- Activity page: period buttons (Today, WTD, MTD, YTD, All time) drive the three cards; a card pulses when its count rises on a refresh. Weeks start Sunday. Counts are now filed by Eastern-time day (was UTC), so "today" matches Michael's calendar.
