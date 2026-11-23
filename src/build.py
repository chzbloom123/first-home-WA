import re, html, sys, json, os
import markdown
from content_home import HOME_INTRO, HOME_SHORT, HOME_TIME, STEPS, HOME_OUTRO
from content_a import MONEY, LOANS, HELP
from content_b import TYPES, CONTRACT, INSPECTION
from content_c import FIRSTYEAR, TRICITIES, CHECKLIST, ABOUT, GLOSSARY_TERMS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REVIEWED = "November 23, 2026"

def md(t):
    h = markdown.markdown(t.strip(), extensions=["tables"])
    h = h.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a class="ext" href="\1"', h)
    return h

def esc(s): return html.escape(s, quote=True)

# ---------- glossary: plain definitions taken from the research report ----------
_g = json.load(open(os.path.join(HERE, "glossary.json"), encoding="utf-8"))
gloss = {k: (v["definition"], v["working_definition"]) for k, v in _g.items()}
missing = [t for t in GLOSSARY_TERMS if t not in gloss]
if missing: print("GLOSSARY MISSING:", missing)
gl_items = []
for t in sorted([t for t in GLOSSARY_TERMS if t in gloss], key=str.lower):
    d, starred = gloss[t]
    gl_items.append(f'<div class="term"><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>')
GLOSSARY_HTML = ('<p class="lead">Plain one-sentence meanings for the words you will hear. Type to filter the list.</p>'
  '<p><label for="gloss-filter">Filter terms</label> <input id="gloss-filter" type="search" autocomplete="off" placeholder="For example: escrow"></p>'
  '<p id="gloss-empty" hidden>No term matches. Try a shorter word.</p>'
  '<dl id="gloss-list">' + "".join(gl_items) + "</dl>")

# ---------- home ----------
def step_html(i, s):
    links = "".join(f'<li><a class="ext" href="{esc(u)}">{esc(t)}</a></li>' for t, u in s["links"])
    links = f'<ul class="steplinks">{links}</ul>' if links else ""
    return f'''<li class="step" id="{s["id"]}">
<h3><span class="num" aria-hidden="true">{i}</span>{esc(s["title"])}</h3>
<dl class="meta"><div><dt>Who</dt><dd>{esc(s["who"])}</dd></div><div><dt>Money that moves</dt><dd>{esc(s["money"])}</dd></div><div><dt>How long</dt><dd>{esc(s["time"])}</dd></div></dl>
{md(s["body"])}
<p class="deeper"><a href="#{s["deeper"][0]}">More on this: {esc(s["deeper"][1])}</a></p>
{links}
</li>'''

steps_nav = "".join(f'<li><a href="#{s["id"]}">{esc(s["title"])}</a></li>' for s in STEPS)
HOME_HTML = f'''
<div class="lead">{md(HOME_INTRO)}</div>
<ul class="promise"><li>No sign-up</li><li>No ads</li><li>No tracking</li><li>Not a lender, broker or inspector</li></ul>
<h2>The short version</h2>
{md(HOME_SHORT)}
<h2>How long it takes</h2>
{md(HOME_TIME)}
<h2>The eight steps</h2>
<ol class="jump">{steps_nav}</ol>
<ol class="steps">{"".join(step_html(i+1, s) for i, s in enumerate(STEPS))}</ol>
{md(HOME_OUTRO)}
<p><a href="#checklist">Open the checklist</a></p>
'''

# ---------- checklist ----------
cl = ['<p class="lead">Every step on one page. Your ticks are saved in this browser only.</p>']
for gi, (g, items) in enumerate(CHECKLIST):
    cl.append(f"<h2>{esc(g)}</h2><ul class=\"checks\">")
    for ii, it in enumerate(items):
        cid = f"chk-{gi}-{ii}"
        cl.append(f'<li><input type="checkbox" id="{cid}"><label for="{cid}">{esc(it)}</label></li>')
    cl.append("</ul>")
