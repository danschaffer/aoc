#!/usr/bin/env python3

# turn on 0,0 through 999,999
# toggle 0,0 through 999,0
# turn off 499,499 through 500,500

class LightsMap:
    def __init__(self):
        self.grid = [0 for _ in range(1000000)]

    def add_lines_part1(self, lines):
        for line in lines:
            self.add_part1(line)

    def add_lines_part2(self, lines):
        for line in lines:
            self.add_part2(line)

    def add_part1(self, line):
        tokens = line.split(' ')
        if tokens[0] == 'turn':
            tokens = tokens[1:]
        start = tokens[1].split(',')
        end = tokens[3].split(',')
        for y in range(int(start[1]), int(end[1]) + 1):
            for x in range(int(start[0]), int(end[0]) + 1):
                if tokens[0] == 'on':
                    self.grid[y * 1000 + x] = 1
                elif tokens[0] == 'off':
                    self.grid[y * 1000 + x] = 0
                else:
                    self.grid[y * 1000 + x] = (self.grid[y * 1000 + x] + 1) % 2

    def add_part2(self, line):
        tokens = line.split(' ')
        if tokens[0] == 'turn':
            tokens = tokens[1:]
        start = tokens[1].split(',')
        end = tokens[3].split(',')
        for y in range(int(start[1]), int(end[1]) + 1):
            for x in range(int(start[0]), int(end[0]) + 1):
                if tokens[0] == 'on':
                    self.grid[y * 1000 + x] += 1
                elif tokens[0] == 'off':
                    self.grid[y * 1000 + x] -= 1
                    self.grid[y * 1000 + x] = max(self.grid[y * 1000 + x], 0)
                else:
                    self.grid[y * 1000 + x] += 2

    def count(self):
        return sum([self.grid[n] for n in range(1000000)])

def test1():
    map = LightsMap()
    map.add_part1('turn on 0,0 through 999,999')
    assert map.count() == 1000000

    map.add_part1('toggle 0,0 through 999,0')
    assert map.count() == 1000000 - 1000

    map.add_part1('turn off 499,499 through 500,500')
    assert map.count() == 1000000 - 1000 - 4

def test2():
    data = open('day6.input').read().strip().split('\n')
    map = LightsMap()
    map.add_lines_part1(data)
    assert map.count() == 543903    

def test3():
    map = LightsMap()
    map.add_part2('turn on 0,0 through 0,0')
    assert map.count() == 1

    map.add_part2('toggle 0,0 through 999,999')
    assert map.count() == 2000001
    
def test4():
    data = open('day6.input').read().strip().split('\n')
    map = LightsMap()
    map.add_lines_part2(data)
    assert map.count() == 14687245    

if __name__ == '__main__':

    data = open('day6.input').read().strip().split('\n')
    map1 = LightsMap()
    map1.add_lines_part1(data)
    print(f"part 1 = {map1.count()}")
    map2 = LightsMap()
    map2.add_lines_part2(data)
    print(f"part 2 = {map2.count()}")
