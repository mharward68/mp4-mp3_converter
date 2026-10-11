# Phase 1: Build and launch the converter
Status: BUILT 2026-10-11 in one continuous run. One session remains (1.8).

Frozen contracts (set in 1.2, unchanged since):
```js
// public/js/queue.js
STATUS = { WAITING, CONVERTING, DONE, FAILED, SKIPPED }
makeItem(file) -> { id, file, name, size, status, error, progress, startedAt, outName, outSize, blob, savedToFolder }
rejectReason(file) -> string | null
mp3Name(name) -> string
uniqueName(name, takenSet) -> string
summarize(items) -> { total, done, failed, waiting, active, busy, fraction, remainingBytes }
// public/js/engine.js
convert(file, { onProgress(fraction) }) -> { promise: Promise<Blob>, cancel() }   // rejects with ConvertError { message, code }
// counter
POST api/count?e=visit|install|convert -> 204
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
| 1.8 | Connect to youravdept.com/mp3-converter, push to GitHub, Michael's real-file run | INFRA | S | 15 min | OPEN, needs Michael |

Calibration: 7 sessions estimated at about 4 hours of build time. No session needed Michael's input mid-run. The only overrun was the stats key (two extra deploys).
