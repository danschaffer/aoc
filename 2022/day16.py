#!/usr/bin/env python3
import functools
import sys
class Day16:
    def __init__(self, file):
        self.data = {}
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split()
            valve = parts[1]
            rate = int(parts[4][5:-1])
            tunnels = []
            for tunnel in parts[9:]:
                if tunnel.endswith(","):
                    tunnel = tunnel[:-1]
                tunnels.append(tunnel)
            self.data[valve] = {'rate':rate,'tunnels':tunnels}

    @functools.cache
    def solve1(self, opened, time, current):
        if time <= 0:
            return 0
        best = 0
        data = self.data[current]
        for tunnel in data['tunnels']:
            best = max(best, self.solve1(opened, time-1, tunnel))

        if current not in opened and data['rate'] > 0 and time > 0:
            opened = set(opened)
            opened.add(current)
            time -= 1
            result = time * data['rate']

            for valve in data['tunnels']:
                best = max(best, result + self.solve1(frozenset(opened), time - 1, valve))
        return best

    @functools.cache
    def solve2(self, opened, time, current):
        if time <= 0:
            return self.solve1(opened, 26, 'AA')
        best = 0
        data = self.data[current]
        for tunnel in data['tunnels']:
            best = max(best, self.solve2(opened, time-1, tunnel))

        if current not in opened and data['rate'] > 0 and time > 0:
            opened = set(opened)
            opened.add(current)
            time -= 1
            result = time * data['rate']

            for valve in data['tunnels']:
                best = max(best, result + self.solve2(frozenset(opened), time - 1, valve))
        return best

    def run_part1(self):
        return self.solve1(frozenset(), 30, 'AA')

    def run_part2(self):
        return self.solve2(frozenset(), 26, 'AA')

def test1():
    test_day16 = Day16('./day16-test.input')
    assert test_day16.run_part1() == 1651
    assert test_day16.run_part2() == 1707

def test2():
    test_day16 = Day16('./day16.input')
    assert test_day16.run_part1() == 1767
    assert test_day16.run_part2() == 2528

if __name__ == '__main__':
    print("advent of code: day16")
    file = './day16.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day16 = Day16(file)
    print(f"part 1: {day16.run_part1()}")
    print(f"part 2: {day16.run_part2()}")
