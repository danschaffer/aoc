#!/usr/bin/env python3
class Day07:
    def __init__(self, file):
        self.data = [int(item) for item in open(file).read().strip().split(',')]

    def run_part1(self):
        min_ = min(self.data)
        max_ = max(self.data)
        answer = 9999999999
        for guess in range(min_, max_):
            answer = min(answer, sum([abs(item - guess) for item in self.data]))
        return answer

    def run_part2(self):
        min_ = min(self.data)
        max_ = max(self.data)
        answer = 9999999999
        cache = {}
        for guess in range(min_, max_):
            answer0 = 0
            for item in self.data:
                diff = abs(item - guess)+1
                if diff not in cache:
                    summation = sum(range(diff))
                    cache[diff] = summation
                else:
                    summation = cache[diff]
                answer0 += summation
            answer = min(answer, answer0)
        return answer

def test1():
    test_day07 = Day07('./day07-test.input')
    assert test_day07.run_part1() == 37
    assert test_day07.run_part2() == 168

def test2():
    test_day07 = Day07('./day07.input')
    assert test_day07.run_part1() == 336040
    assert test_day07.run_part2() == 94813675

if __name__ == '__main__':
    print("advent of code: day07")
    day07 = Day07('./day07.input')
    print(f"part 1: {day07.run_part1()}")
    print(f"part 2: {day07.run_part2()}")
