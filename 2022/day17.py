#!/usr/bin/env python3
import sys
class Day17:
    def __init__(self, file):
        self.jet_pattern = []
        for line in open(file).readlines():
            for ch in line.strip():
                if ch == '<':
                    self.jet_pattern.append(-1)
                else:
                    self.jet_pattern.append(1)
        self.shapes = [
            [(2,0),(3,0),(4,0),(5,0)], 
            [(3,0),(2,1),(3,1),(4,1),(3,2)],
            [(2,0),(3,0),(4,0),(4,1),(4,2)],
            [(2,0),(2,1),(2,2),(2,3)],
            [(2,0),(3,0),(2,1),(3,1)],
        ]

    @staticmethod
    def add_shape(shape, data):
        for pt in shape:
            data.add(pt)

    @staticmethod
    def collision(shape, data):
        result = False
        for pt in shape:
            if pt in data or pt[1] == 0:
                return True

    @staticmethod
    def move(shape,dir):
        shape1 = []
        for pt in shape:
            shape1.append((pt[0]+dir[0],pt[1]+dir[1]))
            if pt[0]+dir[0] < 0 or pt[0]+dir[0] > 6:
                return shape
        return shape1

    @staticmethod
    def add(shape,data,height):
        for pt in shape:
            data.add(pt)
            height = max(height,pt[1])
        return data, height

    @staticmethod
    def print_board(data, shape):
        maxy = 0
        for pt in data:
            maxy = max(maxy, pt[1])
        for pt in shape:
            maxy = max(maxy, pt[1])
        for y in range(maxy,0,-1):
            line = '|'
            for x in range(7):
                if (x,y) in data:
                    line += '#'
                elif (x,y) in shape:
                    line += '@'
                else:
                    line += '.'
            line += '|'
            print(line)
        print('+-------+')

    def run_part1(self):
        data = set()
        rocks = 0
        height = 0
        jet = 0
        while rocks < 2022:
            shape = self.shapes[rocks % len(self.shapes)]
            rocks += 1
            shape = Day17.move(shape, (0,height + 4))
            while True:
                move1 = (self.jet_pattern[jet % len(self.jet_pattern)], 0)
                jet += 1
                shape1 = Day17.move(shape, move1)
                if not Day17.collision(shape1, data):
                    shape = shape1
                shape1 = Day17.move(shape, (0,-1))
                if Day17.collision(shape1, data):
                    break
                shape = shape1
            data, height = Day17.add(shape,data,height)
        return height

    @staticmethod
    def collision2(shape, data):
        for pt in shape:
            if pt[1] == 0 or pt[1] == data[pt[0]]:
                return True
            if pt[1] < 0 or pt[1] > 6:
                return True
        return False

    @staticmethod
    def add2(shape,data,height):
        for pt in shape:
            data[pt[0]] = max(data[pt[0]], pt[1])
            height = max(height,pt[1])
        return data, height

    def run_part2(self):
        data = [-1 for _ in range(7)]
        rocks = 0
        height = 0
        jet = 0
        while rocks < 2022:
            shape = self.shapes[rocks % len(self.shapes)]
            rocks += 1
            shape = Day17.move(shape, (0,height + 4))
            while True:
                move1 = (self.jet_pattern[jet % len(self.jet_pattern)], 0)
                jet += 1
                print(f"{move1} {shape}")
                shape1 = Day17.move(shape, move1)
                if not Day17.collision2(shape1, data):
                    shape = shape1
                shape1 = Day17.move(shape, (0,-1))
                if Day17.collision2(shape1, data):
                    break
                shape = shape1
            import pdb; pdb.set_trace()
            data, height = Day17.add2(shape,data,height)
        return height

def test1():
    test_day17 = Day17('./day17-test.input')
    assert test_day17.run_part1() == 3068

def test2():
    test_day17 = Day17('./day17.input')
    assert test_day17.run_part1() == 3102

if __name__ == '__main__':
    print("advent of code: day17")
    file = './day17-test.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day17 = Day17(file)
    print(f"part 1: {day17.run_part1()}")
    print(f"part 2: {day17.run_part2()}")

