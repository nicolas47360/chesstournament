import datetime
from tinydb import TinyDB, Query


class PlayerData:

    db = TinyDB("players.json")
    players_table = db.table("Players")


    def save_player_data(self, player):

        self.players_table.insert(
            {"last_name": player.last_name, "first_name": player.first_name, "birth_date": str(player.birth_date),
             "gender": player.gender, "ranking": player.ranking
             })

    def delete_player(self):
        query = Query()


class TournamentData:

    db = TinyDB("tournaments.json")
    tournaments_table = db.table("tournaments")

    def save_tournaments(self, tournament):
        self.tournaments_table.insert(
            {"name": tournament.name, "location": tournament.location, "date": tournament.dated,
             "time control": tournament.time_control, "round number": tournament.round_number,
             "description": tournament.description}
        )


class Feature:

    def for_string(self, text):
        while True:
            write = input(text).capitalize()
            if not write.isalpha():
                print("Veuillez entrer des lettres")
            else:
                break
        return write

    def birth_date(self, text):
        while True:
            try:
                birth_date = input(text)
                date = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
                date = date.date()
                break
            except ValueError:
                print("Veuillez entrer une date de naissance valide")

        return date

    def gender(self, text):
        while True:
            gender = input(text)
            if not gender in ('f', 'm'):
                print("Veuillez saisir soit f ou m")
            else:
                break
        return gender

    def ranking(self, text):
        while True:
            try:
                ranking = int(input(text))
                if ranking <= 0:
                    print("Veuillez entré une valeur > 0")
                else:
                    break
            except ValueError:
                print("Veuillez entrer un chiffre")
        return ranking
