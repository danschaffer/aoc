#!/usr/bin/env python3
import sys
class Day05:
    def __init__(self, file):
        self.data = []
        self.moves = []
        parse_top = False
        for line in open(file).readlines():
            if line.strip() == '' or line.startswith(' 1'):
                parse_top = True
                continue
            if not parse_top:
                i = 0
                n = 1
                while n < len(line):
                    item = line[n]
                    if i == len(self.data):
                        self.data.append([])
                    if item != ' ':
                        self.data[i].append(item)
                    n += 4
                    i += 1
            else:
                parts = line.split()
                self.moves.append((int(parts[1]), int(parts[3])-1, int(parts[5])-1))

    def run_part1(self):
        self.data1 = self.data[:]
        self.data2 = self.data[:]
        for (num, _from, to) in self.moves:
            for _ in range(num):
                item = self.data[_from].pop(0)
                self.data[to].insert(0, item)
        return ''.join([item[0] for item in self.data])

    def run_part2(self):
        for (num, _from, to) in self.moves:
            for n in range(num):
                item = self.data[_from].pop(0)
                self.data[to].insert(n, item)
        return ''.join([item[0] for item in self.data])

def test1():
    test_day05 = Day05('./day05-test.input')
    assert test_day05.run_part1() == 'CMZ'
    test_day05 = Day05('./day05-test.input')
    assert test_day05.run_part2() == 'MCD'

def test2():
    test_day05 = Day05('./day05.input')
    assert test_day05.run_part1() == 'HNSNMTLHQ'
    test_day05 = Day05('./day05.input')
    assert test_day05.run_part2() == 'RNLFDJMCT'

if __name__ == '__main__':
    print("advent of code: day05")
    file = './day05.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day05 = Day05(file)
    print(f"part 1: {day05.run_part1()}")
    day05 = Day05(file)
    print(f"part 2: {day05.run_part2()}")
