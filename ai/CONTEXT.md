# CONTEXT: where things stand
Written 2026-10-12 06:45 ET, after the broadened page copy (version 2.1.0). Michael is deploying.

## What exists
- Version 2.0.0, now named Just the Audio: the tool and its landing page, restyled to match the youravdept.com library pages. Accepts MP4, MOV and M4A.
- The files are in the website folder (`C:\01_AppDevelopment\12.Your-AV-Dept_Website`): `just-the-audio/`, two functions, a headers block in `netlify.toml`, a site map entry on 19 pages, README and BUILD_NOTES updates.
- The website folder also still holds the OLD `mp3-converter\` folder and `netlify\functions\mp3-count.mjs` / `mp3-stats.mjs` from before the rename. They must be deleted before deploying (Claude cannot delete files on the PC).
- NOTHING IS DEPLOYED to youravdept.com yet. Michael runs the website's deploy scripts.
- The old standalone copy (version 1.0.0, old look) is still live at https://yavd-mp3-converter.netlify.app until that project is deleted.
- JUST_THE_AUDIO_STATS_KEY is set on the main Netlify project (takes effect on the next deploy).

## Verification (real output, 2026-10-11, cloud test browser)
Unit tests: `# pass 5  # fail 0`

Browser run after the MOV and M4A changes: all checks passed (large-file check not re-run; it passed on 1.1.0, and the engine code path is unchanged). Including:
```
PASS  MOV file converts  (done  288744)
PASS  MOV output is a real MP3 of the right length (12 s)  (mp3 12.048000)
PASS  M4A file converts  (done  361899)
PASS  M4A output is a real MP3 of the right length (15 s)  (mp3 15.098776)
PASS  large file (1.38 GB) converts  (182 s, MP3 103 MB, peak JS heap 171 MB, error: null)
PASS  large MP3 duration matches source  (4500.088163 vs 4500.000000)
PASS  converter made no requests outside its own address
PASS  landing page renders
PASS  landing page explains all three formats
PASS  landing page links to the converter
PASS  visit was counted
PASS  converter opens offline
PASS  converts while offline
```
Site map: 19 website pages each gained exactly one line (27 entries each).

## Not verified
- Nothing has been checked on a real youravdept.com deploy: the headers block, the two functions, and the install button at the new address.
- Michael's own 1.46 GB recording has not been run.
- The install click, Edge, and Mac.
- A real iPhone MOV or a real Zoom M4A (both AAC audio). The tests used a MOV with PCM audio and an M4A with MP3 audio; AAC itself was verified earlier in real Chrome inside an MP4.
- Andy reviewed screenshots from the cloud test browser, which cannot load Google Fonts, so the landing page was seen in fallback fonts.

## Backup coverage
No store of user data. The website is in Git (github.com/mharward68/youravdept-com); tag it before going live.

## Exact next step
Michael runs Session 1.9: the PowerShell blocks in the chat (preview deploy, check, go live, push).
