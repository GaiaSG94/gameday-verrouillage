# DESIGN — Verrouillage (journal)

> Versions datées, jamais écrasées. Tenu par Claude (rôle DA), d'après `PROMPT-DESIGN.md`.

## V1 — 2026-11-18 — Exploration page « Jeu » (étape B)

**Livré**
- `PAGES.md` : 4 pages proposées (Post, Jeu, Carte de fin, Séries & classement) + 6 questions produit ouvertes.
- `REFS.md` : Shutabug et Framer ouvertes et décodées (principes retenus / exclus).
- `planches/v1/01-forge.html` — **Forge** (direction du brief) : plaque d'acier brossé `#2b2f36`, chaîne horizontale réelle, cadenas pendus, file 01–04 en plaques tamponnées, étiquette d'indices en laiton `#b08d57` rivetée, accent `#ff5d5d` sur la case suivante et Pull all.
- `planches/v1/02-atelier.html` — **Atelier** : fond os `#eceae4`, cadenas posés comme des objets de studio avec ombre au sol, UI en capitales mono, file en pilules, indices centrés, bouton noir ; rouge uniquement sur la case suivante.
- `planches/v1/03-cascade.html` — **Cascade** (écart au brief) : chaîne verticale qui pend du haut du post, 4 cadenas l'un sous l'autre, chiffres d'ordre à gauche ; nuit `#0d1015`, accent vert-de-gris `#5fd3a8` à la place du rouge ; grotesque condensée.
- `tools/gen_planches.py` : générateur des 3 planches (données et cadenas SVG partagés). `python3 tools/gen_planches.py planches/v1`.

