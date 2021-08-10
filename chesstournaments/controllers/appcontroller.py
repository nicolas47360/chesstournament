from ..utils.utilsanddata import PlayerData, TournamentData
from .tournamentcontroller import TournamentMenuController
from .playercontroller import PlayerMenuController
from .reportcontroller import ReportMenuController
from ..utils.menu import Menu
from chesstournaments.views.homemenuview import HomeMenuView


class ApplicationController:
    def __init__(self):
        self.controller = None
        self.store = {"players": PlayerData.load_player(),
                      "current_tournament": None,
                      "tournaments": TournamentData.load_tournaments()}

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


class QuitAppController:
    def __call__(self, store):
        print("-------FIN DE L'APPLICTAION-------")
