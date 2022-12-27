#!/usr/bin/env python3
import heapq
import sys
class Day24:
    def __init__(self, file):
        self.cycle = None
        self.start = None
        self.goal = None
        self.storms = ([],[],[],[])
        self.storm_states = {}
        self.maxx = 0
        self.maxy = 0
        for y, line in enumerate(open(file).readlines()):
            for x, ch in enumerate(line):
                line = line.strip()
                if y == 0:
                    if ch == '.':
                        self.start = (x,y)
                elif line.startswith('##'):
                    if ch == '.':
                        self.goal = (x,y)
                elif ch == '<':
                    self.storms[0].append((x,y))
                elif ch == '>':
                    self.storms[1].append((x,y))
                elif ch == '^':
                    self.storms[2].append((x,y))
                elif ch == 'v':
                    self.storms[3].append((x,y))
                self.maxx = max(self.maxx, x)
            self.maxy = max(self.maxy, y)
        self.storm_states[0] = self.storms
        self.maxx -= 1
        time = 0
        while not self.cycle:
            self.get_storms(time)
            time += 1

    def dist_from_goal(self, pt):
        return abs(pt[0] - self.goal[0]) + abs(pt[1] - self.goal[1])

    def get_storms(self, time):
        if self.cycle:
            time = time % self.cycle
        if time in self.storm_states:
            return self.storm_states[time][0] + self.storm_states[time][1] + self.storm_states[time][2] + self.storm_states[time][3]
        storm0 = self.storm_states[time-1]
        storm1 = ([],[],[],[])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in range(4):
            for i in range(len(storm0[d])):
                s = (storm0[d][i][0] + dirs[d][0], storm0[d][i][1] + dirs[d][1])
                if s[0] == 0:
                    s = (self.maxx-1,s[1])
                elif s[0] == self.maxx:
                    s = (1,s[1])
                elif s[1] == 0:
                    s = (s[0],self.maxy-1)
                elif s[1] == self.maxy:
                    s = (s[0], 1)
                storm1[d].append(s)
        
        if (storm1[0], storm1[1], storm1[2], storm1[3]) in self.storm_states.values():
            self.cycle = time
        else:
            self.storm_states[time] = (storm1[0], storm1[1], storm1[2], storm1[3])
        return storm1[0] + storm1[1] + storm1[2] + storm1[3]

    def print_board(self, time, state):
        storms = self.storm_states[time]
        for y in range(self.maxy+1):
            line = ''
            for x in range(self.maxx+1):
                if state == (x,y):
                    line += 'E'
                elif self.goal == (x,y):
                    line += 'G'
                elif x == 0 or x == self.maxx or y == 0 or y == self.maxy:
                    line += '#'
                else:
                    n = 0
                    ch = '.'
                    for i in range(4):
                        if (x,y) in storms[i]:
                            n += 1
                            ch = ['<','>','^','v'][i]
                    if n > 1:
                        ch = str(n)
                    line += ch
            print(line)

    @staticmethod
    def manhattan(pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def run(self, time, start, goal):
        frontier = []
        visited = set()
        heapq.heappush(frontier,(self.manhattan(start,goal), (start[0],start[1],time)))
        dirs = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
        while frontier:
            _, (posx,posy,time) = heapq.heappop(frontier)
            for dir in dirs:
                pos1 = (posx + dir[0], posy + dir[1])
                if pos1 == goal:
                    return time + 1
                if pos1 == start or pos1[0] > 0 and pos1[0] < self.maxx and pos1[1] > 0 and pos1[1] < self.maxy and (pos1[0],pos1[1],time+1) not in visited and pos1 not in self.get_storms(time+1):
                    heapq.heappush(frontier, (time+1+self.manhattan(pos1,goal),(pos1[0],pos1[1],time+1)))
                    visited.add((pos1[0],pos1[1],time+1))
        return -1

    def run_all(self):
        time1 = self.run(0, self.start, self.goal)
        time2 = self.run(time1, self.goal, self.start)
        time3 = self.run(time2, self.start, self.goal)
        return time1, time3


def test1():
    p1, p2 = Day24('./day24-test.input').run_all()
    assert p1 == 18
    assert p2 == 54

def test2():
    p1, p2 = Day24('./day24.input').run_all()
    assert p1 == 283
    assert p2 == 883

if __name__ == '__main__':
    print("advent of code: day24")
    file = './day24-test.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    p1, p2 = Day24(file).run_all()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")
