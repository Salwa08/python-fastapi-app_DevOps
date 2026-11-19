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

## Q3 - Différence entre > et >> dans GITHUB_OUTPUT

`>` tronque le fichier avant d'écrire ; `>>` ajoute à son contenu. Si deux
commandes écrivent chacune un output avec `>`, la seconde efface le premier :
seul le second output reste disponible. Une première écriture avec `>` suivie
d'une seconde avec `>>` conserve les deux, mais utiliser systématiquement
`>>` évite d'écraser des valeurs déjà présentes dans cette step.

## Q4 - Transmission d'une valeur entre jobs

`GITHUB_ENV` ne sort pas du job qui l'écrit. `GITHUB_OUTPUT` définit d'abord
un output de step ; il ne transmet pas automatiquement l'environnement à un
autre job. Il faut exposer cet output dans `jobs.build.outputs`, puis déclarer
`needs: build` dans `deploy` et lire `needs.build.outputs.full_version`.

Dans ce TP, la step `version` produit `<version>-<date>` ; le job `build`
expose `steps.version.outputs.full_version` et `deploy` réutilise cette valeur.

## Q5 - Retrait de needs: build

Sans `needs: build`, `deploy` ne dépend plus de `build` et peut démarrer en
parallèle, avant le calcul de la version. Le job `build` n'est plus une
dépendance accessible dans le contexte `needs` de `deploy`, donc
`needs.build.outputs.full_version` ne fournit plus la valeur attendue
(une propriété absente est évaluée en chaîne vide). Il faut conserver `needs`
pour garantir à la fois l'ordre d'exécution et l'accès à l'output.

Source : [transmission d'outputs entre jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).
