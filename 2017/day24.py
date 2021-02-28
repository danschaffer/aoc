#!/usr/bin/env python3
import heapq
class Day24:
    def __init__(self, file):
        self.data = []
        for line in open(file).readlines():
            value1,value2 = line.split('/')
            self.data.append((int(value1.strip()),int(value2.strip())))

    def count(self, bridges):
        result = 0
        for bridge in bridges:
            result += bridge[0] + bridge[1]
        return result

    def run(self):
        highest = 0
        longest = []
        longest_value = 0
        frontier = []
        heapq.heappush(frontier, (0,(0,[],self.data[:])))
        while frontier:
            (_,(next, moves, data)) = heapq.heappop(frontier)
            for pair in data:
                if pair[0] == next:
                    data0 = data[:]
                    data0.remove(pair)
                    moves0 = moves[:] + [pair]
                    count = self.count(moves0)
                    highest = max(highest, count)
                    if len(moves0) > len(longest) or len(moves0) == len(longest) and self.count(moves0) > longest_value:
                        longest = moves0
                        longest_value = self.count(moves0)
                    heapq.heappush(frontier, (count,(pair[1],moves0,data0)))
                elif pair[1] == next:
                    data0 = data[:]
                    data0.remove(pair)
                    moves0 = moves[:] + [pair]
                    count = self.count(moves0)
                    highest = max(highest, count)
                    if len(moves0) > len(longest) or len(moves0) == len(longest) and self.count(moves0) > longest_value:
                        longest = moves0
                        longest_value = self.count(moves0)
                    heapq.heappush(frontier, (count,(pair[0],moves0,data0)))
        return highest, longest_value

def test1():
    test_day24 = Day24('./day24-test.input')
    highest, longest = test_day24.run() 
    assert highest == 31
    assert longest == 19

    test_day24 = Day24('./day24.input')
    highest, longest = test_day24.run()
    assert highest == 1868
    assert longest == 1841

if __name__ == '__main__':
    print("advent of code: day24")
    day24 = Day24('./day24.input')
    highest, longest = day24.run()
    print(f"part 1: {highest}")
    print(f"part 2: {longest}")
