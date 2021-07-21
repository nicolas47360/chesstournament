import datetime


class Match:
    WIN_POINT = 1
    EQUALITY_POINT = 0.5

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.start_date = None
        self.end_date = None

    def start_match(self):
        self.start_date = datetime.datetime.today()

    def end_match(self, winner):
        self.end_date = datetime.datetime.today()
        self.winner = winner
        if winner == 1:
            self.player1.update_points(self.WIN_POINT)
        if winner == 2:
            self.player2.update_points(self.WIN_POINT)
        if winner == 0:
            self.player1.update_points(self.EQUALITY_POINT)
            self.player2.update_points(self.EQUALITY_POINT)

    def finished(self):
        return self.winner is not None

    def to_dict(self):
        return {"player1": self.player1.identity, "player2": self.player2.identity,
                "start_match": str(self.start_date), "end_match": str(self.end_date)}














