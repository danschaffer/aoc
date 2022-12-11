#!/usr/bin/env python3
import sys
class Day10:
    def __init__(self, file):
        self.lines = [line.strip() for line in open(file).readlines()]

    @staticmethod
    def get_char(cycle, x):
        if abs((cycle % 40) - x) < 2:
            return '#'
        return '.'

    def run(self):
        cycle = 0
        x = 1
        answer2 = ''
        answer1 = 0
        part1 = [20, 60, 100, 140, 180, 220]
        while cycle < 240:
            answer2 += Day10.get_char(cycle, x)
            cycle += 1
            if cycle in part1:
                answer1 += cycle * x
            line = self.lines.pop(0)
            if line.startswith('addx'):
                answer2 += Day10.get_char(cycle, x)
                cycle += 1
                if cycle in part1:
                    answer1 += cycle * x
                x += int(line.split()[1])
        answer2_fmt = ''.join([answer2[40*i:40*(i+1)] + '\n' for i in range(6)])
        return answer1, answer2_fmt
            
def test1():
    answer1, answer2 = Day10('./day10-test.input').run()
    assert answer1 == 13140
    assert answer2.count('#') == 124
    assert answer2.count('.') == 116

def test2():
    answer1, answer2 = Day10('./day10.input').run()
    assert answer1 == 11220
    assert answer2.count('#') == 97
    assert answer2.count('.') == 143

if __name__ == '__main__':
    print("advent of code: day10")
    file = './day10.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    answer1, answer2 = Day10(file).run()
    print(f"part 1: {answer1}")
    print(f"part 2: \n{answer2}") # BZPAJELK
