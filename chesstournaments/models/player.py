class Player:

    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.age = birth_date
        self.gender = gender
        self.ranking = ranking

    def new_player(self):
        pass

    def classify_player(self):
        pass

    def search_player(self):
        pass


players = []
player1 = Player(last_name="Kasparov", first_name="Yuri", birth_date=str(10/2/1958), gender="M", ranking=str(317))
player2 = Player(last_name="Merlin", first_name="Sacha", birth_date=str(28/10/2000), gender="M", ranking=str(78))
player3 = Player(last_name="Izumi", first_name="Sakura", birth_date=str(3/4/1996), gender="F", ranking=str(128))
player4 = Player(last_name="Stevenson", first_name="Patrick", birth_date=str(22/6/1982), gender="M", ranking=str(42))
player5 = Player(last_name="Weber", first_name="Bernard", birth_date=str(15/11/1968), gender="M", ranking=str(247))
player6 = Player(last_name="April", first_name="Marie", birth_date=str(29/9/1999), gender="F", ranking=str(109))
player7 = Player(last_name="Freon", first_name="Angele", birth_date=str(8/3/1992), gender="F", ranking=str(179))
player8 = Player(last_name="Craven", first_name="Rowan", birth_date=str(13/12/1988), gender="M", ranking=str(223))
players.extend([player1, player2, player3, player4, player5, player6, player7, player8])
