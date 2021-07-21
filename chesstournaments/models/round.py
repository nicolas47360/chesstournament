import datetime


class Round:

    def __init__(self, start_dated):

        self.matches = []
        self.start_dated = start_dated
        self.end_dated = None

    def start_round(self):
        self.start_dated = datetime.datetime.today()

    def end_round(self):
        self.end_dated = datetime.datetime.today()
        for match in self.matches:
            self.matches.append(match)

    def finished(self):
        return all(match.finished() for match in self.matches)
        #return self.matches[0].finished() and self.matches[1].finished() and self.matches[2].finished() and self.matches[3].finished()

    def round_dict(self):
        return {"matches": [match.to_dict() for match in self.matches], "start_round": str(self.start_dated),
                "end_round": str(self.end_dated)}

    @property
    def players(self):
        players = []
        for match in self.matches:
            players.append(match.player1)
            players.append(match.player2)
        return players
