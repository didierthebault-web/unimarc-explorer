# Références documentaires — édition 0.3

Consultation et extraction : 23 octobre 2026. Les PDF conservent la responsabilité intellectuelle et les crédits de leurs producteurs. La synthèse pédagogique n’est pas une publication de la BnF.

## Référence principale : 105 fiches

**Bibliothèque nationale de France, Département des Métadonnées. Format UNIMARC des notices bibliographiques fournies par la BnF. Version 11.0, 2023.** Historique : septembre 2023 ; génération affichée le 3 octobre 2023 ; 66 pages.

- Page de diffusion : https://www.bnf.fr/fr/format-unimarc-de-diffusion-des-donnees-de-la-bnf
- PDF : https://www.bnf.fr/sites/default/files/2023-10/UNIMARC_B.pdf
- Copie locale : `UNIMARC_B_BnF_2023.pdf`.

Ce document décrit la conversion en UNIMARC de données saisies en INTERMARC. Il comporte des adaptations nationales et propres à la diffusion BnF. Il n’est pas le manuel international complet. Le lien BnF vers ce manuel renvoie au site Transition bibliographique.

Chaque fiche enregistre les pages, l’URL, la version et le périmètre. Les intitulés des 6XX reprennent le terme « vedette » employé par le document BnF 2023 ; les explications utilisent aussi « point d’accès ». Les listes de sous-zones peuvent conserver des mentions d’obsolescence afin de permettre la lecture de données anciennes ; ces mentions ne sont pas des recommandations de saisie actuelle.

Les règles de répétabilité et d’obligation ne sont généralement pas fournies dans ce document de diffusion. Leur absence est explicitement indiquée. Ne pas assimiler cette absence à une facultativité ou à une non-répétabilité.

## Compléments : neuf fiches

| Zone | Référence utilisée | Portée |
| --- | --- | --- |
| 017 | https://www.transition-bibliographique.fr/B017_fre — IFLA 2017, traduction CfU 2019 | Autre identifiant, indicateurs 7/8 et 0/1/2, sous-zones et occurrences |
| 317 | https://www.transition-bibliographique.fr/B317_fre — IFLA 2008, traduction CfU 2010 | Provenance d’exemplaire ; obligation de $a et $5 dans cette édition |
| 320 | https://www.transition-bibliographique.fr/B320_fre — IFLA 2008, traduction CfU 2011 | Bibliographies et index contenus dans la ressource |
| 359 | https://www.transition-bibliographique.fr/B359_fre — recommandation CfU du 6 décembre 2002 | Zone française de table des matières ; conversion vers 327 pour les échanges internationaux |
| 830 | https://www.transition-bibliographique.fr/B830_fre — IFLA 2008, traduction CfU 2010 | Note de travail du catalogueur |
| 850 | https://www.transition-bibliographique.fr/B850_fre — IFLA 2008, traduction CfU 2010 | Établissements détenteurs |
| 852 | https://www.transition-bibliographique.fr/B852_fre — IFLA 2008, traduction CfU 2010 | Localisation et cote ; cote en $j, sans emprunt aux sous-zones MARC 21 |
| 930 | https://www.transition-bibliographique.fr/Description_FormatUnimarcEchange_Exemplaire — version 3, mai 2022, p. 29–30 | Échange français des données d’exemplaire, hors diffusion bibliographique BnF 2023 |
| 995 | https://www.transition-bibliographique.fr/wp-content/uploads/2020/10/unimarc-bibliographique-995.pdf — version 3, décembre 2005 | Exemplaires prêtés ou déposés ; compléter par les correspondances CfU 2022, p. 66–67 |

Index des éditions françaises : https://www.transition-bibliographique.fr/unimarc/manuel-unimarc-format-bibliographique/ . Certaines traductions anciennes y sont signalées comme dépassées par des modifications IFLA ultérieures. La fiche conserve donc la date de l’édition effectivement consultée ; elle ne revendique pas une comparaison exhaustive avec le manuel international actuel.

Compléments d’occurrence pour 200 et 214 :

- https://www.transition-bibliographique.fr/B200_fre — texte IFLA 2018, traduction CfU 2019, p. 1–2.
- https://www.transition-bibliographique.fr/wp-content/uploads/2025/05/B214_fre.pdf — fiche CfU portant 2019, p. 1–2 ; le répertoire 2025/05 n’est pas une nouvelle édition normative.

## Points vérifiés et divergences conservées

