#!/usr/bin/env python
import heapq
class Day13:
    def __init__(self, seed, goal):
        self.seed = seed
        self.goal = goal

    def is_wall(self, location):
        x,y = location
        value = x*x + 3*x + 2*x*y + y + y*y + self.seed
        return sum([int(a) for a in bin(value)[2:]]) % 2 == 1

    def get_moves(self, location):
        x,y = location
        moves = []
        if x > 0 and not self.is_wall((x-1,y)):
            moves.append((x-1,y))
        if y > 0 and not self.is_wall((x,y-1)):
            moves.append((x,y-1))
        if not self.is_wall((x+1,y)):
            moves.append((x+1,y))
        if not self.is_wall((x,y+1)):
            moves.append((x,y+1))
        return moves

    def get_distance(self, location):
        return abs(location[0] - self.goal[0]) + abs(location[1] - self.goal[1])

    def run(self, part2=False):
        cache = []
        frontier = []
        moves0 = [(1,1)]
        cache.append(moves0)
        heapq.heappush(frontier, (0, moves0))
        while len(frontier):
            movelen, moves = heapq.heappop(frontier)
            location = list(moves)[-1]
            for next_move in self.get_moves(location):
                if not part2 and next_move == self.goal:
                    return len(moves)
                if part2 and movelen == 51:
                    return len(cache) - 1 
                moves1 = moves[:] + [next_move]
                if next_move in cache:
                    continue
                cache.append(next_move)
                heapq.heappush(frontier, (len(moves1),moves1))

def test1():
    test_day13 = Day13(10, (7,4))
    assert test_day13.is_wall((0,0)) is False
    assert test_day13.is_wall((1,0))
    assert test_day13.is_wall((6,4)) is False
    assert test_day13.is_wall((6,3))
    assert test_day13.run() == 11

def test2():
    test_day13 = Day13(1358, (31,39))
    assert test_day13.run() == 96
    assert test_day13.run(part2=True) == 141

if __name__ == '__main__':
    print("advent of code: day13")
    day13 = Day13(1358, (31,39))
    print(f"part 1: {day13.run()}")
    print(f"part 2: {day13.run(part2=True)}")
