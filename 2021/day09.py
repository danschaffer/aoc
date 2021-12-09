#!/usr/bin/env python3

class Day09:
    def __init__(self, file):
        self.data = {}
        for y,line in enumerate(open(file).read().split('\n')):
            for x, char in enumerate(line):
                self.data[(x,y)] = int(char)
                self.width = len(line)
        self.height = y+1

    def run_part1(self):
        answer = 0
        for y in range(self.height):
            for x in range(self.width):
                if ((x-1,y) not in self.data or self.data[(x,y)] < self.data[(x-1,y)]) and ((x+1,y) not in self.data or self.data[(x,y)] < self.data[(x+1,y)]) and ((x,y-1) not in self.data or self.data[(x,y)] < self.data[(x,y-1)]) and ((x,y+1) not in self.data or self.data[(x,y)] < self.data[(x,y+1)]):
                    answer += self.data[(x,y)] + 1
        return answer

    def run_part2(self):
        basins = []
        for y in range(self.height):
            for x in range(self.width):
                if ((x-1,y) not in self.data or self.data[(x,y)] < self.data[(x-1,y)]) and ((x+1,y) not in self.data or self.data[(x,y)] < self.data[(x+1,y)]) and ((x,y-1) not in self.data or self.data[(x,y)] < self.data[(x,y-1)]) and ((x,y+1) not in self.data or self.data[(x,y)] < self.data[(x,y+1)]):
                    basin=[(x,y)]
                    basins.append(set(basin))
        for basin in basins:
            lastsize = -1
            while True:
                if lastsize == len(basin):
                    break
                lastsize = len(basin)
                for x,y in basin.copy():
                    for newpoint in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if newpoint in self.data and self.data[newpoint]<9:
                            basin.add(newpoint)
        basins.sort(key=lambda x: len(x), reverse=True)
        return len(basins[0]) * len(basins[1]) * len(basins[2])

def test1():
    test_day09 = Day09('./day09-test.input')
    assert test_day09.run_part1() == 15
    assert test_day09.run_part2() == 1134

def test2():
    test_day09 = Day09('./day09.input')
    assert test_day09.run_part1() == 550
    assert test_day09.run_part2() == 1100682

if __name__ == '__main__':
    print("advent of code: day09")
    day09 = Day09('./day09.input')
    print(f"part 1: {day09.run_part1()}")
    print(f"part 2: {day09.run_part2()}")
