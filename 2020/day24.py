#!/usr/bin/env python3
import sys
# read about heaxagon coordinate and axial system here
#   https://www.redblobgames.com/grids/hexagons/
class Day24:
    def __init__(self):
        self.data = {}

    def process_line(self, line):
        col, row = 0, 0
        directions = {
            'e': (1,0),
            'w': (-1,0),
            'se': (0,1),
            'sw': (-1,1),
            'nw': (0,-1),
            'ne': (1,-1)
        }
        index = 0
        while index < len(line):
            direction = line[index]
            index += 1
            if direction == 's' or direction =='n':
                direction += line[index]
                index += 1
            col += directions[direction][0]
            row += directions[direction][1]
        return (col,row)

    def get_neighbors(self,coord):
        result = 0
        neighbors = [(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(0,1)]
        for neighbor in neighbors:
            if (coord[0]+neighbor[0], coord[1]+neighbor[1]) in self.data and self.data[coord[0]+neighbor[0], coord[1]+neighbor[1]] == 1:
                result += 1
        return result

    def get_count(self):
        return sum([1 for coord in self.data if self.data[coord] == 1])

    def run_part1(self, file):
        for line in open(file).read().strip().split('\n'):
            coord = self.process_line(line)
            if coord not in self.data:
                self.data[coord] = 0
            self.data[coord] = (self.data[coord] + 1) % 2
        return self.get_count()

    def run_part2(self):
        for _ in range(100):
            data0 = {}
#            print(f"{counter} {self.get_count()}")
            maxx = -1*sys.maxsize
            minx = sys.maxsize
            maxy = -1*sys.maxsize
            miny = sys.maxsize
            for coord in self.data:
                minx = min(minx, coord[0])
                miny = min(miny, coord[1])
                maxx = max(maxx, coord[0])
                maxy = max(maxy, coord[1])
            for col in range(minx-2,maxx+2):
                for row in range(miny-2, maxy+2):
                    coord = (col,row)
                    neighbors = self.get_neighbors(coord)
                    if coord not in self.data or self.data[coord] == 0:
                        if neighbors == 2:
                            data0[coord] = 1
                    else:
                        if neighbors == 1 or neighbors == 2:
                            data0[coord] = 1
            self.data = data0
        return self.get_count()

def test1():
    test_day24 = Day24()
    assert test_day24.process_line('esew') == (0,1)
    assert test_day24.process_line('nwwswee') == (0,0)
    assert test_day24.run_part1('./day24-test.input') == 10
    assert test_day24.run_part2() == 2208

def test2():
    test_day24 = Day24()
    assert test_day24.run_part1('./day24.input') == 332
    assert test_day24.run_part2() == 3900

if __name__ == '__main__':
    print("advent of code: day24")
    day24 = Day24()
    print(f"part 1: {day24.run_part1('./day24.input')}")
    print(f"part 2: {day24.run_part2()}")
