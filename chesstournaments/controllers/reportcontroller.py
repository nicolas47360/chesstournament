from chesstournaments.controllers.homemenuapp import HomeMenuTournament


class Report:

    def __call__(self):
        print("bienvenue dans la gestion des statistiques")
        return HomeMenuTournament()

