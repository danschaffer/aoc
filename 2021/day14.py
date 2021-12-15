#!/usr/bin/env python3
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
        counts = {}
        for n,ch in enumerate(self.start):
            if n < len(self.start) - 1:
                key = ch+self.start[n+1]
                counts[key] = counts.get(key,0) + 1
        for ct in range(steps):
            counts1 = counts
            counts = {}
            print(f"{ct} {counts}")
            for key in counts.keys():
                print(key)
                result = self.data[key]
                first = key[0] + result
                second = result + key[1]
                value = counts[key]
                for i in range(value):
                    counts[first] = counts.get(first,0) + 1
                    counts[second] = counts.get(second,0) + 1
        return max(counts.values()) - min(counts.values())

def test1():
    test_day14 = Day14('./day14-test.input')
    assert test_day14.run(steps=10) == 1588
    assert test_day14.run(steps=40) == 2188189693529

def test2():
    test_day14 = Day14('./day14.input')
    assert test_day14.run(steps=10) == 2447
#    assert test_day14.run(steps=40) == -1

if __name__ == '__main__':
    print("advent of code: day14")
    day14 = Day14('./day14-test.input')
    print(f"part 1: {day14.run(steps=10)}")
#    print(f"part 2: {day14.run(steps=40)}")
