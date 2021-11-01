#!/usr/bin/env python3

class Day23:
    def __init__(self, file):
        self.data = []
        for line in open(file).readlines():
            part1,part2 = line.split()
            coords=part1[5:-2].split(',')
            self.data.append([int(coords[0]),int(coords[1]),int(coords[2]),int(part2[2:])])

    def run_part1(self):
        max_range = 0
        max_nanobot = 0
        for i in range(len(self.data)):
            range_ = self.data[i][3]
            if range_ > max_range:
                max_range = range_
                max_nanobot = i
        result = 0
        for i in range(len(self.data)):
            dist = abs(self.data[i][0] - self.data[max_nanobot][0]) + abs(self.data[i][1] - self.data[max_nanobot][1]) + abs(self.data[i][2] - self.data[max_nanobot][2])
            if dist <= max_range:
                result += 1
        return result  

def test1():
    assert Day23('day23-test.input').run_part1() == 7
    assert Day23('day23.input').run_part1() == 721

if __name__ == '__main__':
    print("advent of code: day23")
    print(f"part 1: {Day23('day23.input').run_part1()}")
