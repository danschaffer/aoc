#!/usr/bin/env python3

class Day02:
    def __init__(self, file):
        self.file = file

    def run(self):
        # A rock, B paper, C scissors
        # X rock, Y paper, Z scissors
        # rock beats scissors
        # scissors beats paper
        # paper beats rock
        answer1 = answer2 = 0
        my_score = {'X': 1, 'Y': 2, 'Z': 3}
        lose_score = {'A': 3,'B': 1, 'C': 2}
        tie_score = {'A': 1, 'B': 2, 'C': 3}
        win_score = {'A': 2, 'B': 3, 'C': 1}
        for line in open(self.file).readlines():
            opp, me = line.split()
            answer1 += my_score[me]
            if opp == 'A' and me == 'X' or opp == 'B' and me == 'Y' or opp == 'C' and me == 'Z':
                answer1 += 3
            elif me == 'X' and opp == 'C' or me == 'Z' and opp == 'B' or me == 'Y' and opp == 'A':
                answer1 += 6
            if me == 'X': # lose
                answer2 += lose_score[opp]
            elif me == 'Y': # tie
                answer2 += 3 + tie_score[opp]
            elif me == 'Z': # win
                answer2 += 6 + win_score[opp]
        return answer1, answer2

def test1():
    answer1, answer2 = Day02('./day02-test.input').run()
    assert answer1 == 15
    assert answer2 == 12

def test2():
    answer1, answer2 = Day02('./day02.input').run()
    assert answer1 == 8392
    assert answer2 == 10116

if __name__ == '__main__':
    print("advent of code: day02")
    answer1, answer2 = Day02('./day02.input').run()
    print(f"part 1: {answer1}")
    print(f"part 2: {answer2}")
