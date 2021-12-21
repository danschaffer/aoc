#!/usr/bin/env python3

class Day21:
    def __init__(self, file):
        self.data = {}
        lines=[line.strip() for line in open(file).read().split('\n')]
        self.player1 = int(lines[0].split()[4])
        self.player2 = int(lines[1].split()[4])
        self.score1 = 0
        self.score2 = 0
        self.dice = 1
        self.rolls = 0

    def roll(self):
        answer = self.dice
        self.dice += 1
        if self.dice > 100:
            self.dice = 1
        self.rolls += 1
        return answer

    def run_part1(self):
        while True:
            rolls = []
            for _ in range(3):
                roll = self.roll()
                rolls.append(roll)
                self.player1 += roll
                while self.player1 > 10:
                    self.player1 = self.player1 - 10
            self.score1 += self.player1
            print(f"player 1 rolls {rolls} and moves to space {self.player1} for a total score of {self.score1}")
            if self.score1 >= 1000:
                return self.score2 * self.rolls
            rolls = []
            for _ in range(3):
                roll = self.roll()
                rolls.append(roll)
                self.player2 += roll
                while self.player2 > 10:
                    self.player2 = self.player2 - 10
            self.score2 += self.player2
            print(f"player 2 rolls {rolls} and moves to space {self.player2} for a total score of {self.score2}")
            if self.score2 >= 1000:
                return self.score1 * self.rolls

    def run_part2(self):
        return -1

def test1():
    test_day21 = Day21('./day21-test.input')
    assert test_day21.run_part1() == 739785
    assert test_day21.run_part2() == 444356092776315

def test2():
    test_day21 = Day21('./day21.input')
    assert test_day21.run_part1() == 597600
    assert test_day21.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day21")
    day21 = Day21('./day21.input')
    print(f"part 1: {day21.run_part1()}")
    print(f"part 2: {day21.run_part2()}")
