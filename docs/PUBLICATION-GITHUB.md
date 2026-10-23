# Publication sur GitHub Pages

Destination souhaitée : compte `didierthebault-web`, nouveau dépôt proposé `unimarc-explorer`.

Le dépôt doit contenir uniquement l’application et ses sources. Les PDF externes téléchargés et les extractions intermédiaires restent hors du suivi Git ; leurs références officielles sont conservées dans les données et la documentation.

Le workflow `.github/workflows/pages.yml` vérifie les données, génère le HTML autonome et prépare les fichiers publics sous `_site/`. GitHub Pages ne reçoit que l’application, le fichier autonome et les trois fichiers de données. Aucune dépendance JavaScript distante n’est utilisée par l’application.

Après création du dépôt et envoi de la branche `main`, activer **Settings → Pages → Source : GitHub Actions**, puis exécuter le workflow « Publier UNIMARC Explorer ». Les mises à jour suivantes de `main` déclencheront automatiquement la publication.

Adresse attendue, uniquement après confirmation d’un déploiement réussi : `https://didierthebault-web.github.io/unimarc-explorer/`. Cette adresse est prévisionnelle tant que la publication n’est pas vérifiée.

Le code généré, les synthèses pédagogiques et les documents externes ont des responsabilités intellectuelles distinctes. Aucune licence générale couvrant les documents BnF/CfU n’est attribuée par ce dépôt.
