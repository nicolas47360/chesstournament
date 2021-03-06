# Chess Tournament

##Description
Application permettant la création et la gestion d'un tournoi d'échec hors ligne selon le système suisse.
## Prérequis
**Python 3**
## Installation:
Cloner le repository à partir de l'adresse:
https://github.com/nicolas47360/chesstournament.git

Créer un environnement virtuel:<br>
`python -m venv env`


Activer votre environnement virtuel:<br>
`source env/bin/activate`

Installer les packages à partir du fichier requirements.txt:<br>
`pip install -r requirements.txt`

Lancer le script:<br>
`python -m chesstournaments.main`

## Démarage
### Menu d'accueil
1. Tournoi:<br>
    *Vous permettra de créer un nouveau tournoi et de charger un tournoi après sa création ou si celui-ci fut 
sauvegardé.*


2. Joueur:<br>
    *Vous permettra de créer un joueur ou de le supprimer de la base de donnée.*


3. Rapport:<br>
*Vous obtiendrez l'ensemble des informations:*
- *la liste de tous les joueurs par ordre alphabétique et classement.*
- *la liste de tous les joueurs ayant participé à un tournoi.*
- *la liste de tous les tournois.*
- *la liste de tous les tours et matchs d'un tournoi.*
4. Quitter

### Execution d'un Tournoi
- *Commencer par créer au minimum huit joueurs avant de lancer le tournoi
ou vous pouvez utiliser le fichier `playersdemo.json` qu'il faudra renommer `players.json` pour pouvoir l'utiliser*
- *Lancer le tournoi en sélectionnant "tournoi en cours"*
- *Commencer le "premier round" si vous venez de créer un tournoi ou "nouveau round" si vous reprenez un tournoi*
- *"Ajouter les points" lorsque les matchs sont finis*
- *continuer les rounds ou sauvegarder*

## Génerer un rapport flake8-html
Veuillez entrer la ligne de code suivante dans votre terminal:<br>
`flake8 --format=html --htmldir=flake-report`

##Contributeur
 



