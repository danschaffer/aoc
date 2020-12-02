#!/usr/bin/env python3

class Day2:
    def __init__(self, lines=None):
        self.lines = lines

    def load(self, file):
        self.lines = open(file).read().strip().split('\n')

    def run_part1(self):
        count = 0
        for line in self.lines:
            (minmax, key, value) = line.split()
            min_ = int(minmax.split('-')[0])
            max_ = int(minmax.split('-')[1])
            key = key[:-1]
            occurrences = value.count(key)
            if occurrences >= min_ and occurrences <= max_:
                count += 1
        return count

    def run_part2(self):
        count = 0
        for line in self.lines:
            (positions, key, value) = line.split()
            pos1 = int(positions.split('-')[0])
            pos2 = int(positions.split('-')[1])
            key = key[:-1]
            matches = 0
            if value[pos1 - 1] == key:
                matches += 1
            if value[pos2 - 1] == key:
                matches += 1
            if matches == 1:
                count += 1
        return count

def test1():
    test_day2 = Day2([
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc',
    ])
    assert test_day2.run_part1() == 2
    assert test_day2.run_part2() == 1

def test2():
    test_day2 = Day2()
    test_day2.load('./day2.input')
    assert test_day2.run_part1() == 422
    assert test_day2.run_part1() == 451

if __name__ == '__main__':
    day2 = Day2()
    day2.load('./day2.input')
    print(f"part 1: {day2.run_part1()}")
    print(f"part 2: {day2.run_part2()}")
