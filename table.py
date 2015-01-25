class Table:
    def __init__(self,name):
        self.name = name
        self.players = []
    def addPlayer(self,player):
        self.players.append(player)
    def getPlayers(self):
        return self.players
    def newRound(self):
        self.players = []
    def __str__(self):
        return "Table " + str(self.name)
