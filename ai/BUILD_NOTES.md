# BUILD NOTES: what a future session would waste time rediscovering

## MAP
```
ai/                         project docs (start with CONTEXT.md)
mp3-mp4_app/
  package.json              scripts: test, test:e2e, serve
  tools/build-landing.py    builds public/index.html from the website's library/av365.html
  site-functions/           copied to the WEBSITE's netlify/functions/ and netlify.toml
    mp3-count.mjs           POST /api/mp3-converter/count?e=visit|install|convert
    mp3-stats.mjs           GET  /api/mp3-converter/stats?key=...
    netlify-snippet.toml    the headers block that belongs in the website's netlify.toml
  public/                   mirrors the website's mp3-converter/ folder exactly
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
    serve.mjs               local server at /mp3-converter/ with the production policy on /app/
    e2e.mjs                 full browser run, including a large file
```

## Releasing to the website
1. Change and test here. Bump VERSION in `public/sw.js`.
2. Copy `mp3-mp4_app\public\*` over `C:\01_AppDevelopment\12.Your-AV-Dept_Website\mp3-converter\`.
3. In the website folder: `.\deploy-preview.ps1`, check https://offers--your-av-dept.netlify.app/mp3-converter/, then `.\deploy.ps1`.
- The website's deploy scripts publish everything in its folder that is not on their exclude list. Only `public/` contents go there: never tests, package files or docs.
- On the website, a class rule like `.btn{display:inline-flex}` beats the `hidden` attribute. Hide and show with `style.display`.

## Engine
- The test browser in Claude's cloud workspace (Playwright Chromium) cannot decode AAC, the audio format in almost every real MP4. Tests there use MP4 files with MP3 audio. AAC was verified in Michael's real Chrome on the live site. Do not read an "audio format this browser cannot read" failure in that test browser as an app bug.
- The MP3 encoder runs in its own background worker created from a blob, so the content security policy needs `worker-src blob:` and `script-src 'wasm-unsafe-eval'`. Removing either breaks conversion with no visible error on the page.
- `public/vendor/mediabunny-mp3-encoder.min.mjs` has one edit: `from"mediabunny"` became `from"./mediabunny.min.mjs"`. Redo this if the library is ever updated.
- Finished MP3s are held in memory until cleared or the window closes. About 1.4 MB per minute of audio. Chrome moves large blobs to disk on its own.
- Measured 2026-10-11 in the cloud test browser: 1.38 GB, 75 minute file in 181 seconds, peak script memory 171 MB.

## Netlify
- Setting a key through the Netlify tool with the "secret" option silently saved nothing. Set it as a normal variable, confirm by listing, then redeploy (values are frozen per deploy).
- Test deploys write to `mp3-usage-test`, the live site to `mp3-usage`.
- Function response headers are set in code. `netlify.toml` headers only apply to the static files.

## Install button
- Chrome only offers install when the page is on https, has a manifest with 192 and 512 icons, and a service worker. The button stays hidden until Chrome says install is available, and stays hidden if the app is already installed.

## Testing
- `tests/e2e.mjs <media dir> <chrome path>` needs `small.mp4`, `noaudio.mp4`, and optionally `big.mp4` in the media dir.
- `window.__addFiles(files)` and `window.__state()` exist on the converter page for automated tests.
