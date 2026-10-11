import { count, registerServiceWorker } from './count.js';

const installBtn = document.getElementById('install');
const note = document.getElementById('install-note');
const openApp = document.getElementById('open-app');
let promptEvent = null;

const standalone = window.matchMedia('(display-mode: standalone)').matches;
const canRun = typeof AudioDecoder === 'function';

if (standalone) {
  location.replace('convert.html');
} else if (!canRun) {
  note.textContent = 'This tool needs Google Chrome or Microsoft Edge on a Windows or Mac computer. Open this page there to install it.';
  openApp.hidden = true;
} else {
  note.textContent = 'No account. No email. No cost. To install, open this page in Chrome or Edge on a computer.';
}

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  promptEvent = e;
  installBtn.hidden = false;
  note.textContent = 'No account. No email. No cost. Installs in a few seconds.';
});
installBtn.addEventListener('click', async () => {
  if (!promptEvent) return;
  promptEvent.prompt();
  await promptEvent.userChoice;
  promptEvent = null;
  installBtn.hidden = true;
});
window.addEventListener('appinstalled', () => {
  count('install');
  installBtn.hidden = true;
  note.textContent = 'Installed. Look for "MP4 to MP3" in your apps, or open it from here.';
});

count('visit');
registerServiceWorker();
