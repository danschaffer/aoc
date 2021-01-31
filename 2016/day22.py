#!/usr/bin/env python
import itertools
def solve1(file):
    solutions = 0
    data = {}
    for line in open(file).read().strip().split('\n')[2:]:
        parts = line.split()
        names = parts[0].split('-')
        name = (int(names[1][1:]), int(names[2][1:]))
        size = int(parts[1][:-1])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        data[name] = (size,used,avail)
    for pair1, pair2 in itertools.permutations(data, 2):
        if data[pair1][1] == 0:
            continue
        if data[pair2][2] > data[pair1][1]:
            solutions += 1
    return solutions

def test1():
    assert solve1('./day22.input') == 1038

if __name__ == '__main__':
    print("advent of code day 22")
    print(f"part 1: {solve1('./day22.input')}")
    