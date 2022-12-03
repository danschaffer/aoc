#!/usr/bin/env python3
import sys
class Day:
    def __init__(self, file):
        self.data = {}
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split()

    def run_part1(self):
        return -1

    def run_part2(self):
        return -1

def test1():
    test_day = Day('./day-test.input')
    assert test_day.run_part1() == -1
    assert test_day.run_part2() == -1

def test2():
    test_day = Day('./day.input')
    assert test_day.run_part1() == -1
    assert test_day.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day")
    file = './day.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day = Day(file)
    print(f"part 1: {day.run_part1()}")
    print(f"part 2: {day.run_part2()}")
