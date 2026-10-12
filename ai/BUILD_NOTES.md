# BUILD NOTES: what a future session would waste time rediscovering

## MAP
```
ai/                         project docs (start with CONTEXT.md)
mp3-mp4_app/
  package.json              scripts: test, test:e2e, serve
  tools/build-landing.py    builds public/index.html from the website's library/av365.html
  site-functions/           copied to the WEBSITE's netlify/functions/ and netlify.toml
    just-the-audio-count.mjs           POST /api/just-the-audio/count?e=visit|install|convert
    just-the-audio-stats.mjs           GET  /api/just-the-audio/stats?key=...
    netlify-snippet.toml    the headers block that belongs in the website's netlify.toml
  public/                   mirrors the website's just-the-audio/ folder exactly
    index.html              landing page (GENERATED, do not edit by hand)
    manifest.webmanifest    install settings
    sw.js                   offline cache. Bump VERSION on every release
    icon-192.png icon-512.png
    app/
      index.html            the converter (the installed app opens here)
      licenses.html         open source notices
      css/styles.css        all styles, site tokens as variables at the top
      js/queue.js           pure queue logic, unit tested
      js/engine.js          MP4 in, MP3 out
      js/app.js             the converter screen
      js/count.js           usage counter call, service worker registration
      vendor/ fonts/ img/   Mediabunny libraries, self-hosted fonts, site emblem
  tests/
    queue.test.mjs          unit tests
    serve.mjs               local server at /just-the-audio/ with the production policy on /app/
    e2e.mjs                 full browser run, including a large file
```

## Activity page
- `site-pages/just-the-audio-activity.html` is copied to the WEBSITE ROOT (not into just-the-audio/). It reads `GET /api/just-the-audio/stats?format=json&key=...`. A 404 means a wrong key: the page forgets it and asks again.
- It is in the site map of every website page; build-landing.py keeps it in the landing page's copy automatically.

## Releasing to the website
1. Change and test here. Bump VERSION in `public/sw.js`.
2. Copy `mp3-mp4_app\public\*` over `C:\01_AppDevelopment\12.Your-AV-Dept_Website\just-the-audio\`.
3. In the website folder: `.\deploy-preview.ps1`, check https://offers--your-av-dept.netlify.app/just-the-audio/, then `.\deploy.ps1`.
- The website's deploy scripts publish everything in its folder that is not on their exclude list. Only `public/` contents go there: never tests, package files or docs.
- On the website, a class rule like `.btn{display:inline-flex}` beats the `hidden` attribute. Hide and show with `style.display`.

## Engine
- The test browser in Claude's cloud workspace (Playwright Chromium) cannot decode AAC, the audio format in almost every real MP4. Tests there use MP4 files with MP3 audio. AAC was verified in Michael's real Chrome on the live site. Do not read an "audio format this browser cannot read" failure in that test browser as an app bug.
- MOV test files for the cloud test browser must use PCM audio (`-c:a pcm_s16le -f mov`). MP3 audio inside a MOV is reported as unreadable, and AAC cannot be decoded there at all. Real iPhone MOVs carry AAC, which real Chrome decodes. Likewise M4A test files use MP3 audio in an MP4 wrapper (`-vn -c:a libmp3lame -f mp4 memo.m4a`); real M4A files carry AAC.
- The MP3 encoder runs in its own background worker created from a blob, so the content security policy needs `worker-src blob:` and `script-src 'wasm-unsafe-eval'`. Removing either breaks conversion with no visible error on the page.
- `public/vendor/mediabunny-mp3-encoder.min.mjs` has one edit: `from"mediabunny"` became `from"./mediabunny.min.mjs"`. Redo this if the library is ever updated.
- Finished MP3s are held in memory until cleared or the window closes. About 1.4 MB per minute of audio. Chrome moves large blobs to disk on its own.
- Measured 2026-10-11 in the cloud test browser: 1.38 GB, 75 minute file in 181 seconds, peak script memory 171 MB.

## Netlify
- Setting a key through the Netlify tool with the "secret" option silently saved nothing. Set it as a normal variable, confirm by listing, then redeploy (values are frozen per deploy).
- Test deploys write to `just-the-audio-usage-test`, the live site to `just-the-audio-usage`.
- Function response headers are set in code. `netlify.toml` headers only apply to the static files.

## Install button
- Chrome only offers install when the page is on https, has a manifest with 192 and 512 icons, and a service worker. The button stays hidden until Chrome says install is available, and stays hidden if the app is already installed.

## Testing
- `tests/e2e.mjs <media dir> <chrome path>` needs `small.mp4`, `noaudio.mp4`, and optionally `big.mp4` in the media dir.
- `window.__addFiles(files)` and `window.__state()` exist on the converter page for automated tests.
