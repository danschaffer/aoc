#!/usr/bin/env python3

class Lights:
    def __init__(self, corners=False, verbose=False):
        self.forceCorners = corners
        self.verbose = verbose
        self.data = {}
        self.xlen = 0
        self.ylen = 0
        self.round = 0
    
    def load_file(self, file):
        self.load(open(file).read().strip().split('\n'))

    def load(self, lines):
        self.xlen = len(lines[0])
        self.ylen = len(lines)
        for yindex in range(self.ylen):
            line = lines[yindex]
            for xindex in range(self.xlen):
                if line[xindex] == '#':
                    value = 1
                else:
                    value = 0
                self.data[(xindex,yindex)] = value

    def get_value(self, x, y):
        if x < 0 or y < 0 or x >= self.xlen or y >= self.ylen or self.data[(x,y)] == 0:
            result=0
        else:
            result=1
        return result

    def get_next(self, x, y):
        total = 0
        total += self.get_value(x - 1, y - 1)
        total += self.get_value(x, y - 1)
        total += self.get_value(x + 1, y - 1)
        total += self.get_value(x - 1, y)
        total += self.get_value(x + 1, y)
        total += self.get_value(x - 1, y + 1)
        total += self.get_value(x, y + 1)
        total += self.get_value(x + 1, y + 1)

        if self.get_value(x, y) == 0 and total == 3:
            return 1
        elif self.get_value(x, y) == 1 and (total == 2 or total == 3):
            return 1
        return 0

    def next_round(self):
        newdata = {}
        for y in range(self.ylen):
            for x in range(self.xlen):
                newdata[(x,y)] = self.get_next(x, y)
        self.data = newdata
        self.round += 1

    def force_corners(self):
        self.data[(0,0)] = 1
        self.data[(self.xlen-1,0)] = 1
        self.data[(0,self.ylen-1)] = 1
        self.data[(self.xlen-1,self.ylen-1)] = 1


    def count_lights(self):
        return sum(self.data.values())

    def do_rounds(self, count):
        if self.forceCorners:
            self.force_corners()
        self.print_round()
        for _ in range(count):
            self.next_round()
            if self.forceCorners:
                self.force_corners()
            self.print_round()

    def print_round(self):
        if not self.verbose:
            return
        print(f"round {self.round}")
        for yindex in range(self.ylen):
            line = ''
            for xindex in range(self.xlen):
                if self.data[(xindex, yindex)] == 1:
                    line += '#'
                else:
                    line += '.'
            print(line)

def test1():
    data = '.#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..'.split('\n')
    lights = Lights(verbose=True)
    lights.load(data)
    lights.do_rounds(4)
    assert lights.count_lights() == 4

    lights2 = Lights(corners=True, verbose=True)
    lights2.load(data)
    lights2.do_rounds(5)
    assert lights2.count_lights() == 17

def test2():
    lights = Lights()
    lights.load_file('./day18.input')
    lights.do_rounds(100)
    assert lights.count_lights() == 821

    lights2 = Lights(corners=True)
    lights2.load_file('./day18.input')
    lights2.do_rounds(100)
    assert lights2.count_lights() == 886

if __name__ == '__main__':
    lights = Lights()
    lights.load_file('./day18.input')
    lights.do_rounds(100)
    print(f"part 1: {lights.count_lights()}")

    lights2 = Lights(corners=True)
    lights2.load_file('./day18.input')
    lights2.do_rounds(100)
    print(f"part 2: {lights2.count_lights()}")
