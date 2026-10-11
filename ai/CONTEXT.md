# CONTEXT: where things stand
Written 2026-10-11 12:20 ET, after Session 1.8 (move into youravdept.com, library page look).

## What exists
- Version 1.1.0 of the converter and its landing page, restyled to match the youravdept.com library pages.
- The files are in the website folder (`C:\01_AppDevelopment\12.Your-AV-Dept_Website`): `mp3-converter/`, two functions, a headers block in `netlify.toml`, a site map entry on 19 pages, README and BUILD_NOTES updates.
- NOTHING IS DEPLOYED to youravdept.com yet. Michael runs the website's deploy scripts.
- The old standalone copy (version 1.0.0, old look) is still live at https://yavd-mp3-converter.netlify.app until that project is deleted.
- MP3_STATS_KEY is set on the main Netlify project (takes effect on the next deploy).

## Verification (real output, 2026-10-11, cloud test browser)
Unit tests: `# pass 5  # fail 0`

Browser run, 23 of 23 checks passed, including:
```
PASS  large file (1.38 GB) converts  (182 s, MP3 103 MB, peak JS heap 171 MB, error: null)
PASS  large MP3 duration matches source  (4500.088163 vs 4500.000000)
PASS  converter made no requests outside its own address
PASS  landing page renders
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
- Andy reviewed screenshots from the cloud test browser, which cannot load Google Fonts, so the landing page was seen in fallback fonts.

## Backup coverage
No store of user data. The website is in Git (github.com/mharward68/youravdept-com); tag it before going live.

## Exact next step
Michael runs Session 1.9: the PowerShell blocks in the chat (preview deploy, check, go live, push).
