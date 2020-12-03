#!/usr/bin/env python3

class Day3:
    def __init__(self):
        self.trees = []
        self.width = 0
        self.height = 0

    def load(self, file):
        lines = open(file).read().strip().split('\n')
        self.height = len(lines)
        for height,line in enumerate(lines):
            self.width = len(line)
            for index,char in enumerate(line):
                if char == '#':
                    self.trees += [(index,height)]
            height += 1

    def traverse(self, right=3, down=1):
        count = 0
        locx = right
        locy = down
        while locy < self.height:
            if (locx,locy) in self.trees:
                count += 1
            locx = (locx + right) % self.width
            locy += down
        return count

    def run_part1(self):
        return self.traverse()

    def run_part2(self):
        return self.traverse(1,1) * self.traverse(3,1) * self.traverse(5,1) * self.traverse(7,1) * self.traverse(1,2)

def test1():
    test_day3 = Day3()
    test_day3.load('./day3-test.input')
    assert test_day3.run_part1() == 7
    assert test_day3.run_part2() == 336

def test2():
    test_day3 = Day3()
    test_day3.load('./day3.input')
    assert test_day3.run_part1() == 289
    assert test_day3.run_part2() == 5522401584

if __name__ == '__main__':
    day3 = Day3()
    day3.load('./day3.input')
    print(f"part 1: {day3.run_part1()}")
    print(f"part 2: {day3.run_part2()}")
