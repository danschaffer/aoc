#!/usr/bin/env python3

class Day19:
    def __init__(self, file):
        self.data = {}
        self.start = None
        for row, line in enumerate(open(file).read().split('\n')):
            for col, ch in enumerate(line):
                if ch != ' ':
                    if not self.start:
                        self.start=(col,row)
                    self.data[(col,row)] = ch

    def run(self):
        result = ''
        current = self.start
        moves = 0
        dir = (0,1)
        while True:
            ch = self.data[current]
            if ch >= 'A' and ch <= 'Z':
                result += ch
            if ch == '+':
                if dir[0] == 0:
                    if (current[0]-1,current[1]) in self.data:
                        dir=(-1,0)
                    else:
                        dir=(1,0)
                else:
                    if (current[0],current[1]-1) in self.data:
                        dir=(0,-1)
                    else:
                        dir=(0,1)
            current = (current[0]+dir[0], current[1]+dir[1])
            moves += 1
            if current not in self.data:
                break
        return moves, result

def test1():
    test_day19 = Day19('./day19-test.input')
    moves, result = test_day19.run()
    assert result == 'ABCDEF'
    assert moves == 38

    day19 = Day19('./day19.input')
    moves, result = day19.run()
    assert result == 'VTWBPYAQFU'
    assert moves == 17358

if __name__ == '__main__':
    print("advent of code: day19")
    day19 = Day19('./day19.input')
    moves, result = day19.run()
    print(f"part 1: {result}")
    print(f"part 2: {moves}")
