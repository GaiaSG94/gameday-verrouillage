"""Pages restantes en style « Relief » validé : Post, Carte de fin, Séries & classement.
Usage : python3 gen_pages.py <planches/v2> <polices> <gen_planches.py> <gen_v2.py>"""
import sys, pathlib, tempfile

OUT_DIR, FONTS_DIR, V1_PATH, V2_PATH = sys.argv[1:5]
_tmp = tempfile.mkdtemp()
sys.argv = [V2_PATH, _tmp, FONTS_DIR, V1_PATH]
exec(pathlib.Path(V2_PATH).read_text(encoding="utf-8"))  # actifs V1+V2 (sortie jetée)
OUT = pathlib.Path(OUT_DIR)

RELIEF_TXT = "text-shadow:1px 1px 0 #b6452f,2px 2px 0 #b6452f,3px 3px 0 #b6452f,4px 4px 0 #b6452f,10px 14px 12px #00000030"
P_CSS = R_CSS + """
.r-mid{position:relative;flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:14px}
.r-row{display:grid;grid-template-columns:repeat(4,1fr);column-gap:6px;position:relative}
.r-row.nums{padding-top:calc(var(--lw)*.62)}
.r-hand{font:700 22px/1.15 Caveat}
.r-hand.sm{font-size:19px}
.r-big{font:58px/.9 Anton;color:var(--acc);""" + RELIEF_TXT + """}
.r-links{display:block;max-width:100%;filter:drop-shadow(6px 9px 5px #0000002e)}
.r-link-old{display:inline-block;width:34px;height:20px;border:4.5px solid #d6d3cc;border-radius:12px;box-shadow:3px 4px 0 #9a968e,8px 12px 8px #0000002a;margin-right:-9px;background:transparent}
.r-link.off{border-color:#e2e0da;box-shadow:none;border-style:dashed;border-width:2.5px}
.r-note{position:relative;background:#fbfaf7;padding:12px 14px 12px;box-shadow:6px 9px 0 -2px #00000012,10px 16px 14px #0000001f;transform:rotate(-1.2deg)}
.r-note::before{content:"";position:absolute;left:50%;top:-6px;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:#e4654c;box-shadow:inset -2px -2px 0 #b6452f,2px 3px 3px #0003}
.r-board{list-style:none;display:flex;flex-direction:column;gap:2px}
.r-board li{display:grid;grid-template-columns:40px 1fr auto;align-items:baseline;gap:8px;padding:3px 0;border-bottom:1.5px solid #16161614}
.r-board li b{font:26px/1 Anton;color:var(--acc);text-shadow:1px 1px 0 #b6452f,2px 2px 0 #b6452f}
.r-board li span{font:600 13px var(--sans)}
.r-board li i{font:700 21px Caveat;font-style:normal}
.r-board li.me{background:linear-gradient(transparent 20%,#e4654c26 20% 90%,transparent 90%)}
.r-split{display:flex;flex-direction:column;gap:18px}
.r-sec{height:46px;padding:0 14px;border:2px solid var(--ink);font:17px Anton;letter-spacing:.06em;text-transform:uppercase}
@container (min-width:600px){.r-mid{gap:18px;padding:0 30px}.r-big{font-size:76px}.r-row{column-gap:30px;padding:0 30px}
 .r-split{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}}
"""

def wall(inner, floor, sub="", notes=True):
    return f"""<div class="g"><div class="r">
<div class="r-meta"><span>{DAY}</span><span><b>{CLOCK}</b> · <b>{STREAK}</b>-day streak</span></div>
{inner}
<div class="r-floor">{floor}</div>
</div></div>"""

def lock_row(opened=False, nums=None, order=LOCKS, w=None):
    cells = ""
    for i, m in enumerate(order):
        n = f'<span class="r-num">{nums[i]}</span>' if nums else ""
        cells += f'<div class="r-lock">{n}{relief_lock(m, opened=opened)}<span class="r-name">{m}</span></div>'
    style = f' style="--lw:{w}"' if w else ""
    chain = "" if opened else '<svg class="r-chain" style="top:calc(var(--lw)*.42)" preserveAspectRatio="none"><rect width="100%" height="20" fill="url(#rel-chain)"/></svg>'
    return f'<div class="r-row{" nums" if nums else ""}"{style}>{chain}{cells}</div>'

