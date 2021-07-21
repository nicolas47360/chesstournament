class Player:

    def __init__(self, identity, last_name, first_name, birth_date, gender, ranking):
        self.identity = identity
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.score = 0

    def __repr__(self):
        return f" {self.last_name.upper()} {self.first_name} ({self.ranking})"

    def update_points(self, point):
        self.score += point
