# BUILD NOTES: what a future session would waste time rediscovering

## MAP
```
ai/                         project docs (start with CONTEXT.md)
mp3-mp4_app/
  netlify.toml              publish dir, security headers (the content security policy lives here)
  package.json              scripts: test, test:e2e, serve
  netlify/functions/
    count.mts               POST /api/count?e=visit|install|convert
    stats.mts               GET  /api/stats?key=...   private usage report
  public/
    index.html              landing page (copy by Alex, brand by Andy)
    convert.html            the converter (the installed app opens here)
    licenses.html           open source notices
    manifest.webmanifest    install settings
    sw.js                   offline cache. Bump VERSION on every release
    css/styles.css          all styles, brand colors as variables at the top
    js/queue.js             pure queue logic, unit tested
    js/engine.js            MP4 in, MP3 out
    js/app.js               the converter screen
    js/install.js           landing page install button
    js/count.js             usage counter call, service worker registration
    vendor/                 Mediabunny libraries and license
    fonts/ img/             self-hosted fonts, logo, app icons
  tests/
    queue.test.mjs          unit tests
    serve.mjs               local server with production security headers
    e2e.mjs                 full browser run, including a large file
```

## Engine
- The test browser in Claude's cloud workspace (Playwright Chromium) cannot decode AAC, the audio format in almost every real MP4. Tests there use MP4 files with MP3 audio. AAC was verified in Michael's real Chrome on the live site. Do not read an "audio format this browser cannot read" failure in that test browser as an app bug.
- The MP3 encoder runs in its own background worker created from a blob, so the content security policy needs `worker-src blob:` and `script-src 'wasm-unsafe-eval'`. Removing either breaks conversion with no visible error on the page.
- `public/vendor/mediabunny-mp3-encoder.min.mjs` has one edit: `from"mediabunny"` became `from"./mediabunny.min.mjs"`. Redo this if the library is ever updated.
- Finished MP3s are held in memory until cleared or the window closes. About 1.4 MB per minute of audio. Chrome moves large blobs to disk on its own.
- Measured 2026-10-11 in the cloud test browser: 1.38 GB, 75 minute file in 181 seconds, peak script memory 171 MB.

## Netlify
- Setting STATS_KEY through the Netlify tool with the "secret" option silently saved nothing. Set it as a normal variable, confirm by listing, then redeploy (values are frozen per deploy).
- The Blobs store `usage` is shared by every deploy of the project, previews included.
- Function response headers are set in code. `netlify.toml` headers only apply to the static files.

## Install button
- Chrome only offers install when the page is on https, has a manifest with 192 and 512 icons, and a service worker. The button stays hidden until Chrome says install is available, and stays hidden if the app is already installed.

## Testing
- `tests/e2e.mjs <media dir> <chrome path>` needs `small.mp4`, `noaudio.mp4`, and optionally `big.mp4` in the media dir.
- `window.__addFiles(files)` and `window.__state()` exist on the converter page for automated tests.
