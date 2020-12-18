#!/usr/bin/env python3
import sys

def run_part1(file):
    points = set()
    for y, line in enumerate(open(file).read().strip().split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                points.add((x,y,0))

    for _ in range(6):
        max_x = -sys.maxsize
        max_y = -sys.maxsize
        max_z = -sys.maxsize
        min_x = sys.maxsize
        min_y = sys.maxsize
        min_z = sys.maxsize
        points1 = set()
        assert len(points) > 0
        for point in list(points):
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
            max_z = max(max_z, point[2])
            min_x = min(min_x, point[0])
            min_y = min(min_y, point[1])
            min_z = min(min_z, point[2])
        for point in points:
            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    for z in range(min_z - 1, max_z + 2):
                        neighbors = [(x + i, y + j, z + k) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if i != 0 or j != 0 or k != 0]
                        num_neighbors = sum([1 for neighbor in neighbors if neighbor in points])
                        if (x,y,z) not in points1 and (x,y,z) in points and (num_neighbors == 2 or num_neighbors == 3):
                            points1.add((x,y,z))
                        elif (x,y,z) not in points1 and (x,y,z) not in points and num_neighbors == 3:
                            points1.add((x,y,z))
        points = points1
    return len(points)

def run_part2(file):
    points = set()
    for y, line in enumerate(open(file).read().strip().split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                points.add((x,y,0,0))
    for _ in range(6):
        max_x = -sys.maxsize
        max_y = -sys.maxsize
        max_z = -sys.maxsize
        max_w = -sys.maxsize
        min_x = sys.maxsize
        min_y = sys.maxsize
        min_z = sys.maxsize
        min_w = sys.maxsize
        points1 = set()
        assert len(points) > 0
        for point in list(points):
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
            max_z = max(max_z, point[2])
            max_w = max(max_w, point[3])
            min_x = min(min_x, point[0])
            min_y = min(min_y, point[1])
            min_z = min(min_z, point[2])
            min_w = min(min_w, point[3])
        for point in points:
            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    for z in range(min_z - 1, max_z + 2):
                        for w in range(min_w - 1, max_w + 2):
                            neighbors = [(x + i, y + j, z + k, w + l) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) for l in (-1,0,1) if i != 0 or j != 0 or k != 0 or l != 0]
                            num_neighbors = sum([1 for neighbor in neighbors if neighbor in points])
                            if (x,y,z,w) not in points1 and (x,y,z,w) in points and (num_neighbors == 2 or num_neighbors == 3):
                                points1.add((x,y,z,w))
                            elif (x,y,z,w) not in points1 and (x,y,z,w) not in points and num_neighbors == 3:
                                points1.add((x,y,z,w))
        points = points1
    return len(points)

def test1():
    assert run_part1('./day17-test.input') == 112
#    assert run_part1('./day17-test.input') == 448
#    assert run_part2('./day17-test.input') == 848  # 800s, why takes so long? my solution stinks

if __name__ == '__main__':
    print("advent of code: day17")
    print(f"part 1: {run_part1('./day17.input')}")  # 16s
#    print(f"part 2: {run_part2('./day17.input')}")  # 65m
