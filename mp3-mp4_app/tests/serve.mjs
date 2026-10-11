// Local test server: serves public/ with the same security headers netlify.toml sets in production,
// and stubs the usage counter. Usage: node tests/serve.mjs [port]
import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'public');
// The same policy the website's netlify.toml sets for /mp3-converter/app/* (kept in site-functions/netlify-snippet.toml).
const toml = readFileSync(path.join(root, '..', 'site-functions', 'netlify-snippet.toml'), 'utf8');
const csp = toml.match(/Content-Security-Policy = "([^"]+)"/)[1];
const BASE = '/mp3-converter';
const types = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css',
  '.png': 'image/png', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json', '.txt': 'text/plain', '.webp': 'image/webp' };
export const counted = [];

export function start(port = 8080) {
  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://x');
    if (url.pathname === '/api/mp3-converter/count') { counted.push(url.searchParams.get('e')); res.writeHead(204).end(); return; }
    if (!url.pathname.startsWith(BASE + '/')) { res.writeHead(url.pathname === BASE ? 301 : 404, url.pathname === BASE ? { location: BASE + '/' } : {}).end(); return; }
    let file = path.normalize(path.join(root, decodeURIComponent(url.pathname.slice(BASE.length))));
    if (!file.startsWith(root)) { res.writeHead(403).end(); return; }
    if (url.pathname.endsWith('/')) file = path.join(file, 'index.html');
    try {
      const body = await readFile(file);
      const headers = { 'content-type': types[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-cache' };
      if (url.pathname.startsWith(BASE + '/app/')) headers['content-security-policy'] = csp;   // the landing page uses the site's inline styles
      res.writeHead(200, headers).end(body);
    } catch { res.writeHead(404).end('Not found'); }
  });
  return new Promise((resolve) => server.listen(port, () => resolve(server)));
}
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const port = Number(process.argv[2] || 8080);
  await start(port); console.log(`http://localhost:${port}/mp3-converter/`);
}
