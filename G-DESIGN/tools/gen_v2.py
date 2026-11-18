"""V2 — 3 planches page Jeu, famille de refs « narratif-jeu ».
Usage : python3 gen_v2.py <dossier sortie planches/v2> <dossier polices fontsource> <gen_planches.py v1>"""
import sys, base64, pathlib

OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
FONTS = pathlib.Path(sys.argv[2])
V1 = pathlib.Path(sys.argv[3]).read_text(encoding="utf-8")
# hôte, données réelles et FIT_JS repris de la V1
exec(V1.split("# =====================================================================\n# 01")[0].replace("OUT = pathlib.Path(sys.argv[1])", "OUT = None"))
OUT = pathlib.Path(sys.argv[1])
FIT_JS = FIT_JS.replace("apply();})();", "apply();document.fonts&&document.fonts.ready.then(apply);})();")

def font(family, pkg, file, weight=400):
    b = base64.b64encode((FONTS / pkg / "files" / file).read_bytes()).decode()
    return f'@font-face{{font-family:"{family}";src:url(data:font/woff2;base64,{b}) format("woff2");font-weight:{weight};font-display:block}}'

# ---------- répliques : les indices réels, dits par les cadenas ----------
ORD = ["first", "second", "third", "fourth"]
SAYS = {}
for c in [("iron", "position", 0), ("silver", "position", 3), ("brass", "before", "shadow")]:
    a, kind, x = c
    line = f"I open {ORD[x]}." if kind == "position" else f"I open before {x.capitalize()}."
    SAYS.setdefault(a, []).append(line)

NOISE = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)' opacity='.28'/></svg>\")")

DEFS2 = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<filter id="rough" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.4" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="rough2" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.2" xChannelSelector="R" yChannelSelector="G"/></filter>
<pattern id="ink-chain" width="30" height="18" patternUnits="userSpaceOnUse"><ellipse cx="10" cy="9" rx="8.6" ry="5.4" fill="#f3f1ea" stroke="#161616" stroke-width="3"/><path d="M18.5 9H30" stroke="#161616" stroke-width="3.6" stroke-linecap="round"/></pattern>
<pattern id="rel-chain" width="30" height="18" patternUnits="userSpaceOnUse"><ellipse cx="11" cy="10" rx="8.6" ry="5.4" fill="none" stroke="#a8a49c" stroke-width="3.4"/><ellipse cx="10" cy="9" rx="8.6" ry="5.4" fill="none" stroke="#d9d6cf" stroke-width="3"/><path d="M19 9H30" stroke="#bdb9b1" stroke-width="3.6" stroke-linecap="round"/></pattern>
<pattern id="rim-chain" width="30" height="18" patternUnits="userSpaceOnUse"><ellipse cx="10" cy="9" rx="8.6" ry="5.4" fill="none" stroke="#2a262c" stroke-width="3.4"/><path d="M3 6.5a8.6 5.4 0 0 1 14 0" fill="none" stroke="#ffd27a" stroke-opacity=".55" stroke-width="1.4"/><path d="M18.5 9H30" stroke="#2a262c" stroke-width="3.6"/></pattern>
</defs></svg>"""

CAP = lambda s: s[0].upper() + s[1:]

# =====================================================================
# Cadenas — 3 traitements
# =====================================================================
INK = {"brass": "#e2ad3c", "iron": "#a3a8ae", "silver": "#ffffff", "shadow": "#161616"}

def ink_lock(m, done=False, opened=False, stamp=None):
    eye = "#f3f1ea" if m == "shadow" else "#161616"
    sh = 'transform="rotate(-24 70 66) translate(0 -14)"' if opened else ""
    if done or opened:
        eyes = f'<path d="M31 88q7-7 14 0M55 88q7-7 14 0" fill="none" stroke="{eye}" stroke-width="3.6" stroke-linecap="round"/>'
    else:
        eyes = f'<ellipse cx="38" cy="87" rx="4.4" ry="6.2" fill="{eye}"/><ellipse cx="62" cy="87" rx="4.4" ry="6.2" fill="{eye}"/><circle cx="39.5" cy="85" r="1.4" fill="{"#161616" if m=="shadow" else "#fff"}"/><circle cx="63.5" cy="85" r="1.4" fill="{"#161616" if m=="shadow" else "#fff"}"/>'
    hatch = "" if m == "shadow" else '<path d="M71 126l11-11M63 127l17-17M78 127l6-6" stroke="#161616" stroke-width="2.4" stroke-linecap="round"/>'
    st = ""
    if stamp:
        st = f'<g transform="rotate(-12 74 70)" opacity=".93"><circle cx="76" cy="68" r="15" fill="#f3f1ea" stroke="#e5482f" stroke-width="3.2"/><text x="76" y="75.5" text-anchor="middle" font-family="Bowlby" font-size="20" fill="#e5482f">{stamp}</text></g>'
    return f"""<svg class="lk" viewBox="0 0 100 140" aria-hidden="true"><g filter="url(#rough)">
