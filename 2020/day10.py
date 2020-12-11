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
        numbers = [0] + self.adapters
        placeholders = [1] + [0 for x in range(len(numbers)-1)]
        for index1, number in enumerate(numbers):
            for index2 in range(1, 4):
                if number + index2 in numbers:
                    placeholders[numbers.index(number + index2)] += placeholders[index1]
        return placeholders[-1]

def test1():
    test_day10a = Day10('./day10-test2.input')
    assert test_day10a.run_part1() == 220

    test_day10b = Day10('./day10.input')
    assert test_day10b.run_part1() == 2343

def test2():
    test_day10a = Day10('./day10-test1.input')
    assert test_day10a.run_part2() == 8

    test_day10b = Day10('./day10-test2.input')
    assert test_day10b.run_part2() == 19208

    test_day10c = Day10('./day10.input')
    assert test_day10c.run_part2() == 31581162962944

if __name__ == '__main__':
    print("advent of code: day10")
    day10 = Day10('./day10.input')
    print(f"part 1: {day10.run_part1()}")
    print(f"part 2: {day10.run_part2()}")
