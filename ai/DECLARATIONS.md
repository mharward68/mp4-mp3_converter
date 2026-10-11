# DECLARATIONS: what was decided (the standard of truth; if the code disagrees, the code wins)

## Stack
- Plain HTML, CSS and JavaScript modules. No framework, no build step. `public/` is deployed as is.
- Conversion: Mediabunny 1.61.3 and @mediabunny/mp3-encoder 1.61.3, vendored in `public/vendor/`.
- Hosting: Netlify project `yavd-mp3-converter` (id 7029ce11-879d-4dcc-9305-6ff7cce83e0b). Base directory `mp3-mp4_app`, publish `public`.
- Counter: two Netlify Functions (`count`, `stats`) using Netlify Blobs store `usage`.
- Tests: Node's built-in test runner for logic, Playwright for the browser run.

## Conventions
- All paths in HTML, CSS, JS and the manifest are relative, so the app works at a subpath (/mp3-converter/).
- Pure logic lives in `public/js/queue.js` (no DOM). The engine lives in `public/js/engine.js`. The screen lives in `public/js/app.js`.
- Errors shown to users are plain English and say what to do or why.
- Colors come from the CSS variables at the top of `public/css/styles.css`.

## Environment
- Repo root on Michael's PC: `C:\01_AppDevelopment\19_mp4-mp3_converter`
- App folder: `C:\01_AppDevelopment\19_mp4-mp3_converter\mp3-mp4_app`
- Run locally: `npm run serve`, then http://localhost:8080/
- Live: https://yavd-mp3-converter.netlify.app
- Stats: https://yavd-mp3-converter.netlify.app/api/stats?key=<STATS_KEY from Netlify>
- GitHub: https://github.com/mharward68/mp4-mp3_converter

## Done means
- The app runs with a clean console, and `npm test` passes.
- Existing behavior still works (`npm run test:e2e` passes).
- No new store of user data. If one is added, its backup story is stated.
- Verification is pasted real output.
- The app is left usable, and VERSION in `public/sw.js` is bumped on any release.
