#!/usr/bin/env python
class Marble:
    def __init__(self, number, left=None, right=None):
        self.number = number
        if not left:
            left = self
        self.left = left
        if not right:
            right = self
        self.right = right

    def __str__(self):
        return str(self.number)

class Board:
    def __init__(self):
        self._current = Marble(0)

    def move(self, player, marble):
        score = 0
        if marble.number % 23 == 0:
            score = marble.number
            marble6 = self._current.left.left.left.left.left.left
            marble7 = marble6.left
            marble8 = marble7.left
            score += marble7.number
            self._current = marble6
            marble6.left = marble6.left.left
            marble8.right = marble6
        else:
            cw = self._current.right
            cw2 = self._current.right.right
            marble.left = cw
            marble.right = cw2
            cw.right = marble
            cw2.left = marble
            self._current = marble
        return score

class Game:
    def __init__(self, players, marbles):
        self.players = players
        self.marbles = marbles
        self.scores = [0 for _ in range(players+1)]
        self.board = Board()

    def run(self):
        for marble in range(1, self.marbles):
            player = marble % self.players
            self.scores[player] += self.board.move(player, Marble(marble))
        return max(self.scores)

game = Game(9,25) # 32
print("9 25 = %d" % game.run())
game = Game(10, 1618) # 8317
print("10 1618 = %d" % game.run())
game = Game(13, 7999) # 146373
print("13 7999 = %d" % game.run())
game = Game(17, 1104) # 2764
print("17 1104 = %d" % game.run())
game = Game(21, 6111) # 54718
print("21 6111 = %d" % game.run())
game = Game(30, 5807) # 37305
print("30 5807 = %d" % game.run())

game = Game(405, 71700) # 428690
print("405 71700 = %d" % game.run())

game = Game(405, 7170000) # 3628143500
print("405 7170000 = %d" % game.run())
