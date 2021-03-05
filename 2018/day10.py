#!/usr/bin/env python3
import sys
class Day10:
    def __init__(self, file):
        self.round = 0
        self.min_range = sys.maxsize
        self.min_round = 0

        self.data = []
        self.lines =open(file).readlines()
        self.reset()

    def reset(self):
        self.round = 0
        self.data = []
        posx_start = self.lines[0].find('<') + 1
        posx_end = self.lines[0].find(',')
        posy_start = posx_end + 1
        posy_end = self.lines[0].find('>')

        velx_start = self.lines[0].find('<', posy_end) + 1
        velx_end = self.lines[0].find(',', posy_end)
        vely_start = velx_end + 1
        vely_end = self.lines[0].find('>', posy_end+1)
        for line in self.lines:
            posx = int(line[posx_start:posx_end])
            posy = int(line[posy_start:posy_end])
            velx = int(line[velx_start:velx_end])
            vely = int(line[vely_start:vely_end])
            self.data.append((posx,posy,velx,vely))

    def update(self):
        self.round += 1
        for n,point in enumerate(self.data):
            posx,posy,velx,vely=point
            posx+=velx
            posy+=vely
            self.data[n] = (posx,posy,velx,vely)

    def get_message(self):
        minx = self.data[0][0]
        miny = self.data[0][1]
        maxx = self.data[0][0]
        maxy = self.data[0][1]
        for item in self.data:
            minx = min(minx, item[0])
            maxx = max(maxx, item[0])
            miny = min(miny, item[1])
            maxy = max(maxy, item[1])
        outputs = []
        for n in range(miny,maxy+1):
            outputs.append([' ' for _ in range(minx, maxx+1)])
        for item in self.data:
            outputs[item[1]-miny][item[0]-minx] = '#'
        out = ''
        for line in outputs:        
            out += ''.join(line) + '\n'
        return out

    def check_range(self):
        minx = self.data[0][0]
        miny = self.data[0][1]
        maxx = self.data[0][0]
        maxy = self.data[0][1]
        data0 = {}
        data1 = {}
        for item in self.data:
            minx = min(minx, item[0])
            maxx = min(maxx, item[0])
            miny = max(miny, item[1])
            maxy = max(maxy, item[1])
            if item[0] not in data0:
                data0[item[0]] = 1
            else:
                data0[item[0]] += 1
            if item[1] not in data1:
                data1[item[1]] = 1
            else:
                data1[item[1]] += 1
        range_ = len(data0)*len(data1)
        if range_ < self.min_range:
            self.min_range = range_
            self.min_round = self.round

    def run(self, max_iterations=15000):
        for n in range(max_iterations):
            self.update()
            self.check_range()
        self.reset()
        for _ in range(self.min_round):
            self.update()
        return self.get_message(), self.min_round

def test1():
    day10 = Day10('./day10-test.input')
    part1, part2 = day10.run(50)
    assert part2 == 3
    print(part1)  # HELLO

if __name__ == '__main__':
    print("advent of code: day10")
    day10 = Day10('./day10.input')
    part1, part2 = day10.run()
    print(f"part 1: \n{part1}") # CZKPNARN
    print(f"part 2: {part2}")
