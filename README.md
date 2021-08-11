# Chess Tournament


Application permettant la création et la gestion d'un tournoi d'echec hors ligne.
## Notice d'utilisation
### Installation:
Cloner le repository à partir de l'adresse:
https://github.com/nicolas47360/chesstournament.git

Créer un environement virtuel:<br>
`python -m venv env`


Activer votre environement virtuel:<br>
`source env/bin/activate`

Installer les packages à partir du fichier requirements.txt:<br>
`pip install -r requirements.txt`

Lancer le script:<br>
`python -m chesstournaments.main`

### Utilisation
#### Menu d'accueil
1. Tournoi:<br>
    *Vous permettra de créer un nouveau tournoi et de charger un tournoi après sa création ou si celui-ci fut sauvegarder.*


2. Joueur:<br>
    *Vous permettra de créer un joueur ou de le supprimer de la base de donnée.*


3. Rapport:<br>
*Vous obtiendrez l'ensemble des informations:*
- *la liste de tous les joueurs par ordre alphabétique et classement.*
- *la liste de tous les joueurs ayant participé à un tournoi.*
- *la liste de tous les tournois.*
- *la liste de tous les tours et matchs d'un tournoi.*
4. Quitter

#### Execution d'un Tournoi
- *Commencer par créer au minimum huit joueurs avant de lancer le tournoi*
- *Charger un tournoi par son nom.*
- *Lancer le tournoi en séléctionant "tournoi en cours"*
- *Commencer le "premier round" si vous venez de créer un tournoi ou "nouveau round" si vous reprennez un tournoi*
- *"Ajouter les points" lorsque les matchs sont finis*
- *continuer les rounds ou sauvegarder*

## Génerer un rapport flake8-html
Veuillez entrer la ligne de code suivante dans votre terminal:<br>
`flake8 --format=html --htmldir=flake-report`

 



