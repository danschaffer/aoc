#!/usr/bin/env python3
import sys
from collections import Counter
class Day01:
    def __init__(self, file):
        self.first = []
        self.second = []
        with open(file) as f:
            for line in f:
                a, b = line.split()
                self.first.append(int(a))
                self.second.append(int(b))

    def run_part1(self):
        first = sorted(self.first)
        second = sorted(self.second)
        total = 0
        return sum(abs(a-b) for a,b in zip(self.first, self.second))
        
    def run_part2(self):
        total = 0
        freq = Counter(self.second)
        return sum(v * freq.get(v, 0) for v in self.first)

def test1():
    test_day = Day01('./sample.txt')
    assert test_day.run_part1() == 11
    assert test_day.run_part2() == 31

def test2():
    test_day = Day01('./input.txt')
    assert test_day.run_part1() == 2756096
    assert test_day.run_part2() == 23117829

if __name__ == '__main__':
    print("advent of code: day01")
    file = './input.txt'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day = Day01(file)
    print(f"part 1: {day.run_part1()}")
    print(f"part 2: {day.run_part2()}")
