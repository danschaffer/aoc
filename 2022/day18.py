#!/usr/bin/env python3
import sys
class Day18:
    def __init__(self, file):
        self.data = []
        self.maxpt = 0
        self.minpt = 9999
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split(',')
            self.append((int(parts[0]),int(parts[1]),int(parts[2])))
        self.maxpt +=1
        self.minpt -=1

    def append(self, pt):
        self.data.append(pt)
        for n in pt:
            self.maxpt = max(self.maxpt, n)
            self.minpt = min(self.minpt, n)

    def run_part1(self):
        answer = 0
        for pt in self.data:
            for adj in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
                adjpt = (pt[0]+adj[0],pt[1]+adj[1],pt[2]+adj[2])
                if adjpt not in self.data:
                    answer +=1
        return answer

    def get_neighbors(self, pt):
        x, y, z = pt
        nbrs = []
        for adj in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            nbr = (x+adj[0],y+adj[1],z+adj[2])
            for k in nbr:
                if not (self.minpt <= k <= self.maxpt):
                    break
            else:
                nbrs.append(nbr)
        return nbrs

    def dfs(self,start):
        q = [start]
        frontier = set()
        frontier.add(start)
        while q:
            curr = q.pop()
            for nbr in self.get_neighbors(curr):
                if nbr in frontier or nbr in self.data:
                    continue
                q.append(nbr)
                frontier.add(nbr)
        return frontier

    def run_part2(self):
        cells=self.dfs((self.minpt, self.minpt, self.minpt))
        answer = 0
        for pt in self.data:
            for nbr in self.get_neighbors(pt):
                if nbr in cells:
                    answer += 1
        return answer

def test1():
    test_day18 = Day18('./day18-test.input')
    assert test_day18.run_part1() == 64
    assert test_day18.run_part2() == 58

def test2():
    test_day18 = Day18('./day18.input')
    assert test_day18.run_part1() == 3494
    assert test_day18.run_part2() == 2062

if __name__ == '__main__':
    print("advent of code: day18")
    file = './day18.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day18 = Day18(file)
    print(f"part 1: {day18.run_part1()}")
    print(f"part 2: {day18.run_part2()}")
