"""Builds public/index.html (the landing page) from a youravdept.com library page, so the header,
footer, styles, site map and scripts are the site's own. Re-run after the site's template changes.

Usage: python tools/build-landing.py "C:\\01_AppDevelopment\\12.Your-AV-Dept_Website\\library\\av365.html"
"""
import re, sys, pathlib

template = pathlib.Path(sys.argv[1]).read_text(encoding="utf8")
out = pathlib.Path(__file__).resolve().parent.parent / "public" / "index.html"

TITLE = "Free MP4 to MP3 Converter | Your AV Department"
DESC = ("Turn session recordings into MP3 audio on your own computer. Free, no account, nothing uploaded. "
        "A free tool for meeting and event professionals from Your AV Department.")
URL = "https://www.youravdept.com/mp3-converter/"
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>'

def sub1(pattern, repl, text):
    new, n = re.subn(pattern, lambda m: repl, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"Template changed: could not find {pattern!r}")
    return new

html = template
html = sub1(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
html = sub1(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', html)
html = sub1(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{URL}">\n<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#152B4A">', html)
html = sub1(r'<meta property="og:type" content="[^"]*">', '<meta property="og:type" content="website">', html)
html = sub1(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{TITLE}">', html)
html = sub1(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Turn session recordings into MP3 audio on your own computer. Free, no account, nothing uploaded.">', html)
html = sub1(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{URL}">', html)

logo = re.search(r'<img class="lm-logo[^>]*src="([^"]+)"', html).group(1)

MAIN = f'''  <section class="lm-hero">
    <div class="container">
      <div class="lm-grid">

        <div class="lm-copy">
          <img class="lm-logo pop-in reveal" src="{logo}" alt="Your AV Department logo">
          <span class="eyebrow reveal is-visible">A Free Tool for Meeting and Event Professionals</span>
          <h1 class="reveal is-visible">MP4 to MP3 Converter</h1>
          <p class="lead reveal is-visible">Turn your session recordings into MP3 audio. Drop in the video files and get an MP3 of each one.</p>
          <p class="lead reveal is-visible" style="margin-top:14px;">Nothing uploads. The conversion runs on your own computer, so speaker and member content stays with you.</p>
          <ul class="lm-checks reveal">
            <li>{CHECK}<span><b>A whole conference at once.</b> Drag in as many recordings as you have. Each one becomes its own MP3 with the same file name.</span></li>
            <li>{CHECK}<span><b>Private by design.</b> No upload, no account, and no email address required.</span></li>
            <li>{CHECK}<span><b>Works offline once installed.</b> It opens like any other app on your computer, no internet needed.</span></li>
          </ul>
          <span class="byline reveal">From Michael Harward, Founder, Your AV Department</span>
        </div>

        <div class="lm-cardwrap reveal">
          <div class="lm-card">
            <h2>Get the free converter</h2>
            <p class="lm-card-sub">Installs in a few seconds. No sign-up.</p>
            <div style="display:flex; flex-direction:column; gap:12px;">
              <button type="button" class="btn btn-primary" id="mp3Install" style="display:none;">Install the Free Converter</button>
              <a href="app/" class="btn btn-primary" id="mp3Open">Use It in Your Browser</a>
              <p class="form-note" id="mp3Note">To install it as an app, open this page in Chrome or Edge on a Windows or Mac computer.</p>
              <p class="form-note">Handles recordings up to about 2 GB each. Saves standard 192 kbps MP3 files.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <section class="section" style="background:linear-gradient(180deg,#ffffff 0%, #f3fbfa 100%); padding-top:20px;">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How It Works</span>
        <h2>Drop, wait, download</h2>
        <p>There are no settings to learn. If you can drag a file, you can use it.</p>
      </div>

      <div class="lever-grid">
        <div class="lever-card is-yours reveal">
          <div class="lever-num">01</div>
          <div class="lever-body">
            <h3>Drop in your recordings <span class="lever-tag">As many as you like</span></h3>
            <p>Drag your MP4 files onto the page, or click to browse. Add more any time, even while a batch is running. Files convert one at a time, in order.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num">02</div>
          <div class="lever-body">
            <h3>Watch the progress</h3>
            <p>Each file shows how far along it is and about how long is left. If a file has a problem, it tells you why in plain language and the rest of the batch carries on.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num">03</div>
          <div class="lever-body">
            <h3>Save your MP3s</h3>
            <p>Download them one by one or all at once. Or pick a folder first, and every finished MP3 lands there on its own.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="article-copy">
        <div class="section-head reveal" style="text-align:left; margin:0 0 24px;">
          <span class="eyebrow">What Planners Use It For</span>
        </div>
        <ul class="check-list">
          <li>{CHECK}<span>Posting session audio for members who could not attend.</span></li>
          <li>{CHECK}<span>Sending recordings out for transcripts or captions.</span></li>
          <li>{CHECK}<span>Turning a large video file into audio that is a fraction of the size.</span></li>
        </ul>
        <div class="pull-quote">
          <p>Your recordings never leave your computer. There is no upload, so there is nothing for anyone else to see.</p>
        </div>
        <p>Most free converters online work by sending your file to someone else's server. That is a strange thing to do with a keynote your speaker has not released, or a members-only session. This one does the work on your own machine.</p>
        <p>We count how many people visit, install and convert, so we know if the tool is useful. We never see your files, their names or their contents.</p>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="getconverter">
    <div class="container">
      <div class="section-head reveal" style="margin-bottom:30px;">
        <span class="eyebrow">Why Is It Free?</span>
        <h2>The same reason our service is</h2>
        <p>We built it for our own recordings and figured planners could use it too.</p>
      </div>

      <div class="author-card reveal">
        <div class="rule"></div>
        <h3>No cost to the planner. We say so up front.</h3>
        <p>Your AV Department is independent AV production sourcing and advocacy for association and corporate meeting planners. We scope your show, bid it to production partners, negotiate, and stay with you through load-out. We are paid by the production partner you choose.</p>
        <div class="author-meta">
          <b>Michael Harward</b> <span>&middot; Your AV Department</span><br>
          <a href="mailto:michaelh@youravdept.com">michaelh@youravdept.com</a> <span>&middot;</span> <a href="../how-we-get-paid.html">How we get paid</a> <span>&middot;</span> <a href="https://www.youravdept.com/">youravdept.com</a>
        </div>
      </div>

      <div style="text-align:center; margin-top:36px;">
        <a href="app/" class="btn btn-primary reveal">Open the Converter</a>
      </div>
      <a href="../library/index.html" class="article-back-link reveal">&larr; More free resources in the Library</a>
    </div>
  </section>

'''
start = html.index('  <section class="lm-hero">')
end = html.index("<footer>")
html = html[:start] + MAIN + "\n" + html[end:]

# Site map: this page sits in its own folder, so the library's own links need a prefix.
for name in ("12-av-concessions.html", "av365.html", "the-levers-of-labor.html", "index.html"):
    html = html.replace(f'<li><a href="{name}">', f'<li><a href="../library/{name}">')
if "../mp3-converter/index.html" in html:      # template already lists this page: point the link at itself
    html = html.replace('<li><a href="../mp3-converter/index.html">', '<li><a href="index.html">')
else:
    html = sub1(r'(<li><a href="\.\./michaelh\.html">[^\n]*</li>\n)',
                '      <li><a href="../michaelh.html">Michael Harward &mdash; Digital Card</a></li>\n      <li><a href="index.html">MP4 to MP3 Converter: Free Tool</a></li>\n', html)

SCRIPT = r'''<script>
// MP4 to MP3 Converter: install button, usage count, offline support.
(function(){
  var btn = document.getElementById('mp3Install');
  var note = document.getElementById('mp3Note');
  var open = document.getElementById('mp3Open');
  var promptEvent = null;
  function count(e){
    try {
      var url = '/api/mp3-converter/count?e=' + e;
      if (!(navigator.sendBeacon && navigator.sendBeacon(url))) fetch(url, { method:'POST', keepalive:true }).catch(function(){});
    } catch (err) {}
  }
  if (typeof AudioDecoder !== 'function'){
    note.textContent = 'This tool needs Google Chrome or Microsoft Edge on a Windows or Mac computer. Open this page there to use it.';
    open.style.display = 'none';
  }
  window.addEventListener('beforeinstallprompt', function(e){
    e.preventDefault();
    promptEvent = e;
    btn.style.display = '';
    open.className = 'btn btn-ghost';
    note.textContent = 'Or use it right here in your browser, no install needed.';
  });
  btn.addEventListener('click', function(){
    if (!promptEvent) return;
    promptEvent.prompt();
    promptEvent.userChoice.then(function(){ promptEvent = null; btn.style.display = 'none'; open.className = 'btn btn-primary'; });
  });
  window.addEventListener('appinstalled', function(){
    count('install');
    btn.style.display = 'none';
    open.className = 'btn btn-primary';
    note.textContent = 'Installed. Look for "MP4 to MP3" in your apps, or open it from here.';
  });
  count('visit');
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('/mp3-converter/sw.js', { scope:'/mp3-converter/' }).catch(function(){});
})();
</script>
'''
html = html.replace("</body>", SCRIPT + "</body>", 1)

# Guard: every relative link must point somewhere that exists from /mp3-converter/.
bad = sorted(set(h for h in re.findall(r'href="([^"]+)"', html)
                 if not re.match(r"(\.\./|https?:|mailto:|tel:|#|data:|app/|index\.html$|manifest\.webmanifest$)", h)))
if bad:
    raise SystemExit(f"Links that would break from /mp3-converter/: {bad}")
out.write_text(html, encoding="utf8", newline="\n")
print(f"Wrote {out} ({len(html):,} characters)")
