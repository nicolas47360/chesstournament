from chesstournaments.views.tournamentview import TournamentView, NewTournamentView
from chesstournaments.utils.utilsanddata import TournamentData
from chesstournaments.utils.menu import Menu


class TournamentController:
    class TournamentController:
        def __init__(self):
            self.menu = Menu()
            self.view = TournamentView(self.menu)

        def __call__(self, store):
            self.menu.add("auto", "Créer un nouveau tournoi", NewTournamentController())
            self.menu.add("auto", "Ajouter les joueurs", AddPlayersController())
            self.menu.add("auto", "Lancer le tournoi", StartTournamentController())
            self.menu.add("auto", "Reprendre le tournoi", ResumeTournamentController())
            self.menu.add("auto", "Retour à l'écran d'accueil", BackHomeMenuController())

            user_choice = self.view.get_user_choice()

            return user_choice.handler

    class NewTournamentController:
        def __init__(self):
            self.view = NewTournamentView()
            self.save = TournamentData()

        def __call__(self, store):
            data = self.view.create_tournament()
            tournament = Tournament(**data)
            store["Tournaments"] = tournament
            self.save.save_tournaments(tournament)

            return TournamentController

    class AddPlayersController:
        def __call__(self, store):
            return TournamentController()

    class StartTournamentController:
        def __call__(self, store):
            return HomeMenuAppController()

    class ResumeTournamentController:
        def __call__(self, store):
            return HomeMenuAppController()

    class BackHomeMenuController:
        def __call__(self, store):
            return HomeMenuAppController()
