#!/usr/bin/env python3
import math
import sys
class Day09:
    def __init__(self, file):
        self.moves = [line.strip() for line in open(file).readlines()]
        self.h = (0,0)
        self.t = (0,0)
        self.visited = {(0,0)}

    @staticmethod
    def is_adjacent(p1,p2):
        return (p1[0]==p2[0] and abs(p1[1]-p2[1]) == 1) or (p1[1]==p2[1] and abs(p1[0]-p2[0])==1)

    @staticmethod
    def is_2adjacent(p1,p2):
        return (p1[0]==p2[0] and abs(p1[1]-p2[1]) == 2) or (p1[1]==p2[1] and abs(p1[0]-p2[0])==2)

    @staticmethod
    def is_diagonal(p1,p2):
        return abs(p1[0]-p2[0])==1 and abs(p1[1]-p2[1])==1

    @staticmethod
    def is_touching(p1,p2):
        return p1 == p2 or Day09.is_adjacent(p1,p2) or Day09.is_diagonal(p1,p2)

    @staticmethod
    def do_move(p, move):
        if move == 'R':
            p =(p[0]+1,p[1])
        elif move == 'L':
            p =(p[0]-1,p[1])
        elif move == 'U':
            p =(p[0],p[1]-1)
        elif move == 'D':
            p =(p[0],p[1]+1)
        elif move == 'UL':
            p =(p[0]-1,p[1]-1)
        elif move == 'UR':
            p =(p[0]+1,p[1]-1)
        elif move == 'DL':
            p =(p[0]-1,p[1]+1)
        elif move == 'DR':
            p =(p[0]+1,p[1]+1)
        return p

    def move_tail(self):
        if Day09.is_touching(self.h, self.t):
            return
        for move in ['R','L','U','D','UR','UL','DR','DL']:
            t2 = Day09.do_move(self.t, move)
            if Day09.is_adjacent(self.h, t2):
                self.t = t2
                break
        self.visited.add(self.t)

    def run_part1(self):
        for movestr in self.moves:
            move, num = movestr.split()
            for _ in range(int(num)):
                self.h = Day09.do_move(self.h, move)
                self.move_tail()
        return len(self.visited)

    def run_part2(self):
        return -1

    def print_grid(self):
        for y in range(-4,1):
            s = ''
            for x in range(0,5):
                if self.h == (x,y):
                    s += 'H'
                elif self.t == (x,y):
                    s += 'T'
                else:
                    s += '.'
            print(s)
        print()

def test1():
    test_day09 = Day09('./day09-test.input')
    assert test_day09.run_part1() == 13
    assert test_day09.run_part2() == -1

def test2():
    test_day09 = Day09('./day09.input')
    assert test_day09.run_part1() == 5683
    assert test_day09.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day09")
    file = './day09.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day09 = Day09(file)
    print(f"part 1: {day09.run_part1()}")
    print(f"part 2: {day09.run_part2()}")
