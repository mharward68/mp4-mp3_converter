# Phase 1: Build and launch the converter
Status: BUILT 2026-10-11. One step remains (1.9), and it is Michael's.

Frozen contracts (set in 1.2, unchanged since):
```js
// public/app/js/queue.js
STATUS = { WAITING, CONVERTING, DONE, FAILED, SKIPPED }
makeItem(file) -> { id, file, name, size, status, error, progress, startedAt, outName, outSize, blob, savedToFolder }
rejectReason(file) -> string | null
mp3Name(name) -> string
uniqueName(name, takenSet) -> string
summarize(items) -> { total, done, failed, waiting, active, busy, fraction, remainingBytes }
// public/app/js/engine.js
convert(file, { onProgress(fraction) }) -> { promise: Promise<Blob>, cancel() }   // rejects with ConvertError { message, code }
// counter
POST /api/mp3-converter/count?e=visit|install|convert -> 204   (path changed in 1.8, a plan revision Michael asked for)
```

| # | Session | Compartment | Size | Est. | Result |
|---|---|---|---|---|---|
| 1.1 | Spike: prove the engine on a 1.4 GB file | LOGIC | M | 30 min | Done. Engine chosen and proven |
| 1.2 | Contracts and queue logic with unit tests | LOGIC | S | 20 min | Done. 5 of 5 tests pass |
| 1.3 | Converter screen | UI | L | 50 min | Done |
| 1.4 | Folder saving, cancel, close warning, unsupported browser | STATE | M | 30 min | Done |
| 1.5 | Install and offline | INFRA | M | 30 min | Done. Offline conversion verified |
| 1.6 | Usage counter and stats page | API | M | 30 min | Done. Live and verified |
| 1.7 | Landing page (Alex copy, Andy brand), deploy, full test | UI | L | 50 min | Done. 21 of 21 checks pass |
| 1.8 | Move into the youravdept.com site, rebrand to the library page look | INFRA + UI | L | 50 min | Done in the build. Files are in the website folder, NOT yet deployed |
| 1.9 | Michael: preview deploy, check, go live, push both repos, real-file run | INFRA | S | 20 min | OPEN, needs Michael |

Calibration: 7 sessions estimated at about 4 hours of build time. No session needed Michael's input mid-run. The only overrun was the stats key (two extra deploys).
