import datetime
from .match import Match



class Round:

    def __init__(self, start_dated):

        self.matches = []
        self.start_dated = start_dated
        self.end_dated = None
        self.players = []

    def start_round(self):
        self.start_dated = datetime.datetime.today()



    def end_round(self):
        self.end_dated = datetime.datetime.today()
        # chaque match sont finis
        # les point sont attribués
        pass




