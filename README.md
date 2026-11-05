# La Grille — projet de fin d’études

Application de bureau Python pour saisir des critères d’évaluation d’enseignants, calculer des scores et afficher un classement. Cette description est issue du code ; le titre académique exact, les auteurs, l’établissement et l’année restent à compléter.

## Fonctionnalités présentes dans le code

- Connexion à une base MySQL locale et sélection par grade et type de passage.
- Saisie de critères liés aux activités pédagogiques, à la recherche et aux responsabilités.
- Calcul de scores et classement des enseignants.
- Export des résultats en PDF et commande d’impression sous Windows.

## Organisation

`src/Interface.py` contient l’application. Les images et l’icône restent à côté du programme afin de préserver les chemins existants.

## Installation et lancement sous Windows

Python avec Tkinter et un serveur MySQL local sont nécessaires. Depuis ce dossier :

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\Interface.py
```

Les dépendances ont été identifiées dans les imports. Leurs versions historiques ne sont pas connues et cette installation n’a pas été testée.

## Base de données nécessaire

Le dossier `database/` contient la structure réelle (`schema.sql`) et les 13 lignes avec noms de démonstration N1/P1, etc. (`demo-data.sql`), exportées de la base locale. MySQL 8.0 est requis pour la collation utilisée. Le programme attend la base `grille` sur `localhost` et la table `enseignant` :

| Colonne | Utilisation |
| --- | --- |
| id | Identifiant |
| nom | Nom |
| prenom | Prénom |
| grade | MCA, MCH ou PES |
| type_garde | A to B, B to C ou C to D (orthographe attendue par le code) |
| date_effet | Départage du classement |

La structure et les types ont été confirmés sur la base d’origine. Les identifiants MySQL sont saisis dans l’interface. Sélectionner explicitement les deux menus avant de cliquer sur Submit, puis poursuivre avec Suivant après une connexion réussie.

### Importer la base sur un nouvel ordinateur

Sur votre ordinateur actuel, la base existe déjà : ne réimportez pas ces fichiers par-dessus vos données.

Pour une nouvelle installation, dans MySQL Workbench :

1. Se connecter à MySQL avec un compte autorisé à créer une base.
2. Utiliser File > Open SQL Script pour ouvrir `database/schema.sql`, puis exécuter le script complet avec le bouton éclair.
3. Ouvrir `database/demo-data.sql` et l’exécuter une seule fois sur la table vide.
4. Vérifier avec `SELECT COUNT(*) FROM grille.enseignant;` : résultat attendu, 13.
5. Lancer l’application et saisir les identifiants MySQL de cet ordinateur. Aucun mot de passe n’est fourni dans le dépôt.

Pour un premier essai, choisir explicitement `MCA` et `B to C`, puis Submit et Suivant : cette sélection contient un enseignant. Remplir toutes les cases, avec 0 pour les critères non applicables.

## État de cette version

Le code original est conservé sans modification. Sa syntaxe a été vérifiée, mais le fonctionnement de l’interface, les calculs, l’export PDF et l’impression n’ont pas été validés. La connexion MySQL a été vérifiée. Le SQL exporté a été réimporté dans une table temporaire : les 13 lignes sont identiques à la source. La base existante n’a pas été modifiée. Une installation complète sur un autre ordinateur reste à tester.

## À compléter avant diffusion

- Renseigner le titre académique, les auteurs, l’établissement et l’année.
- Choisir une licence avec les personnes détenant les droits du projet.

Les dossiers `archives/` et `executable/` ne sont pas inclus dans le ZIP de publication. Le rapport et les présentations ne sont pas inclus dans ce ZIP.

## Captures de l’interface

Captures fournies par l’auteur. Le score visible dépend des valeurs saisies pendant sa démonstration.

### Accueil

![Accueil](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20153144.png)

### Production pédagogique

![Production pédagogique](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152538.png)

### Encadrement pédagogique

![Encadrement pédagogique](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152335.png)

### Encadrement pédagogique — autre capture

![Encadrement pédagogique — autre capture](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152509.png)

### Production scientifique

![Production scientifique](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152603.png)

### Encadrement scientifique

![Encadrement scientifique](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152637.png)

### Responsabilité scientifique

![Responsabilité scientifique](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152704.png)

### Classement et export PDF

![Classement et export PDF](screenshots/Capture%20d%E2%80%99%C3%A9cran%202026-11-05%20152750.png)

