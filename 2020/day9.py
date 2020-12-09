#!/usr/bin/env python3
from itertools import permutations
class Day9:
    def __init__(self, file, preamble=25):
        self.lines = [int(item) for item in self.load(file)]
        self.preamble = preamble
        self.weakness = -1

    def load(self, file):
        return open(file).read().strip().split('\n')

    def run_part1(self):
        for index in range(self.preamble, len(self.lines)):
            combinations = set()
            for perms in permutations(self.lines[index-self.preamble:index], 2):
                combinations.add(sum(perms))
            if self.lines[index] not in combinations:
                self.weakness = self.lines[index]
                return self.lines[index]

    def run_part2(self):
        for index1 in range(len(self.lines)):
            index2 = index1 + 1
            while index2 < len(self.lines) and sum(self.lines[index1:index2]) <= self.weakness:
                if sum(self.lines[index1:index2]) == self.weakness:
                    return min(self.lines[index1:index2]) + max(self.lines[index1:index2])
                index2 += 1

def test1():
    test_day9 = Day9('./day9-test.input', 5)
    assert test_day9.run_part1() == 127
    assert test_day9.run_part2() == 62

def test2():
    test_day9 = Day9('./day9.input', 25)
    assert test_day9.run_part1() == 530627549
    assert test_day9.run_part2() == 77730285

if __name__ == '__main__':
    print("advent of code: day9")
    day9 = Day9('./day9.input')
    print(f"part 1: {day9.run_part1()}")
    print(f"part 2: {day9.run_part2()}")
