#!/usr/bin/env python3

import heapq
from queue import PriorityQueue

class Day22:
    def __init__(self, depth, target):
        self.depth = depth
        self.target_x = target[0]
        self.target_y = target[1]
        self.table = {}

    def print_board(self):
        for y in range(self.target_y+1):
            line = ''
            for x in range(self.target_x+1):
                line += ['.','=','|'][self.table[(x,y)]%3]
            print(line)
        print('')

    def run_part1(self):
        answer = 0
        for x in range(self.target_x+1):
            for y in range(self.target_y+1):
                if x == 0:
                    geo_index = y * 48271
                elif y == 0:
                    geo_index = x * 16807
                elif (x,y) == (self.target_x, self.target_y):
                    geo_index = 0
                else:
                    geo_index = self.table[(x-1,y)] * self.table[(x,y-1)]
                erosion_level = (geo_index + self.depth) % 20183
                self.table[(x,y)] = erosion_level
                answer += erosion_level % 3
        return answer

    def get_distance(self, loc, goal):
        return abs(loc[0] - goal[0]) + abs(loc[1] - goal[1])

def test1():
    assert Day22(510,(10,10)).run_part1() == 114
    assert Day22(7305,(13,734)).run_part1() == 10204

if __name__ == '__main__':
    print("advent of code: day22")
    print(f"part 1: {Day22(7305,(13,734)).run_part1()}")

