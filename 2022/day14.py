#!/usr/bin/env python3
import sys
class Day14:
    def __init__(self, file):
        self.data = {}
        self.start = (500,0)
        self.lowest = 0
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split()
            n = 0
            point1 = None
            while n < len(parts):
                x2,y2 = parts[n].split(',')
                x2 = int(x2)
                y2 = int(y2)
                point2 = (x2,y2)
                if point1:
                    x1,y1 = point1

                    for x in range(min(x1,x2), max(x1,x2)+1):
                        for y in range(min(y1,y2), max(y1,y2)+1):
                            self.data[(x,y)] = '#'
                            self.lowest = max(y,self.lowest)
                point1 = point2
                n += 2

    def draw_screen(self):
        start = self.start
        minx = maxx = 500
        miny = maxy = 0
        for pt in self.data:
            x, y = pt
            minx = min(x,minx)
            maxx = max(x,maxx)
            miny = min(y,miny)
            maxy = max(y,maxy)
        for y in range(miny, maxy+2):
            line = ''
            for x in range(minx, maxx+2):
                if (x,y) == start:
                    line += '+'
                elif (x,y) in self.data:
                    line += self.data[(x,y)]
                else:
                    line += '.'
            print(line)

    def drop(self):
        x = self.start[0]
        y = self.start[1]
        while True:
            if y > self.lowest + 1:
                return False
            if (x,y+1) in self.data and (x-1,y+1) in self.data and (x+1,y+1) in self.data:
                self.data[(x,y)] = 'o'
                return True
            elif (x,y+1) not in self.data:
                y += 1
            elif (x-1,y+1) not in self.data:
                x -= 1
                y += 1
            elif (x+1,y+1) not in self.data:
                x += 1
                y += 1
            else:
                assert False
            
    def drop2(self):
        x = self.start[0]
        y = self.start[1]
        while True:
            if y > self.lowest:
                self.data[(x,y)] = 'o'
                return True
            if (x,y+1) in self.data and (x-1,y+1) in self.data and (x+1,y+1) in self.data:
                self.data[(x,y)] = 'o'
                return True
            elif (x,y+1) not in self.data:
                y += 1
            elif (x-1,y+1) not in self.data:
                x -= 1
                y += 1
            elif (x+1,y+1) not in self.data:
                x += 1
                y += 1
            else:
                assert False


    def run_part1(self):
        drops = 0
        while self.drop():
            drops += 1
        return drops

    def run_part2(self):
        drops = 0
        while self.start not in self.data:
            self.drop2()
            drops += 1
        return drops

def test1():
    test_day14 = Day14('./day14-test.input')
    assert test_day14.run_part1() == 24
    test_day14 = Day14('./day14-test.input')
    assert test_day14.run_part2() == 93

def test2():
    test_day14 = Day14('./day14.input')
    assert test_day14.run_part1() == 614
    test_day14 = Day14('./day14.input')
    assert test_day14.run_part2() == 26170

if __name__ == '__main__':
    print("advent of code: day14")
    file = './day14.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day14 = Day14(file)
    print(f"part 1: {day14.run_part1()}")
    day14 = Day14(file)
    print(f"part 2: {day14.run_part2()}")
