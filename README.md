# UNIMARC Explorer — édition documentée 0.3

127 fiches documentées, réparties dans les dix blocs. Référence principale : **Format UNIMARC des notices bibliographiques fournies par la BnF, version 11.0 (2023)**. Vingt-deux zones absentes de ce document sont couvertes par des compléments officiels français, identifiés dans les fiches.

**Application en ligne : [UNIMARC Explorer](https://didierthebault-web.github.io/unimarc-explorer/)**. Publication et fonctionnement public vérifiés le 23 octobre 2026. Les modifications de la branche `main` sont publiées automatiquement par le workflow GitHub Pages ; voir [le guide de publication](docs/PUBLICATION-GITHUB.md).

## Utilisation

Ouvrir `unimarc-explorer.html` dans un navigateur, sans installation, serveur ou connexion. La version organisée s’ouvre aussi directement par `index.html`.

1. Choisir un bloc, puis un champ. Les blocs de plus de dix champs proposent des pages précédentes et suivantes ; tous les champs restent accessibles dans le panneau. Le panneau présente son rôle et un exemple.
2. Cliquer sur « Lire la fiche & son anatomie » pour consulter les explications, indicateurs, occurrences documentées, exemples décomposés et références.
3. Activer « Mode expert » pour afficher toutes les sous-zones recensées pour la fiche et les distinctions entre format, règles de catalogage et paramétrage du SIGB.
4. Utiliser la liste « Consulter un autre champ » pour parcourir les 127 fiches sans revenir à la carte.
5. Rechercher par numéro, titre, fonction, mot-clé ou sous-zone : ISBN, auteur, publication, résumé, 606, $j… Les résultats ouvrent directement la fiche complète.

Les segments des exemples sont cliquables et accessibles au clavier. Les zones de contrôle 001, 003 et 005 sont présentées sans indicateurs ni sous-zones. Pour les zones codées, dont 100, 105, 106, 110, 115, 117, 121, 135, 181 et 182, un tableau explique les positions codées de l’exemple.

Le bouton de copie copie une **représentation pédagogique** : `#` représente un blanc et `|` un caractère de remplissage. Ce résultat ne constitue pas un export ISO 2709. Les exemples sont réduits et fictifs, sauf l’ARK 003 explicitement repris de la source. Les points d’accès d’autorité fictifs ne sont pas présentés comme des autorités validées.

Le quiz pilote reste disponible. La construction progressive d’une notice complète et les simulations SIGB/portail ne font pas partie de cette mise à jour documentaire.

## Clavier et mobile

Tab parcourt les actions ; Entrée ou Espace active les cercles. `/` place le focus dans la recherche ; Échap ferme les résultats. Les préférences système de réduction des animations sont respectées. Sur smartphone, une grille lisible remplace la carte. Les longues fiches et leurs tableaux restent consultables.

Les liens externes vers les sources nécessitent une connexion. Les fiches et toutes leurs interactions restent disponibles hors connexion. Des copies des documents consultés sont conservées sous `docs/` et `docs/sources/`, avec leurs crédits.

## Source éditoriale et génération

- `data/unimarc.json` : **source éditoriale unique** des blocs, fiches, sous-zones et références. Elle peut être modifiée directement.
- `data/exemples.json` : exemples générés avec leurs limites et leur provenance.
- `data/catalogue.js` : pont généré pour un chargement direct sans `fetch`.
- `app.js` : moteur de navigation, recherche, fiches et anatomie, indépendant des étiquettes particulières.
- `styles.css` : présentation et adaptations responsive.
- `scripts/build.cjs` : validation minimale, génération des données embarquées, de l’inventaire et du fichier autonome ; **ne réécrit pas unimarc.json**.

Après modification des données ou de l’interface, exécuter `node scripts/build.cjs` depuis le dossier du projet.

L’extension 0.3 ajoute 68 champs pour les périodiques, le numérique, le son, la vidéo, la musique notée, les cartes, les images, les objets et les exemplaires. `scripts/expand-data.cjs` conserve l’import éditorial de cette extension ; il nécessite les extractions locales et ne doit pas écraser des modifications ultérieures sans examen.

Les scripts `collect-sources.py`, `extract-bnf.py` et `enrich-data.cjs` conservent la méthode d’import initial. **Ne pas relancer enrich-data.cjs après une modification éditoriale sans examiner ses changements : il reconstruit les fiches.** Les extractions intermédiaires ne sont pas des sources normatives ; les PDF officiels le sont pour l’édition et le périmètre indiqués.

## Vérifications

`node scripts/test-data.cjs` vérifie les 127 fiches, leur provenance, les sous-zones des exemples, les longueurs de 100/105/106 et plusieurs particularités BnF. `node scripts/test-browser.cjs` les parcourt réellement dans Chromium hors connexion. Le script navigateur utilise les chemins du runtime local de réalisation ; les adapter sur une autre machine. Aucune dépendance n’est requise pour ouvrir l’application livrée.

Voir `docs/TESTS.md`, `docs/tests.json` et `docs/tests-donnees.json` pour le bilan, `docs/INVENTAIRE.md` pour la couverture et `docs/SOURCES.md` pour les références et les limites.

## Périmètre de rigueur

Le document BnF est un **profil de diffusion issu d’INTERMARC**, distinct du manuel international. Ses valeurs d’indicateurs, caractères de remplissage et adaptations sont identifiés. Lorsqu’il ne précise pas l’obligation ou la répétabilité, cette absence est signalée au lieu de supposer une règle. Des compléments CfU datés sont utilisés pour 200 et 214 sur ces points.

La présence d’une fiche documentée ne certifie pas sa conformité à toutes les éditions du format ni aux pratiques de tous les réseaux. Les grilles locales Koha ne sont pas définies par la BnF. Une comparaison exhaustive avec la dernière édition internationale et une validation professionnelle indépendante restent possibles. L’interface ne revendique ni affiliation BnF ni certification DSFR ou RGAA.
