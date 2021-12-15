#!/usr/bin/env python3
import heapq
class Day15:
    def __init__(self, file, part2=False):
        self.data = {}
        for y,line in enumerate(open(file).readlines()):
            for x,ch in enumerate(line.strip()):
                self.data[(x,y)] = int(ch)
        if part2:
            last = max(self.data)
            for multy in range(5):
                for multx in range(5):
                    for y in range(last[0]+1):
                        for x in range(last[1]+1):
                            data0 = self.data[(x,y)] + multx + multy
                            if data0 > 9:
                                data0 = data0 - 9
                            self.data[(x+(last[0]+1)*multx,y+(last[1]+1)*multy)] = data0

    def print_board(self):
        last = max(self.data)
        for y in range(last[0]+1):
            line = ''
            for x in range(last[1]+1):
                line += str(self.data[(x,y)])
            print(line)

    def run(self):
        #self.print_board()
        start=(0,0)
        finish=max(self.data)
        frontier = []
        heapq.heappush(frontier, (0, [(0,0)]))
        visited = set()
        visited.add((0,0))
        while frontier:
            _, moves = heapq.heappop(frontier)
            x,y = moves[-1]
            if (x,y) == finish:
                return self.count(moves)
            for nextmove in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if nextmove not in self.data or nextmove in visited:
                    continue
                visited.add(nextmove)
                moves1 = moves[:] + [nextmove]
                heapq.heappush(frontier, (self.count(moves1), moves1))


    def count(self,moves):
        return sum([self.data[move] for move in moves[1:]])

    def distance(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def run_part2(self):
        return -1

def test1():
    test_day15 = Day15('./day15-test.input')
    assert test_day15.run() == 40
    test_day15 = Day15('./day15-test.input',part2=True)
    assert test_day15.run() == 315

def test2():
    test_day15 = Day15('./day15.input')
    assert test_day15.run() == 811
    test_day15 = Day15('./day15.input',part2=True)
    assert test_day15.run() == 3012

if __name__ == '__main__':
    print("advent of code: day15")
    day15 = Day15('./day15.input')
    print(f"part 1: {day15.run()}")
    day15 = Day15('./day15.input',part2=True)
    print(f"part 2: {day15.run()}")
