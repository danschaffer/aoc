#!/usr/bin/env python3

from itertools import permutations
from math import prod

class Day1:
    def __init__(self, numbers=None):
        self.numbers = numbers

    def load(self, file):
        self.numbers = [int(number) for number in open(file).read().strip().split('\n')]

    def run_part1(self):
        return self.find_answer(2)

    def run_part2(self):
        return self.find_answer(3)

    def find_answer(self, size):
        for permutation in permutations(self.numbers, size):
            if sum(permutation) == 2020:
                return prod(permutation)
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

    test_day1a = Day1()
    test_day1a.load('./day1.input')
    assert test_day1a.run_part2() == 199068980

if __name__ == '__main__':
    day1 = Day1()
    day1.load('./day1.input')
    print(f"part 1: {day1.run_part1()}")
    print(f"part 2: {day1.run_part2()}")
