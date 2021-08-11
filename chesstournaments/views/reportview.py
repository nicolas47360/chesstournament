class ReportView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("\n-------RAPPORT------\n")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input(">> ")
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
                print(f"ID: {p.identity} nom: {p.last_name} "
                      f" prenom: {p.first_name}  age: {p.birth_date} "
                      f" sexe : {p.gender}  rang: {p.ranking}")

        if user_choice == "2":
            for p in sorted(players, key=lambda x: x.ranking, reverse=True):
                print(f"ID: {p.identity} nom: {p.last_name} "
                      f" prenom: {p.first_name}  age: {p.birth_date} "
                      f" sexe : {p.gender}  rang: {p.ranking}")

    @staticmethod
    def players_for_tournament(tournament):
        print("1: Classement des joueurs par ordre alphabetique")
        print("2: classement des joueurs par rang\n")
        choice = input("choisir: ")

        if choice == "1":
            for player in sorted(tournament.players,
                                 key=lambda x: x.last_name):
                print(f"nom: {player.last_name} prenom: {player.first_name}"
                      f" age: {player.birth_date}"
                      f" sexe: {player.gender} rang: {player.ranking}")

        if choice == "2":
            for player in sorted(tournament.players,
                                 key=lambda x: x.ranking, reverse=True):
                print(f"nom: {player.last_name} prenom: {player.first_name}"
                      f" age: {player.birth_date} "
                      f" sexe: {player.gender} rang: {player.ranking}")

    @staticmethod
    def tournament_rounds(tournament):
        for t_round in tournament.rounds:
            print(f" {t_round}\n")
            for m, match in enumerate(t_round.matches):
                print(f"match{m + 1}: {match}")
                if match.winner == 1:
                    print(f" le gagnant est le joueur {match.player1}")
                elif match.winner == 2:
                    print(f" le gagnant est le joueur {match.player2}")
                elif match.winner == 0:
                    print(f" le joueur {match.player1}"
                          f" et le joueur {match.player2} sont equalités")
            print("\n")
        print("\n")
