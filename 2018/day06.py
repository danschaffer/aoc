#!/usr/bin/env python3
import sys
class Day06:
    def __init__(self, file):
        self.data = []
        for line in open(file).readlines():
            parts = line.split(',')
            self.data.append((int(parts[0].strip()),int(parts[1].strip())))

    def run1(self, max_coord=500, outer=5000):
        grid = {}
        for i in range(-1*max_coord,max_coord):
            for j in range(-1*max_coord,max_coord):
                best = []
                for k,val in enumerate(self.data):
                    dist = abs(i - val[0]) + abs(j - val[1])
                    best.append(dist)
                best0 = min(best)
                count = 0
                for val in best:
                    if val == best0:
                        count += 1
                if count == 1:
                    grid[(i,j)] = best.index(best0)
        counts = [0 for n in range(len(self.data))]
        for i in range(-1*max_coord,max_coord):
            for j in range(-1*max_coord,max_coord):
                if (i,j) not in grid:
                    continue
                counts[grid[(i,j)]] += 1
        for n in range(len(counts)):
            if counts[n] > outer:
                counts[n] = 0
        best = max(counts)
        return best

    def run2(self, max_coord=400, threshold=10000):
        count = 0
        for i in range(-1*max_coord,max_coord):
            for j in range(-1*max_coord,max_coord):
                value = 0
                for k in self.data:
                    value += abs(k[0]-i) + abs(k[1]-j)
                if value < threshold:
                    count += 1
        return count

def test1():
    test_day06 = Day06('./day06-test.input')
    assert test_day06.run1(max_coord=20,outer=100) == 17
    assert test_day06.run2(max_coord=20,threshold=32) == 16

    day06 = Day06('./day06.input')
    assert day06.run1() == 3293
    assert day06.run2() == 45176


if __name__ == '__main__':
    print("advent of code: day06")
    day06 = Day06('./day06.input')
    print(f"part 1: {day06.run1()}")
    print(f"part 2: {day06.run2()}")