def links(n, off=0, k=1.5):
    w = (n + off) * 30
    ghost = f'<rect x="{n*30}" width="{off*30}" height="20" fill="url(#rel-chain)" opacity=".28"/>' if off else ""
    return f'<svg class="r-links" viewBox="0 0 {w} 20" width="{w*k}" height="{20*k}"><rect width="{n*30}" height="20" fill="url(#rel-chain)"/>{ghost}</svg>'

CIRCLE = '<svg class="r-doodle" style="{pos}" width="{w}" height="{h}" viewBox="0 0 120 60" preserveAspectRatio="none"><path d="M10 34C8 14 46 5 70 7s44 12 40 28-40 22-66 19S6 46 16 22" fill="none" stroke="#161616" stroke-width="2.2" stroke-linecap="round"/></svg>'

# =====================================================================
# 10 — POST (vue inline dans le feed)
# =====================================================================
def post_game(username="u/ferrous_fox", streak=True):
    inner = f"""<h2 class="r-title">VERROUILLAGE</h2>
<div class="r-mid">{lock_row()}
<div class="r-hand" style="text-align:center">Four chained padlocks, one valid order.<br><span style="font-size:.86em">Hi {username}.</span></div>
{'<svg class="r-doodle" style="left:50%;bottom:-6px;margin-left:120px" width="50" height="70" viewBox="0 0 50 70"><path d="M40 4C10 10 6 36 18 62" fill="none" stroke="#161616" stroke-width="2.2" stroke-linecap="round"/><path d="M9 52l9 12 8-12" fill="none" stroke="#161616" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>' if streak else ''}
</div>"""
    return wall(inner, '<button class="r-go">Work the locks<small>today\'s chest</small></button>')

post_states = [
    ('<div class="r" style="--lw:56px"><h2 class="r-title" style="font-size:34px;margin:0">VERROUILLAGE</h2><div class="r-hand sm">Hi u/new_here. First chest?</div></div>',
     "First visit", "Sans série, la méta de droite disparaît. La note de main s’adresse au joueur avec la phrase actuelle du splash (« Hi {username} »)."),
    ('<div class="r"><div style="display:flex;gap:6px;width:220px">' + "".join(f'<div style="flex:1;filter:drop-shadow(8px 10px 6px #0003)">{relief_lock(m, opened=True)}</div>' for m in LOCKS) + '</div><div class="r-hand sm">Opened in 01:52. See you tomorrow.</div><button class="r-sec" style="height:34px;font-size:14px">See today\'s board</button></div>',
     "Already solved", "Si solvedToday : les anses sont levées dans le feed. Le bouton mène à la carte de fin (libellé à valider)."),
    ('<div class="r"><div style="font:30px Anton;color:#e4654c;' + RELIEF_TXT + '">VERROUILLAGE</div><svg style="width:200px;height:20px"><rect width="200" height="20" fill="url(#rel-chain)"/></svg></div>',
     "Loading", "Le titre est déjà là (HTML statique), la chaîne apparaît maillon par maillon. Le splash reste léger : pas de polices de la main avant l’ouverture."),
    ('<div class="r"><div class="r-hand">Lost the key.</div><div class="r-hand sm">Try again.</div><button class="r-sec" style="height:34px;font-size:14px">Retry</button></div>',
     "Error", "Erreur réseau : note de main, sans rouge. Remplace le message brut du code (« init failed: … »)."),
]

page2("10", "post", "Post", "page 1 · le post dans le feed",
      "Le post fermé, tel qu’on le croise dans le feed : le mur, le titre en relief, les quatre cadenas encore sur leur chaîne, et la phrase actuelle du splash écrite à la main. Un seul bouton au sol, avec le libellé actuel du code : « Work the locks ».",
      [("Mur", "#ecebe7"), ("Sol", "#cbc2b2"), ("Encre", "#161616"), ("Relief", "#e4654c"), ("Relief ombre", "#b6452f")],
      R_FONTS, P_CSS, post_game(), post_states,
      "<b>Contenu :</b> repris de <code>splash.tsx</code> (titre, « Four chained padlocks, one valid order. Hi {username}. », « Work the locks »). "
      "<b>Lecture dans le feed :</b> c’est le seul post clair avec du relief corail ; les cadenas fermés suffisent à dire « jeu à ouvrir ». "
      "<b>Build :</b> le splash doit rester léger (pas de Caveat ni de SVG lourds) ; la note de main peut être une image du texte rendu.",
      "style Relief validé")

