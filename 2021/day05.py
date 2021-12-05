#!/usr/bin/env python3

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
            if x0 == x1 or y0 == y1:
                if x0 > x1 or y0 > y1:
                    x0, x1 = x1, x0
                    y0, y1 = y1, y0
                for x in range(x0,x1+1):
                    for y in range(y0,y1+1):
                        self.data[(x,y)] = self.data.get((x,y), 0) + 1
            elif part2:
                xoffset = yoffset = 1
                if x0 > x1:
                    xoffset = -1
                if y0 > y1:
                    yoffset = -1
                for i in range(abs(x0-x1)+1):
                    self.data[(x0+i*xoffset,y0+i*yoffset)] = self.data.get((x0+i*xoffset,y0+i*yoffset),0) + 1


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
