import datetime


class Match:
    WIN_POINT = 1
    EQUALITY_POINT = 0.5

    def __init__(self, opponent1, opponent2):
        self.opponent1 = opponent1
        self.opponent2 = opponent2
        self.winner = None
        self.start_date = None
        self.end_date = None
        self.points = 0

    def start_match(self):
        self.start_date = datetime.datetime.today()

    def end_match(self, winner=None):
        self.end_date = datetime.datetime.today()
        if winner:
            self.winner.update_points(self.WIN_POINT)
        else:
            self.opponent1.update_points(self.EQUALITY_POINT)
            self.opponent2.update_points(self.opponent2)

    def update_points(self, points):
        self.points += points
















