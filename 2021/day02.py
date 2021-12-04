#!/usr/bin/env python3

class Day02:
    def __init__(self, file):
        self.data = open(file).readlines()

    def run_part1(self):
        horz = 0
        depth = 0
        for line in self.data:
            parts = line.split()
            command = parts[0]
            amount = int(parts[1])
            if command == 'forward':
                horz += amount
            elif command == 'down':
                depth += amount
            elif command == 'up':
                depth -= amount
        return horz * depth

    def run_part2(self):
        aim = 0
        horz = 0
        depth = 0
        for line in self.data:
            parts = line.split()
            command = parts[0]
            amount = int(parts[1])
            if command == 'forward':
                horz += amount
                depth += aim * amount
            elif command == 'down':
                aim += amount
            elif command == 'up':
                aim -= amount
        return horz * depth

def test1():
    test_day02 = Day02('./day02-test.input')
    assert test_day02.run_part1() == 150
    assert test_day02.run_part2() == 900

def test2():
    test_day02 = Day02('./day02.input')
    assert test_day02.run_part1() == 1693300
    assert test_day02.run_part2() == 1857958050

if __name__ == '__main__':
    print("advent of code: day02")
    day02 = Day02('./day02.input')
    print(f"part 1: {day02.run_part1()}")
    print(f"part 2: {day02.run_part2()}")
