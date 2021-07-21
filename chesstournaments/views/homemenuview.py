class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("-------PRÊT A GÉRER VOS TOURNOIS------\n")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        while True:
            #afficher menu
            self._display_menu()
            #demander a l'utilisateur de faire un choix
            choice = input(">> ")
            #valider choix de l'utilisateur
            if choice in self.menu:
                return self.menu[choice]










