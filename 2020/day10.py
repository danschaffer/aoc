#!/usr/bin/env python3

class Day10:
    def __init__(self, file):
        self.adapters = sorted([int(line) for line in open(file).read().strip().split('\n')])

    def run_part1(self):
        count1 = 1
        count3 = 1
        for index,item in enumerate(self.adapters):
            if item > 0 and item - self.adapters[index-1] == 1:
                count1 +=1
            if item > 0 and item - self.adapters[index-1] == 3:
                count3 += 1
        return count1 * count3

    def run_part2(self):
        combinations = [[0]]
        while max(combinations[0]) != max(self.adapters):
            combination = combinations.pop(0)
            if max(combination) + 1 in self.adapters:
                combinations += [combination + [max(combination) + 1]]
            if max(combination) + 2 in self.adapters:
                combinations += [combination + [max(combination) + 2]]
            if max(combination) + 3 in self.adapters:
                combinations += [combination + [max(combination) + 3]]
        return len(combinations)

def test1():
    test_day10a = Day10('./day10-test2.input')
    assert test_day10a.run_part1() == 220

    test_day10b = Day10('./day10.input')
    assert test_day10b.run_part1() == 2343

def test2():
    test_day10a = Day10('./day10-test1.input')
    assert test_day10a.run_part2() == 8

if __name__ == '__main__':
    print("advent of code: day10")
    day10 = Day10('./day10.input')
    print(f"part 1: {day10.run_part1()}")
#    print(f"part 2: {day10.run_part2()}")
