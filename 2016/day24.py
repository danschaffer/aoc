#!/usr/bin/env python
import heapq
import itertools
import sys
import time
class Day24:
    def __init__(self,file):
        self.grid = []
        self.locations = {}
        self.distances = {}
        for y,line in enumerate(open(file).read().strip().split('\n')):
            for x, char in enumerate(line):
                if char == '.' or char in ['0','1','2','3','4','5','6','7','8','9']:
                    self.grid.append((x,y))
                    if char != '.':
                        self.locations[char] = (x,y)
        for (loc1, loc2) in itertools.combinations(self.locations,2):
            shortest = self.find_shortest(self.locations[loc1], self.locations[loc2])
            self.distances[(loc1,loc2)] = shortest
            self.distances[(loc2,loc1)] = shortest
#            print(f"{loc1} {loc2} {shortest}")

    def get_moves(self, loc):
        x, y = loc
        moves = []
        if (x-1,y) in self.grid:
            moves.append((x-1,y))
        if (x+1,y) in self.grid:
            moves.append((x+1,y))
        if (x,y-1) in self.grid:
            moves.append((x,y-1))
        if (x,y+1) in self.grid:
            moves.append((x,y+1))
        return moves

    def find_shortest(self, loc1, loc2):
        frontier = []
        visited = [loc1]
        heapq.heappush(frontier,(0, (loc1,[])))
        while frontier:
            index, (loc, moves) = heapq.heappop(frontier)
            for loc0 in self.get_moves(loc):
                if loc0 in visited:
                    continue
                visited.append(loc0)
                if loc0 == loc2:
                    return len(moves) + 1
                distance = abs(loc0[0] - loc2[0]) + abs(loc0[1] - loc2[1])
                moves0=moves[:] + [loc0]
                heapq.heappush(frontier,(distance+len(moves0), (loc0,moves0)))

    def run(self, part2=False):
        frontier = []
        heapq.heappush(frontier,(0, ['0']))
        while frontier:
            moves, visited = heapq.heappop(frontier)
            if len(visited) == len(self.locations) + 1:
                return moves
            if len(visited) == len(self.locations):
                if part2 == False:
                    return moves
                else:
                    moves0 = moves + self.distances[(visited[-1],'0')]
                    heapq.heappush(frontier, (moves0, visited + ['0']))
                    continue
            for node in self.locations:
                if node in visited:
                    continue
                current = visited[-1]
                moves0 = moves + self.distances[(current,node)]
                visited0 = visited[:] + [node]
                heapq.heappush(frontier, (moves0 , visited0))
def test1():
    day24 = Day24('./day24-test.input')
    assert day24.run() == 14
    assert day24.run(part2=True) == 20

def test2():
    day24 = Day24('./day24.input')
    assert day24.run() == 502
    assert day24.run(part2=True) == 724


if __name__ == '__main__':
    print("advent of code: day24")
    start = time.time()
    day24 = Day24('./day24.input')
    print(f"load time {round(time.time()-start,2)}")
    print(f"part 1: {day24.run()}")
    print(f"part 2: {day24.run(part2=True)}")