# =====================================================================
# 11 — CARTE DE FIN
# =====================================================================
WIN_ORDER = ["iron", "brass", "shadow", "silver"]

def end_game():
    inner = f"""<h2 class="r-title" style="margin-bottom:0">CHEST OPEN</h2>
<div class="r-mid">{lock_row(opened=True, nums=[1, 2, 3, 4], order=WIN_ORDER)}
<div class="r-split"><div style="position:relative;text-align:center"><div class="r-hand">Freed in <b style="position:relative;font-size:1.3em;padding:0 6px">01:52{CIRCLE.format(pos="left:-10px;top:-6px", w=100, h=48)}</b></div>
<div style="margin-top:8px">{links(7)}</div>
<div class="r-hand sm" style="margin-top:6px">7 days in a row. Four new padlocks tomorrow.</div></div>
<div class="r-note"><div style="font:600 11px var(--sans);color:#6f6c66;margin-bottom:4px">Your comment</div><div class="r-hand sm">Opened today's chest in 01:52 — 7 days in a row. No spoilers.</div></div></div>
</div>"""
    floor = '<button class="r-sec">Streaks</button><button class="r-go">Comment my time<small>one tap</small></button>'
    return wall(inner, floor)

end_states = [
    ('<div class="r"><div style="font:34px Anton;color:#e4654c;' + RELIEF_TXT + '">STILL CHAINED</div><div class="r-hand sm">A link snapped. Try a different order.</div><button class="r-go" style="flex:none;height:36px;padding:0 18px;font-size:15px">Back to the chest</button></div>',
     "Wrong order", "Textes actuels du code. Les chiffres d’ordre glissent du mur, la file se vide, et le chrono continue."),
    ('<div class="r"><div class="r-note" style="max-width:250px"><div class="r-hand sm">Opened today\'s chest in 01:52 — 7 days in a row.</div></div><div class="r-hand" style="margin-top:6px">Posted. See you tomorrow.</div></div>',
     "Comment posted", "La note se décolle et file vers le haut (vers les commentaires), et un « posted » griffonné la remplace. Le bouton devient « See the thread »."),
    ('<div class="r"><div style="margin-bottom:2px">' + links(1) + '</div><div class="r-hand">Day one. Come back tomorrow.</div></div>',
     "First win", "Série de 1 : un seul maillon en relief sur le mur. Le texte change avec la série (1, 2–6, 7+)."),
    ('<div class="r"><div style="margin-bottom:2px">' + links(3, off=2) + '</div><div class="r-hand sm">The chain broke yesterday. New chain, day one.</div></div>',
     "Streak lost", "Si la série est retombée à zéro, les anciens maillons sont en pointillé. Ton neutre, sans culpabiliser."),
]

page2("11", "carte-de-fin", "Carte de fin", "page 3 · résultat, série, commentaire",
      "Le coffre est ouvert : les anses sont levées et les chiffres en relief montrent l’ordre trouvé. Le temps est entouré au marqueur, et la série s’affiche en maillons de chaîne en relief, un par jour. À droite, la note épinglée montre le commentaire qui partira en un geste. Elle ne révèle pas l’ordre, donc pas de spoiler dans le fil.",
      [("Mur", "#ecebe7"), ("Sol", "#cbc2b2"), ("Encre", "#161616"), ("Relief", "#e4654c"), ("Note", "#fbfaf7")],
      R_FONTS, P_CSS, end_game(), end_states,
      "<b>Ce qui vient du code :</b> « Chest open », « Still chained », « A link snapped. Try a different order. », « Four new padlocks tomorrow. », « Back to the chest », le temps et la série. "
      "<b>Ce qui vient d’IDEE.md :</b> l’invitation à commenter en un geste. <b>À trancher (question 6 de PAGES.md) :</b> le texte exact du commentaire. Je propose temps + série, sans l’ordre. "
      "<b>Ajout de style :</b> la note épinglée (papier, punaise corail), qui sert aussi à la page Séries.",
      "style Relief validé")

