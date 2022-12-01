#!/usr/bin/env python3

class Day01:
    def __init__(self, file):
        self.data = [0]
        for line in open(file).readlines():
            if line.strip() == '':
                self.data.append(0)
            else:
                self.data[-1] += int(line.strip())

    def run_part1(self):
        return max(self.data)

    def run_part2(self):
        sorted_data = sorted(self.data, reverse=True)
        return sum(sorted_data[0:3])

def test1():
    test_day01 = Day01('./day01-test.input')
    assert test_day01.run_part1() == 24000
    assert test_day01.run_part2() == 45000

def test2():
    test_day01 = Day01('./day01.input')
    assert test_day01.run_part1() == 70613
    assert test_day01.run_part2() == 205805

if __name__ == '__main__':
    print("advent of code: day01")
    day01 = Day01('./day01.input')
    print(f"part 1: {day01.run_part1()}")
    print(f"part 2: {day01.run_part2()}")
