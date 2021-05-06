import datetime
from chesstournaments.utils.utilsanddata import Feature

class PlayerView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("-------TOURNOI-------")
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

    def __init__(self):
        self.feature = Feature()

    def create_player(self):
        print("--------Nouveau joueur-------")
        last_name = self.feature.for_string("Veuillez entrer le nom : ")
        first_name = self.feature.for_string("Veuillez entrer votre prénom : ")
        birth_date = self.feature.birth_date("veuillez entrer la date de naissasnce dd/mm/yyyy: ")
        gender = self.feature.gender("Veuillez entrer le sexe (f/m) : ")
        ranking = self.feature.ranking("Veuillez entrer le classement: ")

        return {"last_name": last_name,  "first_name": first_name, "birth_date": birth_date,
                "gender": gender, "ranking": ranking}

    def delete_player(self):
        print("--------supprimer un joueur---------")
        last_name = input("Nom du joueur : ")
        first_name = input("prenom du joueur : ")
        return last_name, first_name


    def diplay_players_list(self, players):
        print("--------liste des joueurs--------\n")

        for player in players:
            print(("nom :{}, prenom :{}, age :{}, sexe  :{}, rang :{}").format(player.last_name,
                  player.first_name, player.birth_date, player.gender, player.ranking))

        print("\n")
