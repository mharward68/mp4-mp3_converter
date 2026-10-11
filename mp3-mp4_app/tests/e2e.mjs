// End-to-end check in a real browser. Usage:
//   node tests/e2e.mjs <dir with test media> [path to chrome]
// Expects in the media dir: small.mp4 (has audio), noaudio.mp4, and optionally big.mp4 (1 GB+).
import { chromium } from 'playwright-core';
import { execFileSync } from 'node:child_process';
import { existsSync, statSync, writeFileSync, mkdtempSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { start, counted } from './serve.mjs';

const media = process.argv[2];
const exe = process.argv[3] || process.env.CHROME_PATH;
const server = await start(8090);
const browser = await chromium.launch({ executablePath: exe, args: ['--enable-precise-memory-info'] });
const context = await browser.newContext({ acceptDownloads: true });
const page = await context.newPage();
const problems = [];
page.on('console', (m) => { if (m.type() === 'error') problems.push('console: ' + m.text()); });
page.on('pageerror', (e) => problems.push('pageerror: ' + e.message));
const external = [];
page.on('request', (r) => { if (!r.url().startsWith('http://localhost:8090/') && !r.url().startsWith('blob:')) external.push(r.url()); });

let failed = 0;
const check = (name, ok, detail = '') => { console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}${detail ? '  (' + detail + ')' : ''}`); if (!ok) failed++; };
const state = () => page.evaluate(() => window.__state());
const waitIdle = (ms) => page.waitForFunction(() => window.__state().every((i) => i.status !== 'waiting' && i.status !== 'converting'), null, { timeout: ms, polling: 500 });

await page.goto('http://localhost:8090/convert.html');
check('page loads with drop zone enabled', await page.locator('#dropzone').isEnabled());
check('empty note shows', await page.locator('#empty-note').isVisible());

const tmp = mkdtempSync(path.join(os.tmpdir(), 'e2e-'));
const notMp4 = path.join(tmp, 'Venue Walkthrough.mov'); writeFileSync(notMp4, 'x');
const broken = path.join(tmp, 'broken.mp4'); writeFileSync(broken, Buffer.alloc(5000, 7));

// Mixed batch: good file, wrong type, no audio, damaged file. One bad file must not stop the rest.
await page.setInputFiles('#picker', [path.join(media, 'small.mp4'), notMp4, path.join(media, 'noaudio.mp4'), broken]);
await waitIdle(120000);
let s = await state();
const by = (n) => s.find((i) => i.name === n);
check('good file converts', by('small.mp4').status === 'done' && by('small.mp4').outName === 'small.mp3', JSON.stringify(by('small.mp4').outSize));
check('non-MP4 is skipped with a reason', by('Venue Walkthrough.mov').status === 'skipped' && /Not an MP4/.test(by('Venue Walkthrough.mov').error));
check('no-audio file fails with a reason', by('noaudio.mp4').status === 'failed' && /no audio track/.test(by('noaudio.mp4').error), by('noaudio.mp4').error);
check('damaged file fails with a reason', by('broken.mp4').status === 'failed', by('broken.mp4').error);
check('summary line', (await page.locator('#summary').textContent()).startsWith('1 of 3 converted, 2 failed'), await page.locator('#summary').textContent());

// Download and inspect the MP3 with ffprobe.
const [dl] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Download small.mp3' }).click()]);
const out = path.join(tmp, dl.suggestedFilename()); await dl.saveAs(out);
const probe = JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-show_format', '-show_streams', '-of', 'json', out]).toString());
const a = probe.streams[0];
check('download is a real MP3', a.codec_name === 'mp3', `${a.codec_name} ${a.channels}ch ${a.sample_rate}Hz`);
check('bitrate is 192 kbps', Math.abs(Number(a.bit_rate) - 192000) < 2000, a.bit_rate);
check('duration matches the source (20 s)', Math.abs(Number(probe.format.duration) - 20) < 0.3, probe.format.duration);

// Same name twice must not overwrite.
await page.setInputFiles('#picker', [path.join(media, 'small.mp4')]);
await waitIdle(120000);
s = await state();
check('duplicate gets a numbered name', s.some((i) => i.outName === 'small (2).mp3'));
await page.getByRole('button', { name: 'Clear finished' }).click();
check('clear finished empties the list', (await state()).length === 0);

// Cancel mid-conversion, with a second file waiting behind it.
const big = path.join(media, 'big.mp4');
if (existsSync(big)) {
  await page.setInputFiles('#picker', [big, path.join(media, 'small.mp4')]);
  await page.waitForFunction(() => window.__state()[0]?.progress > 0.02, null, { timeout: 120000 });
  await page.getByRole('button', { name: 'Cancel big.mp4' }).click();
  await waitIdle(120000);
  s = await state();
  check('cancel removes the active file and the queue carries on', s.length === 1 && s[0].status === 'done', JSON.stringify(s.map((i) => [i.name, i.status])));
  await page.getByRole('button', { name: 'Clear finished' }).click();

  // The large-file run: time it and watch memory.
  const sizeGb = (statSync(big).size / 1024 ** 3).toFixed(2);
  const t0 = Date.now();
  let peak = 0;
  const poll = setInterval(async () => { try { const m = await page.evaluate(() => performance.memory.usedJSHeapSize); peak = Math.max(peak, m); } catch {} }, 2000);
  await page.setInputFiles('#picker', [big]);
  await waitIdle(30 * 60000);
  clearInterval(poll);
  const secs = ((Date.now() - t0) / 1000).toFixed(0);
  s = await state();
  check(`large file (${sizeGb} GB) converts`, s[0].status === 'done', `${secs} s, MP3 ${(s[0].outSize / 1024 ** 2).toFixed(0)} MB, peak JS heap ${(peak / 1024 ** 2).toFixed(0)} MB, error: ${s[0].error}`);
  if (s[0].status === 'done') {
    const [d2] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Download big.mp3' }).click()]);
    const o2 = path.join(tmp, 'big.mp3'); await d2.saveAs(o2);
    const p2 = JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-show_format', '-of', 'json', o2]).toString());
    const src = JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-show_format', '-of', 'json', big]).toString());
    check('large MP3 duration matches source', Math.abs(Number(p2.format.duration) - Number(src.format.duration)) < 1, `${p2.format.duration} vs ${src.format.duration}`);
  }
} else {
  console.log('SKIP  large-file checks (no big.mp4)');
}

check('no requests left the page origin', external.length === 0, external.join(', '));
check('conversions were counted, and only an event name was sent', counted.filter((e) => e === 'convert').length >= 2, counted.join(','));
check('no console or page errors', problems.length === 0, problems.join(' | '));

// Landing page and offline.
await page.goto('http://localhost:8090/');
check('landing page renders', await page.getByRole('heading', { level: 1 }).isVisible());
await page.evaluate(() => navigator.serviceWorker.ready);
await page.waitForFunction(() => caches.keys().then((k) => k.length > 0));
await page.waitForTimeout(1500);
await context.setOffline(true);
await page.goto('http://localhost:8090/convert.html');
check('converter opens offline', await page.locator('#dropzone').isVisible());
await page.setInputFiles('#picker', [path.join(media, 'small.mp4')]);
await waitIdle(120000);
check('converts while offline', (await state())[0].status === 'done');

await browser.close(); server.close();
console.log(failed ? `\n${failed} check(s) FAILED` : '\nAll checks passed');
process.exit(failed ? 1 : 0);
