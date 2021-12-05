#!/usr/bin/env python3
import math
class Day05:
    def __init__(self, file, part2=False):
        self.data = {}
        self.load(file, part2)

    def load(self, file, part2):
        for line in open(file).readlines():
            c0,_,c1 = line.split()
            x0,y0 = c0.split(',')
            x0 = int(x0)
            y0 = int(y0)
            x1,y1 = c1.split(',')
            x1 = int(x1)
            y1 = int(y1)
            segments = max(abs(x0-x1),abs(y0-y1))
            slopex = (x1 - x0)//segments
            slopey = (y1 - y0)//segments
            if part2 or x0 == x1 or y0 == y1:
                for i in range(segments+1):
                    self.data[(x0+i*slopex, y0+i*slopey)] = self.data.get((x0+i*slopex,y0+i*slopey), 0) + 1

    def run(self):
        return sum([1 for c in self.data if self.data[c]>1])        

    def print_map(self):
        maxx = maxy = 0
        for x,y in self.data:
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
        for y in range(maxy+1):
            line = ''
            for x in range(maxx+1):
                if (x,y) not in self.data:
                    line += '.'
                else:
                    line += f"{self.data[(x,y)]}"
            print(line)

def test1():
    test_day05 = Day05('./day05-test.input')
    assert test_day05.run() == 5
    test_day05 = Day05('./day05-test.input', part2=True)
    assert test_day05.run() == 12

def test2():
    test_day05 = Day05('./day05.input')
    assert test_day05.run() == 6005
    test_day05 = Day05('./day05.input', part2=True)
    assert test_day05.run() == 23864

if __name__ == '__main__':
    print("advent of code: day05")
    day05 = Day05('./day05.input')
    print(f"part 1: {day05.run()}")
    day05 = Day05('./day05.input', part2=True)
    print(f"part 2: {day05.run()}")
