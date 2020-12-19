#!/usr/bin/env python3

class Day16:
    def __init__(self, file):
        self.rules = dict()
        self.rulesall = list()
        self.nearbyall = list()
        self.nearby = list()
        self.mine = list()
        lines=open(file).read().strip().split('\n')
        index0 = lines.index('')
        rules = lines[0:index0]
        index1 = lines.index('', index0+1)
        self.mine = [int(n) for n in lines[index0+2].split(',')]
        nearby = lines[index1+2:]
        for line in rules:
            (name,line) = line.split(':')
            line=line.strip()
            (range1,_,range2)=line.split()
            (range0,range1) = range1.split('-')
            self.rules[name] = list(range(int(range0),int(range1)+1))
            self.rulesall += list(range(int(range0),int(range1)+1))
            (range0,range1) = range2.split('-')
            self.rules[name] += list(range(int(range0),int(range1)+1))
            self.rulesall += list(range(int(range0),int(range1)+1))
        for line in nearby:
            self.nearby.append([int(n) for n in line.split(',')])
            self.nearbyall += [int(n) for n in line.split(',')]

    def run_part1(self):
        return sum([n for n in self.nearbyall if n not in self.rulesall])

    def run_part2(self):
        nearby = []
        for nearby0 in self.nearby:
            match = True
            for num in nearby0:
                if num not in self.rulesall:
                    match = False
                    break
            if match:
                nearby += [nearby0]
        matches = dict()
        for name in self.rules:
            matches[name] = []
        for name in self.rules:
            for index in range(len(nearby[0])):
                match = True
                for value in nearby:
                    if value[index] not in self.rules[name]:
                        match = False
                        break
                if match:
                    matches[name] += [index]
        while True:
            done = True
            for name in matches:
                if len(matches[name]) > 1:
                    done = False
                    break
            if done:
                break
            for name in matches:
                if len(matches[name]) == 1:
                    for name0 in matches:
                        if name0 != name and matches[name][0] in matches[name0]:
                            matches[name0].remove(matches[name][0])
        result = 1
        for name in matches:
            if name.startswith('departure'):
                result *= self.mine[matches[name][0]]
        return result

def test1():
    test_day16 = Day16('./day16-test.input')
    assert test_day16.run_part1() == 71
    test_day16a = Day16('./day16.input')
    assert test_day16a.run_part1() == 20048
    assert test_day16a.run_part2() == 4810284647569

if __name__ == '__main__':
    print("advent of code: day16")
    day16 = Day16('./day16.input')
    print(f"part 1: {day16.run_part1()}")
    print(f"part 2: {day16.run_part2()}")
