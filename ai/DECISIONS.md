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
