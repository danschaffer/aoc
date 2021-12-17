#!/usr/bin/env python3

class Day17:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def run_part1(self,minx,maxx,miny,maxy):
        best = -1
        for x in range(minx,maxx):
            for y in range(miny,maxy):
                height = self.simulate(x,y)
                best = max(best, height)
        return best

    def run_part2(self,minx,maxx,miny,maxy):
        count = 0
        for x in range(minx,maxx):
            for y in range(miny,maxy):
                if self.simulate(x,y) > -1:
                    count += 1
        return count

    def simulate(self, xvel, yvel):
        xpos = 0
        ypos = 0
        ymax = 0
        while ypos >= self.ymin:
            xpos += xvel
            ypos += yvel
            if xvel > 0:
                xvel -= 1
            elif xvel < 0:
                xvel += 1
            yvel -= 1
            ymax = max(ymax, ypos)
            if xpos >= self.xmin and xpos <= self.xmax and ypos >= self.ymin and ypos <= self.ymax:
                return ymax
        return -1


def test1():
    xmin, xmax, ymin, ymax = parse_input('./day17-test.input')
    day17 = Day17(xmin, xmax, ymin, ymax)
    assert day17.simulate(6,9) == 45
    assert day17.run_part1(0,10,0,10) == 45
    assert day17.run_part2(0,40,-20,20) == 112

def test2():
    xmin, xmax, ymin, ymax = parse_input('./day17.input')
    day17 = Day17(xmin, xmax, ymin, ymax)
    assert day17.run_part1(0,50,0,200) == 6555
    assert day17.run_part2(0,300,-200,400) == 4973


def parse_input(input):
    _, _, xin, yin = open(input).read().split() 
    xmin = int(xin.split('=')[1].split('..')[0])
    xmax = int(xin.split('=')[1].split('..')[1][:-1])
    ymin = int(yin.split('=')[1].split('..')[0])
    ymax = int(yin.split('=')[1].split('..')[1])
    return xmin, xmax, ymin, ymax

if __name__ == '__main__':
    print("advent of code: day17")
    xmin, xmax, ymin, ymax = parse_input('./day17.input')
    day17 = Day17(xmin, xmax, ymin, ymax)
    print(f"part 1: {day17.run_part1(0,50,0,200)}")
    print(f"part 2: {day17.run_part2(0,300,-200,400)}")