<g {sh}><path d="M30 68V42a20 20 0 0 1 40 0v26" fill="none" stroke="#161616" stroke-width="14" stroke-linecap="round"/><path d="M30 68V42a20 20 0 0 1 40 0v26" fill="none" stroke="#f3f1ea" stroke-width="5.4" stroke-linecap="round"/></g>
<rect x="12" y="60" width="76" height="72" rx="15" fill="{INK[m]}" stroke="#161616" stroke-width="4.6"/>{hatch}{eyes}
<circle cx="50" cy="106" r="4.6" fill="{eye}"/><path d="M47.6 108h4.8l1.6 9h-8z" fill="{eye}"/>{st}</g></svg>"""

REL = {"brass": ("#d8a54c", "#9a7232"), "iron": ("#80868e", "#4e535a"), "silver": ("#f6f5f2", "#b5b7ba"), "shadow": ("#2c2c2e", "#0e0e0f")}

def relief_lock(m, opened=False):
    base, dark = REL[m]
    sh = 'transform="rotate(-24 72 64) translate(0 -14)"' if opened else ""
    key = "#e9e6df" if m == "shadow" else "#1d1d1f"
    def layer(dx, body, shk):
        return (f'<g transform="translate({dx} {dx*1.3})"><g {sh}><path d="M31 66V42a21 21 0 0 1 42 0v24" fill="none" stroke="{shk}" stroke-width="10" stroke-linecap="round"/></g>'
                f'<rect x="12" y="58" width="80" height="72" rx="10" fill="{body}"/></g>')
    return (f'<svg class="lk" viewBox="0 0 104 140" aria-hidden="true">{layer(4, dark, "#8f8b84")}{layer(0, base, "#d6d3cc")}'
            f'<path d="M20 61h64" stroke="#ffffff" stroke-opacity=".55" stroke-width="2"/>'
            f'<circle cx="52" cy="92" r="6" fill="{key}"/><path d="M49 95h6l2 13h-10z" fill="{key}"/></svg>')

RIM = {"brass": "#f0b85a", "iron": "#a9b6c4", "silver": "#ffffff", "shadow": "#5a5560"}
LIT = {"brass": "#b98a45", "iron": "#59606a", "silver": "#c9ccd1", "shadow": "#232126"}

def rim_lock(m, lit=False, opened=False):
    r = RIM[m]; body = LIT[m] if lit else "#141217"
    sh = 'transform="rotate(-24 70 64) translate(0 -14)"' if opened else ""
    glow = 'style="filter:drop-shadow(0 0 10px #ffd27a55)"' if lit else ""
    return f"""<svg class="lk" viewBox="0 0 100 140" aria-hidden="true" {glow}>
<g {sh}><path d="M30 66V42a20 20 0 0 1 40 0v24" fill="none" stroke="{r}" stroke-opacity=".7" stroke-width="12" stroke-linecap="round"/><path d="M30 66V42a20 20 0 0 1 40 0v24" fill="none" stroke="#1b191e" stroke-width="8" stroke-linecap="round"/></g>
<rect x="12" y="58" width="76" height="74" rx="13" fill="{body}" stroke="{r}" stroke-opacity=".45" stroke-width="1.5"/>
<path d="M22 59.5h56" stroke="{r}" stroke-width="3" stroke-linecap="round"/>
<circle cx="50" cy="95" r="5" fill="{r}" opacity=".85"/><path d="M47.6 97.5h4.8l1.6 10h-8z" fill="{r}" opacity=".85"/></svg>"""

def page2(num, slug, name, title_fr, intro, swatches, fonts_css, css, game, states, notes, refs):
    sw = "".join(f'<div class="sw"><i style="background:{h}"></i>{n}<br>{h}</div>' for n, h in swatches)
    st = "".join(f'<div class="st"><div class="v g">{v}</div><div class="t"><b>{t}</b>{d}</div></div>' for v, t, d in states)
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Verrouillage — V2 · {num} {name}</title>
<style>{fonts_css}
{HOST_CSS}
.states{{grid-template-columns:repeat(4,1fr)}}
/* ===== Direction {num} « {name} » ===== */
{css}
</style>
</head>
<body>
{DEFS}{DEFS2}
<div class="toolbar"><b>Verrouillage</b> · V2 · page Jeu · direction {num} « {name} » · refs : {refs} · données du 2026-12-11<button id="fit">100 %</button></div>
<div class="stage"><div class="board">
<div class="intro"><h1><small>V2 · Direction {num} · {title_fr}</small>{name}</h1><p>{intro}</p><div class="swatches">{sw}</div></div>
<div class="row"><div><div class="cap">Desktop · 1440 × 900 · post dans le feed</div>{post(game, False)}</div>
<div><div class="cap">Mobile · 390 × 844</div>{post(game, True)}</div></div>
<div><div class="cap">États &amp; mouvement</div><div class="states">{st}</div></div>
<p class="notes">{notes}</p>
</div></div>
{FIT_JS}
</body></html>"""
    (OUT / f"{num}-{slug}.html").write_text(html, encoding="utf-8")

