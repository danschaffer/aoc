#!/usr/bin/env python

class Day1:
    def __init__(self, file):
        self.data = [int(line) for line in open(file).readlines()]
    
    def part1(self):
        return sum([1 for n in range(len(self.data)-1) if self.data[n]<self.data[n+1]])

    def part2(self):
        return sum([1 for n in range(len(self.data)-3) if self.data[n]+self.data[n+1]+self.data[n+2]<self.data[n+1]+self.data[n+2]+self.data[n+3]])

def test1():
    assert Day1('day1-test.inp').part1() == 7
    assert Day1('day1.inp').part1() == 1301
    assert Day1('day1-test.inp').part2() == 5
    assert Day1('day1.inp').part2() == 1346

if __name__ == '__main__':
    print("aoc 2021 day 1")
    print(f"part 1: {Day1('day1.inp').part1()}")
    print(f"part 2: {Day1('day1.inp').part2()}")
