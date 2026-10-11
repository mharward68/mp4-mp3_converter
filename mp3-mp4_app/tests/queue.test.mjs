import test from 'node:test';
import assert from 'node:assert/strict';
import {
  STATUS, rejectReason, mp3Name, uniqueName, formatBytes, formatRemaining, makeItem, summarize, nextWaiting, MAX_BYTES,
} from '../public/app/js/queue.js';

const f = (name, size = 1000, type = '') => ({ name, size, type });

test('accepts mp4, rejects everything else in plain English', () => {
  assert.equal(rejectReason(f('Keynote.mp4')), null);
  assert.equal(rejectReason(f('KEYNOTE.MP4')), null);
  assert.equal(rejectReason(f('clip', 10, 'video/mp4')), null);
  assert.match(rejectReason(f('Walkthrough.mov')), /Not an MP4/);
  assert.match(rejectReason(f('notes.mp4.txt')), /Not an MP4/);
  assert.match(rejectReason(f('empty.mp4', 0)), /empty/);
  assert.match(rejectReason(f('huge.mp4', MAX_BYTES + 1)), /over 2 GB/);
});

test('mp3 names keep the original name and stay legal on Windows', () => {
  assert.equal(mp3Name('Opening Keynote.mp4'), 'Opening Keynote.mp3');
  assert.equal(mp3Name('a.b.c.MP4'), 'a.b.c.mp3');
  assert.equal(mp3Name('Q&A: Day 2?.mp4'), 'Q&A_ Day 2_.mp3');
  assert.equal(mp3Name('.mp4'), 'audio.mp3');
});

test('duplicate names get a number, not an overwrite', () => {
  const taken = new Set(['a.mp3', 'a (2).mp3']);
  assert.equal(uniqueName('b.mp3', taken), 'b.mp3');
  assert.equal(uniqueName('A.mp3', taken), 'A (3).mp3');
});

test('sizes and time read naturally', () => {
  assert.equal(formatBytes(1464900997), '1.4 GB');
  assert.equal(formatBytes(82 * 1024 * 1024), '82 MB');
  assert.equal(formatRemaining(20), 'less than a minute left');
  assert.equal(formatRemaining(60), 'about 1 minute left');
  assert.equal(formatRemaining(240), 'about 4 minutes left');
});

test('summary counts the batch and ignores skipped files', () => {
  const items = [f('a.mp4', 100), f('b.mp4', 100), f('c.mov', 100), f('d.mp4', 200)].map(makeItem);
  assert.equal(items[2].status, STATUS.SKIPPED);
  items[0].status = STATUS.DONE;
  items[1].status = STATUS.CONVERTING; items[1].progress = 0.5;
  const s = summarize(items);
  assert.deepEqual([s.total, s.done, s.waiting, s.busy], [3, 1, 1, true]);
  assert.equal(s.fraction, 150 / 400);
  assert.equal(nextWaiting(items), items[3]);
  items[1].status = STATUS.FAILED; items[3].status = STATUS.DONE;
  assert.equal(summarize(items).busy, false);
  assert.equal(summarize(items).fraction, 1);
});