# =====================================================================
# 04 — ENCRE  (Don't Look Up + Gemeos : trait d'encre, personnages, bulles)
# =====================================================================
E_FONTS = font("Bowlby", "bowlby-one", "bowlby-one-latin-400-normal.woff2") + font("Hand", "patrick-hand", "patrick-hand-latin-400-normal.woff2") + font("JBM", "jetbrains-mono", "jetbrains-mono-latin-700-normal.woff2", 700)
E_CSS = f"""
.g{{--ink:#161616;--paper:#f3f1ea;--acc:#e5482f;container-type:size;width:100%;height:100%;color:var(--ink);
background:{NOISE},var(--paper);font-family:Hand,var(--sans)}}
.e{{--lw:72px;--bh:78px;height:100%;display:flex;flex-direction:column;padding:12px 14px 14px}}
.e-top{{display:flex;justify-content:space-between;align-items:center}}
.e-mark{{font:23px/1 Bowlby;letter-spacing:-.01em;filter:url(#rough)}}
.e-meta{{display:flex;gap:8px;align-items:center;font-size:15px}}
.e-meta b{{font:700 13px JBM}}
.e-streak{{display:inline-flex;align-items:center;gap:4px;border:2.5px solid var(--ink);border-radius:999px;padding:0 9px 0 7px;height:26px;background:#fff}}
.e-line{{font-size:19px;line-height:1.15;margin:6px 0 2px}}
.e-scene{{position:relative;flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:var(--bh) auto auto 1fr;column-gap:4px}}
.e-chest{{position:absolute;left:2%;right:2%;top:calc(var(--bh) + 4px);bottom:2px;border:4.5px solid var(--ink);border-radius:26px 26px 12px 12px;filter:url(#rough);
background:repeating-linear-gradient(90deg,transparent 0 52px,#16161626 52px 55px),#e8dfc9}}
.e-chest::before{{content:"";position:absolute;left:0;right:0;top:0;height:32%;border-bottom:4.5px solid var(--ink);border-radius:22px 22px 0 0;background:#efe7d4}}
.e-chain{{position:absolute;left:0;width:100%;top:calc(var(--bh) + var(--lw)*.36);height:18px;filter:url(#rough)}}
.e-say{{grid-row:1;align-self:end;justify-self:center;position:relative;z-index:2;max-width:100%;padding:5px 9px 6px;font-size:15px;line-height:1.05;text-align:center;margin-bottom:8px}}
.e-say::before{{content:"";position:absolute;inset:0;border:3px solid var(--ink);border-radius:16px;background:#fff;filter:url(#rough2);z-index:-1}}
.e-say::after{{content:"";position:absolute;left:50%;bottom:-8px;width:12px;height:12px;margin-left:-6px;background:#fff;border-right:3px solid var(--ink);border-bottom:3px solid var(--ink);transform:rotate(45deg)}}
.e-say.mute{{color:#8b877c}}
.e-lock{{grid-row:2;position:relative;z-index:1;display:flex;flex-direction:column;align-items:center}}
.e-lock .lk{{width:var(--lw)}}
.e-lock.q .lk{{transform:translateY(5px) rotate(-4deg)}}
.e-name{{grid-row:3;justify-self:center;align-self:start;position:relative;z-index:1;font:15px/1 Bowlby;margin-top:4px;padding:3px 7px;background:var(--paper);border-radius:6px}}
.e-order{{grid-column:1/-1;grid-row:4;align-self:center;position:relative;z-index:1;display:grid;grid-template-columns:repeat(4,1fr);gap:7px;margin:0 12px}}
.e-plate{{grid-column:1/-1;grid-row:4;align-self:center;justify-self:center;position:relative;z-index:1;font-size:15px;color:#6d6656;margin-top:-86px}}
.e-cell{{position:relative;height:46px;display:flex;align-items:center;justify-content:center;gap:6px;font:15px Bowlby}}
.e-cell::before{{content:"";position:absolute;inset:0;border:3px solid var(--ink);border-radius:12px;background:#fff;filter:url(#rough2)}}
.e-cell>*{{position:relative}}
.e-cell i{{font:700 11px JBM;font-style:normal;position:absolute;left:8px;top:5px}}
.e-cell.e0{{color:#c9c4b6;font-size:22px}}
.e-cell.e0::before{{background:#efe7d4;border-style:dashed;border-color:#b8b3a5}}
.e-cell.nx{{color:var(--acc)}}
.e-cell.nx::before{{border-color:var(--acc)}}
.e-act{{display:flex;gap:12px;margin-top:12px}}
.e-btn{{position:relative;height:50px;border-radius:14px;font:17px Bowlby;border:3px solid var(--ink);box-shadow:0 5px 0 var(--ink)}}
.e-undo{{width:104px;background:#fff}}
.e-go{{flex:1;background:var(--ink);color:var(--paper)}}
.e-go small{{font:700 13px JBM;margin-left:8px;opacity:.7}}
.e-foot{{text-align:center;font-size:14px;color:#77736a;margin-top:10px}}
@container (min-width:600px){{.e{{--lw:104px;--bh:92px;padding:16px 26px 18px}}.e-mark{{font-size:34px}}.e-line{{font-size:22px}}.e-say{{font-size:18px;padding:7px 14px 8px}}.e-scene{{column-gap:22px;padding:0 40px}}.e-chain{{left:-2px}}
.e-order{{margin:0 30px;gap:14px}}.e-cell{{height:54px;font-size:18px}}.e-act{{max-width:460px;margin:14px auto 0}}.e-plate{{margin-top:-100px;font-size:17px}}}}
.st .e{{align-items:center;justify-content:center;gap:8px}}
"""

