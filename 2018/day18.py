#!/usr/bin/env python

class Day18:
    '''
    . open ground
    | tree
    # lumberyard
    open -> trees if 3 or more adjacent contain trees
    tree -> lumberyard if 3 or more adjacent lumberyards
    lumberyard -> open if no adjacent lumberyards
    '''
    def __init__(self, file):
        self.data = {}
        self.time = 0
        self.maxx = self.maxy = 0
        for y,line in enumerate(open(file).readlines()):
            self.maxy = y+1
            self.maxx = len(line)
            for x,char in enumerate(line):
                self.data[(x,y)] = char

    def print_board(self):
        print(f"time: {self.time}")
        for y in range(self.maxy):
            line = ''
            for x in range(self.maxx):
                line += self.data[(x,y)]
            print(line)

    def next_spot(self, x, y):
        trees, open, lumberyards = self.get_adjacent(x,y)
        next = self.data[(x,y)]
        if self.data[(x,y)] == '.' and trees >= 3:
            next = '|'
        if self.data[(x,y)] == '|' and lumberyards >= 3:
            next = '#'
        if self.data[(x,y)] == '#':
            if lumberyards > 0 and trees > 0:
                next = '#'
            else:
                next = '.'
        return next
    
    def get_adjacent(self, x, y):
        trees = open = lumberyards = 0
        for x0, y0 in [(x-1,y+1),(x+0,y+1),(x+1,y+1),(x-1,y+0),(x+1,y+0),(x-1,y-1),(x+0,y-1),(x+1,y-1)]:
            if (x0,y0) in self.data:
                if self.data[(x0,y0)] == '.':
                    open += 1
                if self.data[(x0,y0)] == '|':
                    trees += 1
                elif self.data[(x0,y0)] == '#':
                    lumberyards += 1
        return trees, open, lumberyards

    def next_board(self):
        d = {}
        for y in range(self.maxy):
            for x in range(self.maxx):
                d[(x,y)] = self.next_spot(x,y)
        return d

    def resources(self):
        trees = open = lumberyards = 0
        for y in range(self.maxy):
            for x in range(self.maxx):
                if self.data[(x,y)] == '.':
                    open += 1
                elif self.data[(x,y)] == '|':
                    trees += 1
                else:
                    lumberyards += 1
        return trees * lumberyards

    def run(self, time=10):
        for _ in range(time):
            self.data = self.next_board()
            self.time += 1
        return self.resources()

    def run_part2(self, time=1000000000):
        # repeats after 467 times
        for n in range(466):
            self.data = self.next_board()
        history = []
        for _ in range(28):
            self.data = self.next_board()
            history.append(self.resources())
        answer = (time - 467) % 28
        return history[answer]

def test1():
    assert Day18('day18-test.input').run(10) == 1147
    assert Day18('day18.input').run(10) == 539682
    assert Day18('day18.input').run_part2() == 226450

if __name__ == '__main__':
    print('advent of code: day18')
    print(f"part 1: {Day18('day18.input').run(10)}")
    print(f"part 2: {Day18('day18.input').run_part2(1000000000)}")


