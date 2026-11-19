# TP 07 - Actions tierces et actions personnalisées

## Q1 - Paramètres with de checkout et setup-node

`with` fournit des inputs à une action ; il n'est pas obligatoire pour toutes
les actions. `actions/checkout` possède des valeurs par défaut adaptées ici :
le dépôt et la référence du run sont récupérés sans paramètre explicite.
`actions/setup-node` accepte aussi des valeurs par défaut, mais `node-version: '20'`
est nécessaire pour demander explicitement la version de Node.js imposée par
ce TP. `with` permet donc de configurer le comportement souhaité.

## Q2 - Partage de report.txt entre jobs

Les jobs `build` et `verify` utilisent des runners et des espaces de travail
isolés. Un fichier généré pendant `build` n'est pas ajouté au dépôt Git et
n'apparaît pas automatiquement sur le runner de `verify`. `needs: build`
garantit l'ordre, pas le partage du disque. `upload-artifact` conserve
`report.txt` sous le nom `build-report`, puis `download-artifact` le récupère
dans `verify`, où `cat report.txt` affiche son contenu.