def encre_game():
    cols = ""
    for m in LOCKS:
        q = m in QUEUE
        say = SAYS.get(m)
        bubble = f'<div class="e-say">{"<br>".join(say)}</div>' if say else '<div class="e-say mute">…</div>'
        cols += bubble
    locks = "".join(f'<div class="e-lock{" q" if m in QUEUE else ""}">{ink_lock(m, done=m in QUEUE, stamp=(QUEUE.index(m)+1 if m in QUEUE else None))}</div>' for m in LOCKS)
    names = "".join(f'<div class="e-name">{CAP(m)}</div>' for m in LOCKS)
    cells = ""
    for i in range(4):
        if i < len(QUEUE):
            cells += f'<div class="e-cell"><i>{i+1}</i><span>{CAP(QUEUE[i])}</span></div>'
        else:
            cells += f'<div class="e-cell e0{" nx" if i == len(QUEUE) else ""}"><span>{i+1}</span></div>'
    return f"""<div class="g"><div class="e">
<div class="e-top"><span class="e-mark">Verrouillage</span><span class="e-meta"><b>{CLOCK}</b><span class="e-streak">{LINK_ICON}<b>{STREAK}</b>&nbsp;days</span></span></div>
<p class="e-line">Four padlocks, one right order. Listen to them.</p>
<div class="e-scene"><div class="e-chest"></div><svg class="e-chain" preserveAspectRatio="none"><rect width="100%" height="18" fill="url(#ink-chain)"/></svg>{cols}{locks}{names}<div class="e-order">{cells}</div></div>
<div class="e-bottom">
<div class="e-act"><button class="e-btn e-undo">Undo</button><button class="e-btn e-go">Pull all<small>2/4</small></button></div></div>
<p class="e-foot">Tap them in the order they open. A new chest every day.</p>
</div></div>"""

encre_states = [
    ('<div class="e"><div style="width:88px">' + ink_lock("iron", done=True, stamp=1) + '</div></div>',
     "Lock queued", "Le cadenas ferme les yeux, il bascule de 4° sur la chaîne, et le tampon rouge tombe (scale 1,4 → 1, rotation −12°, 160 ms). Undo retire le tampon."),
    ('<div class="e"><div class="e-say" style="font-size:16px;max-width:200px">A link snapped.<br>Try a different order.</div><div style="display:flex;gap:4px;width:220px">' + "".join(f'<div style="flex:1">{ink_lock(m)}</div>' for m in ["iron","brass","silver","shadow"]) + '</div></div>',
     "Still chained", "Les quatre se tournent vers le joueur, les yeux grands ouverts. La bulle reprend le texte actuel du code. Petite secousse du coffre (± 3 px, 2 fois)."),
    ('<div class="e"><div style="display:flex;gap:4px;width:220px">' + "".join(f'<div style="flex:1;transform:translateY({(i%2)*8}px) rotate({(-1)**i*8}deg)">{ink_lock(m, opened=True)}</div>' for i, m in enumerate(["iron","brass","shadow","silver"])) + f'</div><div style="font:22px Bowlby;filter:url(#rough)">Chest open!</div><div style="font:700 12px JBM">01:52 · streak 7</div></div>',
     "Chest open", "Cascade dans l’ordre joué : chaque anse saute à +120 ms, le cadenas sourit et tombe en tournant. Le couvercle se soulève en dernier."),
    ('<div class="e"><svg style="width:190px;height:18px;filter:url(#rough)"><rect width="190" height="18" fill="url(#ink-chain)"/></svg><div style="font-size:19px">Wrapping the chains…</div></div>',
     "Loading", "La chaîne d’encre défile (pattern translaté, 1,2 s). Le trait « bout » légèrement : la graine du filtre change toutes les 120 ms, comme une animation dessinée image par image."),
]

page2("04", "encre", "Encre", "trait d’encre, cadenas personnages",
      "Les cadenas deviennent des personnages : chacun dit lui-même son indice dans une bulle (« I open first. »), et Shadow, qui n’a pas d’indice aujourd’hui, se tait. Le trait est noir et tremblé, sur un papier crème, avec des aplats francs et un titre gras taillé à la main. Le seul accent est le tampon rouge qui numérote les cadenas déjà tirés.",
      [("Papier", "#f3f1ea"), ("Encre", "#161616"), ("Coffre", "#e8dfc9"), ("Laiton", "#e2ad3c"), ("Tampon", "#e5482f")],
      E_FONTS, E_CSS, encre_game(), encre_states,
      "<b>Ce qui change vs V1 :</b> fini l’interface en cartes et dégradés ; l’étiquette d’indices disparaît, les indices sont dits par les cadenas (mêmes données que le générateur, reformulées à la première personne). "
      "<b>Refs :</b> Don’t Look Up (trait noir sur crème, boutons à ombre dure, bulles « whatever »), Gemeos (aplats cernés, titre gras irrégulier). "
      "<b>Polices :</b> Bowlby One + Patrick Hand + JetBrains Mono, toutes OFL, intégrées en base64 dans le fichier.",
      "Don’t Look Up · Gemeos")