cl.append('<p><button type="button" id="chk-clear">Clear all ticks</button> <span id="chk-note" role="status"></span></p>')
CHECKLIST_HTML = "".join(cl)

VIEWS = [
 ("home", "Start", "Buying your first home in Washington, start to keys", HOME_HTML),
 ("money", "Money", "Money and costs", md(MONEY)),
 ("loans", "Loans", "Loan types", md(LOANS)),
 ("help", "Help", "Help and classes", md(HELP)),
 ("home-types", "Home types", "Home types: what changes", md(TYPES)),
 ("contract", "Contract", "Contract and closing", md(CONTRACT)),
 ("inspection", "Inspection", "Home inspections", md(INSPECTION)),
 ("first-year", "First year", "Insurance and your first year", md(FIRSTYEAR)),
 ("tri-cities", "Tri-Cities", "Tri-Cities resources", md(TRICITIES)),
 ("glossary", "Glossary", "Glossary", GLOSSARY_HTML),
 ("checklist", "Checklist", "Checklist", CHECKLIST_HTML),
 ("about", "About", "About this guide", md(ABOUT)),
]

nav = "".join(f'<li><a href="#{vid}" data-view="{vid}">{esc(label)}</a></li>' for vid, label, _, _ in VIEWS)
sections = []
for vid, label, title, body in VIEWS:
    back = "" if vid == "home" else '<p class="back"><a href="#home">Back to the eight steps</a></p>'
    sections.append(f'<section class="view" id="{vid}" aria-labelledby="{vid}-h"><h1 id="{vid}-h">{esc(title)}</h1>{body}{back}</section>')

