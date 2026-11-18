# PAGES — Verrouillage

> Statuts : à dessiner / en revue / validée. Style **Relief** validé et verrouillé (/lock) le 2026-11-18 (voir `STYLE.md`).
> Chaque planche montre le cadre desktop 1440 × 900 et le cadre mobile 390 × 844 côte à côte.
> Données de démo : vrai coffre généré par `generateOrder('2026-12-11')` — solution iron › brass › shadow › silver, 3 indices :
> « the iron lock is the first to open », « the silver lock is the fourth to open », « the brass lock opens before the shadow lock ».
> État montré : le joueur a déjà tiré iron (#1) et brass (#2), à 01:24, série 6.

| # | Page | Rôle | Contenu clé | Statut |
|---|------|------|-------------|--------|
| 1 | **Post** | Vue dans le feed (splash inline) : donner envie d'ouvrir le coffre du jour | En-tête du post, coffre fermé aux 4 cadenas, date du jour, série du joueur, bouton d'entrée | **validée** — `planches/v2/10-post.html` (2026-11-18) |
| 2 | **Jeu** | Écran principal, une seule règle : « Pull the four locks in the one order the tag allows » | 4 cadenas (brass, iron, silver, shadow) sur la chaîne, file d'ordre 1–4, étiquette d'indices, chrono, série, Undo, Pull all (n/4) | **validée** — style Relief, `planches/v2/05-relief.html` (2026-11-18) |
| 3 | **Carte de fin** | Résultat + boucle quotidienne + accroche commentaire | Cascade d'ouverture, « Chest open » / « Still chained », temps, série, invitation à commenter en un geste, « Four new padlocks tomorrow » | **validée** — `planches/v2/11-carte-de-fin.html` (2026-11-18) |
| 4 | **Séries & classement** | Montrer la série et la communauté | Série perso, scores de la communauté du jour | **validée** — `planches/v2/12-series-classement.html` (2026-11-18 ; métrique supposée : temps d'ouverture, question 4) |

États transverses (dessinés dans la planche Jeu, panneau « États ») : cadenas mis en file, mauvais ordre, cascade de victoire, chargement « Wrapping the chains… » (libellé actuel du code), déjà résolu aujourd'hui (`solvedToday` existe dans l'API).

## Questions produit ouvertes (non tranchées)

1. **Le générateur ne garantit pas l'unicité.** Sur 365 jours testés (01/12/2026 → 30/11/2027), **8 coffres ont 2 ordres valides** (ex. 2026-12-12 : seulement « shadow first » + « silver fourth », brass/iron interchangeables). Le serveur n'accepte que l'ordre stocké : un joueur qui raisonne juste peut perdre. À corriger côté générateur avant le build (hors périmètre design, signalé).
2. **Indices en phrases ou en notation ?** Les planches gardent l'anglais du code mais compacté (« Iron opens 1st », « Brass before Shadow »), avec la pastille de matière. Une notation purement symbolique (`IRON = 1`, `BRASS ‹ SHADOW`) est possible : à choisir.
3. **Essais illimités** (comportement actuel : « Back to the chest » après un échec) ou nombre de tentatives compté ? Les planches montrent « Still chained » sans compteur.
4. **Scores communautaires** (page 4) : le serveur ne stocke que la série. Quelle métrique : temps d'ouverture, % de joueurs qui ont ouvert du premier coup, nombre d'essais ?
5. **Le chrono est-il affiché** pendant le jeu ? Il existe dans le code (00:00) ; une partie des joueurs le vit comme une pression. Les planches l'affichent, discret.
6. **Accroche commentaire** : que poste le « one-tap comment » (temps + série en texte ? grille d'ordre masquée ?) — décision produit à prendre avant la page 3.
