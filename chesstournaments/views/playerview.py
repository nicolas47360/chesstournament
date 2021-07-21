from chesstournaments.utils.utilsanddata import Feature


class PlayerView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("-------TOURNOI-------\n")
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


class PlayerOptionView:

    @staticmethod
    def create_player():
        print("--------Nouveau joueur-------\n")
        identity = Feature.for_int("entrer un chiffre: ")
        last_name = Feature.for_string("Veuillez entrer le nom : ")
        first_name = Feature.for_string("Veuillez entrer votre prénom : ")
        birth_date = Feature.birth_date("veuillez entrer la date de naissasnce dd/mm/yyyy: ")
        gender = Feature.gender("Veuillez entrer le sexe (f/m) : ")
        ranking = Feature.ranking("Veuillez entrer le classement: ")

        return {"identity": identity, "last_name": last_name,  "first_name": first_name, "birth_date": birth_date,
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
            print("ID: {} nom: {}, prenom: {}, age: {}, sexe : {}, rang: {}".format(p.identity,
                  p.last_name, p.first_name, p.birth_date, p.gender, p.ranking))
        print("\n")
