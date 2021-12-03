#!/usr/bin/env python3

class Day03:
    def __init__(self, file):
        self.lines = [line.strip() for line in open(file).readlines()]
        self.data = [int(line,2) for line in self.lines]
        self.length = len(self.lines[0])

    def run_part1(self):
        gamma = 0
        epsilon = 0
        for i in range(self.length):
            count = sum([j >> i & 1 for j in self.data])
            if count >= len(self.data) / 2:
                gamma = gamma | 1 << i
            else:
                epsilon = epsilon | 1 << i
        return gamma * epsilon

    def run_part2(self):
        oxygen = self.data[:]
        co2 = self.data[:]
        for i in range(self.length-1,-1,-1):
            count = sum([j >> i & 1 for j in oxygen])
            if count >= len(oxygen) / 2:
                oxygen=[j for j in oxygen if j >> i & 1 == 1]
            else:
                oxygen=[j for j in oxygen if j >> i & 1 == 0]
            if len(oxygen) == 1:
                break
        for i in range(self.length-1,-1,-1):
            count = sum([j >> i & 1 for j in co2])
            if count >= len(co2) / 2:
                co2 = [j for j in co2 if j >> i & 1 == 0]
            else:
                co2 = [j for j in co2 if j >> i & 1 == 1]
            if len(co2) == 1:
                break
        return oxygen[0] * co2[0]

def test1():
    test_day03 = Day03('./day03-test.input')
    assert test_day03.run_part1() == 198
    assert test_day03.run_part2() == 230

def test2():
    test_day03 = Day03('./day03.input')
    assert test_day03.run_part1() == 2648450
    assert test_day03.run_part2() == 2845944

if __name__ == '__main__':
    print("advent of code: day03")
    day03 = Day03('./day03.input')
    print(f"part 1: {day03.run_part1()}")
    print(f"part 2: {day03.run_part2()}")
