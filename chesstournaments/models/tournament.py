from chesstournaments.models.player import Player
from chesstournaments.models.round import Round
from chesstournaments.models.match import Match
import datetime
from tinydb import TinyDB


class Tournament:

    def __init__(self, name, location, dated,  time_control, description, round_number=4):
        self.name = name
        self.location = location
        self.dated = dated
        self.round_number = round_number
        self.time_control = time_control
        self.description = description
        self.rounds = []
        self.players = []

    def sort_by_ranking(self):
        self.players.sort(key=lambda players: players.ranking, reverse=True)

    def start_first_round(self):
        round = Round(datetime.date.today())
        match1 = Match(self.players[0], self.players[3])
        match2 = Match(self.players[1], self.players[4])
        match3 = Match(self.players[2], self.players[6])
        match4 = Match(self.players[3], self.players[7])
        round.match_list = [match1, match2, match3, match4]
        self.rounds.append(round)

    def end_tournament(self):
        self.dated = datetime.datetime.today()
        #tous les rounds sont finis
        #classez les joueurs en fonction du nombre de points
        pass









