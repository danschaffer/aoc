#!/usr/bin/env python3
import sys
class Day07:
    def __init__(self, file):
        self.data = [int(item) for item in open(file).read().strip().split(',')]

    def run(self):
        min_ = min(self.data)
        max_ = max(self.data)
        answer1 = answer2 = sys.maxsize
        for guess in range(min_, max_):
            answer1 = min(answer1, sum([abs(item - guess) for item in self.data]))
            answer2 = min(answer2, sum([(abs(item - guess))*(abs(item - guess)+1)//2 for item in self.data]))
        return answer1, answer2

def test1():
    p1, p2 = Day07('./day07-test.input').run()
    assert p1 == 37
    assert p2 == 168

def test2():
    p1, p2 = Day07('./day07.input').run()
    assert p1 == 336040
    assert p2 == 94813675

if __name__ == '__main__':
    print("advent of code: day07")
    p1, p2 = Day07('./day07.input').run()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")
