#!/usr/bin/env python3
import heapq
import sys
class Day24:
    def __init__(self, file):
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

    def dist_from_goal(self, pt):
        return abs(pt[0] - self.goal[0]) + abs(pt[1] - self.goal[1])

    def get_storms(self, time):
        if time in self.storm_states:
            return self.storm_states[0][0] + self.storm_states[0][1] + self.storm_states[0][2] + self.storm_states[0][3]
        storm0 = self.storm_states[time-1]
        storm1 = ([],[],[],[])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in range(4):
            for i in range(len(storm0[d])):
                s = (storm0[d][i][0] + dirs[d][0], storm0[d][i][1] + dirs[d][1])
                if s[0] < 1:
                    s = (self.maxx,s[1])
                elif s[0] > self.maxx:
                    s = (1,s[1])
                elif s[1] < 1:
                    s = (s[0],self.maxy)
                elif s[1] > self.maxy:
                    s = (s[0], 1)
                storm1[d].append(s)
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
                            ch = ['<','>','v','^'][i]
                    if n > 1:
                        ch = str(n)
                    line += ch
            print(line)

    def run_part1(self):
        frontier = []
        heapq.heappush(frontier,(0, self.start))
        visited = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        self.print_board(0, self.start)
        while frontier:
            time, pos = heapq.heappop(frontier)
            storms = self.get_storms(time+1)
            print(f"time: {time}")
            self.print_board(time+1, pos)
            for dir in dirs:
                pos1 = (pos[0] + dir[0], pos[1] + dir[1])
                if pos1 == self.goal:
                    return time + 1
                if pos1[0] < 1 or pos1[0] > self.maxx or pos[1] < 1 or pos[1] > self.maxy or (time+1,pos1) in visited or pos1 in storms:
                    continue
                heapq.heappush(frontier, (time+1,pos1))
                visited.append((time,pos))

    def run_part2(self):
        return -1



def test1():
    test_day24 = Day24('./day24-test.input')
#    assert test_day24.run_part1() == -1
#    assert test_day24.run_part2() == -1

def test2():
    test_day24 = Day24('./day24.input')
#    assert test_day24.run_part1() == -1
#    assert test_day24.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day24")
    file = './day24-test.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day24 = Day24(file)
    print(f"part 1: {day24.run_part1()}")
    print(f"part 2: {day24.run_part2()}")
