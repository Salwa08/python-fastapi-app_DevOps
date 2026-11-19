# TP 06 - Variables d'environnement, inputs et outputs

## Q1 - Disponibilité d'une variable écrite dans GITHUB_ENV

Chaque step `run` utilise son propre processus shell. Écrire dans
`GITHUB_ENV` ne modifie pas l'environnement du processus en cours : le runner
lit ce fichier à la fin de la step et transmet ses valeurs aux steps suivantes
du même job. Il faut donc utiliser une affectation shell ou `export` si l'on
souhaite aussi employer la variable dans la step qui la définit.

## Q2 - Portée de GITHUB_ENV

Le job `verify-env` affiche `APP_NAME in another job is ''` : `APP_NAME` y est
vide, même si le job `build` l'a enregistrée. Les jobs ont des environnements
isolés. `GITHUB_ENV` partage les variables avec les steps suivantes d'un même
job, pas avec les autres jobs. Ajouter seulement `needs: build` ne transfère
pas cet environnement.

Source : [commandes de workflow et fichiers d'environnement](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-an-environment-variable).
