#!/usr/bin/env python3

class Day22:
    def __init__(self, infile):
        self.infile = infile
        self.directions = [(0,-1),(1,0),(0,1),(-1,0)]
        self.reset()

    def reset(self):
        self.data = []
        self.dir = 0
        length = 0
        for row, line in enumerate(open(self.infile).readlines()):
            length = len(line)
            for col, ch in enumerate(line):
                if ch == '#':
                    self.data.append((col,row))
        self.location = (length//2,length//2)
            
    def run(self, iterations):
        return sum([self.iteration() for _ in range(iterations)])

    def iteration(self):
        result = 0
        if self.location in self.data:
            self.dir = (self.dir + 1) % 4
            self.data.remove(self.location)
            result = 0
        else:
            self.dir = (self.dir - 1) % 4
            self.data.append(self.location)
            result = 1
        oldloc = self.location
        self.location = (self.location[0] + self.directions[self.dir][0], self.location[1] + self.directions[self.dir][1])
#        print(f"{result} {oldloc} {self.location}")
        return result

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run(7) == 5
    test_day22.reset()
    assert test_day22.run(70) == 41
    test_day22.reset()
    assert test_day22.run(10000) == 5587

if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22('./day22.input')
    print(f"part 1: {day22.run(10000)}")
