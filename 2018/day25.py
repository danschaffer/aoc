#!/usr/bin/env python
from collections import deque

def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2]) + abs(p1[3]-p2[3])

def day25(file):
    stars = []
    matches = {}
    for line in open(file).read().strip().split('\n'):
        points = [int(n) for n in line.split(',')]
        stars.append((points[0],points[1],points[2],points[3]))
    for i,p1 in enumerate(stars):
        matches[i] = set()
        for j,p2 in enumerate(stars):
            if distance(p1,p2) <= 3:
                matches[i].add(j)
    ans = 0
    constellations = set()
    for i in range(len(stars)):
        if i in constellations:
            continue
        ans += 1
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            if x in constellations:
                continue
            constellations.add(x)
            for y in matches[x]:
                q.append(y)
    return ans

def test1():
    assert day25('./day25-test1.input') == 2
    assert day25('./day25-test2.input') == 4
    assert day25('./day25-test3.input') == 3
    assert day25('./day25-test4.input') == 8
    assert day25('./day25.input') == 338

if __name__ == '__main__':
    print('advent of code 2018: day 25')
    print(f"part 1: {day25('./day25.input')}")