Chaque planche : cadre desktop 1440 × 900 + cadre mobile 390 × 844 côte à côte, dans un post (en-tête neutre, sans marque), panneau « États & mouvement » (mise en file, mauvais ordre, cascade, chargement, déjà résolu). Données réelles du générateur pour le 2026-12-11 (joueur à 2/4 : iron #1, brass #2).

**Décisions**
- Les quatre cadenas portent leur matière (laiton, fer, argent, ombre) : c'est le code couleur du jeu, l'UI reste neutre. Plus d'emoji (le code actuel en utilise).
- Indices : anglais du code compacté (« Iron opens 1st », « Brass opens before Shadow ») + pastille de matière. Notation symbolique possible (question 2).
- Une seule couleur d'accent par direction ; grotesque lourde pour les titres, mono pour chiffres et chrono.
- Polices : piles système dans les planches (aucune requête réseau). Au build, polices libres (OFL) embarquées à cause de la CSP Devvit.

**Signalé hors design** : le générateur produit ~2 % de coffres à deux solutions (8/365, ex. 2026-12-12) — question 1 de `PAGES.md`.

**En attente** : choix de direction par Gaia, réponses aux questions de `PAGES.md`. Ensuite : `STYLE.md` puis planches Post, Carte de fin, Séries & classement.

## V2 — 2026-11-18 — Exploration page « Jeu », refs `narratif-jeu`

**Retour de Gaia sur V1** : aucune des trois, « ça fait trop slop IA ». S'appuyer sur la famille de refs `narratif-jeu`.

**Diagnostic** : la V1 avait l'allure d'une interface générique (cartes, dégradés métalliques, capitales mono espacées, accent unique sur fond sombre). Il lui manquait une scène, une voix et un trait.

**Livré** (`planches/v2/`, les fichiers V1 sont conservés)
- `04-encre.html` — **Encre** (Don't Look Up, Gemeos) : trait d'encre tremblé sur papier crème. Les cadenas ont des yeux et disent eux-mêmes leur indice dans une bulle ; Shadow, sans indice ce jour-là, se tait (« … »). Les cases d'ordre sont des plaques posées sur le coffre, le tampon rouge `#e5482f` numérote les cadenas tirés, et les boutons ont une ombre dure. Polices : Bowlby One, Patrick Hand, JetBrains Mono.
- `05-relief.html` — **Relief** (Gapsy, Matchball, Merci) : mur blanc avec la lumière du soleil en biais, titre et chiffres d'ordre en lettres corail `#e4654c` en relief, cadenas accrochés à une chaîne, indices et « who's 3rd ? » griffonnés à la main, boutons posés au sol. Polices : Anton, Caveat.
- `06-veilleuse.html` — **Veilleuse** (MemoryQuest, Funtech, Sponge) : coffre dans une pièce noire sous une lampe suspendue, cadenas en contre-jour qui prennent la lumière quand on les tire, étiquettes d'indice reliées par un fil, dock d'ordre et bouton jaune `#ffd66b`. Polices : Archivo Black, JetBrains Mono.
- `tools/gen_v2.py` : générateur (reprend l'hôte et les données de `gen_planches.py`).

**Décisions**
- Les indices réels du générateur sont reformulés à la première personne (« I open first. », « I open before Shadow. ») et attribués au cadenas concerné. C'est un choix de texte, pas une nouvelle fonctionnalité : à valider.
- Polices OFL intégrées en base64 : chaque planche s'ouvre toujours sans réseau ni serveur.

**En attente** : choix de direction parmi 04 / 05 / 06. Les questions de `PAGES.md` restent ouvertes.

## V3 — 2026-11-18 — Style « Relief » validé, déclinaison (étape C)

**Retour de Gaia sur V2** : direction **05 Relief** validée.

**Livré**
- `STYLE.md` : les trois couches (mur, relief, main), la palette avec ses hex, la typo (Anton et Caveat), les recettes du relief et du griffonnage, la grille, les composants, le mouvement et les états.
- `planches/v2/10-post.html` — **Post** : le post fermé dans le feed. Textes repris de `splash.tsx` (« Four chained padlocks, one valid order. Hi {username}. », « Work the locks »). États : première visite, déjà résolu, chargement, erreur.
- `planches/v2/11-carte-de-fin.html` — **Carte de fin** : coffre ouvert avec l'ordre en chiffres en relief, temps entouré au marqueur, série en maillons de chaîne, note épinglée avec le commentaire proposé (temps + série, sans l'ordre) et le bouton « Comment my time ». États : mauvais ordre, commentaire posté, première victoire, série perdue.
- `planches/v2/12-series-classement.html` — **Séries & classement** : série en grand chiffre et en chaîne, plus une note épinglée « Today's fastest » (top 5 et la ligne du joueur). États : pas de série, podium, classement vide, longue série.
- `tools/gen_pages.py` : générateur des trois pages.

**Décisions**
- Ajout au style : la **note épinglée** (papier, punaise corail), qui porte ce que la communauté voit (commentaire, classement).
- La série se dessine en maillons de chaîne, un par jour : c'est le motif du jeu, et ce n'est pas un thème Reddit.

**Hypothèses à valider** : texte du commentaire (question 6), métrique du classement = temps d'ouverture (question 4, le serveur ne stocke pas `elapsedMs` aujourd'hui). Les pseudos et les temps du classement sont fictifs.

**Prochaine étape** : revue des trois pages. `/lock` seulement quand les quatre pages seront validées.

## V3.1 — 2026-11-18 — Toutes les pages validées

**Retour de Gaia** : Post, Carte de fin et Séries & classement validées telles quelles. Les quatre pages ont donc leur planche validée (`PAGES.md`), et `/lock` est possible.

**Restent ouverts (produit, pas style)** : unicité du générateur (question 1), texte exact du commentaire (question 6), métrique du classement et stockage de `elapsedMs` (question 4), essais illimités (question 3).

## V4 — 2026-11-18 — /lock

Style **Relief** verrouillé : fin des explorations. Références de build : `STYLE.md` + `planches/v2/05-relief.html` (Jeu), `10-post.html`, `11-carte-de-fin.html`, `12-series-classement.html`. Les planches V1 (01–03) et V2 non retenues (04, 06) restent comme archive.