- 001 et 003 : zones de contrôle, sans indicateurs ni sous-zones.
- 073 : indicateurs #0 dans le document BnF.
- 100 : données de 36 positions ; 105 : 13 positions ; 106 : code de présentation physique. Les chaînes d’exemple sont des représentations pédagogiques avec # pour les blancs.
- 200 : le titre parallèle est traité en 510 dans la conversion BnF, avec une note 304, plutôt qu’en 200 $d.
- 225 : le profil BnF utilise notamment | au premier indicateur et 9 au second pour un titre d’ensemble monographique.
- 700/701/702 : #| dans la diffusion BnF ; 710/711 : ||. Ces caractères ne sont pas des valeurs renseignées à interpréter comme en saisie internationale.
- 856 : valeur 1 du second indicateur pour une vignette, ajout BnF 2023 ; $q rendu répétable par la BnF selon la note 26.
- 930 : le tableau p. 29 marque $j facultatif, alors que le commentaire p. 30 le dit obligatoire. La fiche signale la divergence, sans la résoudre arbitrairement.
- 995 : les conditions citées relèvent de la recommandation française ; elles ne définissent pas toutes les installations Koha. Les correspondances de 2022 ne remplacent pas la lecture du texte détaillé de 2005.

## Limites des exemples

Les exemples sont réduits et fictifs, sauf l’ARK 003 repris du document BnF. ISBN et ISSN ont une clé de contrôle cohérente mais aucune attribution réelle n’est revendiquée. Le DOI et les URL de démonstration sont fictifs. Les formes de noms et de sujets ne sont pas présentées comme des autorités existantes et vérifiées. Aucun numéro d’autorité inventé n’est fourni en $3.

Les fréquences sont des appréciations pédagogiques, sans statistiques. Les règles RDA-FR et les paramétrages Koha ne sont pas déduits automatiquement du format. Les tests vérifient la cohérence de l’application et de ses données ; ils ne remplacent pas une revue professionnelle du catalogage.

## Extension 0.3 : 68 zones supplémentaires

105 fiches prennent pour référence principale le profil BnF 2023 ; 22 sont des compléments explicitement identifiés. Les fiches conservent toutes leur URL, leurs pages, l’édition, la consultation du 23 octobre 2026 et le statut de vérification documentaire.

- Les données codées des zones 110, 115, 116, 120, 121, 125, 126, 127, 128, 135, 181 et 182 sont complétées par les fiches du manuel CfU. Leurs longueurs et codes ne sont pas déduits des seuls exemples.
- 005, 033, 117, 183, 231, 301, 316 et 541 : fiches CfU datées dans l’application. 231 conserve l’intitulé [provisoire] de la traduction 2022.
- [203](https://www.transition-bibliographique.fr/B203_eng) et [283](https://www.transition-bibliographique.fr/B283_eng) : édition IFLA en ligne 1.1.0 (2024), en anglais. Les libellés français sont des traductions pédagogiques identifiées, pas une traduction officielle revendiquée.
- 915, 917 et 955 : recommandations françaises d’échange des données d’exemplaire 2022. Elles ne décrivent pas une grille Koha universelle. Le $5 des exemples contient un établissement et un identifiant d’exemplaire ; aucune détention réelle n’est affirmée.

### Différences conservées et expliquées

- 181 et 182 : le profil BnF emploie 0 ou blanc au second indicateur ; la traduction CfU 2016 prévoit aussi 1.
- 121 : l’exemple suit les neuf positions de $a du manuel CfU 2008, traduction 2010 ; le profil de diffusion n’en décrit pas tous les éléments.
- 123 : les indicateurs internationaux de la fiche CfU 2008 et ceux du profil BnF ne coïncident pas. Les libellés BnF « Longitude nord/sud » sont signalés ; le manuel CfU décrit les latitudes nord/sud.
- 283 : utiliser $a selon l’édition IFLA 2024, malgré un ancien exemple de 183 utilisant $c. Le tableau de 283 qualifie $2 de MA alors que sa description le dit obligatoire : divergence indiquée, référentiel fourni dans l’exemple.
- 325 : $t est explicitement une particularité de diffusion BnF.
- 955 : le tableau indique facultatif, tandis que le texte d’utilisation le dit obligatoire pour les publications en série. La fiche conserve cette divergence.
- 802 : le code ISSN France est 07, vérifié dans la fiche CfU, exemple 4. Les indices de classification pédagogiques ne remplacent pas la consultation des tables de l’édition utilisée.

Les listes de codes complètes, toutes les éditions du format, les grilles locales et les correspondances RDA-FR ne sont pas déclarées couvertes. L’inventaire complet est dans INVENTAIRE.md.
