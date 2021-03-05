#!/usr/bin/env python3
import sys
class Day11:
    def __init__(self, serial=8):
        self.serial = serial
        self.data = {}
        self.fill_data()

    def fill_data(self):
        for i in range(1,301):
            for j in range(1,301):
                self.data[(i,j)] = self.get_powerlevel(i,j)

    def get_powerlevel(self,i,j):
        rackid = i + 10
        powerlevel = (rackid * j + self.serial) * rackid % 1000 // 100 - 5
        return powerlevel

    def run1(self):
        best0 = -1 * sys.maxsize
        best1 = (0,0)
        for i in range(1,301-3):
            for j in range(1,301-3):
                sum_ = 0
                for i0 in range(3):
                    for j0 in range(3):
                        sum_ += self.data[(i+i0,j+j0)]
                if sum_ > best0:
                    best0 = sum_
                    best1 = (i,j)
        return best0, best1

    def run2(self):
        best0 = -1 * sys.maxsize
        best1 = (0,0)
        for h in range(1,20):
#            print(f"{h} {best0} {best1}")
            for i in range(1,301-h):
                for j in range(1,301-h):
                    sum_ = 0
                    for i0 in range(h):
                        for j0 in range(h):
                            sum_ += self.data[(i+i0,j+j0)]
                    if sum_ > best0:
                        best0 = sum_
                        best1 = (i,j,h)
        return best0, best1

def test1():
    assert Day11(8).get_powerlevel(3,5) == 4
    assert Day11(57).get_powerlevel(122,79) == -5
    assert Day11(39).get_powerlevel(217,196) == 0
    assert Day11(71).get_powerlevel(101,153) == 4

    best0, best1 = Day11(18).run1()
    assert best0 == 29
    assert best1 == (33,45)

    day11 = Day11(4455)
    best0, best1 = day11.run1()
    assert best0 == 33
    assert best1 == (21,54)

    day11 = Day11(4455)
    best0, best1 = day11.run2()
    assert best0 == 74
    assert best1 == (236,268,11)

if __name__ == '__main__':
    print("advent of code: day11")
    best0, best1 = Day11(4455).run1()
    print(f"part 1: {best1}")
    best0, best1 = Day11(4455).run2()
    print(f"part 2: {best1}")
