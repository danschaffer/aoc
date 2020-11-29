#!/usr/bin/env python3

class Day:
    def __init__(self):
        self.lines = []

    def load(self, file):
        self.lines = open(file).strip().split('\n')

    def run_part1(self):
        pass

def test1():
    test_day = Day()
    assert test_day.run_part1() == 1

if __name__ == '__main__':
    day = Day()
    day.load('./day.input')
    print(f"part 1: {day.run_part1()}")
#    print(f"part 2: {day.run_part2()}")
