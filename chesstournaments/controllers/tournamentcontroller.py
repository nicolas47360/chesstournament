from ..views.tournamentview import TournamentView, NewTournamentView
from ..views.playerview import PlayerOptionView
from ..utils.utilsanddata import TournamentData
from ..utils.menu import Menu
from ..models.tournament import Tournament
from . import appcontroller


class TournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = TournamentView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Créer un nouveau tournoi", NewTournamentController())
        self.menu.add("auto", "charger un tournoi", LoadTournamentController())
        if store["cuurent_tournament"] != None:
            self.menu.add("auto", "tournoi en cours", CurrentTournamentController())
        self.menu.add("auto", "Retour à l'écran d'accueil", appcontroller.BackHomeMenuController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class NewTournamentController:
    def __init__(self):
        self.save = TournamentData()

    def __call__(self, store):

        data = NewTournamentView.create_tournament()
        tournament = Tournament(**data)
        PlayerOptionView.display_players_list(store["players"])
        players_ids = NewTournamentView.add_players_tournament()
        for player_id in players_ids:
            for player in store["players"]:
                if player_id == player.identity:
                    tournament.players.append(player)
        store["current_tournament"] = tournament
        self.save.save_tournaments(tournament)

        return TournamentController()


class LoadTournamentController:
    def __init__(self):
        pass

    def __call__(self, store):
        NewTournamentView.display_tournament_list(store["tournaments"])
        tournament = NewTournamentView.choice_tournament(store["tournaments"])
        store["current_tournament"] = tournament

        return TournamentController()