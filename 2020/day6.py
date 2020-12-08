#!/usr/bin/env python3

class Day6:
    def __init__(self):
        self.lines = list()

    def load(self, file):
        self.lines = open(file).read().strip().split('\n') + [""]

    def run_part1(self):
        count = 0
        data = set()
        line = ""
        for line in self.lines:
            if line.strip() == "":
                count += len(data)
                data = set()
            else:
                for _,value in enumerate(line):
                    data.add(value)
        return count

    def run_part2(self):
        count = 0
        data = {}
        line = ""
        lines = 0
        for line in self.lines:
            if line.strip() == "":
                count += sum([1 for key in data if data[key] == lines])
                data = {}
                lines = 0
            else:
                for _,value in enumerate(line):
                    if value not in data.keys():
                        data[value] = 1
                    else:
                        data[value] += 1
                lines += 1
        return count

def test1():
    test_day6 = Day6()
    test_day6.load('./day6-test.input')
    assert test_day6.run_part1() == 11
    assert test_day6.run_part2() == 6

def test2():
    test_day6 = Day6()
    test_day6.load('./day6.input')
    assert test_day6.run_part1() == 6161
    assert test_day6.run_part2() == 2971

if __name__ == '__main__':
    print("advent of code: day6")
    day6 = Day6()
    day6.load('./day6.input')
    print(f"part 1: {day6.run_part1()}")
    print(f"part 2: {day6.run_part2()}")
