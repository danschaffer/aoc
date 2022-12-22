#!/usr/bin/env python3
import sys
class Day22:
    def __init__(self, file):
        self.data = {}
        self.start = None
        self.directions = []
        points, direction_list = open(file).read().split('\n\n')
        for y,line in enumerate(points.split('\n')):
            for x,ch in enumerate(line):
                if ch in ['.','#']:
                    self.data[(x,y)] = ch
                    if not self.start:
                        self.start = (x,y)
        start = n = 0
        while n < len(direction_list):
            if direction_list[n] in ['L','R']:
                self.directions.append((int(direction_list[start:n]), direction_list[n]))
                start = n + 1
            n += 1

    def move(self, move, loc):
        loc1 = (loc[0] + move[0], loc[1] + move[1])
        if loc1 not in self.data:
            if move == (-1,0):
                max1 = 0
                for pt in self.data:
                    if pt[1] == loc1[1]:
                        max1 = max(max1, pt[0])
                loc1 = (max1,loc[1])
            elif move == (1,0):
                min1 = 9999
                for pt in self.data:
                    if pt[1] == loc1[1]:
                        min1 = min(min1, pt[0])
                loc1 = (min1,loc[1])
            elif move == (0,-1):
                max1 = 0
                for pt in self.data:
                    if pt[0] == loc1[0]:
                        max1 = max(max1, pt[1])
                loc1 = (loc[0],max1)
            elif move == (0,1):
                min1 = 9999
                for pt in self.data:
                    if pt[0] == loc1[0]:
                        min1 = min(min1, pt[1])
                loc1 = (loc[0],min1)
        if self.data[loc1] == '#':
            loc1 = loc
        return loc1

    def run_part1(self):
        dir = 0
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        loc = self.start
        for steps, move in self.directions:
            for i in range(steps):
                loc1 = self.move(dirs[dir], loc)
                if loc == loc1:
                    break
                loc = loc1
            if move == 'R':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
        return (loc[1]+1) * 1000 + (loc[0]+1) * 4 + dir

    def run_part2(self):
        return -1

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run_part1() == 6032
    assert test_day22.run_part2() == -1

def test2():
    test_day22 = Day22('./day22.input')
    assert test_day22.run_part1() == 88268
    assert test_day22.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day22")
    file = './day22.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day22 = Day22(file)
    print(f"part 1: {day22.run_part1()}")
    print(f"part 2: {day22.run_part2()}")
