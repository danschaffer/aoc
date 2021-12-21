#!/usr/bin/env python3

class Day20:
    def __init__(self, file):
        lines = [line.strip() for line in open(file).read().split('\n')]
        self.data = {}
        self.algorithm = list(lines.pop(0))
        lines.pop(0)
        for y,line in enumerate(lines):
            for x,ch in enumerate(line):
                self.data[(x,y)] = ch

    def count(self):
        return sum([1 for ch in self.data if self.data[ch]=='#'])

    def get_point(self, point, outside_on):
        if point not in self.data:
            if outside_on:
                return '1'
            else:
                return '0'
        if self.data[point] == '.':
            return '0'
        return '1'
 
    def print_data(self):
        minx, miny = min(self.data)
        maxx, maxy = max(self.data)
        for y in range(miny,maxy+1):
            line = ''
            for x in range(minx, maxx+1):
                line += self.data[(x,y)]
            print(line)

    def run(self,rounds):
        for ct in range(rounds):
            newdata = {}
            minx, miny = min(self.data)
            maxx, maxy = max(self.data)
            for y in range(miny-1, maxy+2):
                for x in range(minx-1, maxx+2):
                    value = ''
                    for x0,y0 in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                        value += self.get_point((x0,y0),self.algorithm[0]=='#' and ct%2==1)
                    newdata[(x,y)] = self.algorithm[int(value,2)]
            self.data = newdata
        return self.count()

def test1():
    test_day20 = Day20('./day20-test.input')
    assert test_day20.run() == 35
    assert test_day20.run_part2() == 3351

def test2():
    test_day20 = Day20('./day20.input')
    assert test_day20.run_part1() == 5432
    assert test_day20.run_part2() == 16550

if __name__ == '__main__':
    print("advent of code: day20")
    day20 = Day20('./day20.input')
    print(f"part 1: {day20.run(2)}")
    print(f"part 2: {day20.run(50)}")
