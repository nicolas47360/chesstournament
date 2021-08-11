from chesstournaments.models.round import Round
from chesstournaments.models.match import Match
import datetime


class Tournament:

    def __init__(self, name, location, dated,
                 time_control, description, round_number=4):
        self.name = name
        self.location = location
        self.dated = dated
        self.round_number = round_number
        self.time_control = time_control
        self.description = description
        self.rounds = []
        self.players = []

    def first_round(self):
        tournament_round = Round(datetime.datetime.today(),
                                 name=f"round {len(self.rounds) +1}")
        self.players.sort(key=lambda players: players.ranking, reverse=True)
        first_parts_players = []
        second_part_players = []
        for player in self.players:
            if player in self.players[:4]:
                first_parts_players.append(player)
            if player in self.players[4:]:
                second_part_players.append(player)
        tournament_round.matches = [Match(first_parts_players[i],
                                          second_part_players[i])
                                    for i in range(0, 4)]
        self.rounds.append(tournament_round)

    def next_round(self):
        while len(self.rounds) < 4:
            next_round = Round(datetime.datetime.today(),
                               name=f"round {len(self.rounds) +1}")
            self.players.sort(key=lambda p: (p.score, p.ranking), reverse=True)

            available = [p for p in self.players]
            while available:
                current = available.pop(0)
                for player in available:
                    if not self.has_played(current, player)\
                            or len(available) == 1:
                        next_round.matches.append(Match(current, player))
                        available = [i for i in available if i != player]
                        break
                    else:
                        continue
            self.rounds.append(next_round)
            return next_round

    def get_last_round(self):
        if self.rounds or len(self.rounds) == 4:
            tournament_round = self.rounds[-1]
            if tournament_round.finished():
                tournament_round = self.next_round()
            return tournament_round

    def has_played(self, player1, player2):
        for tournament_round in self.rounds:
            for match in tournament_round.matches:
                if player1 in (match.player1, match.player2) \
                        and player2 in (match.player1, match.player2):
                    return True
        return False

    @classmethod
    def from_dict(cls, tournaments_dict):
        tournament = cls(name=tournaments_dict["name"],
                         location=tournaments_dict["location"],
                         dated=tournaments_dict["dated"],
                         time_control=tournaments_dict["time_control"],
                         description=tournaments_dict["description"])
        for player_id in tournaments_dict["players"]:
            player = next(p for p in player_id if p.identity == player_id)
            tournament.players.append(player)
        return tournament

    def __repr__(self):
        return f"{self.name} {self.location} " \
               f"{self.time_control} {self.description} {self.dated}"