CSS = r'''
:root{
  /* layout: one reading column; the home page is a numbered rail of eight steps */
  --paper:#f3f6f2; --surface:#ffffff; --ink:#1b2725; --muted:#566660; --accent:#1c5b47; --accent-soft:#dcebe3; --rule:#cdd7d1; --money:#734700; --money-soft:#f6ebcf;
  --display:"Bitter", Georgia, "Times New Roman", serif;
  --body:"Public Sans", "Segoe UI", Verdana, sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){ --paper:#111816; --surface:#19231f; --ink:#e5ece8; --muted:#a2b0aa; --accent:#80c9ab; --accent-soft:#1f372d; --rule:#2d3c36; --money:#eac67d; --money-soft:#382d15; color-scheme: dark; }
}
:root[data-theme="dark"]{ --paper:#111816; --surface:#19231f; --ink:#e5ece8; --muted:#a2b0aa; --accent:#80c9ab; --accent-soft:#1f372d; --rule:#2d3c36; --money:#eac67d; --money-soft:#382d15; color-scheme: dark; }
*{box-sizing:border-box}
html{font-size:112.5%;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.65}
a{color:var(--accent);text-underline-offset:.18em}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.wrap{max-width:44rem;margin:0 auto;padding:0 1.1rem}
header.site{background:var(--surface);border-bottom:1px solid var(--rule)}
header.site .wrap{display:flex;flex-direction:column;gap:.6rem;padding-top:1rem;padding-bottom:.8rem}
.brand{font-family:var(--display);font-weight:700;font-size:1.15rem;color:var(--ink);text-decoration:none}
.brand small{display:block;font-family:var(--body);font-weight:400;font-size:.8rem;color:var(--muted)}
nav ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:.3rem .35rem}
nav a{display:block;padding:.2rem .6rem;border:1px solid var(--rule);border-radius:999px;text-decoration:none;font-size:.85rem;color:var(--ink);background:var(--paper)}
nav a[aria-current="page"]{background:var(--accent);border-color:var(--accent);color:var(--surface)}
main{padding:1.6rem 0 2.5rem}
h1,h2,h3{font-family:var(--display);line-height:1.25;text-wrap:balance}
h1{font-size:1.75rem;margin:0 0 .8rem}
h2{font-size:1.25rem;margin:2.2rem 0 .6rem;padding-top:1rem;border-top:1px solid var(--rule)}
h3{font-size:1.08rem;margin:1.5rem 0 .4rem}
p,ul,ol,dl{margin:0 0 1rem}
ul,ol{padding-left:1.3rem}
li{margin-bottom:.35rem}
.lead{font-size:1.08rem}
.promise{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.4rem}
.promise li{margin:0;padding:.15rem .7rem;border-radius:999px;background:var(--accent-soft);font-size:.85rem}
.jump{columns:2;column-gap:2rem;font-size:.95rem}
.steps{list-style:none;padding:0;margin:1.5rem 0 1rem}
.step{position:relative;margin:0;padding:0 0 1.6rem 3.1rem;border-left:2px solid var(--rule);margin-left:1.05rem}
.step:last-child{border-left-color:transparent}
.step h3{margin:0 0 .6rem;font-size:1.2rem;padding-top:.15rem}
.num{position:absolute;left:-1.1rem;top:0;width:2.1rem;height:2.1rem;border-radius:50%;background:var(--accent);color:var(--surface);display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:700;font-size:1rem}
.meta{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.5rem;margin:0 0 .9rem}
.meta div{background:var(--surface);border:1px solid var(--rule);border-radius:6px;padding:.4rem .6rem}
.meta div:nth-child(2){background:var(--money-soft);border-color:transparent}
.meta div:nth-child(2) dt{color:var(--money)}
.meta dt{font-size:.72rem;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.meta dd{margin:0;font-size:.88rem;line-height:1.4}
.deeper{font-weight:700}
.steplinks{font-size:.92rem}
.tablewrap{overflow-x:auto;margin:0 0 1.1rem;border:1px solid var(--rule);border-radius:6px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}
th,td{text-align:left;vertical-align:top;padding:.5rem .65rem;border-bottom:1px solid var(--rule)}
tr:last-child td{border-bottom:0}
th{font-family:var(--body);font-weight:700;background:var(--accent-soft)}
td:first-child{font-weight:700;min-width:7.5rem}
#gloss-filter{font:inherit;padding:.35rem .6rem;border:1px solid var(--rule);border-radius:6px;background:var(--surface);color:var(--ink);width:min(100%,18rem)}
.term{padding:.6rem 0;border-bottom:1px solid var(--rule)}
.term dt{font-weight:700}
.term dd{margin:0}
.checks{list-style:none;padding:0}
.checks li{display:flex;gap:.6rem;align-items:flex-start;margin-bottom:.5rem}
.checks input{width:1.15rem;height:1.15rem;margin-top:.3rem;accent-color:var(--accent);flex:none}
.checks input:checked+label{color:var(--muted);text-decoration:line-through}
button{font:inherit;padding:.3rem .8rem;border:1px solid var(--accent);border-radius:6px;background:var(--surface);color:var(--accent);cursor:pointer}
.back{margin-top:2rem;padding-top:1rem;border-top:1px solid var(--rule)}
footer.site{border-top:1px solid var(--rule);background:var(--surface);font-size:.85rem;color:var(--muted)}
footer.site .wrap{padding-top:1rem;padding-bottom:1.5rem}
footer.site p{margin:0 0 .5rem}
@media (max-width:30rem){ .meta{grid-template-columns:1fr} .jump{columns:1} h1{font-size:1.5rem} .step{padding-left:2.2rem} }
@media (prefers-reduced-motion:no-preference){ html{scroll-behavior:smooth} }
@media print{ header.site nav,.back,#chk-clear,#gloss-filter,label[for="gloss-filter"]{display:none} body{background:#fff;color:#000} a{color:#000} .tablewrap{overflow:visible} }
'''

