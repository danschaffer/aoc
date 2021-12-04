#!/usr/bin/env python3

class Day04:
    def __init__(self, file):
        self.numbers = []
        self.boards = []
        self.lines = self.load(file)
    
    def load(self, file):
        board = []
        lines = {}
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
                lines[f"{i}c{j}"] = 0
                lines[f"{i}r{j}"] = 0
        return lines

    def run(self):
        part1 = None
        boards_won = set()
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
                        boards_won.add(n)
                        answer = sum([b for b in board if b > -1])*number
                        if part1 is None:
                            part1 = answer
                        if len(boards_won) == len(self.boards):
                            return part1, answer

def test1():
    test_day04 = Day04('./day04-test.input')
    part1, part2 = test_day04.run()
    assert part1 == 4512
    assert part2 == 1924

def test2():
    test_day04 = Day04('./day04.input')
    part1, part2 = test_day04.run()
    assert part1 == 38594
    assert part2 == 21184

if __name__ == '__main__':
    print("advent of code: day04")
    day04 = Day04('./day04.input')
    part1, part2 = day04.run()
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