# =====================================================================
# 05 — RELIEF  (Gapsy + Matchball + Merci : mur blanc, lumière, relief, griffonnages)
# =====================================================================
R_FONTS = font("Anton", "anton", "anton-latin-400-normal.woff2") + font("Caveat", "caveat", "caveat-latin-700-normal.woff2", 700)
R_CSS = """
.g{--wall:#ecebe7;--ink:#161616;--acc:#e4654c;--accd:#b6452f;container-type:size;width:100%;height:100%;color:var(--ink);font-family:var(--sans);
background:
 linear-gradient(118deg,transparent 0 14%,#ffffff8c 14% 25%,transparent 25% 39%,#ffffff70 39% 47%,transparent 47% 64%,#ffffff60 64% 70%,transparent 70%),
 linear-gradient(118deg,transparent 0 25%,#0000000d 25% 31%,transparent 31% 47%,#0000000a 47% 53%,transparent 53%),
 linear-gradient(#e6e4df,#efeeea 70%)}
.r{--lw:80px;position:relative;height:100%;display:flex;flex-direction:column;padding:12px 16px 0}
.r-meta{display:flex;justify-content:space-between;font:600 11px var(--sans);color:#6f6c66}
.r-meta b{color:var(--ink)}
.r-title{font:44px/.9 Anton;letter-spacing:.005em;color:var(--acc);margin:12px 0 4px;
 text-shadow:1px 1px 0 var(--accd),2px 2px 0 var(--accd),3px 3px 0 var(--accd),4px 4px 0 var(--accd),5px 5px 0 var(--accd),14px 18px 16px #00000030}
.r-sub{font:700 21px/1 Caveat;color:#2b2b2b;display:flex;align-items:center;gap:8px}
.r-wall{position:relative;flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);align-content:center;column-gap:6px}
.r-chain{position:absolute;left:-16px;width:calc(100% + 32px);top:calc(50% - var(--lw)*.5);height:20px;filter:drop-shadow(10px 14px 6px #0000002a)}
.r-lock{position:relative;display:flex;flex-direction:column;align-items:center;gap:6px}
.r-lock .lk{width:var(--lw);filter:drop-shadow(12px 16px 10px #4a3a2a40)}
.r-num{position:absolute;top:calc(var(--lw)*-.62);font:46px/1 Anton;color:var(--acc);text-shadow:1px 1px 0 var(--accd),2px 2px 0 var(--accd),3px 3px 0 var(--accd),10px 14px 10px #00000030}
.r-name{font:15px Anton;letter-spacing:.06em;text-transform:uppercase}
.r-q{position:absolute;top:calc(var(--lw)*-.9);font:700 26px Caveat;color:var(--ink)}
.r-notes{position:relative;display:flex;flex-direction:column;gap:2px;font:700 22px/1.12 Caveat;padding:4px 4px 10px}
.r-notes u{text-decoration:none;background:linear-gradient(transparent 72%,#e4654c55 72% 92%,transparent 92%)}
.r-floor{margin:0 -16px;padding:12px 16px 14px;background:linear-gradient(#d8d0c2,#cbc2b2);box-shadow:inset 0 10px 18px -12px #00000040;display:flex;gap:10px;align-items:center}
.r-undo{height:46px;width:96px;border:2px solid var(--ink);font:18px Anton;letter-spacing:.06em;text-transform:uppercase}
.r-go{flex:1;height:46px;background:var(--ink);color:#fff;font:19px Anton;letter-spacing:.06em;text-transform:uppercase}
.r-go small{font:700 18px Caveat;letter-spacing:0;margin-left:8px;color:#e4654c;text-transform:none}
.r-doodle{position:absolute;pointer-events:none;overflow:visible}
@container (min-width:600px){.r{--lw:112px;padding:16px 28px 0}.r-title{font-size:64px;margin-top:6px}.r-wall{column-gap:30px;padding:0 30px}
 .r-notes{position:absolute;right:28px;top:22px;text-align:right;font-size:24px}.r-floor{margin:0 -28px;padding:14px 28px 16px}.r-num{font-size:60px}.r-wall{padding:30px 60px 0}}
.st .r{align-items:center;justify-content:center;gap:8px;padding:12px}
"""

BURST = '<svg class="r-doodle" style="{pos}" width="64" height="52" viewBox="0 0 64 52"><path d="M32 3l5 11 12-7-3 13 13 1-10 9 9 9-13 0 2 13-11-8-6 11-4-12-12 6 4-12-13-3 11-7-8-10 13 2 1-13 8 9z" fill="none" stroke="#161616" stroke-width="2" stroke-linejoin="round"/><text x="32" y="32" text-anchor="middle" font-family="Caveat" font-weight="700" font-size="16">click</text></svg>'

