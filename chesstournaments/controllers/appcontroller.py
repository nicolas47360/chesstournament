from chesstournaments.views.homemenuview import HomeMenuView
from chesstournaments.views.tournamentview import TournamentView, NewTournamentView
from chesstournaments.views.reportview import ReportView
from chesstournaments.views.playerview import PlayerView, PlayerOptionView
from chesstournaments.models.player import Player
from chesstournaments.models.tournament import Tournament
from chesstournaments.utils.menu import Menu
from chesstournaments.utils.utilsanddata import PlayerData, TournamentData


class ApplicationController:
    def __init__(self):
        self.controller = None
        players_dict = PlayerData().players_table.all()
        players = [Player(**data) for data in players_dict]
        tournaments_dict = TournamentData().tournaments_table.all()
        tournaments = [Tournament(**data) for data in tournaments_dict]
        self.store = {"players": players,
                      "tournaments": [tournaments]}

    def start(self):
        self.controller = HomeMenuAppController()
        while self.controller:
            self.controller = self.controller(self.store)


class HomeMenuAppController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Tournoi", TournamentController())
        self.menu.add("auto", "Joueur", PlayerController())
        self.menu.add("auto", "Rapport", ReportController())
        self.menu.add("auto", "Quitter", QuitAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


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
        store["tournaments"].append(tournament)
        self.save.save_tournaments(tournament)

        return TournamentController()


class AddPlayersController:
    def __init__(self):
        self.view = PlayerOptionView()

    def __call__(self, store):
        self.view.diplay_players_list("players")
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


class PlayerController:
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
        self.view = PlayerOptionView()
        self.save = PlayerData()

    def __call__(self, store):
        data = self.view.create_player()
        player = Player(**data)
        store["players"].append(player)
        self.save.save_player_data(player)

        return PlayerController()


class DeletePlayer:
    def __init__(self):
        self.view = PlayerOptionView()
        self.delete = PlayerData()

    def __call__(self, store):
        self.view.diplay_players_list("players")
        self.delete.delete_player()

        return PlayerController()


class ReportController:
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
    def __init__(self):
        self.view = PlayerOptionView()
        self.data = PlayerData()

    def __call__(self, store):

        self.view.diplay_players_list(store["players"])

        return ReportController()


class PlayersTournamentController:
    def __call__(self, store):
        return ReportController()


class TournamentListController:
    def __call__(self, store):
        return ReportController()


class TournamentRoundListController:
    def __call__(self, store):
        return ReportController()


class TournamentMatchListController:
    def __call__(self, store):
        return ReportController()


class QuitAppController:
    def __call__(self, store):
        print("-------FIN DE L'APPLICTAION-------")









