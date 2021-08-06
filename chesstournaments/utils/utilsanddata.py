import datetime
from tinydb import TinyDB, where
from ..models.player import Player
from ..models.tournament import Tournament
from ..models.round import Round
from ..models.match import Match


class PlayerData:

    db = TinyDB("players.json")
    players_table = db.table("Players")

    def save_player_data(self, player):

        self.players_table.insert(
            {"identity": player.identity,
             "last_name": player.last_name,
             "first_name": player.first_name,
             "birth_date": str(player.birth_date),
             "gender": player.gender,
             "ranking": player.ranking
             })

    def delete_player(self, identity):
        self.players_table.remove(where("identity") == int(identity))

    @staticmethod
    def load_player():
        players_dict = PlayerData().players_table.all()
        players = [Player(**data) for data in players_dict]
        return players

    @staticmethod
    def get_player(player_id):
        players_dict = PlayerData().players_table.all()
        for player_dict in players_dict:
            if player_dict["identity"] == player_id:
                return Player(**player_dict)


class TournamentData:

    db = TinyDB("tournaments.json")
    tournaments_table = db.table("tournaments")

    def save_tournaments(self, tournament):

        self.tournaments_table.insert(
            {"name": tournament.name,
             "location": tournament.location,
             "dated": tournament.dated,
             "time_control": tournament.time_control,
             "round_number": tournament.round_number,
             "description": tournament.description,
             "players": [player.identity for player in tournament.players],
             "rounds": [tournament_round.round_dict() for tournament_round in tournament.rounds]
             }
        )

    @staticmethod
    def load_tournaments():
        tournaments = []
        for tournament_dict in TournamentData().tournaments_table.all():
            tournament = Tournament(name=tournament_dict["name"],
                                    location=tournament_dict["location"],
                                    dated=tournament_dict["dated"],
                                    time_control=tournament_dict["time_control"],
                                    round_number=tournament_dict["round_number"],
                                    description=tournament_dict["description"])
            tournaments.append(tournament)
            TournamentData.load_players(tournament, tournament_dict.get("players", []))
            TournamentData.load_rounds(tournament, tournament_dict.get("rounds", []))

        return tournaments

    @staticmethod
    def load_players(tournament, player_ids):
        for player_id in player_ids:
            tournament.players.append(PlayerData.get_player(player_id))

    @staticmethod
    def load_rounds(tournament, tournament_rounds):
        for tournament_round in tournament_rounds:
            turn = Round(start_dated=tournament_round["start_round"], name=tournament_round["name"])
            for match_dict in tournament_round.get("matches", []):
                match = Match(PlayerData.get_player(match_dict["player1"]),
                              PlayerData.get_player(match_dict["player2"]))
                match.start_date = match_dict["start_match"]
                match.end_date = match_dict["end_match"]
                turn.matches.append(match)
            tournament.rounds.append(turn)


class Feature:

    @staticmethod
    def for_string(text):
        while True:
            write = input(text).capitalize()
            if not write.isalpha():
                print("Veuillez entrer des lettres")
            else:
                break
        return write

    @staticmethod
    def birth_date(text):
        while True:
            try:
                birth_date = input(text)
                date = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
                date = date.date()
                break
            except ValueError:
                print("Veuillez entrer une date de naissance valide")

        return date

    @staticmethod
    def gender(text):
        while True:
            gender = input(text)
            if gender not in ('f', 'm'):
                print("Veuillez saisir soit f ou m")
            else:
                break
        return gender

    @staticmethod
    def ranking(text):
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

    @staticmethod
    def for_int(text):
        while True:
            try:
                write = int(input(text))
                break
            except ValueError:
                print("Veuillez entrer un chiffre")
        return write

    @classmethod
    def time_control(cls, text):
        while True:
            time_control = input(text)
            if time_control not in ("split", "blitz", "rapide"):
                print("veuillez rentrer split ou blitz ou rapide")
            else:
                break
        return time_control
