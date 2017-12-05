class Game(object):
    """ Represent a game"""

    def __init__(self, player='Guest'):
        self.player = player
        self.score = 0
        self.turn = 1
