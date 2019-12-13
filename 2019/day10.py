#!/usr/bin/env python
import math
class Asteroids:
    def __init__(self, input):
        self.data = {}
        self.load(input)

    def load(self, input):
        y =0
        for line in input.strip().split('\n'):
            for x in range(len(line)):
                if line[x] == '#':
                    self.data[(x, y)] = 0
            y += 1

    def calculate_angle(self, origin, point1):
        angle = math.atan2(point1[1] - origin[1], point1[0] - origin[0]) * 180 / math.pi
        return int(angle)

    def distance(self, a,b):
        return round(math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2), 1)

    def is_between(self, a,c,b):
        return self.distance(a,c) + self.distance(c,b) == self.distance(a,b)

    def find_best(self):
        matches = {}
        for point in self.data.keys():
            num = self.find_match(point)
            if num not in matches:
                matches[num] = []
            matches[num] += [point]
        maxn = max(matches.keys())
#        assert(len(matches[maxn]) == 1)
        return maxn, matches[maxn][0]

    def find_match(self, origin):
        matches = []
        for point in self.data.keys():
            if origin == point:
                continue
            found = False
            for match in matches:
                if self.is_between(origin, match, point) or self.is_between(origin, point, match):
                    found = True
                    continue
            if not found:
                matches += [point]
        return len(matches)


def test_1():
    input1 = """
.#..#
.....
#####
....#
...##
"""
    asteroids = Asteroids(input1)
    assert len(asteroids.data.keys()) == 10
    maxn, best = asteroids.find_best()
    assert maxn == 8
    assert best == (3,4)


def test_2():
    input2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""
    asteroids = Asteroids(input2)
    maxn, best = asteroids.find_best()
    assert maxn == 33
    assert best == (5, 8)

def test_3():
    input3 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""
    asteroids = Asteroids(input3)
    maxn, best = asteroids.find_best()
    assert maxn == 35
    assert best == (1, 2)

def test_4():
    input4 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""
    asteroids = Asteroids(input4)
    maxn, best = asteroids.find_best()
    assert maxn == 41
    assert best == (6, 3)

#def test_5():
#     input5 = """
# .#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# """
#     asteroids = Asteroids(input5)
#     maxn, best = asteroids.find_best()
#     assert maxn == 210
#     assert best == (11, 13)

if __name__ == '__main__':
    data = """
##.##..#.####...#.#.####
##.###..##.#######..##..
..######.###.#.##.######
.#######.####.##.#.###.#
..#...##.#.....#####..##
#..###.#...#..###.#..#..
###..#.##.####.#..##..##
.##.##....###.#..#....#.
########..#####..#######
##..#..##.#..##.#.#.#..#
##.#.##.######.#####....
###.##...#.##...#.######
###...##.####..##..#####
##.#...#.#.....######.##
.#...####..####.##...##.
#.#########..###..#.####
#.##..###.#.######.#####
##..##.##...####.#...##.
###...###.##.####.#.##..
####.#.....###..#.####.#
##.####..##.#.##..##.#.#
#####..#...####..##..#.#
.##.##.##...###.##...###
..###.########.#.###..#.
"""
    asteroids = Asteroids(data)
    maxn, best = asteroids.find_best()
    print(f"part 1: {maxn}")
