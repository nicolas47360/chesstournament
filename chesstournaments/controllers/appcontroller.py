from ..views.homemenuview import HomeMenuView
from ..views.tournamentview import TournamentView, NewTournamentView, CurrentTournamentView
from ..views.reportview import ReportView, ReportPlayer
from ..views.playerview import PlayerView, PlayerOptionView
from ..models.player import Player
from ..models.tournament import Tournament
from ..utils.menu import Menu
from ..utils.utilsanddata import PlayerData, TournamentData


class ApplicationController:
    def __init__(self):
        self.controller = None
        players_dict = PlayerData().players_table.all()
        players = [Player(**data) for data in players_dict]
        tournaments_dict = TournamentData().tournaments_table.all()
        tournaments = [Tournament(name=data["name"], location=data["location"], dated=data["dated"],
                                  time_control=data["time_control"],
                                  description=data["description"]) for data in tournaments_dict]
        self.store = {"players": players,
                      "current_tournament": None,
                      "tournaments": tournaments}
        players = []
        tournament = Tournament("paris", "loi", "08/07/2021", "split", "lit")
        self.store["current_tournament"] = tournament
        player1 = Player(1, "melin", "nicolas", "28/10/1977", "m", 325)
        player2 = Player(2, "pap", "pol", "12/12/1988", "f", 234)
        player3 = Player(3, "moarc", "mer", "14/02/1965", "m", 189)
        player4 = Player(4, "herty", "kuit", "21/03/1987", "f", 214)
        player5 = Player(5, "fric", "pol", "25/01/178", "m", 206)
        player6 = Player(6, "tyu", "port", "12/02/1987", "f", 125)
        player7 = Player(7, "orti", "lirt", "23/03/2001", "m", 187)
        player8 = Player(8, "rty", "eart", "05/09/2002", 'f', 589)
        players.append(player1)
        players.append(player2)
        players.append(player3)
        players.append(player4)
        players.append(player5)
        players.append(player6)
        players.append(player7)
        players.append(player8)
        for player in players:
            tournament.players.append(player)
        self.store["tournaments"].append(tournament)

    def start(self):
        self.controller = HomeMenuAppController()
        while self.controller:
            self.controller = self.controller(self.store)


class HomeMenuAppController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Tournoi", TournamentMenuController())
        self.menu.add("auto", "Joueur", PlayerMenuController())
        self.menu.add("auto", "Rapport", ReportMenuController())
        self.menu.add("auto", "Quitter", QuitAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class TournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = TournamentView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Créer un nouveau tournoi", CreateTournamentController())
        self.menu.add("auto", "charger un tournoi", LoadTournamentController())
        if store["current_tournament"] is not None:
            self.menu.add("auto", "tournoi en cours", CurrentTournamentMenuController())
        self.menu.add("auto", "Retour à l'écran d'accueil", BackHomeMenuController())

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


class BackHomeMenuController:
    def __call__(self, store):
        return HomeMenuAppController()


class PlayerMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = PlayerView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Créer un nouveau joueur", CreatePlayerController())
        self.menu.add("auto", "Supprimer un joueur", DeletePlayer())
        self.menu.add("auto", "Retour à l'écran d'accueil", BackHomeMenuController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class CreatePlayerController:
    def __init__(self):
        self.save = PlayerData()

    def __call__(self, store):
        data = PlayerOptionView.create_player()
        player = Player(**data)
        store["players"].append(player)
        self.save.save_player_data(player)

        return PlayerMenuController()


class DeletePlayer:
    def __init__(self):
        self.delete = PlayerData()

    def __call__(self, store):
        PlayerOptionView.display_players_list(store["players"])
        player_id = PlayerOptionView.delete_player()
        store["players"] = [p for p in store["players"] if p.identity != player_id]
        self.delete.delete_player(player_id)

        return PlayerMenuController()


class ReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = ReportView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Liste de tous les joueurs", PlayerListController())
        self.menu.add("auto", "Joueurs d'un tournoi", PlayersTournamentController())
        self.menu.add("auto", "Liste des Tournois", TournamentListController())
        self.menu.add("auto", "Liste de tous les tours d'un tournoi", TournamentRoundListController())
        self.menu.add("auto", "Liste de tous les matchs d'un tournoi", TournamentMatchListController())
        self.menu.add("auto", "Retour à l'écran d'accueil", BackHomeMenuController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class PlayerListController:

    def __call__(self, store):
        player = PlayerData.load_player()
        ReportPlayer.player_view(player)
        return ReportMenuController()


class PlayersTournamentController:
    def __call__(self, store):
        tournaments = TournamentData.load_tournament()
        NewTournamentView.display_tournament_list(tournaments)
        NewTournamentView.choice_tournament(tournaments)
        ReportPlayer.players_for_tournament(tournaments)

        return ReportMenuController()


class TournamentListController:
    def __call__(self, store):
        tournaments = TournamentData.load_tournaments()
        NewTournamentView.display_tournament_list(tournaments)
        return ReportMenuController()


class TournamentRoundListController:

    def __call__(self, store):
        tournaments = TournamentData.load_tournament()
        NewTournamentView.display_tournament_list(tournaments)
        choice = NewTournamentView.choice_tournament(tournaments)
        tournament = TournamentData.load_rounds(choice)
        ReportPlayer.tournament_rounds(tournament)
        return ReportMenuController()


class TournamentMatchListController:
    def __call__(self, store):
        tournaments = TournamentData.load_tournaments()
        NewTournamentView.display_tournament_list(tournaments)
        choice = NewTournamentView.choice_tournament(tournaments)
        ReportPlayer.tournament_matches(choice)
        return ReportMenuController()


class QuitAppController:
    def __call__(self, store):
        print("-------FIN DE L'APPLICTAION-------")