JS = r'''
(function(){
  var views=[].slice.call(document.querySelectorAll('.view'));
  var links=[].slice.call(document.querySelectorAll('nav a'));
  function show(){
    var name=(location.hash||'').replace(/^#/,'')||'home';
    var el=document.getElementById(name);
    var view=el?el.closest('.view'):null;
    if(!view){view=document.getElementById('home');el=null;}
    views.forEach(function(v){v.hidden=(v!==view);});
    links.forEach(function(a){ if(a.getAttribute('data-view')===view.id){a.setAttribute('aria-current','page');}else{a.removeAttribute('aria-current');} });
    if(el&&el!==view){el.scrollIntoView();}else{window.scrollTo(0,0);}
  }
  window.addEventListener('hashchange',show);
  show();

  var f=document.getElementById('gloss-filter');
  if(f){
    var terms=[].slice.call(document.querySelectorAll('#gloss-list .term'));
    var empty=document.getElementById('gloss-empty');
    f.addEventListener('input',function(){
      var q=f.value.trim().toLowerCase(),n=0;
      terms.forEach(function(t){var hit=!q||t.textContent.toLowerCase().indexOf(q)>-1;t.hidden=!hit;if(hit){n++;}});
      empty.hidden=n>0;
    });
  }

  var KEY='wa-first-home-checklist';
  var boxes=[].slice.call(document.querySelectorAll('.checks input'));
  var saved={};
  try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){saved={};}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(saved));}catch(e){}}
  boxes.forEach(function(b){
    b.checked=!!saved[b.id];
    b.addEventListener('change',function(){saved[b.id]=b.checked;save();});
  });
  var clr=document.getElementById('chk-clear');
  if(clr){clr.addEventListener('click',function(){saved={};save();boxes.forEach(function(b){b.checked=false;});document.getElementById('chk-note').textContent='All ticks cleared.';});}
})();
'''

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Your First Home in Washington</title>
<meta name="description" content="A free, plain-language overview of buying a first home in Washington State. No sign-up, no ads, no tracking.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;700&family=Bitter:wght@600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="#home">Your First Home in Washington<small>A plain-language guide to buying, start to keys</small></a>
<nav aria-label="Sections"><ul>{nav}</ul></nav>
</div></header>
<main><div class="wrap">
{"".join(sections)}
</div></main>
<footer class="site"><div class="wrap">
<p><strong>Education, not advice.</strong> Rules and numbers change. Confirm anything important with the official source or a licensed professional before you act.</p>
<p>An independent guide. Not a government site, lender, real estate firm or inspector. Built with AI assistance from official sources gathered in November 2026. Last reviewed {REVIEWED}. <a href="#about">How this guide was made</a>.</p>
</div></footer>
<script>{JS}</script>
</body>
</html>
'''
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(PAGE)

# ---------- checks ----------
# every outside link on the site must come from the research report's source list
rep_urls = set(l.strip() for l in open(os.path.join(HERE, "source_links.txt"), encoding="utf-8") if l.strip())
site_urls = set(re.findall(r'href="(https?://[^"]+)"', PAGE))
bad = sorted(u for u in site_urls if html.unescape(u) not in rep_urls and "fonts.g" not in u)
print("external links:", len(site_urls), "| not in source list:", bad)

def text_of(h):
    h = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", h)
    h = re.sub(r"</(p|li|h\d|dd|dt|td|th)>", ". ", h)
    return html.unescape(re.sub(r"<[^>]+>", " ", h))
def syll(w):
    w = w.lower(); w = re.sub(r"[^a-z]", "", w)
    if not w: return 0
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1: n -= 1
    return max(n, 1)
def fk(t):
    sents = [s for s in re.split(r"[.!?]+", t) if re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", t)
    return len(words), round(0.39 * len(words) / len(sents) + 11.8 * sum(map(syll, words)) / len(words) - 15.59, 1)
for vid, label, title, body in VIEWS:
    if vid in ("glossary", "checklist"): continue
    w, g = fk(text_of(body))
    print(f"{vid:11s} words={w:5d} FK grade={g}")
print("glossary terms:", len(gl_items), "| page bytes:", len(PAGE.encode()))
if "--dump-gloss" in sys.argv:
    for t in sorted([t for t in GLOSSARY_TERMS if t in gloss], key=str.lower):
        print(("* " if gloss[t][1] else "  ") + t + " :: " + gloss[t][0])
