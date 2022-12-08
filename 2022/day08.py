#!/usr/bin/env python3
import sys
class Day08:
    def __init__(self, file):
        self.data = {}
        for y,line in enumerate(open(file).readlines()):
            line = line.strip()
            for x,ch in enumerate(line):
                self.data[(x,y)] = ch
        self.size_y = y + 1
        self.size_x = len(line)

    def is_visible(self, x, y):
        visible = True
        for left in range(0, x):
            if self.data[(left,y)] >= self.data[(x,y)]:
                visible = False
                break
        if visible:
            return True
        visible = True 
        for right in range(x+1,self.size_x):
            if self.data[(right,y)] >= self.data[(x,y)]:
                visible = False
                break
        if visible:
            return True
        visible = True
        for up in range(0, y):
            if self.data[(x,up)] >= self.data[(x,y)]:
                visible = False
        if visible:
            return True
        visible = True
        for down in range(y+1,self.size_y):
            if self.data[(x,down)] >= self.data[(x,y)]:
                visible = False
        return visible

    def scenic_score(self, x, y):
        lscore = 1
        for left in range(x-1, 0, -1):
            if self.data[(left,y)] >= self.data[(x,y)]:
                break
            lscore += 1
        rscore = 1
        for right in range(x+1,self.size_x-1):
            if self.data[(right,y)] >= self.data[(x,y)]:
                break
            rscore += 1
        uscore = 1
        for up in range(y-1, 0, -1):
            if self.data[(x,up)] >= self.data[(x,y)]:
                break
            uscore += 1
        dscore = 1
        for down in range(y+1,self.size_y-1):
            if self.data[(x,down)] >= self.data[(x,y)]:
                break
            dscore += 1
        score = lscore * rscore * uscore * dscore
        return score

    def run_part1(self):
        answer = 2 * self.size_x + 2 * (self.size_y - 2)
        for y in range(1, self.size_y-1):
            for x in range(1, self.size_x-1):
                if self.is_visible(x,y):
                    answer += 1
        return answer

    def run_part2(self):
        max_scenic = 0
        for y in range(1, self.size_y-1):
            for x in range(1, self.size_x-1):
                max_scenic = max(max_scenic, self.scenic_score(x,y))
        return max_scenic

def test1():
    test_day08 = Day08('./day08-test.input')
    assert test_day08.run_part1() == 21
    assert test_day08.run_part2() == 8

def test2():
    test_day08 = Day08('./day08.input')
    assert test_day08.run_part1() == 1684
    assert test_day08.run_part2() == 486540

if __name__ == '__main__':
    print("advent of code: day08")
    file = './day08.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day08 = Day08(file)
    print(f"part 1: {day08.run_part1()}")
    print(f"part 2: {day08.run_part2()}")
