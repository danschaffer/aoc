#!/usr/bin/env python3
import sys
class Day15:
    def __init__(self, file, row):
        self.row = row
        self.sensors = set()
        self.beacons = set()
        self.data = []
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split()
            sensor = (Day15.parse(parts[2]),Day15.parse(parts[3]))
            self.sensors.add(sensor)
            beacon = (Day15.parse(parts[8]), Day15.parse(parts[9]))
            self.beacons.add(beacon)
            self.data.append({'sensor': sensor,'beacon': beacon})

    @staticmethod
    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def parse(str):
        if str.endswith(',') or str.endswith(':'):
            str = str[:-1]
        result = int(str[2:])
        return result

    def find_matches(self, row, limit=-1):
        matches = set()
        for item in self.data:
            sensor = item['sensor']
            dist = Day15.manhattan(sensor,item['beacon'])
            for i in range(1 + dist - abs(sensor[1] - row)):
                if limit == -1:
                    if (sensor[0]-i,row) not in self.beacons:
                        matches.add(sensor[0]-i)
                    if (sensor[0]+i,row) not in self.beacons:
                        matches.add(sensor[0]+i)
                else:
                    if sensor[0]-i > 0 and sensor[0]-i < limit:
                        matches.add(sensor[0]-i)
                    if sensor[0]+i > 0 and sensor[0]+i < limit:
                        matches.add(sensor[0]+i)                
        return matches

    def run_part1(self):
        matches = self.find_matches(self.row)
        return len(matches)

    def run_part2(self):
        return -1
        limit = self.row*2
        expected = len(self.find_matches(0, limit=limit))
        for i in range(limit):
            matches = self.find_matches(i, limit=limit)
            print(f"{i} {len(matches)}")
            if len(matches) + 1 == expected:
                for n in range(1, len(matches)):
                    if n not in matches:
                        return n * 4000000 + i

def test1():
    test_day15 = Day15('./day15-test.input', 10)
    assert test_day15.run_part1() == 26
    assert test_day15.run_part2() == -1
#    assert test_day15.run_part2() == 56000011

def test2():
    test_day15 = Day15('./day15.input', 2000000)
    assert test_day15.run_part1() == 5147333

if __name__ == '__main__':
    print("advent of code: day15")
    file = './day15.input'
    row = 10
#    file = './day15.input'
#   row = 2000000
    if len(sys.argv) > 2:
        file = sys.argv[1]
        row = int(sys.argv[2])
    day15 = Day15(file, row)
    print(f"part 1: {day15.run_part1()}") 
    print(f"part 2: {day15.run_part2()}") 