def relief_game():
    locks = ""
    for i, m in enumerate(LOCKS):
        q = m in QUEUE
        top = f'<span class="r-num">{QUEUE.index(m)+1}</span>' if q else ""
        if q and QUEUE.index(m) == len(QUEUE) - 1:
            top += BURST.format(pos='right:-26px;top:-18px')
        locks += f'<div class="r-lock">{top}{relief_lock(m)}<span class="r-name">{m}</span></div>'
    notes = "<div class=\"r-notes\">" + "".join(
        f"<span>— <u>{CAP(a)}</u> {'opens ' + ORD[x] if k=='position' else 'before <u>'+CAP(x)+'</u>'}</span>"
        for a, k, x in [("iron", "position", 0), ("silver", "position", 3), ("brass", "before", "shadow")]) + "</div>"
    arrow = '<svg class="r-doodle" style="right:22%;top:11%;transform:scaleX(-1)" width="90" height="70" viewBox="0 0 90 70"><path d="M8 10c30-6 58 6 66 40" fill="none" stroke="#161616" stroke-width="2.2" stroke-linecap="round"/><path d="M64 44l10 8 4-13" fill="none" stroke="#161616" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f"""<div class="g"><div class="r">
<div class="r-meta"><span>{DAY}</span><span><b>{CLOCK}</b> · <b>{STREAK}</b>-day streak</span></div>
<h2 class="r-title">VERROUILLAGE</h2>
<div class="r-sub">Pull the four locks in the one right order.</div>
{notes}
<div class="r-wall"><svg class="r-chain" preserveAspectRatio="none"><rect width="100%" height="20" fill="url(#rel-chain)"/></svg>{locks}
<span class="r-q" style="right:9%;top:4%;position:absolute">who's 3rd ?</span>{arrow}</div>
<div class="r-floor"><button class="r-undo">Undo</button><button class="r-go">Pull all<small>2 of 4</small></button></div>
</div></div>"""

relief_states = [
    ('<div class="r"><div class="r-lock" style="margin-top:40px;--lw:80px"><span class="r-num">1</span>' + relief_lock("iron") + '</div></div>',
     "Lock queued", "Le chiffre en relief se pose au-dessus du cadenas en tombant de 12 px, avec son ombre qui se resserre (220 ms, ease-out). Un « click » griffonné apparaît puis s’efface."),
    ('<div class="r"><div style="font:30px Anton;color:#e4654c;text-shadow:1px 1px 0 #b6452f,2px 2px 0 #b6452f,3px 3px 0 #b6452f">STILL CHAINED</div><div style="font:700 21px Caveat">A link snapped. Try a different order.</div></div>',
     "Still chained", "Le titre en relief tombe de travers (rotation −3°), puis les chiffres d’ordre glissent du mur. Les griffonnages restent."),
    ('<div class="r"><div style="display:flex;gap:6px;width:230px">' + "".join(f'<div style="flex:1;filter:drop-shadow(8px 10px 6px #0003)">{relief_lock(m, opened=True)}</div>' for m in ["iron","brass","shadow","silver"]) + '</div><div style="font:30px Anton;color:#e4654c;text-shadow:1px 1px 0 #b6452f,2px 2px 0 #b6452f,3px 3px 0 #b6452f">CHEST OPEN</div><div style="font:700 19px Caveat">01:52 — 7 days in a row!</div></div>',
     "Chest open", "Les anses sautent l’une après l’autre (+120 ms), et la chaîne glisse du mur et tombe hors du cadre. Un « wow » griffonné vient entourer le temps."),
    ('<div class="r"><svg style="width:200px;height:20px"><rect width="200" height="20" fill="url(#rel-chain)"/></svg><div style="font:700 22px Caveat">Wrapping the chains…</div></div>',
     "Loading", "La lumière du mur glisse lentement (les bandes de soleil se translatent sur 2 s), et la chaîne apparaît maillon par maillon."),
]

page2("05", "relief", "Relief", "mur blanc, objets en relief, griffonnages",
      "La scène est un mur blanc dans une salle, avec la lumière du soleil en biais. Le titre et les numéros d’ordre sont des lettres en relief corail fixées au mur, avec leur ombre portée. Les quatre cadenas sont accrochés à une vraie chaîne. Par-dessus, une main a griffonné les indices, une flèche et un « click », comme si quelqu’un résolvait le coffre au marqueur.",
      [("Mur", "#ecebe7"), ("Sol", "#cbc2b2"), ("Encre", "#161616"), ("Relief", "#e4654c"), ("Relief ombre", "#b6452f")],
      R_FONTS, R_CSS, relief_game(), relief_states,
      "<b>Refs :</b> Gapsy (lettres en relief sur un mur blanc, ombres de soleil, griffonnages à la main), Matchball (objets alignés, grotesque condensée énorme), Merci Studio (une seule couleur franche). "
      "<b>Lecture en 5 s :</b> titre, notes manuscrites, quatre cadenas, chiffres en relief, bouton au sol. "
      "<b>Risque :</b> les bandes de lumière doivent rester discrètes sur un écran de 390 px. "
      "<b>Polices :</b> Anton et Caveat, OFL, intégrées en base64.",
      "Gapsy · Matchball · Merci Studio")

# =====================================================================
# 06 — VEILLEUSE  (MemoryQuest + Funtech + Sponge : objet dans le noir, une lampe, HUD)
# =====================================================================
V_FONTS = font("Archivo", "archivo-black", "archivo-black-latin-400-normal.woff2") + font("JBM", "jetbrains-mono", "jetbrains-mono-latin-400-normal.woff2", 400) + font("JBM", "jetbrains-mono", "jetbrains-mono-latin-700-normal.woff2", 700)
V_CSS = """
.g{--ink:#efe9df;--muted:#8d8579;--acc:#ffd66b;container-type:size;width:100%;height:100%;color:var(--ink);font-family:var(--sans);
background:
 radial-gradient(46% 70% at 50% 0%,#ffd27a30 0%,#ffd27a10 50%,transparent 75%),
 radial-gradient(42% 10% at 50% 78%,#ffd27a26 0%,transparent 70%),
 radial-gradient(40% 30% at 12% 70%,#6a2a2a2a 0%,transparent 70%),
 radial-gradient(40% 30% at 90% 30%,#2a2f5a26 0%,transparent 70%),
 #0b0a0d}
.v{--lw:76px;--cord:150px;position:relative;height:100%;display:flex;flex-direction:column;padding:12px 14px 14px}
.v-top{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center}
.v-lamp{position:absolute;left:50%;top:0;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;pointer-events:none}
.v-lamp i{width:2px;height:var(--cord);background:linear-gradient(#000,#3d363f)}
.v-lamp b{width:78px;height:34px;background:linear-gradient(#332c33,#141116);clip-path:polygon(30% 0,70% 0,100% 100%,0 100%)}
.v-lamp u{width:78px;height:2px;background:#ffd27a;opacity:.7;margin-top:-2px}
.v-lamp em{width:28px;height:9px;border-radius:50%;background:#fff1cf;box-shadow:0 0 16px 6px #ffd27a99,0 0 70px 26px #ffd27a33;margin-top:-1px}
.v-mark{font:19px/1 Archivo;letter-spacing:.01em}
.v-meta{display:flex;gap:6px}
.v-chip{font:700 11px JBM;border:1px solid #ffffff22;border-radius:6px;padding:5px 8px;color:var(--muted)}
.v-chip b{color:var(--ink)}
.v-room{position:relative;flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:auto auto;align-content:end;column-gap:6px;padding-bottom:6%}
.v-chest{position:absolute;left:4%;right:4%;bottom:2%;height:calc(var(--lw)*.95 + 4%);border-radius:20px 20px 8px 8px;background:linear-gradient(#1d1a1f,#121014);
 box-shadow:inset 0 2px 0 #ffd27a66,inset 0 -30px 40px #000a,0 30px 60px #000}
.v-chest::before{content:"";position:absolute;left:0;right:0;top:0;height:30%;border-bottom:2px solid #000;border-radius:20px 20px 0 0;background:linear-gradient(#2a2528,#1a171b);box-shadow:inset 0 2px 0 #ffd27a99}
.v-chain{position:absolute;left:2%;width:96%;bottom:calc(6% + var(--lw)*.98);height:18px}
.v-tip{grid-row:1;align-self:end;justify-self:center;position:relative;margin-bottom:14px;min-width:0;max-width:100%;background:#16141a;border:1px solid #ffffff1c;border-radius:9px;padding:6px 8px;font-size:11.5px;line-height:1.25}
.v-tip b{display:flex;align-items:center;gap:5px;font-size:12px}
.v-tip b::before{content:"";width:6px;height:6px;border-radius:50%;box-shadow:0 0 0 2px #0b0a0d,0 0 0 3px currentColor}
.v-tip span{display:block;font:700 10.5px JBM;color:var(--muted);margin-top:2px}
.v-tip::after{content:"";position:absolute;left:50%;top:100%;width:1px;height:14px;background:#ffffff33}
.v-tip.mute{opacity:.45}
.v-lock{grid-row:2;position:relative;z-index:1;display:flex;flex-direction:column;align-items:center}
.v-lock .lk{width:var(--lw)}
.v-badge{position:absolute;top:44%;font:700 12px JBM;color:#0b0a0d;background:var(--acc);border-radius:5px;padding:2px 6px}
.v-dock{display:grid;grid-template-columns:repeat(4,1fr);gap:4px;padding:5px;background:#141217;border:1px solid #ffffff14;border-radius:14px;margin-bottom:8px}
.v-slot{height:40px;border-radius:9px;display:flex;flex-direction:column;justify-content:center;padding:0 9px;font:700 12px var(--sans);background:#1d1b21}
.v-slot i{font:700 10px JBM;font-style:normal;color:var(--muted)}
.v-slot.e0{background:transparent;border:1px dashed #ffffff22;color:#4b4650}
.v-slot.nx{border-color:var(--acc);color:var(--acc)}
.v-slot.nx i{color:var(--acc)}
.v-act{display:flex;gap:8px}
.v-undo{width:96px;height:46px;border-radius:12px;border:1px solid #ffffff2a;font:700 13px JBM;color:var(--ink)}
.v-go{flex:1;height:46px;border-radius:12px;background:var(--acc);color:#1a1405;font:16px Archivo;box-shadow:0 0 30px #ffd66b33}
.v-go small{font:700 12px JBM;margin-left:8px;opacity:.65}
@container (min-width:600px){.v{--lw:118px;--cord:96px;padding:16px 22px 18px}.v-mark{font-size:24px}.v-room{column-gap:30px;padding:0 60px 6%}.v-tip{font-size:13px;padding:8px 11px}.v-tip b{font-size:14px}
 .v-bottom{display:grid;grid-template-columns:1.3fr 1fr;gap:10px;align-items:center}.v-dock{margin:0}}
.st .v{align-items:center;justify-content:center;gap:8px}
"""

def veille_game():
    tips = ""
    for m in LOCKS:
        say = SAYS.get(m)
        if say:
            tips += f'<div class="v-tip"><b style="color:{RIM[m]}">{CAP(m)}</b><span>{"<br>".join(s.replace("I open ", "opens ").rstrip(".") for s in say)}</span></div>'
        else:
            tips += f'<div class="v-tip mute"><b style="color:{RIM[m]}">{CAP(m)}</b><span>no clue today</span></div>'
    locks = "".join(f'<div class="v-lock">{rim_lock(m, lit=m in QUEUE)}{f"<span class=v-badge>0{QUEUE.index(m)+1}</span>" if m in QUEUE else ""}</div>' for m in LOCKS)
    slots = ""
    for i in range(4):
        if i < len(QUEUE):
            slots += f'<div class="v-slot"><i>0{i+1}</i>{CAP(QUEUE[i])}</div>'
        else:
            slots += f'<div class="v-slot e0{" nx" if i == len(QUEUE) else ""}"><i>0{i+1}</i>{"next" if i == len(QUEUE) else "—"}</div>'
    return f"""<div class="g"><div class="v">
<div class="v-lamp"><i></i><b></b><u></u><em></em></div>
<div class="v-top"><span class="v-mark">VERROUILLAGE</span><span class="v-meta"><span class="v-chip"><b>{CLOCK}</b></span><span class="v-chip">streak <b>{STREAK}</b></span></span></div>
<div class="v-room"><div class="v-chest"></div><svg class="v-chain" preserveAspectRatio="none"><rect width="100%" height="18" fill="url(#rim-chain)"/></svg>{tips}{locks}</div>
<div class="v-bottom"><div class="v-dock">{slots}</div>
<div class="v-act"><button class="v-undo">Undo</button><button class="v-go">Pull all<small>2/4</small></button></div></div>
</div></div>"""

veille_states = [
    ('<div class="v"><div style="position:relative;width:84px;display:flex;justify-content:center">' + rim_lock("iron", lit=True) + '<span class="v-badge" style="top:46%">01</span></div></div>',
     "Lock queued", "La lampe s’allume sur le cadenas : la matière apparaît (200 ms), le badge 01 se pose. Les cadenas pas encore tirés restent en contre-jour."),
    ('<div class="v"><div class="v-tip" style="margin:0"><b style="color:#ffd66b">Still chained</b><span>A link snapped. Try a different order.</span></div></div>',
     "Still chained", "La lampe vacille 2 fois (opacité 1 → .4 → 1, 300 ms) et les cadenas repassent en contre-jour. Le message prend la forme d’une étiquette de la scène."),
    ('<div class="v"><div style="display:flex;gap:6px;width:220px">' + "".join(f'<div style="flex:1">{rim_lock(m, lit=True, opened=True)}</div>' for m in ["iron","brass","shadow","silver"]) + '</div><div style="font:20px Archivo">CHEST OPEN</div><div style="font:700 11px JBM;color:#8d8579">01:52 · STREAK 07</div></div>',
     "Chest open", "Chaque anse s’ouvre sous la lampe (+120 ms), puis le couvercle se soulève et une lumière chaude sort du coffre. C’est le seul moment où la scène s’éclaire en entier."),
    ('<div class="v"><div style="width:6px;height:6px;border-radius:50%;background:#ffd66b;box-shadow:0 0 20px 6px #ffd66b55"></div><div style="font:700 12px JBM;color:#8d8579">Wrapping the chains…</div></div>',
     "Loading", "Le noir complet, puis la lampe s’allume en grésillant (2 éclats). Le libellé actuel du code est conservé."),
]

page2("06", "veilleuse", "Veilleuse", "un coffre dans le noir, une lampe",
      "Le coffre est posé dans une pièce noire, sous une seule lampe. Les cadenas sont d’abord en contre-jour, et chacun a une étiquette de jeu reliée par un fil, qui donne son indice. Quand on tire un cadenas, la lampe l’éclaire et sa matière apparaît. Le bouton jaune est la seule source de couleur vive, comme un bouton d’arcade.",
      [("Nuit", "#0b0a0d"), ("Coffre", "#1d1a1f"), ("Lampe", "#ffd27a"), ("Encre", "#efe9df"), ("Bouton", "#ffd66b")],
      V_FONTS, V_CSS, veille_game(), veille_states,
      "<b>Refs :</b> MemoryQuest (l’objet de jeu comme cadre, la lumière colorée qui déborde), Funtech (étiquettes de scène reliées par un fil, barre d’actions en bas, bouton final jaune), Sponge (la brume, une seule couleur chaude). "
      "<b>Risque :</b> c’est la direction la plus proche d’une esthétique de site d’agence, et son contraste est bas pour les cadenas pas encore tirés. "
      "<b>Polices :</b> Archivo Black et JetBrains Mono, OFL, intégrées en base64.",
      "MemoryQuest · Funtech · Sponge")
print("ok")
