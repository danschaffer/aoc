#!/usr/bin/env python3
import copy
import heapq
import sys
class Day12:
    def __init__(self, file):
        self.unvisited = set()
        self.nodes = {}
        self.data = {}
        for y, line in enumerate(open(file).readlines()):
            for x, ch in enumerate(line.strip()):
                if ch == 'S':
                    self.start = (x,y)
                    ch = 'a'
                elif ch == 'E':
                    self.dest = (x,y)
                    ch = 'z'
                self.data[(x,y)] = ord(ch) - ord('a')
        for y1 in range(y+1):
            for x1 in range(x+1):
                self.unvisited.add((x1,y1))
                value = 999
                if (x1,y1) == self.dest:
                    value = 0
                self.nodes[(x1,y1)] = value

    def run(self):
        answer2 = -1
        while True:
            current = sorted(list(self.unvisited), key=lambda pt:self.nodes[pt])[0]
            if answer2 == -1 and self.data[current] == 0:
                answer2 =self.nodes[current]
            if current == self.start:
                return self.nodes[current], answer2
            self.unvisited.remove(current)
            x,y = current
            for neighbor in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if neighbor not in self.data or self.data[current] - self.data[neighbor] > 1:
                    continue
                x1, y1 = neighbor
                if self.nodes[current] + 1 < self.nodes[neighbor]:
                    self.nodes[neighbor] = self.nodes[current] + 1

def test1():
    answer1, answer2= Day12('./day12-test.input').run()
    assert answer1 == 31
    assert answer2 == 29

def test2():
    answer1, answer2 = Day12('./day12.input').run()
    assert answer1 == 380
    assert answer2 == 375

if __name__ == '__main__':
    print("advent of code: day12")
    file = './day12.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    answer1, answer2 = Day12(file).run()
    print(f"part 1: {answer1}")
    print(f"part 2: {answer2}")
