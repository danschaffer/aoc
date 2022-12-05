#!/usr/bin/env python3
import copy
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

    def run(self):
        data1 = copy.deepcopy(self.data)
        data2 = copy.deepcopy(self.data)
        for (num, src, dest) in self.moves:
            for i in range(num):
                item1 = data1[src].pop(0)
                data1[dest].insert(0, item1)
                item2 = data2[src].pop(0)
                data2[dest].insert(i, item2)
        answer1 = ''.join([item[0] for item in data1])
        answer2 = ''.join([item[0] for item in data2])
        return answer1, answer2

def test1():
    answer1, answer2 = Day05('./day05-test.input').run()
    assert answer1 == 'CMZ'
    assert answer2 == 'MCD'

def test2():
    answer1, answer2 = Day05('./day05.input').run()
    assert answer1 == 'HNSNMTLHQ'
    assert answer2 == 'RNLFDJMCT'

if __name__ == '__main__':
    print("advent of code: day05")
    file = './day05.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    answer1, answer2 = Day05(file).run()
    print(f"part 1: {answer1}")
    print(f"part 2: {answer2}")
