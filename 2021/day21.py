#!/usr/bin/env python3
import functools
import itertools
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

    @functools.cache
    def count_wins(self, position_1, position_2, score_1, score_2):
        wins_1 = 0
        wins_2 = 0
        for roll_1, roll_2, roll_3 in itertools.product((1,2,3), repeat=3):
            new_position_1 = (position_1 - 1 + roll_1 + roll_2 + roll_3) % 10 + 1
            new_score_1 = score_1 + new_position_1
            if new_score_1 >= 21:
                wins_1 += 1
            else:
                new_wins_2, new_wins_1 = self.count_wins(position_2, new_position_1, score_2, new_score_1)
                wins_1 += new_wins_1
                wins_2 += new_wins_2
        return wins_1, wins_2

    def run_part2(self):
        scores = self.count_wins(self.player1, self.player2, 0, 0)
        return max(scores)

def test1():
    test_day21 = Day21('./day21-test.input')
    assert test_day21.run_part1() == 739785
    test_day21 = Day21('./day21-test.input')
    assert test_day21.run_part2() == 444356092776315

def test2():
    test_day21 = Day21('./day21.input')
    assert test_day21.run_part1() == 597600
    test_day21 = Day21('./day21.input')
    assert test_day21.run_part2() == 634769613696613

if __name__ == '__main__':
    print("advent of code: day21")
    day21 = Day21('./day21.input')
    print(f"part 1: {day21.run_part1()}")
    day21 = Day21('./day21.input')
    print(f"part 2: {day21.run_part2()}")
