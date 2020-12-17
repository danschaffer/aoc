#!/usr/bin/env python3
import sys
class Day17:
    def __init__(self, file):
        self.points = []
        self.cycles = 0
        for y, line in enumerate(open(file).read().strip().split('\n')):
            for x, char in enumerate(line):
                if char == '#':
                    self.points +=[(x,y,0)]

    def cycle(self):
        max_x = -sys.maxsize
        max_y = -sys.maxsize
        max_z = -sys.maxsize
        min_x = sys.maxsize
        min_y = sys.maxsize
        min_z = sys.maxsize
        points1 = []
        assert len(self.points) > 0
        for point in self.points:
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
            max_z = max(max_z, point[2])
            min_x = min(min_x, point[0])
            min_y = min(min_y, point[1])
            min_z = min(min_z, point[2])
        cache = []
        for point in self.points:
            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    for z in range(min_z - 1, max_z + 2):
                        if (x,y,z) in cache:
                            continue
                        neighbors = [
                            (x-1,y-1,z-1),
                            (x  ,y-1,z-1),
                            (x+1,y-1,z-1),
                            (x-1,y  ,z-1),
                            (x  ,y  ,z-1),
                            (x+1,y  ,z-1),
                            (x-1,y+1,z-1),
                            (x  ,y+1,z-1),
                            (x+1,y+1,z-1),

                            (x-1,y-1,z  ),
                            (x  ,y-1,z  ),
                            (x+1,y-1,z  ),
                            (x-1,y  ,z  ),
                            (x+1,y  ,z  ),
                            (x-1,y+1,z  ),
                            (x  ,y+1,z  ),
                            (x+1,y+1,z  ),

                            (x-1,y-1,z+1),
                            (x  ,y-1,z+1),
                            (x+1,y-1,z+1),
                            (x-1,y  ,z+1),
                            (x  ,y  ,z+1),
                            (x+1,y  ,z+1),
                            (x-1,y+1,z+1),
                            (x  ,y+1,z+1),
                            (x+1,y+1,z+1),
                        ]
                        num_neighbors = sum([1 for neighbor in neighbors if neighbor in self.points])

                        if (x,y,z) not in points1 and (x,y,z) in self.points and (num_neighbors == 2 or num_neighbors == 3):
                            points1 += [(x,y,z)]
                        elif (x,y,z) not in points1 and (x,y,z) not in self.points and num_neighbors == 3:
                            points1 += [(x,y,z)]
                        cache += [(x,y,z)]
        self.points = points1
        self.cycles += 1

    def run_part1(self):
        for _ in range(6):
            self.cycle()
        return len(self.points)

def test1():
    test_day17a = Day17('./day17-test.input')
    assert test_day17a.run_part1() == 112
#    test_day17b = Day17('./day17-test.input')
#    assert test_day17b.run_part1() == 448

if __name__ == '__main__':
    print("advent of code: day17")
    day17 = Day17('./day17.input')
    print(f"part 1: {day17.run_part1()}")
