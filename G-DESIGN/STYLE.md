# STYLE — Verrouillage · direction « Relief »

> Validée par Gaia le 2026-11-18 (V2, planche `planches/v2/05-relief.html`). Ce fichier fait foi pour toutes les pages et pour le build.
> Refs : Gapsy (relief sur mur blanc, soleil en biais, griffonnages), Matchball (objets en rangée, grotesque condensée), Merci Studio (une couleur franche).

## 1. Idée

Une salle blanche avec la lumière du soleil en biais. Ce qui compte est **fixé au mur en relief** : le titre, les chiffres d'ordre, les cadenas sur leur chaîne. Par-dessus, **une main griffonne au marqueur** : les indices, une flèche, un « click ». Les actions sont **posées au sol**.

Trois couches, jamais mélangées :
1. **Mur** : le fond et sa lumière.
2. **Relief** : les objets fixés (titre, chiffres, cadenas, chaîne), avec leur extrusion et leur ombre portée.
3. **Main** : l'écriture et les traits au marqueur, sans ombre, posés à plat.

## 2. Palette

| Rôle | Hex | Usage |
|---|---|---|
| Mur | `#ecebe7` | Fond (dégradé `#e6e4df` → `#efeeea`) |
| Soleil | `#ffffff` à 44–55 % | Bandes de lumière à 118° |
| Ombre de mur | `#000000` à 4–5 % | Bandes d'ombre à 118° |
| Sol | `#d8d0c2` → `#cbc2b2` | Bande d'actions en bas |
| Encre | `#161616` | Texte, griffonnages, bouton principal |
| Encre douce | `#6f6c66` | Méta (date, chrono) |
| **Relief** (accent unique) | `#e4654c` | Titre, chiffres d'ordre, surlignage d'indice |
| Relief ombre | `#b6452f` | Extrusion du relief uniquement |

**Matières des cadenas** (couleurs d'objets, pas d'UI) : laiton `#d8a54c` / `#9a7232`, fer `#80868e` / `#4e535a`, argent `#f6f5f2` / `#b5b7ba`, ombre `#2c2c2e` / `#0e0e0f` (face / extrusion).

Règles : le corail est la seule couleur d'interface, et il ne sert qu'au relief et au surlignage. Pas de dégradé de couleur, et pas d'emoji.

## 3. Typo

Polices libres (OFL), embarquées au build à cause de la CSP Devvit :

| Rôle | Police | Taille mobile / desktop |
|---|---|---|
| Titre en relief | Anton 400 | 44 / 64 px, interligne .9 |
| Chiffres d'ordre en relief | Anton 400 | 46 / 60 px |
| Libellés objets, boutons | Anton 400, capitales, +0.06em | 15–19 px |
| Main (indices, notes, messages) | Caveat 700 | 21–26 px |
| Méta (date, chrono, série) | Sans système 600 | 11 px |

Pas de capitales espacées hors Anton, et pas de mono.

## 4. Relief (recette)

- **Texte** : `text-shadow` empilé de 1 à 5 px en `#b6452f`, plus une ombre portée `14px 18px 16px rgba(0,0,0,.19)`. Pour les petits corps, 3 couches suffisent.
- **Objets SVG** : un calque d'extrusion décalé de (4, 5.2) dans la teinte sombre, plus `drop-shadow(12px 16px 10px rgba(74,58,42,.25))`.
- La lumière vient du **haut-gauche**, donc toutes les ombres partent vers le bas-droite. Aucune exception.

## 5. Main (recette)

- Écriture en Caveat 700 encre, sans ombre.
- **Surlignage** des noms de cadenas : bande corail à 33 % sur le bas du mot (72–92 %).
- **Griffonnages** en SVG, trait 2–2.2 px, `linecap round` : flèche courbe, étoile « click », cercle, soulignement. Au plus 2 griffonnages par écran.
- Une note se lit comme si quelqu'un résolvait le coffre à côté du joueur : elle pose une question ou commente, elle ne donne pas d'ordre (« who's 3rd ? »).

## 6. Grille et cadre

- Le post occupe 390 × 672 sur mobile (zone de jeu) et 736 × 620 sur desktop.
- Marges : 16 px sur mobile, 28 px sur desktop. La bande de sol fait 72–76 px et touche les bords.
- Ordre de lecture, de haut en bas : méta → titre → phrase de règle → notes → mur aux objets → sol.
- Desktop : les notes passent en haut à droite, alignées à droite, et le mur gagne un retrait de 60 px.

## 7. Composants

| Composant | Spéc |
|---|---|
| Bouton principal | Rectangle encre plein, sans arrondi, 46 px, Anton capitales blanc ; compteur en Caveat corail (« 2 of 4 ») |
| Bouton secondaire | Contour encre 2 px, fond transparent, mêmes dimensions |
| Cadenas | Viewbox 104 × 140, largeur 80 px mobile / 112 px desktop, nom Anton sous l'objet |
| Chaîne | Pattern de maillons gris clairs, avec ombre portée sur le mur |
| Chiffre d'ordre | Anton corail en relief, centré au-dessus du cadenas à −0.62 × largeur |
| Note | Caveat, tiret de main en tête de ligne |
| Méta | Une ligne, gauche = date, droite = chrono et série |

## 8. Mouvement

| Moment | Animation |
|---|---|
| Entrée | Les bandes de lumière glissent de 20 px (600 ms, ease-out), puis les objets tombent sur le mur l'un après l'autre (+60 ms) |
| Tirer un cadenas | Le chiffre en relief tombe de 12 px et son ombre se resserre (220 ms, ease-out) ; un « click » griffonné apparaît puis s'efface (400 ms) |
| Undo | Le chiffre se décolle et remonte (160 ms) |
| Mauvais ordre | Le titre « Still chained » tombe de travers (−3°), puis les chiffres glissent du mur |
| Victoire | Les anses sautent l'une après l'autre (+120 ms), puis la chaîne glisse et tombe hors du cadre ; un cercle griffonné entoure le temps |
| Chargement | La lumière glisse sur 2 s, et la chaîne apparaît maillon par maillon |

Durées : 160–320 ms, ease-out, pas de rebond, sauf pour l'anse qui saute. Avec `prefers-reduced-motion`, on passe en fondus de 120 ms.

## 9. États

| État | Règle |
|---|---|
| Cadenas libre | Plein, à sa couleur, sans chiffre |
| Cadenas tiré | Chiffre corail en relief au-dessus de lui |
| Cadenas pressé | Recule de 2 px, et l'ombre se raccourcit |
| Bouton désactivé | Opacité 35 % (Pull all reste désactivé tant que la file n'est pas pleine) |
| Erreur réseau | Note à la main en encre : « Lost the key. Try again. » + bouton secondaire |
| Déjà résolu | Écran figé sur le coffre ouvert, avec un lien vers la carte de fin |
