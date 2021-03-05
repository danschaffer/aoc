#!/usr/bin/env python3

class Day01:
    def __init__(self, file):
        self.numbers = [int(line) for line in open(file).readlines()]

    def run_part1(self):
        return sum(self.numbers)

    def run_part2(self):
        sums = set()
        freq = 0
        while True:
            for number in self.numbers:
                freq += number
                if freq in sums:
                    return freq
                sums.add(freq)

def test1():
    test_day01 = Day01('./day01-test.input')
    assert test_day01.run_part1() == 2
    assert test_day01.run_part2() == 2
    day01 = Day01('./day01.input')
    assert day01.run_part1() == 556
    assert day01.run_part2() == 448

if __name__ == '__main__':
    print("advent of code: day01")
    day01 = Day01('./day01.input')
    print(f"part 1: {day01.run_part1()}")
    print(f"part 2: {day01.run_part2()}")
