#!/usr/bin/env python3

class Day24:
    def __init__(self):
        self.data = {}

    def process_line(self, line):
        x, y = 0, 0
        dirs = {
            'e': (1,0),
            'w': (-1,0),
            'se': (0,1),
            'sw': (-1,1),
            'nw': (0,-1),
            'ne': (1,-1)
        }
        index = 0
        while index < len(line):
            dir = line[index]
            index += 1
            if dir == 's' or dir =='n':
                dir += line[index]
                index += 1
            x += dirs[dir][0]
            y += dirs[dir][1]
        return (x,y)
    
    def run_part1(self, file):
        for line in open(file).read().strip().split('\n'):
            coord = self.process_line(line)
            if coord not in self.data:
                self.data[coord] = 0
            self.data[coord] = (self.data[coord] + 1) % 2
        return sum([1 for coord in self.data if self.data[coord] == 1])

    def run_part2(self):
        return -1

def test1():
    test_day24 = Day24()
    assert test_day24.process_line('esew') == (0,1)
    assert test_day24.process_line('nwwswee') == (0,0)
    assert test_day24.run_part1('./day24-test.input') == 10

if __name__ == '__main__':
    print("advent of code: day24")
    day24 = Day24()
    print(f"part 1: {day24.run_part1('./day24.input')}")
#    print(f"part 2: {day24.run_part2()}")
