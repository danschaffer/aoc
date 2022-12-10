#!/usr/bin/env python3
import math
import sys
class Day09:
    def __init__(self, file, p2=False):
        self.moves = [line.strip() for line in open(file).readlines()]
        if not p2:
            self.snake = [(0,0) for _ in range(2)]
        else:
            self.snake = [(0,0) for _ in range(10)]
        self.visited = {(0,0)}

    @staticmethod
    def is_adjacent(p1,p2):
        return (p1[0]==p2[0] and abs(p1[1]-p2[1]) == 1) or (p1[1]==p2[1] and abs(p1[0]-p2[0])==1)

    @staticmethod
    def is_diagonal(p1,p2):
        return abs(p1[0]-p2[0])==1 and abs(p1[1]-p2[1])==1

    @staticmethod
    def is_touching(p1,p2):
        return p1 == p2 or Day09.is_adjacent(p1,p2) or Day09.is_diagonal(p1,p2)

    @staticmethod
    def do_move(p, move):
        move1 = {'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1),'UL':(-1,-1),'UR':(1,-1),'DL':(-1,1),'DR':(1,1)}[move]
        return (p[0]+move1[0],p[1]+move1[1])

    def move_tail(self, i):
        if Day09.is_touching(self.snake[i], self.snake[i-1]):
            return
        for move in ['R','L','U','D']:
            t2 = Day09.do_move(self.snake[i], move)
            if Day09.is_adjacent(self.snake[i-1], t2):
                self.snake[i] = t2
                return
        for move in ['UR','UL','DR','DL']:
            t2 = Day09.do_move(self.snake[i], move)
            if Day09.is_adjacent(self.snake[i-1], t2):
                self.snake[i] = t2
                return
        for move in ['UR','UL','DR','DL']:
            t2 = Day09.do_move(self.snake[i], move)
            if Day09.is_diagonal(self.snake[i-1], t2):
                self.snake[i] = t2
                return

    def run(self):
        for movestr in self.moves:
            move, num = movestr.split()
            for _ in range(int(num)):
                self.snake[0] = Day09.do_move(self.snake[0], move)
                for i in range(1,len(self.snake)):
                    self.move_tail(i)
                self.visited.add(self.snake[-1])
        return len(self.visited)

    def print_grid(self):
        for y in range(-20,5):
            s = ''
            for x in range(-5,20):
                try:
                    fnd = self.snake.index((x,y))
                    if fnd == 0:
                        fnd = 'H'
                    else:
                        fnd = str(fnd)
                except:
                    fnd = '.'
                    if (x,y) == (0,0):
                        fnd = 's'
                    else:
                        fnd = '.'
                s += fnd
            print(s)


def test1():
    assert Day09('./day09-test.input').run() == 13
    assert Day09('./day09-test.input', p2=True).run() == 1
    assert Day09('./day09-test2.input').run() == 88
    assert Day09('./day09-test2.input', p2=True).run() == 36

def test2():
    assert Day09('./day09.input').run() == 5683
    assert Day09('./day09.input', p2=True).run() == 2372

if __name__ == '__main__':
    print("advent of code: day09")
    file = './day09.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day09 = Day09(file)
    print(f"part 1: {Day09(file).run()}")
    print(f"part 2: {Day09(file, p2=True).run()}")
