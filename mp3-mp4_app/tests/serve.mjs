// Local test server: serves public/ with the same security headers netlify.toml sets in production,
// and stubs the usage counter. Usage: node tests/serve.mjs [port]
import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'public');
const toml = readFileSync(path.join(root, '..', 'netlify.toml'), 'utf8');
const csp = toml.match(/Content-Security-Policy = "([^"]+)"/)[1];
const types = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css',
  '.png': 'image/png', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json', '.txt': 'text/plain' };
export const counted = [];

export function start(port = 8080) {
  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://x');
    if (url.pathname === '/api/count') { counted.push(url.searchParams.get('e')); res.writeHead(204).end(); return; }
    let file = path.normalize(path.join(root, decodeURIComponent(url.pathname)));
    if (!file.startsWith(root)) { res.writeHead(403).end(); return; }
    if (url.pathname.endsWith('/')) file = path.join(file, 'index.html');
    try {
      const body = await readFile(file);
      res.writeHead(200, { 'content-type': types[path.extname(file)] || 'application/octet-stream',
        'content-security-policy': csp, 'cache-control': 'no-cache' }).end(body);
    } catch { res.writeHead(404).end('Not found'); }
  });
  return new Promise((resolve) => server.listen(port, () => resolve(server)));
}
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const port = Number(process.argv[2] || 8080);
  await start(port); console.log(`http://localhost:${port}/`);
}
