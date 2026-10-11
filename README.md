# MP4 to MP3 Converter by Your AV Department

A free, installable web app that converts MP4 recordings to MP3 on the user's own computer. Nothing uploads.

- Live: https://youravdept.com/mp3-converter/ (part of the main website; this repo is the source)
- App code: `mp3-mp4_app/` (static site in `public/`, usage counter in `netlify/functions/`)
- Project docs: `ai/` (start with `ai/CONTEXT.md`)

## Run and test

```powershell
cd C:\01_AppDevelopment\19_mp4-mp3_converter\mp3-mp4_app
npm install
npm test
npm run serve
```

Then open http://localhost:8080/mp3-converter/ in Chrome or Edge.
