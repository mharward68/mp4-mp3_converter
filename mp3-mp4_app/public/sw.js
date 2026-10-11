// Offline support. Bump VERSION on every release so installed copies pick up the new files.
const VERSION = 'v1.0.0';
const CACHE = 'mp4-mp3-' + VERSION;
const FILES = [
  './', 'index.html', 'convert.html', 'licenses.html', 'manifest.webmanifest',
  'css/styles.css',
  'js/app.js', 'js/queue.js', 'js/engine.js', 'js/count.js', 'js/install.js',
  'vendor/mediabunny.min.mjs', 'vendor/mediabunny-mp3-encoder.min.mjs', 'vendor/LICENSE-mediabunny.txt',
  'fonts/montserrat-latin-700-normal.woff2', 'fonts/open-sans-latin-400-normal.woff2', 'fonts/open-sans-latin-600-normal.woff2',
  'img/logo.png', 'img/icon-192.png', 'img/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('mp4-mp3-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== location.origin || url.pathname.includes('/api/')) return;
  event.respondWith(
    caches.match(event.request, { ignoreSearch: true }).then((hit) => hit || fetch(event.request)),
  );
});
