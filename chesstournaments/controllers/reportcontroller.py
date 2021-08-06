from ..utils.menu import Menu
from .import appcontroller
from ..views.reportview import ReportView, ReportPlayer
from ..views.tournamentview import NewTournamentView


class ReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = ReportView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Liste de tous les joueurs", PlayerListController())
        self.menu.add("auto", "Joueurs d'un tournoi", PlayersTournamentController())
        self.menu.add("auto", "Liste des Tournois", TournamentListController())
        self.menu.add("auto", "Liste de tous les tours et matchs d'un tournoi",
                      TournamentRoundListController())
        self.menu.add("auto", "Retour à l'écran d'accueil", appcontroller.HomeMenuAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class PlayerListController:

    def __call__(self, store):
        ReportPlayer.player_view(store["players"])
        return ReportMenuController()


class PlayersTournamentController:
    def __call__(self, store):
        NewTournamentView.display_tournament_list(store["tournaments"])
        tournament = NewTournamentView.choice_tournament(store["tournaments"])
        ReportPlayer.players_for_tournament(tournament)

        return ReportMenuController()


class TournamentListController:
    def __call__(self, store):
        NewTournamentView.display_tournament_list(store["tournaments"])
        return ReportMenuController()


class TournamentRoundListController:

    def __call__(self, store):
        NewTournamentView.display_tournament_list(store["tournaments"])
        tournament = NewTournamentView.choice_tournament(store["tournaments"])
        ReportPlayer.tournament_rounds(tournament)
        return ReportMenuController()
