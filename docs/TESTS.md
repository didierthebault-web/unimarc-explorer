# Bilan des contrôles — édition documentée 0.2

Les rapports machine de cette livraison sont `tests.json` et `tests-donnees.json`. La vérification bibliographique s’appuie sur les éditions et périmètres décrits dans `SOURCES.md` ; elle ne constitue pas une certification externe.

## Données

- 59 fiches uniques, toutes renseignées, dont 50 BnF et 9 compléments explicitement identifiés.
- 431 sous-zones recensées, avec intitulés et conditions ou absence de précision dans la source.
- Références et pages présentes pour chaque fiche.
- Tous les codes de sous-zones employés dans les exemples existent dans leur fiche.
- Longueurs des données d’exemple : 100 = 36 positions ; 105 = 13 ; 106 = 1.
- Contrôles spécifiques : indicateurs BnF de responsabilités, cote en 852 $j, vignette en 856, divergence d’occurrence de 930 $j, clé de l’ISBN pédagogique.

## Navigateur

Parcours réels dans Chromium, au moyen de Playwright, en ouvrant le HTML par `file://` et en activant le mode hors connexion :

- Les dix blocs et leurs 59 cercles de champs sont cliqués ; les intitulés du panneau sont comparés aux données.
- Toutes les fiches détaillées sont ouvertes, leurs références vérifiées, tous les segments des exemples activés et leurs explications contrôlées.
- Le mode expert affiche le nombre de sous-zones attendu pour chaque fiche ; 001 et 003 n’affichent aucun indicateur.
- Copie puis collage de la représentation de 214, avec comparaison exacte du texte.
- Recherche : ISBN, auteur, résumé, publication, 606 et $j ; ouverture directe des fiches attendues.
- Activation clavier par Entrée et Espace ; corrections du quiz ; réduction des animations effectivement appliquée.
- Les 59 fiches et les autres vues sont parcourues à 390, 768, 1024 et 1440 pixels pour détecter les débordements horizontaux.
- Navigation mobile dans le bloc national/local et consultation de 995.
- Version organisée ouverte sans serveur ; absence d’erreur JavaScript et de requête HTTP(S) durant ces parcours.

## Contrôle visuel et limites

Captures de l’accueil, de la carte 7XX, de la fiche 606 sur ordinateur et de 995 sur mobile. Deux pages du PDF BnF ont également été rendues pour confirmer visuellement les tableaux de 214 et de responsabilités (pages 31 et 55).

Ces contrôles ne sont pas un audit RGAA. L’absence de débordement ne prouve pas à elle seule l’absence de tout défaut visuel. Lecteurs d’écran, autres navigateurs et audit de contraste complet restent hors de ce contrôle. La liste de sources explique les limites documentaires et les références anciennes ; aucune simulation Koha ni notice complète n’a été ajoutée dans cette mise à jour.
