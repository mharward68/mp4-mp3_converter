# DIRECTIVES: how to decide
Edited by Michael, deliberately.

## 0. Parameters
| Parameter | Value | Why |
|---|---|---|
| Scale horizon | Hundreds to low thousands of planners in year one | Promo giveaway. Static hosting makes the number irrelevant to cost |
| Data sensitivity | Users' recordings (member and speaker content). Never leaves their machine. Stored: anonymous event tallies only | The privacy promise is the product |
| UX tier | Polished | Public and branded |
| Accessibility | WCAG 2.1 AA for the two pages | Public page |
| Platforms | Chrome and Edge, Windows and Mac, installable | Michael's choice: installable web app only |
| Telemetry | Own anonymous counter (visit, install, convert). No third-party analytics | Simple to monitor, keeps the privacy promise |
| Recovery | Nothing to back up for users. Code is in Git. Tallies are disposable | No user data stored |
| Compliance | None. No personal data collected | The counter stores no identifiers |

## 1. Gates (all must hold)
1. **No file data leaves the device.** The content security policy stays `connect-src 'self'`, and the only network call the app makes is the counter with an event name. Load-bearing today.
2. **No third-party code at run time.** Every script, font and image is served from the app's own address. Load-bearing today.
3. **The counter never stores anything about a person or a file.** Event name and date only. Load-bearing today.
4. **One bad file never stops a batch.** Load-bearing today.
5. **Source files are never modified or deleted.** Load-bearing today.
6. **Brand:** Your AV Department only. No Onyva elements. No em dashes in copy.
7. **Secrets never in the repo.** JUST_THE_AUDIO_STATS_KEY lives in Netlify only.
8. **The strict content security policy stays on /just-the-audio/app/* and is never widened** to the landing page or the rest of the site, which rely on inline code.

## 2. Ladder
Stability > User experience > Efficiency > Scalability > Simplicity.

## 3. Hard limits (stop and ask)
- Any new network destination, or any change to the content security policy.
- Any change to what the counter records.
- Any new dependency or framework, or a version change to the vendored libraries.
- Any change to the stats key or how the stats page is protected.
- Any change to public copy that describes how Your AV Department is paid.
- Changing anything on the main youravdept.com site.
- Releasing without bumping VERSION in `public/sw.js` (installed copies would keep old files).

## 4. Procedure
Gates eliminate first. Then the ladder decides at the first rung where options differ. Still tied: take the simplest and log it in DECISIONS.
