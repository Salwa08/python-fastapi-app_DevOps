# TP 07 - Sécurité des actions tierces

## Observation de actions/setup-node

Relevé du 19 novembre 2026 :

- Créateur : `actions`, avec le badge **Verified** sur la
  [fiche Marketplace](https://github.com/marketplace/actions/setup-node-js-environment).
- Étoiles : **5 027**, relevées via l'API du
  [dépôt officiel](https://github.com/actions/setup-node). Ce nombre évolue.
- Source TypeScript : dossier [`src/`](https://github.com/actions/setup-node/tree/main/src).
  Le code JavaScript distribué pour l'exécution se trouve dans `dist/`.

## Q3 - Version publiée plutôt que branche main

`@main` suit directement le développement : une modification peut changer
le comportement d'un run sans modification du workflow appelant. `@v4`
sélectionne une version majeure publiée et limite les changements de contrat.
Ce tag reste déplaçable : en production, épingler le SHA complet d'un commit
audité fournit une référence immuable, puis les mises à jour sont revues.

L'expérience `checkout@main` est conservée dans le commit `ea5fce7`, sans
exécution. Le workflow final revient à `checkout@v4`, comme demandé.

## Q4 - Limites du badge de créateur vérifié

Le badge confirme la vérification du créateur par GitHub. Il ne certifie ni
chaque version du code, ni l'absence de vulnérabilités ou de compromission
des dépendances. La popularité ne remplace pas une revue de sécurité.

## Q5 - Deux vérifications avant la production

1. Vérifier l'origine et la maintenance : identité du fournisseur, dépôt
   officiel, historique des versions et traitement des alertes de sécurité.
2. Auditer le commit exécuté, le code distribué et ses dépendances : accès
   réseau, secrets et permissions demandées ; tester avec les droits minimaux.

Dans ce TP, `permissions: contents: read` limite le jeton et
`persist-credentials: false` évite de laisser les identifiants dans la
configuration Git après le checkout.

Référence : [sécurisation des workflows et des actions tierces](https://docs.github.com/en/actions/reference/security/secure-use).
