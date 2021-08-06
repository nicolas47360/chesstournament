import datetime


class Round:

    def __init__(self, start_dated, name):

        self.matches = []
        self.name = name
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

    def round_dict(self):
        return {"matches": [match.to_dict() for match in self.matches],
                "name": self.name,
                "start_round": str(self.start_dated) if self.start_dated else None,
                "end_round": str(self.end_dated) if self.end_dated else None}

    def __repr__(self):
        return f" {self.start_dated} {self.end_dated or 'pas encore fini'} "


