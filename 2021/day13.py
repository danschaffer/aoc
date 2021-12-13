#!/usr/bin/env python3
class Day13:
    def __init__(self, file):
        self.map = set()
        self.folds = []
        for line in open(file).readlines():
            line = line.strip()
            if line == '':
                continue
            if line.startswith("fold along"):
                self.folds.append(line.split()[2])
            else:
                x, y = line.split(',')
                self.map.add((int(x),int(y)))

    def fold(self, line):
        axis, num = line.split('=')
        num = int(num)
        if axis == 'x':
            self.fold_x(num)
        else:
            self.fold_y(num)

    def fold_x(self, fold_x):
        self.map0 = set()
        for (x,y) in self.map:
            if x > fold_x:
                x = fold_x - (x - fold_x)
            self.map0.add((x,y))
        self.map = self.map0

    def fold_y(self, fold_y):
        self.map0 = set()
        for (x,y) in self.map:
            if y > fold_y:
                y = fold_y - (y - fold_y)
            self.map0.add((x,y))
        self.map = self.map0

    def print_map(self):
        maxx = maxy = 0
        for x,y in self.map:
            maxx = max(maxx,x)
            maxy = max(maxy,y)
        lines = []
        for y in range(maxy+1):
            line = ''
            for x in range(maxx+1):
                if (x,y) in self.map:
                    ch = '#'
                else:
                    ch = '.'
                line += ch
            lines.append(line)
        f = open('day13.output','w')
        [f.write(line+'\n') for line in lines]
        f.close()

    def run(self):
        self.fold(self.folds.pop(0))
        part1 = len(self.map)
        for fold in self.folds:
            self.fold(fold)
        return part1

def test1():
    part1 = Day13('./day13-test.input').run()
    assert part1 == 17

def test2():
    part1 = Day13('./day13.input').run()
    assert part1 == 684

if __name__ == '__main__':
    print("advent of code: day13")
    day13 = Day13('./day13.input')
    print(f"part 1: {day13.run()}")
    day13.print_map() # JRZBLGKH
