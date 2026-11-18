"""Génère les 3 planches V1 (page Jeu) de Verrouillage. Sortie : G-DESIGN/planches/v1/."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

# ---------- données réelles : generateOrder('2026-12-11') ----------
LOCKS = ["brass", "iron", "silver", "shadow"]
QUEUE = ["iron", "brass"]  # état de démo
CLUES = [("iron", "opens", "1st"), ("silver", "opens", "4th"), ("brass", "before", "shadow")]
CLOCK, STREAK, DAY = "01:24", 6, "Thu · Dec 11"

# ---------- cadenas SVG (matières partagées) ----------
DEFS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<linearGradient id="m-brass" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#ecd29a"/><stop offset=".28" stop-color="#c29d62"/><stop offset=".7" stop-color="#8e6c3c"/><stop offset="1" stop-color="#5a4225"/></linearGradient>
<linearGradient id="m-iron" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#7a8089"/><stop offset=".3" stop-color="#555b63"/><stop offset=".75" stop-color="#3a3f46"/><stop offset="1" stop-color="#24272c"/></linearGradient>
<linearGradient id="m-silver" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#fbfcfd"/><stop offset=".3" stop-color="#d7dce2"/><stop offset=".72" stop-color="#a3aab3"/><stop offset="1" stop-color="#6f7680"/></linearGradient>
<linearGradient id="m-shadow" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#45474e"/><stop offset=".3" stop-color="#25262b"/><stop offset=".75" stop-color="#151619"/><stop offset="1" stop-color="#0a0a0c"/></linearGradient>
<linearGradient id="m-shackle" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7d838c"/><stop offset=".35" stop-color="#eef0f3"/><stop offset=".6" stop-color="#b3b9c1"/><stop offset="1" stop-color="#5d636b"/></linearGradient>
<linearGradient id="m-sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".0"/><stop offset=".42" stop-color="#fff" stop-opacity=".0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset=".58" stop-color="#fff" stop-opacity=".0"/></linearGradient>
<pattern id="chain-h" width="34" height="20" patternUnits="userSpaceOnUse"><ellipse cx="11" cy="10" rx="10" ry="6" fill="none" stroke="url(#m-shackle)" stroke-width="3.6"/><rect x="21" y="8" width="13" height="4" rx="2" fill="#8a9099"/></pattern>
<pattern id="chain-v" width="20" height="34" patternUnits="userSpaceOnUse"><ellipse cx="10" cy="11" rx="6" ry="10" fill="none" stroke="url(#m-shackle)" stroke-width="3.6"/><rect x="8" y="21" width="4" height="13" rx="2" fill="#8a9099"/></pattern>
</defs></svg>"""

KEY = {"brass": "#3a2a14", "iron": "#15171a", "silver": "#4a5058", "shadow": "#000"}
EDGE = {"brass": "#f7e2b0", "iron": "#9aa1ab", "silver": "#ffffff", "shadow": "#6b6e77"}


def lock(m, opened=False, cls=""):
    shackle = 'transform="rotate(-24 72 58) translate(0 -14)"' if opened else ""
    return f"""<svg class="lk {cls}" viewBox="0 0 100 128" aria-hidden="true">
<g {shackle}><path d="M28 60V36a22 22 0 0 1 44 0v24" fill="none" stroke="#00000055" stroke-width="11" stroke-linecap="round" transform="translate(1.5 2)"/>
<path d="M28 60V36a22 22 0 0 1 44 0v24" fill="none" stroke="url(#m-shackle)" stroke-width="9" stroke-linecap="round"/></g>
<rect x="10" y="52" width="80" height="72" rx="13" fill="url(#m-{m})"/>
<rect x="10" y="52" width="80" height="72" rx="13" fill="url(#m-sheen)"/>
<path d="M23 53.5h54" stroke="{EDGE[m]}" stroke-opacity=".55" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="50" cy="83" r="6.5" fill="{KEY[m]}"/><path d="M46.6 86h6.8l2.2 15h-11.2z" fill="{KEY[m]}"/>
</svg>"""


def dot(m):
    return f'<i class="dot d-{m}"></i>'


def clue_html(c):
    a, verb, b = c
    if verb == "before":
        return f'{dot(a)}<b>{a.capitalize()}</b> opens before {dot(b)}<b>{b.capitalize()}</b>'
    return f'{dot(a)}<b>{a.capitalize()}</b> opens <span class="num">{b}</span>'


LINK_ICON = '<svg class="ic" viewBox="0 0 24 12" aria-hidden="true"><rect x="1" y="2" width="12" height="8" rx="4" fill="none" stroke="currentColor" stroke-width="2"/><rect x="11" y="2" width="12" height="8" rx="4" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