# =====================================================================
# 12 — SÉRIES & CLASSEMENT
# =====================================================================
BOARD = [("1", "u/quiet_hinge", "00:38"), ("2", "u/latchkey_lou", "00:51"), ("3", "u/brass_tacks", "01:04"),
         ("4", "u/tumbler9", "01:09"), ("5", "u/oddbolt", "01:17")]

def series_game():
    rows = "".join(f'<li><b>{r}</b><span>{u}</span><i>{t}</i></li>' for r, u, t in BOARD)
    rows += '<li style="border:0;padding:0;height:6px"></li><li class="me"><b>38</b><span>you</span><i>01:52</i></li>'
    inner = f"""<h2 class="r-title" style="margin-bottom:0">YOUR CHAIN</h2>
<div class="r-mid"><div class="r-split">
<div><div style="display:flex;align-items:flex-end;gap:14px"><span class="r-big">7</span><span class="r-hand" style="padding-bottom:6px">days in a row</span></div>
<div style="margin-top:12px">{links(7)}</div>
<div class="r-hand sm" style="margin-top:8px">Miss a day and the chain starts over.</div></div>
<div class="r-note" style="transform:rotate(.8deg)"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px"><span style="font:18px Anton;letter-spacing:.04em">TODAY'S FASTEST</span><span style="font:600 11px var(--sans);color:#6f6c66">Dec 11</span></div>
<ul class="r-board">{rows}</ul></div>
</div></div>"""
    floor = '<button class="r-go">Back to the chest</button>'
    return wall(inner, floor)

series_states = [
    ('<div class="r"><span class="r-big" style="font-size:48px">0</span><div class="r-hand sm">No chain yet. Open today\'s chest to start one.</div></div>',
     "No streak", "Série à zéro : le grand chiffre reste, avec une seule phrase d’invitation, sans maillons fantômes."),
    ('<div class="r"><div class="r-note" style="width:260px"><ul class="r-board"><li><b>1</b><span>u/quiet_hinge</span><i>00:38</i></li><li><b>2</b><span>u/latchkey_lou</span><i>00:51</i></li><li class="me"><b>3</b><span>you</span><i>00:59</i></li></ul></div></div>',
     "You're on the podium", "Si le joueur est dans le top 5, sa ligne est surlignée dans la liste et la ligne « you » du bas disparaît."),
    ('<div class="r"><div class="r-hand">Be the first to open it today.</div></div>',
     "Empty board", "Personne n’a encore ouvert le coffre du jour (juste après minuit UTC)."),
    ('<div class="r"><div style="max-width:250px;overflow:hidden;white-space:nowrap">' + links(12) + '</div><div class="r-hand sm">42 days in a row</div></div>',
     "Long streak", "Au-delà de 10 maillons, la chaîne sort du cadre à droite, et seul le chiffre en relief compte."),
]

page2("12", "series-classement", "Séries & classement", "page 4 · série et communauté",
      "À gauche, la série du joueur : un grand chiffre en relief et la chaîne des jours, un maillon par jour. À droite, une note épinglée liste les ouvertures les plus rapides du jour, avec la ligne du joueur surlignée en dessous. Les deux mêmes gestes qu’ailleurs : le relief pour ce qui est acquis, la main pour ce qui se raconte.",
      [("Mur", "#ecebe7"), ("Sol", "#cbc2b2"), ("Encre", "#161616"), ("Relief", "#e4654c"), ("Note", "#fbfaf7")],
      R_FONTS, P_CSS, series_game(), series_states,
      "<b>Hypothèse à valider (question 4 de PAGES.md) :</b> le score communautaire est le temps d’ouverture du jour. Le serveur calcule déjà <code>elapsedMs</code> mais ne le stocke pas, et il ne garde que la série. "
      "<b>Données de démo :</b> les pseudos et les temps sont fictifs. "
      "<b>Pas dessiné :</b> la meilleure série et l’historique jour par jour, que le serveur ne stocke pas.",
      "style Relief validé")
print("ok")
