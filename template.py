#!/usr/bin/env python3

class Day:
    def __init__(self):
        self.lines = []

    def load(self, file):
#        self.lines = open(file).read().strip().split('\n')
        pass

    def run_part1(self):
        return -1

    def run_part2(self):
        return -1

def test1():
    test_day = Day()
    test_day.load('./day.input')
    assert test_day.run_part1() == -1
    assert test_day.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day")
    day = Day()
    day.load('./day.input')
    print(f"part 1: {day.run_part1()}")
    print(f"part 2: {day.run_part2()}")
