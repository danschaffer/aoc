#!/usr/bin/env python3

class Day22:
    def __init__(self, infile):
        self.infile = infile
        self.directions = [(0,-1),(1,0),(0,1),(-1,0)]
        self.reset()

    def reset(self):
        self.data = {}
        self.dir = 0
        length = 0
        for row, line in enumerate(open(self.infile).readlines()):
            length = len(line)
            for col, ch in enumerate(line):
                if ch == '#':
                    self.data[(col,row)] = 'i'
        self.location = (length//2,length//2)
            
    def run2(self, iterations):
        return sum([self.iteration2() for _ in range(iterations)])

    def iteration2(self):
        result = 0
        if self.location not in self.data:
            state = 'c'
        else:
            state = self.data[self.location]

        if state == 'c':
            newstate = 'w'
            self.dir = (self.dir - 1) % 4
            self.data[self.location] = newstate
        elif state == 'w':
            newstate = 'i'
            result = 1
            self.data[self.location] = newstate
        elif state == 'i':
            newstate = 'f'
            self.dir = (self.dir + 1) % 4
            self.data[self.location] = newstate
        elif state == 'f':
            newstate = 'c'
            del self.data[self.location]
            self.dir = (self.dir + 2) % 4

        self.location = (self.location[0] + self.directions[self.dir][0], self.location[1] + self.directions[self.dir][1])
        return result

    def run1(self, iterations):
        return sum([self.iteration1() for _ in range(iterations)])

    def iteration1(self):
        result = 0
        if self.location in self.data:
            self.dir = (self.dir + 1) % 4
            del self.data[self.location]
            result = 0
        else:
            self.dir = (self.dir - 1) % 4
            self.data[self.location] = 'i'
            result = 1
        oldloc = self.location
        self.location = (self.location[0] + self.directions[self.dir][0], self.location[1] + self.directions[self.dir][1])
#        print(f"{result} {oldloc} {self.location}")
        return result

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run1(7) == 5
    test_day22.reset()
    assert test_day22.run1(70) == 41
    test_day22.reset()
    assert test_day22.run1(10000) == 5587
    test_day22.reset()
    assert test_day22.run2(100) == 26
    test_day22.reset()
    assert test_day22.run2(10000000) == 2511944

    day22 = Day22('./day22.input')
    assert day22.run1(10000) == 5565
    day22.reset()
    assert day22.run2(10000000) == 2511978


if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22('./day22.input')
    print(f"part 1: {day22.run1(10000)}")
    day22.reset()
    print(f"part 2: {day22.run2(10000000)}")
