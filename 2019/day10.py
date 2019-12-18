#!/usr/bin/env python
import math
class Asteroids:
    def __init__(self, input):
        self.points = []
        self.results = {}
        self.load(input)

    def load(self, input):
        y =0
        for line in input.strip().split('\n'):
            for x in range(len(line)):
                if line[x] == '#':
                    self.points += [(x, y)]
            y += 1

    def get_angle(self, a, b):
        x0, y0 = a
        x1, y1 = b
        angle = ((math.atan2(x1 - x0, y1 - y0) * 180 / math.pi) + 360 + 180) % 360
        return angle

    def find_angle_results(self):
        results = {}
        for p1 in self.points:
            angles = {}
            for p2 in self.points:
                if p1 == p2:
                    continue
                angle = self.get_angle(p1, p2)
                if angle not in angles:
                    angles[angle] = []
                angles[angle] += [p2]
            results[p1] = angles
        self.results = results

    def find_best_all(self):
        self.find_angle_results()
        results = {}
        for p in self.results.keys():
            results[p] = len(self.results[p])
        sorted_results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_results[0]

    def find_best(self):
        return self.find_best_all()[1]

    def vaporize(self, nth):
        best = self.find_best_all()[0]
        angles = self.results[best]
        sorted_angles = sorted(angles.items(), key=lambda kv: kv[0])
        for angle in sorted_angles:
            angle[1].sort(key=lambda kv: math.sqrt((best[0] - kv[0])**2 + (best[1] - kv[1])**2))
        count = 0
        index = 0
        # bug angles are backwards
        match = sorted_angles[len(sorted_angles) - nth + 1][1][0]
        return 100 * match[0] + match[1]
        while True:
            angle0 = sorted_angles[index][1]
            point0 = angle0[0]
            if count == nth - 1:
                return 100 * next[0] + next[1]
            sorted_angles[index][1].remove(next)
            index = (index - 1) % len(sorted_angles)
            count += 1

def test_1():
    input1 = """
.#..#
.....
#####
....#
...##
"""
    asteroids = Asteroids(input1)
    assert len(asteroids.points) == 10
    asteroids = Asteroids(input1)
    assert asteroids.find_best() == 8


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
    assert asteroids.find_best() == 33

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
    assert asteroids.find_best() == 35

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
    assert asteroids.find_best() == 41

def test_5():
    input5 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
    asteroids = Asteroids(input5)
    assert asteroids.find_best() == 210

def test_part2():
    data = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
    """
    asteroids = Asteroids(data)
    assert asteroids.vaporize(2) == 1201
    assert asteroids.vaporize(3) == 1202
    assert asteroids.vaporize(10) == 1208
    assert asteroids.vaporize(20) == 1600
    assert asteroids.vaporize(50) == 1609
    assert asteroids.vaporize(100) == 1016
    assert asteroids.vaporize(199) == 906
    assert asteroids.vaporize(200) == 802
    assert asteroids.vaporize(201) == 1009

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
    print(f"part 1: {asteroids.find_best()}")
    print(f"part 2: {asteroids.vaporize(200)}")
