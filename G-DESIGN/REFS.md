# REFS — Verrouillage

> Ouvertes le 2026-11-18 dans le navigateur intégré. On prend des **principes**, jamais un layout, un texte, un asset ou une marque.

## Shutabug — shutabug.com

Observé : une galerie 3D courbe sur fond os très clair ; les tirages sont les seuls éléments colorés, posés dans des niches arrondies, au-dessus d'un sol qui s'incurve. L'interface est minuscule — capitales monospaces espacées, pilules fines — et reléguée aux bords. Une seule ligne d'aide centrée en bas.

Ce qu'on retient :
- **L'objet porte la couleur, l'UI reste neutre.** Ici c'est idéal : les quatre cadenas *sont* quatre matières (laiton, fer, argent, ombre) — pas besoin d'inventer un code couleur.
- **Lumière de studio et ombre au sol** pour donner du poids, plutôt que des cartes et des bordures.
- **Densité typo très basse** : une ligne de règle, pas de paragraphe.

Utilisé surtout par la direction 02 « Atelier ».

## Framer — framer.com

Observé : fond noir quasi pur, titres en grotesque serrée blanche, gros corps, interlignage court ; un seul point lumineux coloré par écran ; sections séparées par des filets 1 px gris très sombre, pas par des fonds colorés. Les éléments entrent par un fondu + petite translation, courts et amortis, jamais de rebond.

Ce qu'on retient :
- **Retenue** : un seul accent par écran, le reste en niveaux de gris.
- **Filets 1 px** plutôt que des boîtes pleines pour structurer.
- **Mouvement court et amorti** (≈ 200–320 ms, ease-out), l'élan est réservé à *un* moment : chez nous, le déclic et la cascade d'ouverture.
- **Grotesque serrée, gros corps** pour l'unique titre.

Utilisé surtout par les directions 01 « Forge » (filets, accent unique) et 03 « Cascade » (fond nuit, point lumineux unique).

## Ce qu'on ne prend pas

- Le parcours 3D de Shutabug (couteux, illisible à 390 px) et ses œuvres.
- Les mockups produit, le dégradé bleu et les textes marketing de Framer.
- Aucune police de ces sites : piles système dans les planches ; polices libres (OFL) embarquées au build à cause de la CSP Devvit.

---

## V2 — 2026-11-18 — famille `narratif-jeu` (demande de Gaia après le rejet de la V1)

Source : `REFERENCES-CAPTURES/narratif-jeu/` (catalogue V2 de `REFERENCES-DESIGN.md`, worktree `hackatons-wt/temoignages-design-v1`). Captures lues une par une. Shutabug et Framer sont abandonnées : elles ont produit une V1 jugée « slop IA ».

Ce que la famille a en commun, et que la V1 n'avait pas : **une scène avec des personnages, une voix, du trait à la main, une typo qui a du caractère**. Pas de cartes, pas de dégradés décoratifs, pas de capitales espacées partout.

| Ref | Observé | Pris pour |
|---|---|---|
| Don't Look Up (jeu) | Trait noir sur crème, bonshommes avec des bulles (« whatever », « hm »), titre énorme dessiné à la main, une phrase d'accroche drôle, boutons blanc / noir à ombre dure décalée | **04 Encre** : cadenas personnages, indices en bulles, boutons à ombre dure |
| Gemeos | Stickers cernés de blanc, aplats francs, titre gras irrégulier, griffonnages (flèche, zigzag) | **04 Encre** : aplats cernés, hachures |
| Gapsy Studio | Lettres corail en relief fixées sur un mur blanc, ombres de soleil en biais, sol en bois, griffonnages noirs (« WOW », flèche) par-dessus | **05 Relief** : titre et chiffres en relief, lumière en biais, notes et flèches à la main |
| Matchball | Objets alignés en rangée sur fond clair avec ombre au sol, grotesque condensée énorme, une ligne de règle | **05 Relief** : rangée de cadenas, Anton |
| Merci Studio | Un aplat de couleur unique + un objet 3D en contour | **05 Relief** : une seule couleur franche |
| MemoryQuest | L'objet de jeu (borne d'arcade) est le cadre, lumière colorée qui déborde dans le noir | **06 Veilleuse** : le coffre dans le noir comme cadre |
| Funtech | Scène nocturne, étiquette reliée par un fil (« Hold to dance · 2.7 s to go »), barre d'actions segmentée en bas, bouton final jaune | **06 Veilleuse** : étiquettes d'indice reliées, dock, bouton jaune |
| Sponge | Brume rouge sombre, une créature éclairée, une seule couleur chaude | **06 Veilleuse** : brume, lumière chaude unique |
| Raben Rifaie | Fenêtre sur une scène calme, serif italique | Non retenu (trop éditorial pour un jeu quotidien) |
| Dairy Food Bulgaria | Île 3D réaliste flottante | Non retenu (3D lourde, hors budget) |

On ne prend aucun asset, aucun texte et aucune police de ces sites. Les polices des planches V2 sont libres (OFL, via @fontsource) et intégrées en base64.
