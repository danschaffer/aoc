#!/usr/bin/env python3

class Day10:
    def __init__(self, file):
        self.lines = [line.strip() for line in open(file).readlines()]

    def run_part1(self):
        total = 0
        starts = '([{<'
        ends = ')]}>'
        points = [3, 57, 1197, 25137]
        for line in self.lines:
            stack = []
            for ch in line:
                if ch in starts:
                    stack.insert(0, ch)
                else:
                    start = stack.pop(0)
                    if ends.find(ch) != starts.find(start):
                        total += points[ends.find(ch)]
        return total

    def run_part2(self):
        total = 0
        starts = '([{<'
        ends = ')]}>'
        scores = []
        for line in self.lines:
            stack = []
            corrupt = False
            for ch in line:
                if ch in starts:
                    stack.insert(0, ch)
                else:
                    start = stack.pop(0)
                    if ends.find(ch) != starts.find(start):
                        corrupt = True
                        continue
            if corrupt is False and len(stack) > 0:
                score = 0
                for ch in stack:
                    score = score * 5 + starts.find(ch) + 1
                scores.append(score)
        return sorted(scores)[len(scores)//2]

def test1():
    day10 = Day10('./day10-test.input')
    assert day10.run_part1() == 26397
    assert day10.run_part2() == 288957

def test2():
    day10 = Day10('./day10.input')
    assert day10.run_part1() == 367227
    assert day10.run_part2() == 3583341858

if __name__ == '__main__':
    print("advent of code: day10")
    day10 = Day10('./day10.input')
    print(f"part 1: {day10.run_part1()}")
    print(f"part 2: {day10.run_part2()}")
