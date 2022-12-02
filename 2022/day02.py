#!/usr/bin/env python3

class Day02:
    def __init__(self, file):
        self.file = file

    def run_part1(self):
        # A rock, B paper, C scissors
        # X rock, Y paper, Z scissors
        # rock beats scissors
        # scissors beats paper
        # paper beats rock
        answer = 0
        mescore = {'X': 1, 'Y': 2, 'Z': 3}
        for line in open(self.file).readlines():
            opp, me = line.split()
            answer += mescore[me]
            if opp == 'A' and me == 'X' or opp == 'B' and me == 'Y' or opp == 'C' and me == 'Z':
                answer += 3
            elif me == 'X' and opp == 'C' or me == 'Z' and opp == 'B' or me == 'Y' and opp == 'A':
                answer += 6
        return answer

    def run_part2(self):
        # X lose, Y draw, Z win
        answer = 0
        losescore = {'A': 3,'B': 1, 'C': 2}
        tiescore = {'A': 1, 'B': 2, 'C': 3}
        winscore = {'A': 2, 'B': 3, 'C': 1}
        for line in open(self.file).readlines():
            opp, me = line.split()
            if me == 'X': # lose
                answer += losescore[opp]
            elif me == 'Y': # tie
                answer += 3 + tiescore[opp]
            elif me == 'Z': # win
                answer += 6 + winscore[opp]
        return answer

def test1():
    test_day02 = Day02('./day02-test.input')
    assert test_day02.run_part1() == 15
    assert test_day02.run_part2() == 12

def test2():
    test_day02 = Day02('./day02.input')
    assert test_day02.run_part1() == 8392
    assert test_day02.run_part2() == 10116

if __name__ == '__main__':
    print("advent of code: day02")
    day02 = Day02('./day02.input')
    print(f"part 1: {day02.run_part1()}")
    print(f"part 2: {day02.run_part2()}")
