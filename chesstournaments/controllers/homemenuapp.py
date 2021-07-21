


class HomeMenuApp:

    def __init__(self):
        self.menu = Menu()
        self.view = HomeTournamentView(self.menu)

    def __call__(self):
        self.menu.add("auto", "Tournoi", TournamentController())
        self.menu.add("auto", "Nouveau joueur", CreatePlayer())
        self.menu.add("auto", "Statistiques", Report())
        self.menu.add("auto", "Quitter", quit())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


