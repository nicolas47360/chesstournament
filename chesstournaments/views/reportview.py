class ReportView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("-------RAPPORT------\n")
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


class ReportPlayer:

    @staticmethod
    def player_view(players):
        print("1: Classement des joueurs par ordre alphabetique")
        print("2: classement des joueurs par rang\n")
        user_choice = input("choisir: \n")
        if user_choice == "1":
            for p in sorted(players, key=lambda x: x.last_name):
                print("ID: {} nom: {}, prenom: {}, age: {}, sexe : {}, rang: {}\n".format(p.identity,
                      p.last_name, p.first_name, p.birth_date, p.gender, p.ranking))

        if user_choice == "2":
            for p in sorted(players, key=lambda x: x.ranking, reverse=True):
                print("ID: {} nom: {}, prenom: {}, age: {}, sexe : {}, rang: {}\n".format(p.identity,
                      p.last_name, p.first_name, p.birth_date, p.gender, p.ranking))



    @staticmethod
    def players_for_tournament(tournament):
        print("1: Classement des joueurs par ordre alphabetique")
        print("2: classement des joueurs par rang\n")
        choice = input("choisir: \n")
        if choice == "1":
            for player in sorted(tournament.players,  key=lambda x: x.last_name):
                print(f"nom: {player.last_name} prenom: {player.first_name} age: {player.birth_date}"
                      f"sexe: {player.gender} rang: {player.ranking}")

        if choice == "2":
            for player in sorted(tournament.players, key=lambda x: x.ranking, reverse=True):
                print(f"nom: {player.last_name} prenom: {player.first_name} age: {player.birth_date} "
                      f"sexe: {player.gender} rang: {player.ranking}")

    @staticmethod
    def tournament_rounds(tournament):
        print(f" round : {tournament.rounds}")

    @staticmethod
    def tournament_matches(tournament):
        for match in tournament.rounds:
            print(f"match: {match.player1} Vs {match.player2}")
