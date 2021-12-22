#!/usr/bin/env python3

class Day22:
    def __init__(self, file):
        self.data = set()
        lines = open(file).read().split('\n')
        for line in lines:
            line = line.strip()
            state,coords=line.split()
            xs,ys,zs=coords.split(',')
            x0,x1=xs[2:].split('..')
            y0,y1=ys[2:].split('..')
            z0,z1=zs[2:].split('..')
            if int(x0) < -50 or int(x1) > 50 or int(y0) < -50 or int(y1) > 50 or int(z0) < -50 or int(z1) > 50:
                continue
            for x in range(int(x0),int(x1)+1):
                for y in range(int(y0),int(y1)+1):
                    for z in range(int(z0),int(z1)+1):
                        if state == 'on':
                            self.data.add((x,y,z))
                        elif state == 'off' and (x,y,z) in self.data:
                            self.data.remove((x,y,z))

    def run_part1(self):
        return len(self.data)

    def run_part2(self):
        return -1

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run_part1() == 39
    test_day22 = Day22('./day22-test2.input')
    assert test_day22.run_part1() == 590784

def test2():
    test_day22 = Day22('./day22.input')
    assert test_day22.run_part1() == 582644

if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22('./day22.input')
    print(f"part 1: {day22.run_part1()}")
#    print(f"part 2: {day22.run_part2()}")
