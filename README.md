# Just the Audio by Your AV Department

(Formerly "MP4 to MP3 Converter". The folder and repo names still carry the old name.)

A free, installable web app that converts MP4, MOV and M4A recordings to MP3 on the user's own computer. Nothing uploads.

- Live: https://youravdept.com/just-the-audio/ (part of the main website; this repo is the source)
- App code: `mp3-mp4_app/` (static site in `public/`, usage counter in `netlify/functions/`)
- Project docs: `ai/` (start with `ai/CONTEXT.md`)

## Run and test

```powershell
cd C:\01_AppDevelopment\19_mp4-mp3_converter\mp3-mp4_app
npm install
npm test
npm run serve
```

Then open http://localhost:8080/just-the-audio/ in Chrome or Edge.
