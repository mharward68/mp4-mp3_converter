"""Builds public/index.html (the landing page) from a youravdept.com library page, so the header,
footer, styles, site map and scripts are the site's own. Re-run after the site's template changes.

Usage: python tools/build-landing.py "C:\\01_AppDevelopment\\12.Your-AV-Dept_Website\\library\\av365.html"
"""
import re, sys, pathlib

template = pathlib.Path(sys.argv[1]).read_text(encoding="utf8")
out = pathlib.Path(__file__).resolve().parent.parent / "public" / "index.html"

TITLE = "Just the Audio: Turn MP4, MOV and M4A Files into MP3 | Your AV Department"
DESC = ("You have the video. You need just the audio. A free tool that turns MP4, MOV and M4A files into MP3s "
        "on your own computer. No upload, no account.")
URL = "https://www.youravdept.com/just-the-audio/"
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
html = sub1(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="You have the video. You need just the audio. Free, no upload, no account.">', html)
html = sub1(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{URL}">', html)

logo = re.search(r'<img class="lm-logo[^>]*src="([^"]+)"', html).group(1)

MAIN = f'''  <section class="lm-hero">
    <div class="container">
      <div class="lm-grid">

        <div class="lm-copy">
          <img class="lm-logo pop-in reveal" src="{logo}" alt="Your AV Department logo">
          <span class="eyebrow reveal is-visible">A Free Tool from Your AV Department</span>
          <h1 class="reveal is-visible">Just the Audio</h1>
          <p class="lead reveal is-visible">You have the video. You need just the audio. Drop in a video file or a voice memo and get an MP3 back.</p>
          <p class="lead reveal is-visible" style="margin-top:14px;">Nothing uploads. The work happens on your own computer, so the file stays with you.</p>
          <ul class="lm-checks reveal">
            <li>{CHECK}<span><b>One file or several.</b> Drop in what you have. Each file becomes its own MP3 with the same name.</span></li>
            <li>{CHECK}<span><b>Private by design.</b> No upload, no account, and no email address required.</span></li>
            <li>{CHECK}<span><b>Works offline once installed.</b> It opens like any other app on your computer, no internet needed.</span></li>
          </ul>
          <span class="byline reveal">From Michael Harward, Founder, Your AV Department</span>
        </div>

        <div class="lm-cardwrap reveal">
          <div class="lm-card">
            <h2>Get Just the Audio</h2>
            <p class="lm-card-sub">Installs in a few seconds. No sign-up.</p>
            <div style="display:flex; flex-direction:column; gap:12px;">
              <button type="button" class="btn btn-primary" id="jtaInstall" style="display:none;">Install Just the Audio</button>
              <a href="app/" class="btn btn-primary" id="jtaOpen">Use It in Your Browser</a>
              <p class="form-note" id="jtaNote">To install it as an app, open this page in Chrome or Edge on a Windows or Mac computer.</p>
              <p class="form-note">Handles files up to about 2 GB each. Saves standard 192 kbps MP3 files.</p>
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
            <h3>Drop in your files</h3>
            <p>Drag an MP4, MOV or M4A file onto the page, or click to browse. One file is fine. If you add several, they convert one at a time, in order.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num">02</div>
          <div class="lever-body">
            <h3>Watch the progress</h3>
            <p>Each file shows how far along it is and about how long is left. If a file has a problem, it tells you why in plain language and carries on with the rest.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num">03</div>
          <div class="lever-body">
            <h3>Save your MP3</h3>
            <p>Download each one, or all of them at once. Or pick a folder first, and every finished MP3 lands there on its own.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="formats">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What It Converts</span>
        <h2>Three kinds of file in, MP3 out</h2>
        <p>If you are not sure what you have, look at the last few letters of the file name.</p>
      </div>

      <div class="lever-grid">
        <div class="lever-card reveal">
          <div class="lever-num" style="width:auto; padding:0 10px;">MP4</div>
          <div class="lever-body">
            <h3>MP4 video <span class="lever-tag">Most common</span></h3>
            <p>The standard video file. It is what Zoom, Teams and Webex save, what most phones and cameras can produce, and what an AV company usually hands over after a show. File names end in .mp4 or .m4v.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num" style="width:auto; padding:0 10px;">MOV</div>
          <div class="lever-body">
            <h3>MOV video</h3>
            <p>Apple's video file. It comes from an iPhone or iPad camera, from screen recordings on a Mac, and from some professional cameras. File names end in .mov.</p>
          </div>
        </div>

        <div class="lever-card reveal">
          <div class="lever-num" style="width:auto; padding:0 10px;">M4A</div>
          <div class="lever-body">
            <h3>M4A audio</h3>
            <p>An audio file with no picture. Phone voice memos use it, and Zoom saves one next to its video when you record to your computer. Some websites and older players will not accept it, which is why you would want an MP3. File names end in .m4a.</p>
          </div>
        </div>

        <div class="lever-card is-yours reveal">
          <div class="lever-num" style="width:auto; padding:0 10px;">MP3</div>
          <div class="lever-body">
            <h3>What you get back <span class="lever-tag">Plays everywhere</span></h3>
            <p>One MP3 for each file you drop in, with the same name. MP3 is the audio format every phone, computer, website and podcast service accepts. Files are saved at 192 kbps, a standard quality that suits both speech and music, and come out at a small fraction of the size of a video.</p>
          </div>
        </div>
      </div>

      <div class="article-copy" style="margin-top:36px;">
        <p><b>What it will not take:</b> other file types such as WAV, WMV or AVI, files larger than about 2 GB, and copy-protected video. If a file cannot be converted, the tool says why.</p>
      </div>
    </div>
  </section>

  <section class="section" style="background:linear-gradient(180deg,#ffffff 0%, #f3fbfa 100%);">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What People Use It For</span>
        <h2>Any time the picture is in the way</h2>
      </div>
      <div class="article-copy">
        <p><b>Everyday files</b></p>
        <ul class="check-list">
          <li>{CHECK}<span><b>A meeting you'd rather listen to.</b> Turn a Zoom or Teams recording into audio for the drive or the walk.</span></li>
          <li>{CHECK}<span><b>A voice memo nobody can open.</b> Phone memos save as M4A, which some systems reject. An MP3 opens anywhere.</span></li>
          <li>{CHECK}<span><b>A file too big to send.</b> The video will not attach to an email. The audio usually will.</span></li>
          <li>{CHECK}<span><b>A recording you want transcribed.</b> Most transcript services take audio, and a small file uploads much faster.</span></li>
        </ul>
        <p><b>Getting ready for a show</b></p>
        <ul class="check-list">
          <li>{CHECK}<span><b>A speaker's demo reel.</b> Listen to how they sound without sitting through the video.</span></li>
          <li>{CHECK}<span><b>Music that arrived as a video.</b> Your AV team asked for an audio file for walk-on music. Now you have one.</span></li>
          <li>{CHECK}<span><b>A recorded welcome or announcement.</b> Someone recorded it on a phone. The show needs just the sound.</span></li>
        </ul>
        <p><b>After an event</b></p>
        <ul class="check-list">
          <li>{CHECK}<span><b>Session audio for members.</b> Post a talk as something people can listen to.</span></li>
          <li>{CHECK}<span><b>A testimonial quote.</b> Pull the audio from an attendee clip when all you need is the words.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="article-copy">
        <div class="pull-quote">
          <p>Your files never leave your computer. There is no upload, so there is nothing for anyone else to see.</p>
        </div>
        <p>Many free converters online send your file to someone else's server, and plenty come with pop-up ads, extra downloads or worse. That is a poor trade for a board meeting, a speaker's unreleased talk, or anything else that was not meant to travel.</p>
        <p>This one does the work on your own device. No ads, no add-ons, nothing hiding in the download.</p>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="getit">
    <div class="container">
      <div class="section-head reveal" style="margin-bottom:30px;">
        <span class="eyebrow">Why Is It Free?</span>
        <h2>The same reason our service is</h2>
        <p>We built it because we kept needing it, and figured other people do too.</p>
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
        <a href="app/" class="btn btn-primary reveal">Open Just the Audio</a>
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
if "../just-the-audio/index.html" in html:      # template already lists this page: point the link at itself
    html = html.replace('<li><a href="../just-the-audio/index.html">', '<li><a href="index.html">')
else:                                            # alphabetical: after "How We Get Paid"
    html = sub1(r'(<li><a href="\.\./how-we-get-paid\.html">[^\n]*</li>\r?\n)',
                '      <li><a href="../how-we-get-paid.html">How We Get Paid</a></li>\n      <li><a href="index.html">Just the Audio: Free Tool</a></li>\n', html)

SCRIPT = r'''<script>
// Just the Audio: install button, usage count, offline support.
(function(){
  var btn = document.getElementById('jtaInstall');
  var note = document.getElementById('jtaNote');
  var open = document.getElementById('jtaOpen');
  var promptEvent = null;
  function count(e){
    try {
      var url = '/api/just-the-audio/count?e=' + e;
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
    note.textContent = 'Installed. Look for "Just the Audio" in your apps, or open it from here.';
  });
  count('visit');
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('/just-the-audio/sw.js', { scope:'/just-the-audio/' }).catch(function(){});
})();
</script>
'''
html = html.replace("</body>", SCRIPT + "</body>", 1)

# Guard: every relative link must point somewhere that exists from /just-the-audio/.
bad = sorted(set(h for h in re.findall(r'href="([^"]+)"', html)
                 if not re.match(r"(\.\./|https?:|mailto:|tel:|#|data:|app/|index\.html$|manifest\.webmanifest$)", h)))
if bad:
    raise SystemExit(f"Links that would break from /just-the-audio/: {bad}")
out.write_text(html, encoding="utf8", newline="\n")
print(f"Wrote {out} ({len(html):,} characters)")
