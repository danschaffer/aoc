#!/usr/bin/env python3

class Day16:
    def __init__(self, file):
        self.rules = list()
        self.nearby = list()
        lines=open(file).read().strip().split('\n')
        index0 = lines.index('')
        rules = lines[0:index0]
        index1 = lines.index('', index0+1)
        nearby = lines[index1+2:]
        for line in rules:
            (_,line) = line.split(':')
            line=line.strip()
            (range1,_,range2)=line.split()
            (r0,r1) = range1.split('-')
            self.rules += list(range(int(r0),int(r1)+1))
            (r0,r1) = range2.split('-')
            self.rules += list(range(int(r0),int(r1)+1))
        for line in nearby:
            self.nearby += [int(n) for n in line.split(',')]
    def run_part1(self):
        return sum([n for n in self.nearby if n not in self.rules])

    def run_part2(self):
        return -1

def test1():
    test_day16 = Day16('./day16-test.input')
    assert test_day16.run_part1() == 71
    assert test_day16.run_part2() == -1
    test_day16a = Day16('./day16.input')
    assert test_day16a.run_part1() == 20048

if __name__ == '__main__':
    print("advent of code: day16")
    day16 = Day16('./day16.input')
    print(f"part 1: {day16.run_part1()}")
    print(f"part 2: {day16.run_part2()}")
