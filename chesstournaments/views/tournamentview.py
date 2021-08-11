from chesstournaments.utils.utilsanddata import Feature
import datetime


class TournamentView:

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


class NewTournamentView:

    @staticmethod
    def create_tournament():
        print("-------Création d'un tournoi-------\n")
        name = input("Veuillez entrer le nom du tournoi : ")
        location = input("Veuillez entrer le lieu du tournoi : ")
        dated = str(datetime.date.today())
        print(dated)
        time_control = Feature.time_control("Veuillez entrer "
                                            "le type de partie "
                                            "(split, blitz, rapide): ")
        round_number = 4
        print("nombre de round: " + str(round_number))
        description = input("Veuillez entrer les informations : ")

        return {"name": name, "location": location,
                "dated": dated, "time_control": time_control,
                "round_number": round_number,  "description": description}

    @staticmethod
    def player_not_in_db():
        print("\n Vous n'avez pas 8 joueurs pour commencer un tournoi "
              "vous allez être rediriger vers la page de création "
              "de joueur\n")

    @staticmethod
    def display_tournament_list(tournaments):
        print("--------liste des tournois--------\n")
        for tournament in tournaments:
            print(f"Nom :{tournament.name}  lieu :{tournament.location} "
                  f" date :{tournament.dated}  "
                  f"type de partie :{tournament.time_control} "
                  f" nombre de round :{tournament.round_number} "
                  f" desription :{tournament.description}")
        print("\n")

    @staticmethod
    def add_players_tournament():
        print("--------Choisir 8 joueurs dans la liste---------")
        choices_ids = []
        for i in range(8):
            choices_ids.append(Feature.for_int
                               ("choisir une ID dans la liste:"))

        return choices_ids

    @staticmethod
    def choice_tournament(tournaments):
        user_choice = input("choisir un tournoi par son nom: ")
        for tournament in tournaments:
            if user_choice == tournament.name:
                return tournament


class CurrentTournamentView:

    @staticmethod
    def display_current_tournament(tournament):
        print(f"nom du tournoi: {tournament.name}")
        print(f"Lieu du tournoi: {tournament.location}")
        print(f"date du tournoi: {tournament.dated}")
        print(f"type de partie du tournoi: {tournament.time_control}")
        print(f"nombre de ronde du tournoi: {tournament.round_number}")
        print(f"descritpion du tournoi: {tournament.description}\n")
        print("--------joueurs------")
        for p, players in enumerate(tournament.players):
            print(f"joueur {p + 1}: {players}")
        print("\n")

        print("------rounds------\n")
        if not tournament.rounds:
            print("Pas encore de round commencé")
        else:
            for i, tournament_round in enumerate(tournament.rounds):
                print(f"Round {i + 1} {tournament_round.start_dated}\n")

                for j, match in enumerate(tournament_round.matches):
                    print(f"Match {j + 1}: {match.player1} VS {match.player2}")
                    if match.winner == 1:
                        print(f" le gagnant est le joueur {match.player1}")
                    elif match.winner == 2:
                        print(f" le gagnant est le joueur {match.player2}")
                    elif match.winner == 0:
                        print(f" le joueur {match.player1} et le joueur "
                              f"{match.player2} sont equalités")
                print("\n")

    @staticmethod
    def update_point(tournament_round):
        print("--------Points de la partie--------\n")
        print("0 pour égalité")
        print("1 pour player1 gagne")
        print("2 pour player2 gagne\n")
        matches_results = []
        for j, match in enumerate(tournament_round.matches):
            print(f"{j}. {match.player1} VS {match.player2}")
            user_choice = int(input("choisir le vainqueur: "))
            matches_results.append(user_choice)
        return matches_results
