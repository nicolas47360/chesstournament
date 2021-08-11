from chesstournaments.utils.utilsanddata import Feature


class PlayerView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("\n-------TOURNOI-------\n")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input(">> ")
            if choice in self.menu:
                return self.menu[choice]


class PlayerOptionView:

    @staticmethod
    def create_player():
        print("--------Nouveau joueur-------\n")
        identity = Feature.for_int("entrer un chiffre pour identifier "
                                   "le joueur : ")
        last_name = Feature.for_string("Veuillez entrer le nom : ")
        first_name = Feature.for_string("Veuillez entrer votre prénom : ")
        birth_date = Feature.birth_date("veuillez entrer la date "
                                        "de naissasnce dd/mm/yyyy: ")
        gender = Feature.gender("Veuillez entrer le sexe (f/m) : ")
        ranking = Feature.ranking("Veuillez entrer le classement: ")

        return {"identity": identity, "last_name": last_name,
                "first_name": first_name, "birth_date": birth_date,
                "gender": gender, "ranking": ranking}

    @staticmethod
    def delete_player():
        print("--------supprimer un joueur---------\n")
        identity = Feature.for_int("choisir un joueur par son ID: ")
        return identity

    @staticmethod
    def display_players_list(players):
        print("--------liste des joueurs--------\n")

        for p in players:
            print(f"ID: {p.identity} nom: {p.last_name} "
                  f" prenom: {p.first_name}  age: {p.birth_date} "
                  f" sexe : {p.gender}  rang: {p.ranking}")
        print("\n")
