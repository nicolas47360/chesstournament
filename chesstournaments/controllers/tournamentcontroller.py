from ..views.tournamentview import TournamentView, NewTournamentView, CurrentTournamentView
from ..views.playerview import PlayerOptionView
from ..utils.utilsanddata import TournamentData
from ..utils.menu import Menu
from ..models.tournament import Tournament
from . import appcontroller

class TournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = TournamentView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Créer un nouveau tournoi", CreateTournamentController())
        self.menu.add("auto", "charger un tournoi", LoadTournamentController())
        if store["current_tournament"] is not None:
            self.menu.add("auto", "tournoi en cours", CurrentTournamentMenuController())
        self.menu.add("auto", "Retour à l'écran d'accueil", appcontroller.HomeMenuAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class CreateTournamentController:
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

        return TournamentMenuController()


class LoadTournamentController:

    def __call__(self, store):
        NewTournamentView.display_tournament_list(store["tournaments"])
        tournament = NewTournamentView.choice_tournament(store["tournaments"])
        store["current_tournament"] = tournament

        return TournamentMenuController()


class CurrentTournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = TournamentView(self.menu)

    def __call__(self, store):
        tournament = store["current_tournament"]
        CurrentTournamentView.display_current_tournament(tournament)
        if not tournament.rounds:
            self.menu.add("auto", "commencer premier round", FirstRoundController())
            self.menu.add("auto", "quitter", TournamentMenuController())
        if tournament.rounds:
            self.menu.add("auto", "ajouter les points", UpdatePointController())
            self.menu.add("auto", "nouveau round", NextRoundController())
            self.menu.add("auto", "sauvegarder la partie", SaveGameController())
            self.menu.add("auto", "quitter", TournamentMenuController())
        user_choice = self.view.get_user_choice()

        return user_choice.handler


class FirstRoundController:
    def __call__(self, store):
        tournament = store["current_tournament"]
        tournament.first_round()
        return CurrentTournamentMenuController()


class UpdatePointController:

    def __call__(self, store):
        tournament_round = store["current_tournament"].get_last_round()
        wins_players = CurrentTournamentView.update_point(tournament_round)
        for i, result in enumerate(wins_players):
            tournament_round.matches[i].end_match(result)
        return CurrentTournamentMenuController()


class NextRoundController:

    def __call__(self, store):
        tournament = store["current_tournament"]
        tournament.next_round()

        return CurrentTournamentMenuController()


class SaveGameController:
    def __init__(self):
        self.save = TournamentData()

    def __call__(self, store):
        tournament = store["current_tournament"]
        self.save.save_tournaments(tournament)


