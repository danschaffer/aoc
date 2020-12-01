#!/usr/bin/env python3

from itertools import permutations

class Day1:
    def __init__(self, numbers=[]):
        self.numbers = numbers

    def load(self, file):
        self.numbers = [int(number) for number in open(file).read().strip().split('\n')]

    def run_part1(self):
        for permutation in permutations(self.numbers, 2):
            if sum(permutation) == 2020:
                return permutation[0] * permutation[1]
        assert False, "no combinations found"

    def run_part2(self):
        for permutation in permutations(self.numbers, 3):
            if sum(permutation) == 2020:
                return permutation[0] * permutation[1] * permutation[2]
        assert False, "no combinations found"

def test1():
    test_day1 = Day1([1721, 979, 366, 299, 675, 1456])
    assert test_day1.run_part1() == 514579

    test_day1a = Day1()
    test_day1a.load('./day1.input')
    assert test_day1a.run_part1() == 786811

def test2():
    test_day1 = Day1([1721, 979, 366, 299, 675, 1456])
    assert test_day1.run_part2() == 241861950


if __name__ == '__main__':
    day1 = Day1()
    day1.load('./day1.input')
    print(f"part 1: {day1.run_part1()}")
    print(f"part 2: {day1.run_part2()}")
