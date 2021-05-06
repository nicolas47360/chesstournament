from chesstournaments.controllers.homemenuapp import HomeMenuTournament


class Report:

    def __call__(self):
        print("bienvenue dans la gestion des statistiques")
        return HomeMenuTournament()

    # 1 afficher stat par tous les joueurs
    #   -> ordre alphabétique
    #   -> classement


    # 2 afficher liste de tous les joueurs d'un tournoi
    #   -> ordre alphabetique
    #   -> classement

    # 3 afficher liste des tous les tournois

    # 4 afficher liste de tous les tours d'un tournoi

    # 5 afficher liste de tous les matchs d'un tournoi