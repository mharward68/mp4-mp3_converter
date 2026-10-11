# MP4 to MP3 Converter Scope
Status: APPROVED 2026-10-11 (version 2, public promo tool). Phase 1 built the same day.

## 1. Summary
A free, installable web app from Your AV Department that converts MP4 recordings to MP3. The user drops one or many MP4 files and each becomes its own MP3. All conversion happens on the user's computer: no upload, no account. It is offered to meeting planners as a promo item from a page at youravdept.com/mp3-converter.

## 2. Users and roles
- The public (meeting planners first). No sign-in, no roles.
- Michael: sees anonymous usage totals on a private stats page.

## 3. Core workflows
1. Visit the landing page, click "Install the free converter" (Chrome or Edge), or "Use it in your browser".
2. Drop MP4 files on the drop zone, or click to browse.
3. Files convert one at a time, in order. More can be added while a batch runs.
4. Each finished file shows a Download button. "Download all finished" saves them all.
5. Optional: "Choose a folder" once, and every MP3 is written straight there.
6. A bad file (not an MP4, no audio, damaged) shows a plain-English reason on its own row and the queue carries on.

## 4. Features
**Built (version 1.0.0)**
- Landing page with install button, copy and brand
- Drop zone for multiple files, click to browse
- Queue with waiting, converting (percent and time left), done, failed, skipped
- MP3 at 192 kbps, original file name, numbered if the name repeats
- Per-file download, download all, save to a chosen folder
- Cancel the active file, remove waiting files, dismiss errors, clear finished
- Warning before closing mid-conversion
- Installable, works offline after the first visit
- Anonymous count of visits, installs and conversions, with a private stats page
- Message for browsers that cannot run it

**Later (explicitly deferred)**
- Quality selector, other input and output formats, trimming, ID3 tags
- Safari and Firefox support
- A signed Windows or Mac installer

## 5. Data
- No user data is stored. Files are read from disk, converted in memory, handed back.
- The only stored data is the usage tally: one record per event holding an event name and a date. No IP address, no file name, no file size.

## 6. Identity, auth and integrations
- No sign-in. No third-party services at run time.
- The stats page is protected by a key held in a Netlify environment variable (STATS_KEY).

## 7. Platforms and UX
- Chrome and Edge on Windows and Mac. Other browsers get a clear message.
- UX tier: Polished (public, branded).
- Accessibility: keyboard operable, visible focus, status in text and not color alone, live announcements.
- Brand: Your AV Department. AV Navy #152B4A, Signal Teal #2AA4A2, white base, Montserrat headings, Open Sans body, no-URL logo.

## 8. The five objectives
- **Security:** files never leave the computer, enforced by a content security policy that only allows requests to the app's own address. Libraries are pinned and bundled, not loaded from other sites.
- **Stability:** one bad file never stops a batch. Large files are read in pieces. Source files are never modified.
- **Efficiency:** only the audio is read. Measured: a 1.38 GB, 75 minute file converts in about 3 minutes.
- **User experience:** drop, wait, download. Honest progress and plain-English errors.
- **Scalability:** static hosting, so visitor count is not a concern. Per-file ceiling is about 2 GB by design.

## 9. Constraints
- Hosting: Netlify project `yavd-mp3-converter`. Budget $0.
- Engine: Mediabunny (reads the MP4 in pieces, browser decodes the audio) plus its LAME MP3 encoder. Chosen over browser ffmpeg, which loads whole files into memory and carries GPL terms.

## 10. Out of scope
Server-side conversion, accounts, history, files over about 2 GB, video output, copy-protected files.

## 11. Open items
- Proxy rule on the main youravdept.com site so the app appears at /mp3-converter (needs that site's repo).
- GitHub push (Claude's GitHub access to this repo is not connected).

## 12. Success criteria
Met on 2026-10-11. See `ai/CONTEXT.md` for the pasted test output.