# ---------- hôte (cadre de post neutre, sans marque) ----------
HOST_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#0b0b0c;color:#c9c9c9;font-family:var(--sans)}
button{font:inherit;color:inherit;border:0;background:none;cursor:pointer}
:root{--sans:Inter,"Helvetica Neue",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--heavy:"Helvetica Neue","Arial Black","Inter",system-ui,sans-serif;
--cond:"Roboto Condensed","Arial Narrow","Helvetica Neue",system-ui,sans-serif;
--mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace;
--h-bg:#0f1011;--h-card:#16171a;--h-line:#25272b;--h-ink:#d7d9dc;--h-muted:#7d8085}
.toolbar{position:sticky;top:0;z-index:5;display:flex;gap:14px;align-items:center;padding:10px 24px;background:#0b0b0cee;border-bottom:1px solid #1d1d1f;font:12px var(--mono);color:#8a8a8a}
.toolbar b{color:#e8e8e8;font-weight:600}
.toolbar button{margin-left:auto;border:1px solid #34343a;border-radius:999px;padding:4px 12px;color:#ddd}
.stage{padding:28px 24px;overflow:hidden}
.board{transform-origin:0 0;display:inline-flex;flex-direction:column;gap:30px;width:1870px}
.intro{display:flex;gap:48px;align-items:flex-end}
.intro h1{font:900 46px/1 var(--heavy);color:#f1f1f1;letter-spacing:-.02em}
.intro h1 small{display:block;font:500 12px var(--mono);letter-spacing:.2em;color:#7d7d84;margin-bottom:12px;text-transform:uppercase}
.intro p{max-width:620px;font-size:14px;line-height:1.55;color:#a0a0a6}
.swatches{display:flex;gap:8px;margin-left:auto}
.sw{width:96px;font:11px/1.4 var(--mono);color:#8a8a90}
.sw i{display:block;height:46px;border-radius:6px;margin-bottom:6px;border:1px solid #ffffff14}
.row{display:flex;gap:40px;align-items:flex-start}
.cap{font:500 11px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#77777e;margin-bottom:10px}
.frame{position:relative;overflow:hidden;border-radius:6px;box-shadow:0 0 0 1px #26262a,0 30px 80px #000c;background:var(--h-bg)}
.desk{width:1440px;height:900px}
.mob{width:390px;height:844px;border-radius:30px}
.h-top{height:56px;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1px solid var(--h-line)}
.h-ph{flex:none;width:32px;height:32px;border-radius:8px;background:#2a2c30}
.h-search{flex:0 1 560px;margin:0 auto;height:38px;border-radius:999px;background:#1d1f22;color:var(--h-muted);font-size:14px;display:flex;align-items:center;padding:0 18px}
.h-av{flex:none;width:32px;height:32px;border-radius:50%;background:#2a2c30}
.h-body{display:flex;gap:24px;justify-content:center;padding:16px 24px}
.h-rail{width:220px;display:flex;flex-direction:column;gap:14px;padding-top:8px}
.h-rail span{height:12px;border-radius:6px;background:#1c1e21}
.h-rail span:nth-child(odd){width:70%}
.h-side{width:300px}
.h-side .card{border-radius:12px;background:var(--h-card);padding:16px;display:flex;flex-direction:column;gap:12px}
.h-side .card b{font-size:14px;color:var(--h-ink)}
.h-side .card span{height:10px;border-radius:5px;background:#24262a}
.post{width:760px;border-radius:12px;background:var(--h-card);padding:12px}
.p-head{display:flex;align-items:center;gap:10px;font-size:12px;color:var(--h-muted)}
.p-head i{width:28px;height:28px;border-radius:50%;background:#2b2f36;box-shadow:inset 0 0 0 2px #b08d57}
.p-head b{color:var(--h-ink);font-weight:600}
.p-title{font:600 18px/1.3 var(--sans);color:var(--h-ink);margin:8px 0 10px}
.p-act{display:flex;gap:10px;margin-top:10px}
.p-act span{font-size:12px;font-weight:600;color:var(--h-ink);background:#202226;border-radius:999px;padding:7px 14px}
.desk .slot{width:736px;height:620px;border-radius:10px;overflow:hidden}
.mob .h-top{height:48px;padding:0 14px}
.mob .h-search{height:32px;font-size:13px}
.mob .post{width:auto;border-radius:0;padding:10px 0 0;background:var(--h-bg)}
.mob .p-head,.mob .p-title{padding:0 14px}
.mob .p-title{font-size:15px;margin:6px 0 8px}
.mob .slot{width:390px;height:672px}
.mob .p-act{padding:0 14px;margin-top:8px}
/* panneau états */
.states{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.st{border:1px solid #232327;border-radius:10px;overflow:hidden;background:#111113}
.st .v{height:210px;position:relative;overflow:hidden}
.st .t{padding:12px 14px;font-size:12px;line-height:1.5;color:#9a9aa0}
.st .t b{display:block;font:600 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#e6e6e6;margin-bottom:4px}
.notes{font-size:13px;line-height:1.6;color:#9a9aa0;max-width:1300px}
.notes b{color:#e6e6e6}
/* commun jeu */
.lk{display:block;width:100%;height:auto;overflow:visible}
.dot{flex:none;display:inline-block;width:.62em;height:.62em;border-radius:50%;margin-right:.38em;vertical-align:.04em;box-shadow:inset 0 0 0 1px #ffffff30}
.d-brass{background:linear-gradient(140deg,#e6c98f,#8e6c3c)}
.d-iron{background:linear-gradient(140deg,#7a8089,#2f3339)}
.d-silver{background:linear-gradient(140deg,#fff,#9aa1aa)}
.d-shadow{background:linear-gradient(140deg,#45474e,#0b0b0d);box-shadow:inset 0 0 0 1px #ffffff40}
.ic{width:1.5em;height:.75em;vertical-align:-.02em;margin-right:.3em}
"""

FIT_JS = """<script>
(function(){var b=document.querySelector('.board'),btn=document.getElementById('fit'),fit=true;
function apply(){var s=fit?Math.min(1,(window.innerWidth-48)/1870):1;b.style.transform='scale('+s+')';
document.querySelector('.stage').style.height=(b.getBoundingClientRect().height+64)+'px';btn.textContent=fit?'100 %':'Ajuster';}
btn.onclick=function(){fit=!fit;apply()};window.addEventListener('resize',apply);apply();})();
</script>"""


def post(game, mobile):
    head = f"""<div class="p-head"><i></i><b>r/verrouillage_test</b><span>· 2 h</span></div>
<div class="p-title">Verrouillage — today's chest, {DAY}</div>"""
    act = '<div class="p-act"><span>Vote</span><span>48 comments</span><span>Share</span></div>'
    if mobile:
        return f"""<div class="frame mob"><div class="h-top"><div class="h-ph"></div><div class="h-search">Search</div><div class="h-av"></div></div>
<div class="post">{head}<div class="slot">{game}</div>{act}</div></div>"""
    return f"""<div class="frame desk"><div class="h-top"><div class="h-ph"></div><div class="h-search">Search</div><div class="h-av"></div></div>
<div class="h-body"><div class="h-rail"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="post">{head}<div class="slot">{game}</div>{act}</div>
<div class="h-side"><div class="card"><b>About this community</b><span></span><span style="width:80%"></span><span style="width:60%"></span></div></div></div></div>"""


def page(num, slug, name, title_fr, intro, swatches, css, game, states, notes):
    sw = "".join(f'<div class="sw"><i style="background:{h}"></i>{n}<br>{h}</div>' for n, h in swatches)
    st = "".join(f'<div class="st"><div class="v g">{v}</div><div class="t"><b>{t}</b>{d}</div></div>' for v, t, d in states)
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Verrouillage — V1 · {num} {name}</title>
<style>{HOST_CSS}
/* ===== Direction {num} « {name} » ===== */
{css}
</style>
</head>
<body>
{DEFS}
<div class="toolbar"><b>Verrouillage</b> · V1 · page Jeu · direction {num} « {name} » · données du 2026-12-11<button id="fit">100 %</button></div>
<div class="stage"><div class="board">
<div class="intro"><h1><small>Direction {num} · {title_fr}</small>{name}</h1><p>{intro}</p><div class="swatches">{sw}</div></div>
<div class="row"><div><div class="cap">Desktop · 1440 × 900 · post dans le feed</div>{post(game, False)}</div>
<div><div class="cap">Mobile · 390 × 844</div>{post(game, True)}</div></div>
<div><div class="cap">États &amp; mouvement</div><div class="states">{st}</div></div>
<p class="notes">{notes}</p>
</div></div>
{FIT_JS}
</body></html>"""
    (OUT / f"{num}-{slug}.html").write_text(html, encoding="utf-8")


def slot_label(i):
    return f"{i:02d}"


# =====================================================================
# 01 — FORGE (direction du brief)
# =====================================================================
F_CSS = """
.g{--bg:#2b2f36;--bg2:#22262c;--line:#3c424b;--ink:#eceef1;--muted:#8e96a1;--brass:#b08d57;--acc:#ff5d5d;
container-type:size;width:100%;height:100%;color:var(--ink);font-family:var(--sans);
background:repeating-linear-gradient(90deg,#ffffff04 0 1px,transparent 1px 3px),radial-gradient(110% 60% at 50% 0%,#3a4049 0%,transparent 70%),linear-gradient(#2b2f36,#1f2228)}
.f{height:100%;display:flex;flex-direction:column;gap:12px;padding:14px 16px 16px}
.f-top{display:flex;align-items:center;justify-content:space-between;padding-bottom:10px;border-bottom:1px solid var(--line)}
.f-mark{font:900 17px/1 var(--heavy);letter-spacing:.06em;text-transform:uppercase}
.f-meta{display:flex;gap:14px;font:500 12px var(--mono);color:var(--muted)}
.f-meta b{color:var(--ink);font-weight:600}
.f-rule{font-size:13px;color:var(--muted);text-align:center}
.f-rule em{font-style:normal;color:var(--ink)}
.f-rig{position:relative;flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.f-chain{position:absolute;left:-40px;width:calc(100% + 80px);top:26px;height:20px;z-index:0}
.f-locks{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;width:100%;max-width:560px;padding-top:6px}
.f-lock{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:8px;padding:0 4px 8px}
.f-lock .lk{max-width:130px;filter:drop-shadow(0 14px 14px #0009)}
.f-name{font:800 11px var(--heavy);letter-spacing:.14em;text-transform:uppercase}
.f-tagno{position:absolute;top:44%;z-index:2;left:50%;transform:translateX(-50%);font:700 13px var(--mono);color:#1b1d21;background:#e9ebee;border-radius:4px;padding:2px 6px;box-shadow:0 2px 0 #0007}
.f-lock.q .lk{filter:brightness(.55) saturate(.6) drop-shadow(0 10px 10px #0009);transform:translateY(6px)}
.f-lock.q .f-name{color:var(--muted)}
.f-queue{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.f-s{border:1px solid var(--line);border-radius:6px;padding:8px 10px;display:flex;align-items:baseline;gap:8px;background:#ffffff05}
.f-s i{font:700 12px var(--mono);font-style:normal;color:var(--muted)}
.f-s span{font:800 12px var(--heavy);letter-spacing:.1em;text-transform:uppercase}
.f-s.e span{color:#59606b}
.f-s.nx{border-color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}
.f-s.nx i{color:var(--acc)}
.f-tag{position:relative;border-radius:8px;padding:12px 16px 12px 30px;color:#22180b;
background:linear-gradient(170deg,#d4b47c,#b08d57 40%,#987546);box-shadow:inset 0 1px 0 #f3dfb2,0 10px 22px #0007}
.f-tag::before,.f-tag::after{content:"";position:absolute;left:11px;width:7px;height:7px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#f3e2be,#6d5230)}
.f-tag::before{top:12px}.f-tag::after{bottom:12px}
.f-tag ol{list-style:none;display:flex;flex-direction:column;gap:5px;font-size:14px;line-height:1.3}
.f-tag li{display:block}
.f-tag li>.n{display:inline-block;font:700 11px var(--mono);opacity:.6;width:18px}
.f-tag b{font-weight:800}
.f-tag .num{font:700 13px var(--mono)}
.f-tag .dot{box-shadow:0 0 0 1px #3a2a1466}
.f-act{display:flex;gap:10px}
.f-btn{height:46px;border-radius:6px;font:900 13px var(--heavy);letter-spacing:.14em;text-transform:uppercase}
.f-undo{width:110px;border:1px solid var(--line);color:var(--ink);background:#ffffff06}
.f-go{flex:1;background:var(--acc);color:#2a0d0d;box-shadow:0 4px 0 #a83636,0 14px 24px #ff5d5d30}
.f-go small{font:700 12px var(--mono);letter-spacing:0;margin-left:6px;opacity:.75}
@container (min-width:600px){.f{padding:18px 26px 22px;gap:14px}.f-mark{font-size:20px}.f-locks{gap:28px}.f-lock .lk{max-width:140px}.f-chain{top:30px}.f-tag ol{display:grid;grid-template-columns:1fr 1fr;column-gap:20px}}
@container (max-width:420px){.f-lock .lk{max-width:76px}.f-chain{top:14px;left:-20px;width:calc(100% + 40px)}.f-s{flex-direction:column;gap:2px;padding:7px 8px}.f-tag ol{font-size:13px}}
.st .f{padding:14px;justify-content:center;align-items:center;gap:10px}
"""

def forge_game():
    locks = ""
    for m in LOCKS:
        q = m in QUEUE
        tag = f'<span class="f-tagno">#{QUEUE.index(m)+1}</span>' if q else ""
        locks += f'<div class="f-lock{" q" if q else ""}">{lock(m)}{tag}<span class="f-name">{m}</span></div>'
    slots = ""
    for i in range(4):
        if i < len(QUEUE):
            slots += f'<div class="f-s"><i>{slot_label(i+1)}</i><span>{QUEUE[i]}</span></div>'
        else:
            slots += f'<div class="f-s e{" nx" if i == len(QUEUE) else ""}"><i>{slot_label(i+1)}</i><span>—</span></div>'
    clues = "".join(f"<li><span class=\"n\">{i+1}</span>{clue_html(c)}</li>" for i, c in enumerate(CLUES))
    return f"""<div class="g"><div class="f">
<div class="f-top"><span class="f-mark">Verrouillage</span><span class="f-meta"><span><b>{CLOCK}</b></span><span>{LINK_ICON}<b>{STREAK}</b> days</span></span></div>
<p class="f-rule">Pull the four locks in <em>the one order</em> the tag allows.</p>
<div class="f-rig"><div class="f-locks"><svg class="f-chain" preserveAspectRatio="none"><rect width="100%" height="20" fill="url(#chain-h)"/></svg>{locks}</div></div>
<div class="f-queue">{slots}</div>
<div class="f-tag"><ol>{clues}</ol></div>
<div class="f-act"><button class="f-btn f-undo">Undo</button><button class="f-btn f-go">Pull all<small>2/4</small></button></div>
</div></div>"""

forge_states = [
    (f'<div class="f">{lock("iron", cls="")}</div>'.replace('class="lk "', 'class="lk" style="width:84px;transform:translateY(6px);opacity:.6"') + '<span class="f-tagno" style="position:absolute;top:96px;left:50%">#1</span>',
     "Lock queued", "Tap : le cadenas descend de 6 px sur la chaîne (140 ms, ease-out), clic mécanique, plaque #n tamponnée. Undo le remonte."),
    ('<div class="f"><div style="display:flex;gap:8px;width:220px">' + "".join(f'<div style="flex:1">{lock(m)}</div>' for m in ["iron","brass","silver","shadow"]) + '</div><div class="f-mark" style="color:var(--acc);font-size:15px">Still chained</div><div style="font-size:12px;color:var(--muted)">A link snapped. Try a different order.</div></div>',
     "Wrong order", "La chaîne se tend puis vibre 2 fois (± 4 px, 240 ms). Seul le titre passe en accent. Pas de compteur d’essais (question 3)."),
    ('<div class="f"><div style="display:flex;gap:8px;width:220px">' + "".join(f'<div style="flex:1;transform:translateY({-i*3}px)">{lock(m, opened=True)}</div>' for i, m in enumerate(["iron","brass","shadow","silver"])) + '</div><div class="f-mark" style="font-size:15px">Chest open</div><div style="font:12px var(--mono);color:var(--muted)">01:52 · streak 7</div></div>',
     "Cascade", "Ouverture dans l’ordre joué : chaque anse saute à +120 ms de la précédente (180 ms, overshoot léger), la chaîne tombe en dernier. Le seul moment d’élan."),
    ('<div class="f"><svg style="width:200px;height:20px"><rect width="200" height="20" fill="url(#chain-h)" opacity=".5"/></svg><div style="font-size:13px;color:var(--muted)">Wrapping the chains…</div></div>',
     "Loading", "La chaîne défile lentement de gauche à droite (pattern translaté, 1,2 s linéaire). Libellé actuel du code conservé."),
    ('<div class="f"><div style="width:90px">' + lock("brass", opened=True) + '</div><div class="f-mark" style="font-size:14px">Solved today</div><div style="font-size:12px;color:var(--muted)">Four new padlocks tomorrow.</div></div>',
     "Already solved", "Si solvedToday : coffre ouvert figé, pas de jeu, renvoi vers la carte de fin. Copie actuelle du code."),
]

page("01", "forge", "Forge", "direction du brief",
     "La direction de départ, poussée jusqu’au bout : plaque d’acier brossé, chaîne réelle qui traverse le cadre, cadenas pendus dessus, étiquette en laiton rivetée pour les indices. Un seul accent rouge, réservé à « ce que tu fais maintenant » : la prochaine case de la file et le bouton Pull all. Titres en grotesque lourde, chiffres et chrono en mono.",
     [("Acier", "#2b2f36"), ("Acier nuit", "#1f2228"), ("Laiton", "#b08d57"), ("Encre", "#eceef1"), ("Accent", "#ff5d5d")],
     F_CSS, forge_game(), forge_states,
     "<b>Lecture en 5 s :</b> chaîne → 4 cadenas → file 01–04 → étiquette → bouton. "
     "<b>Couleur :</b> les cadenas portent leur matière (laiton, fer, argent, ombre), l’UI reste en acier ; le rouge n’apparaît qu’à deux endroits. "
     "<b>Risque :</b> beaucoup de matière (brossé, rivets, laiton) — à surveiller pour ne pas tomber dans le skeuomorphisme lourd au build.")

# =====================================================================
# 02 — ATELIER (Shutabug : objet sur fond clair, UI qui s'efface)
# =====================================================================
A_CSS = """
.g{--ink:#16171a;--muted:#7f7d76;--line:#d6d3ca;--acc:#ff5d5d;container-type:size;width:100%;height:100%;color:var(--ink);font-family:var(--sans);
background:radial-gradient(90% 46% at 50% 64%,#f7f6f2 0%,#eceae4 55%,#dfdcd4 100%)}
.a{height:100%;display:flex;flex-direction:column;padding:14px 18px 18px}
.a-top{display:flex;justify-content:space-between;align-items:baseline;font:500 10.5px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.a-top b{font:900 13px var(--heavy);letter-spacing:.02em;color:var(--ink);text-transform:none}
.a-top span b{font:600 10.5px var(--mono);letter-spacing:.16em;color:var(--ink)}
.a-stage{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.a-locks{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;width:100%;max-width:600px;align-items:end}
.a-lock{position:relative;display:flex;flex-direction:column;align-items:center;gap:12px}
.a-lock .lk{max-width:112px;position:relative;z-index:1;filter:drop-shadow(0 10px 8px #00000022)}
.a-lock::after{content:"";position:absolute;bottom:22px;width:70%;height:12px;border-radius:50%;background:#0000002e;filter:blur(6px)}
.a-name{font:500 10px var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.a-badge{position:absolute;top:-4px;right:8%;z-index:2;width:24px;height:24px;border-radius:50%;background:var(--ink);color:#f4f3ef;font:600 12px/24px var(--mono);text-align:center}
.a-lock.q .lk{transform:translateY(-10px)}
.a-seq{display:flex;align-items:center;justify-content:center;gap:0;margin:2px 0 14px}
.a-p{display:flex;align-items:center;gap:6px;height:30px;padding:0 12px 0 6px;border-radius:999px;border:1px solid var(--line);font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;background:#ffffff70}
.a-p i{font-style:normal;width:20px;height:20px;border-radius:50%;background:var(--ink);color:#f4f3ef;font:600 11px/20px var(--mono);text-align:center}
.a-p.e{color:#b3b0a7}.a-p.e i{background:transparent;color:#b3b0a7;box-shadow:inset 0 0 0 1px #c9c5bb}
.a-p.nx{border-color:var(--acc);color:var(--acc)}.a-p.nx i{color:var(--acc);box-shadow:inset 0 0 0 1.5px var(--acc)}
.a-ln{width:18px;height:1px;background:#bdb9ae}
.a-clues{list-style:none;display:flex;flex-direction:column;align-items:center;gap:6px;font-size:15px;line-height:1.35;padding:12px 0 16px;border-top:1px solid var(--line)}
.a-clues b{font-weight:700}
.a-clues .num{font:600 13px var(--mono)}
.a-clues .dot{box-shadow:inset 0 0 0 1px #00000020}
.a-act{display:flex;align-items:center;justify-content:center;gap:22px}
.a-undo{font:500 11px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--muted);text-decoration:underline;text-underline-offset:4px}
.a-go{height:46px;padding:0 30px;border-radius:999px;background:var(--ink);color:#f4f3ef;font:800 14px var(--heavy);letter-spacing:.02em}
.a-go small{font:500 12px var(--mono);margin-left:8px;opacity:.6}
.a-hint{text-align:center;font:500 10px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:#a29f96;margin-top:10px}
@container (min-width:600px){.a{padding:18px 28px 22px}.a-locks{gap:40px}.a-lock .lk{max-width:124px}}
@container (max-width:420px){.a-locks{gap:10px}.a-lock .lk{max-width:74px}.a-p{padding:0 8px 0 4px;font-size:9.5px;letter-spacing:.06em}.a-ln{width:6px}.a-clues{font-size:14px}.a-badge{width:20px;height:20px;line-height:20px;font-size:11px;right:2%}}
.st .a{justify-content:center;align-items:center;gap:10px;padding:14px}
"""

def atelier_game():
    locks = ""
    for m in LOCKS:
        q = m in QUEUE
        badge = f'<span class="a-badge">{QUEUE.index(m)+1}</span>' if q else ""
        locks += f'<div class="a-lock{" q" if q else ""}">{badge}{lock(m)}<span class="a-name">{m}</span></div>'
    seq = []
    for i in range(4):
        if i < len(QUEUE):
            seq.append(f'<span class="a-p"><i>{i+1}</i>{QUEUE[i]}</span>')
        else:
            seq.append(f'<span class="a-p e{" nx" if i == len(QUEUE) else ""}"><i>{i+1}</i>····</span>')
    clues = "".join(f"<li>{clue_html(c)}</li>" for c in CLUES)
    return f"""<div class="g"><div class="a">
<div class="a-top"><b>Verrouillage</b><span>{DAY} · <b>{CLOCK}</b> · streak <b>{STREAK}</b></span></div>
<div class="a-stage"><div class="a-locks">{locks}</div></div>
<div class="a-seq">{'<span class="a-ln"></span>'.join(seq)}</div>
<ul class="a-clues">{clues}</ul>
<div class="a-act"><button class="a-undo">Undo</button><button class="a-go">Pull all<small>2/4</small></button></div>
<p class="a-hint">Tap the locks in the one order the tag allows</p>
</div></div>"""

atelier_states = [
    ('<div class="a"><div class="a-lock q" style="width:90px"><span class="a-badge">1</span>' + lock("iron") + '</div></div>',
     "Lock queued", "Le cadenas se soulève de 10 px, son ombre au sol se resserre (200 ms, ease-out). Pastille noire numérotée. Undo le repose."),
    ('<div class="a"><div style="display:flex;gap:6px;width:210px">' + "".join(f'<div style="flex:1">{lock(m)}</div>' for m in ["iron","brass","silver","shadow"]) + '</div><div style="font:800 15px var(--heavy)">Still chained</div><div style="font:500 10px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--acc)">A link snapped</div></div>',
     "Wrong order", "Les quatre se reposent ensemble au sol, un seul tremblement (± 3 px). L’accent rouge ne colore que la ligne d’explication."),
    ('<div class="a"><div style="display:flex;gap:6px;width:210px">' + "".join(f'<div style="flex:1">{lock(m, opened=True)}</div>' for m in ["iron","brass","shadow","silver"]) + '</div><div style="font:800 15px var(--heavy)">Chest open</div><div style="font:500 11px var(--mono);color:var(--muted)">01:52 · STREAK 7</div></div>',
     "Cascade", "Les anses s’ouvrent l’une après l’autre (+120 ms), chaque cadenas se lève légèrement puis se repose : un geste net, sans particules."),
    ('<div class="a"><div style="width:70px;opacity:.35">' + lock("silver") + '</div><div style="font:500 10px var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)">Wrapping the chains…</div></div>',
     "Loading", "Silhouette d’un cadenas qui respire en opacité (0.25 → 0.45, 1,4 s). Rien d’autre à l’écran."),
    ('<div class="a"><div style="width:84px">' + lock("brass", opened=True) + '</div><div style="font:800 14px var(--heavy)">Solved today</div><div style="font-size:12px;color:var(--muted)">Four new padlocks tomorrow.</div></div>',
     "Already solved", "Coffre ouvert figé, lien vers la carte de fin."),
]

page("02", "atelier", "Atelier", "objet de studio",
     "On retourne la lumière : fond os clair, les quatre cadenas posés comme des pièces de musée, avec une vraie ombre au sol. L’interface se réduit à des capitales mono aux bords, une file 1–4 en pilules et trois indices centrés. Le seul aplat fort est le bouton noir ; le rouge marque uniquement la case suivante.",
     [("Os", "#eceae4"), ("Os clair", "#f7f6f2"), ("Encre", "#16171a"), ("Gris chaud", "#7f7d76"), ("Accent", "#ff5d5d")],
     A_CSS, atelier_game(), atelier_states,
     "<b>Lecture en 5 s :</b> quatre objets, une rangée de cases, trois phrases, un bouton. "
     "<b>Différence nette</b> dans un feed Reddit sombre : le post est le seul rectangle clair, il se repère au scroll. "
     "<b>Risque :</b> l’argent et le fond os se rapprochent — l’arête et l’ombre doivent rester marquées au build ; en thème sombre Reddit, le contraste est maximal.")

# =====================================================================
# 03 — CASCADE (écart : verticale, nuit, accent vert-de-gris)
# =====================================================================
C_CSS = """
.g{--bg:#0d1015;--line:#222832;--ink:#e9ecef;--muted:#7d8794;--acc:#5fd3a8;container-type:size;width:100%;height:100%;color:var(--ink);font-family:var(--sans);
background:radial-gradient(60% 40% at 50% -6%,#f3d9a82a 0%,transparent 70%),linear-gradient(#11151b,#0b0d11)}
.c{height:100%;display:grid;grid-template-columns:1fr;grid-template-rows:auto auto 1fr auto;gap:10px;padding:14px 16px 16px}
.c-top{display:flex;justify-content:space-between;align-items:baseline}
.c-mark{font:800 22px/1 var(--cond);letter-spacing:.02em;text-transform:uppercase;font-stretch:condensed}
.c-meta{font:500 12px var(--mono);color:var(--muted);display:flex;gap:12px}
.c-meta b{color:var(--ink);font-weight:600}
.c-clues{list-style:none;display:flex;flex-direction:column;gap:4px;font-size:13.5px;line-height:1.35;padding:8px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.c-clues li{display:block}
.c-clues b{font-weight:700}
.c-clues .num{font:600 12.5px var(--mono);color:var(--ink)}
.c-hang{position:relative;min-height:0;display:flex;flex-direction:column;justify-content:space-between;padding:8px 0}
.c-chain{position:absolute;left:50%;top:-2px;height:100%;width:20px;transform:translateX(-50%);z-index:0}
.c-row{position:relative;z-index:1;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:14px}
.c-row .lk{width:64px;filter:drop-shadow(0 10px 12px #000a)}
.c-n{justify-self:end;font:600 26px/1 var(--mono);color:var(--ink);min-width:36px;text-align:right}
.c-n.e{justify-self:end;width:12px;height:12px;min-width:0;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--acc);opacity:.8;margin-right:8px}
.c-n.nx{color:var(--acc)}
.c-l{font:700 15px var(--cond);letter-spacing:.12em;text-transform:uppercase}
.c-row.q .lk{filter:brightness(.5) saturate(.6) drop-shadow(0 10px 12px #000a)}
.c-row.q .c-l{color:var(--muted)}
.c-l small{display:block;font:500 10px var(--mono);letter-spacing:.08em;color:var(--muted);text-transform:none;margin-top:3px}
.c-act{display:flex;gap:10px}
.c-btn{height:46px;border-radius:12px;font:800 15px var(--cond);letter-spacing:.12em;text-transform:uppercase}
.c-undo{width:100px;border:1px solid var(--line);color:var(--ink)}
.c-go{flex:1;background:var(--acc);color:#06261b}
.c-go small{font:600 12px var(--mono);letter-spacing:0;margin-left:6px;opacity:.7}
@container (min-width:600px){
 .c{grid-template-columns:1fr 1.05fr;grid-template-rows:auto 1fr auto;column-gap:36px;padding:20px 28px 22px}
 .c-top{grid-column:1/-1}
 .c-hang{grid-row:2/4;grid-column:1}
 .c-clues{grid-column:2;grid-row:2;align-self:center;font-size:16px;gap:12px;padding:18px 0}
 .c-act{grid-column:2;grid-row:3}
 .c-row .lk{width:92px}
 .c-hang{padding:4px 0 0}
 .c-mark{font-size:26px}}
.st .c{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:14px}
"""

def cascade_game():
    rows = ""
    nxt = len(QUEUE)
    for m in LOCKS:
        q = m in QUEUE
        if q:
            n = f'<span class="c-n">{QUEUE.index(m)+1}</span>'
        else:
            n = '<span class="c-n e"></span>'
        rows += f'<div class="c-row{" q" if q else ""}">{n}{lock(m)}<span class="c-l">{m}<small>{"pulled #"+str(QUEUE.index(m)+1) if q else "tap to pull"}</small></span></div>'
    clues = "".join(f"<li>{clue_html(c)}</li>" for c in CLUES)
    return f"""<div class="g"><div class="c">
<div class="c-top"><span class="c-mark">Verrouillage</span><span class="c-meta"><span><b>{CLOCK}</b></span><span>{LINK_ICON}<b>{STREAK}</b></span></span></div>
<ul class="c-clues">{clues}</ul>
<div class="c-hang"><svg class="c-chain" preserveAspectRatio="none"><rect width="20" height="100%" fill="url(#chain-v)"/></svg>{rows}</div>
<div class="c-act"><button class="c-btn c-undo">Undo</button><button class="c-btn c-go">Pull all<small>2/4</small></button></div>
</div></div>"""

cascade_states = [
    ('<div class="c"><div class="c-row q" style="width:220px"><span class="c-n">1</span>' + lock("iron") + '<span class="c-l">iron</span></div></div>',
     "Lock queued", "Le chiffre se tape à gauche en mono (fondu + 4 px, 180 ms), le cadenas s’assombrit. Le prochain chiffre libre luit en vert-de-gris."),
    ('<div class="c"><div style="width:52px">' + lock("silver") + '</div><div class="c-mark" style="font-size:18px">Still chained</div><div style="font-size:12px;color:var(--muted)">A link snapped. Try a different order.</div></div>',
     "Wrong order", "La chaîne verticale se balance une fois (rotation ± 2°, 320 ms, amortie). Les chiffres restent : on corrige avec Undo."),
    ('<div class="c"><div style="display:flex;flex-direction:column;gap:0;width:34px">' + "".join(f'<div style="transform:translateY({i*4}px)">{lock(m, opened=True)}</div>' for i, m in enumerate(["iron","brass","shadow"])) + '</div><div class="c-mark" style="font-size:16px;color:var(--acc)">Chest open</div></div>',
     "Cascade", "De haut en bas dans l’ordre joué : chaque anse saute (+140 ms) et le cadenas tombe le long de la chaîne hors du cadre. La cascade littérale du pitch."),
    ('<div class="c"><svg style="width:20px;height:120px"><rect width="20" height="120" fill="url(#chain-v)" opacity=".45"/></svg><div style="font-size:13px;color:var(--muted)">Wrapping the chains…</div></div>',
     "Loading", "La chaîne descend en boucle (pattern translaté verticalement, 1,2 s)."),
    ('<div class="c"><div style="width:70px">' + lock("shadow", opened=True) + '</div><div class="c-mark" style="font-size:16px">Solved today</div><div style="font-size:12px;color:var(--muted)">Four new padlocks tomorrow.</div></div>',
     "Already solved", "Coffre ouvert figé, lien vers la carte de fin."),
]

page("03", "cascade", "Cascade", "écart au brief",
     "L’écart : je quitte la ligne horizontale et le rouge. La chaîne pend du haut du post et les quatre cadenas y sont accrochés l’un sous l’autre — c’est exactement la forme d’un post Reddit sur mobile, haut et étroit, et la victoire devient une vraie cascade qui tombe. L’accent passe au vert-de-gris, la patine du laiton : il dit « ouvert » sans le ton d’alerte du rouge.",
     [("Nuit", "#0d1015"), ("Filet", "#222832"), ("Encre", "#e9ecef"), ("Gris bleu", "#7d8794"), ("Vert-de-gris", "#5fd3a8")],
     C_CSS, cascade_game(), cascade_states,
     "<b>Lecture en 5 s :</b> indices en haut, colonne de cadenas, chiffres d’ordre à gauche, bouton en bas — on lit de haut en bas comme le feed. "
     "<b>Desktop :</b> la colonne reste à gauche, les indices passent à droite, plus grands. "
     "<b>Risque :</b> sort de la palette du brief (pas de rouge, laiton seulement comme matière) ; la typo condensée doit être embarquée (OFL) au build pour tenir le rendu.")
print("ok")
