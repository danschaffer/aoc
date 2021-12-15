#!/usr/bin/env python3
from collections import Counter
class Day14:
    def __init__(self, file):
        self.start = ''
        self.data = {}
        lines = [line.strip() for line in open(file).readlines()]
        self.start = lines.pop(0)
        lines.pop(0)
        for line in lines:
            key, value = line.split('->')
            self.data[key.strip()] = value.strip()

    def run(self, steps=10):
        pairs = Counter()
        for i in range(len(self.start)-1):
            pairs[self.start[i]+self.start[i+1]] += 1
        elements = Counter(self.start)
        for _ in range(steps):
            pairs1 = Counter()
            for pair in pairs.keys():
                insertion, old_count = self.data[pair], pairs[pair]
                pairs1[pair[0]+insertion] += old_count
                pairs1[insertion+pair[1]] += old_count
                elements[insertion] += old_count
            pairs = pairs1
        return max(elements.values()) - min(elements.values())

def test1():
    test_day14 = Day14('./day14-test.input')
    assert test_day14.run(steps=10) == 1588
    assert test_day14.run(steps=40) == 2188189693529

def test2():
    test_day14 = Day14('./day14.input')
    assert test_day14.run(steps=10) == 2447
    assert test_day14.run(steps=40) == 3018019237563

if __name__ == '__main__':
    print("advent of code: day14")
    day14 = Day14('./day14.input')
    print(f"part 1: {day14.run(steps=10)}")
    print(f"part 2: {day14.run(steps=40)}")
