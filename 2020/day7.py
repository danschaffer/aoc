#!/usr/bin/env python3
import sys
class Day7:
    def __init__(self):
        self.data = {}

    def load(self, file):
        for line in open(file).read().strip().split('\n'):
            tokens = line.split()
            name = tokens[0] + ' ' + tokens[1]
            self.data[name] = {}
            index = 4
            while True:
                if len(tokens) == 7 or index >= len(tokens):
                    break
                self.data[name][tokens[index + 1] + ' ' + tokens[index + 2]] = int(tokens[index])
                index += 4

    def run_part1(self, bag='shiny gold'):
        bags = set()
        for current, contents in self.data.items():
            if bag in contents:
                bags.add(current)
                bags.update(self.run_part1(current))
        return bags

    def run_part2(self, bag='shiny gold'):
        count = 0
        for current, num in self.data[bag].items():
            count += num * (self.run_part2(current) + 1)
        return count

def test1():
    test_day7 = Day7()
    test_day7.load('./day7-test.input')
    assert len(test_day7.run_part1()) == 4
    assert test_day7.run_part2() == 32

    test_day7a = Day7()
    test_day7a.load('./day7-test2.input')
    assert test_day7a.run_part2() == 126

if __name__ == '__main__':
    print(f"advent of code: day7")
    day7 = Day7()
    day7.load('./day7.input')
    print(f"part 1: {len(day7.run_part1())}")
    print(f"part 2: {day7.run_part2()}")
