#!/usr/bin/env python3

from itertools import combinations, starmap
from collections import deque, Counter

class Day19:
    def __init__(self, file):
        self.file = file
        self.ALL_ROTATIONS = (
            self.rotz, self.rotz, self.rotz,
            self.rotx,
            self.rotz, self.rotz, self.rotz,
            self.rotx,
            self.rotz, self.rotz, self.rotz,
            lambda x, y, z: (-x, -z, -y),
            self.rotz, self.rotz, self.rotz,
            self.rotx,
            self.rotz, self.rotz, self.rotz,
            lambda x, y, z: (x, z, -y),
            self.rotz, self.rotz, self.rotz,
        )

    def parse(self):
        for line in open(self.file).read().split('\n'):
            line = line.strip()
            if line.startswith('---'):
                scan = []
            elif line == '':
                yield scan
            else:
                scan.append(tuple(map(int, line.split(','))))
        yield scan

    def rotx(self, x, y, z):
        return x, -z, y

    def rotz(self, x, y, z):
        return -y, x, z

    def rotations(self, scan):
        yield scan
        for rot in self.ALL_ROTATIONS:
            scan = list(starmap(rot, scan))
            yield scan

    def move(self, scan, dx, dy, dz):
        return [(x + dx, y + dy, z + dz) for x, y, z in scan]

    def find_scanner(self, base, rotated_scans):
        for scan in rotated_scans:
            [(diff, count)] = Counter((x2 - x1, y2 - y1, z2 - z1)
                                      for x1, y1, z1 in scan
                                      for x2, y2, z2 in base).most_common(1)
            if count >= 12:
                return diff, self.move(scan, *diff)
        return None, None

    def join(self, scans):
        joined = set(next(scans))
        remaining = deque(list(self.rotations(scan)) for scan in scans)
        scanners = [(0,0,0)]
        while remaining:
            rotated_scans = remaining.popleft()
            scanner, moved = self.find_scanner(joined, rotated_scans)
            if scanner:
                joined |= set(moved)
                scanners.append(scanner)
            else:
                remaining.append(rotated_scans)
        return joined, scanners

    def max_distance(self, scanners):
        return max(abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
            for (x1, y1, z1), (x2, y2, z2) in combinations(scanners, 2))

    def run(self):
        joined, scanners = self.join(self.parse())
        return len(joined), self.max_distance(scanners)

def test1():
    test_day19 = Day19('./day19-test.input')
    assert test_day19.run() == (79, 3621)

def test2():
    test_day19 = Day19('./day19.input')
    assert test_day19.run() == (359, 12292)

if __name__ == '__main__':
    print("advent of code: day19")
    day19 = Day19('./day19.input')
    p1, p2 = day19.run()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")
