#!/usr/bin/env python3

class Day04:
    def __init__(self, file):
        self.numbers = []
        self.boards = []
        board = []
        self.lines = {}
        for line in open(file).readlines():
            if not self.numbers:
                self.numbers = [int(number) for number in line.split(',')]
            elif line.strip() == '':
                if board:
                    self.boards.append(board)
                board = []
            else:
                board += [int(number) for number in line.split()]
        if board:
            self.boards.append(board)
        for i in range(len(self.boards)):
            for j in range(5):
                self.lines[f"{i}c{j}"] = 0
                self.lines[f"{i}r{j}"] = 0

    def run_part1(self):
        while True:
            number = self.numbers.pop(0)
            for n,board in enumerate(self.boards):
                if number in self.boards[n]:
                    loc = board.index(number)
                    row = loc // 5
                    col = loc % 5
                    self.lines[f"{n}c{col}"] += 1
                    self.lines[f"{n}r{row}"] += 1
                    board[loc] = -1
                    if self.lines[f"{n}c{col}"] == 5 or self.lines[f"{n}r{row}"] == 5:
                        return sum([n for n in board if n > -1])*number
            assert self.numbers

    def run_part2(self):
        boards_won = []
        while True:
            number = self.numbers.pop(0)
            for n,board in enumerate(self.boards):
                if number in self.boards[n]:
                    loc = board.index(number)
                    row = loc // 5
                    col = loc % 5
                    self.lines[f"{n}c{col}"] += 1
                    self.lines[f"{n}r{row}"] += 1
                    board[loc] = -1
                    if self.lines[f"{n}c{col}"] == 5 or self.lines[f"{n}r{row}"] == 5:
                        if n not in boards_won:
                            boards_won.append(n)
                        if len(boards_won) == len(self.boards):
                            return sum([n0 for n0 in board if n0 > -1])*number
            assert self.numbers

def test1():
    test_day04 = Day04('./day04-test.input')
    assert test_day04.run_part1() == 4512
    test_day04 = Day04('./day04-test.input')
    assert test_day04.run_part2() == 1924

def test2():
    test_day04 = Day04('./day04.input')
    assert test_day04.run_part1() == 38594
    test_day04 = Day04('./day04.input')
    assert test_day04.run_part2() == 21184

if __name__ == '__main__':
    print("advent of code: day04")
    day04 = Day04('./day04.input')
    print(f"part 1: {day04.run_part1()}")
    day04 = Day04('./day04.input')
    print(f"part 2: {day04.run_part2()}")
