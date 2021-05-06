from chesstournaments.utils.utilsanddata import Feature
import datetime


class TournamentView:

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


class NewTournamentView:
    def __init__(self):
        self.feature = Feature()

    def create_tournament(self):
        print("-------Création d'un tournoi-------")

        name = input("Veuillez entrer le nom du tournoi : ")
        location = input("Veuillez entrer le lieu du tournoi : ")
        dated = str(datetime.date.today())
        print(dated)
        time_control = input("Veuillez entrer le type de partie : ")
        round_number = int(input("Veuillez entrer le nombre de rondes : "))
        description = input("Veuillez entrer les informations : ")

        return {"name": name, "location": location, "dated": dated, "time_contol": time_control,
                "round_number" :round_number,  "description": description}

    def display_tournament_list(self):
        print("--------liste des tournois--------")
