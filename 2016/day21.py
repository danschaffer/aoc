#!/usr/bin/env python
import itertools
def solve2(instructions, solution):
    perms = [''.join(item) for item in list(itertools.permutations(solution, 8))]
    for string in perms:
        if solve1(instructions, string) == solution:
            return string

def solve1(instructions, string):
    for line in instructions:
        parts = line.split()
        if parts[0] == 'swap' and parts[1] == 'position':
            position0 = int(parts[2])
            position1 = int(parts[5])
            string0 = list(string)
            string0[position0], string0[position1] = string[position1], string[position0]
            string = ''.join(string0) 
        elif parts[0] == 'swap' and parts[1] == 'letter':
            position0 = string.find(parts[2])
            position1 = string.find(parts[5])
            string0 = list(string)
            string0[position0], string0[position1] = string[position1], string[position0]
            string = ''.join(string0) 
        elif parts[0] == 'reverse':
            position0 = int(parts[2])
            position1 = int(parts[4])
            string = string[0:position0] + string[position0:position1+1][::-1] + string[position1+1:]
        elif parts[0] == 'move':
            position0 = int(parts[2])
            position1 = int(parts[5])
            letter = string[position0]
            string0 = list(string)
            del string0[position0]
            string0.insert(position1, letter)
            string = ''.join(string0)
        elif parts[0] == 'rotate' and parts[1] == 'right':
            amount = int(parts[2])
            for _ in range(amount):
                string = string[-1] + string[0:-1]
        elif parts[0] == 'rotate' and parts[1] == 'left':
            amount = int(parts[2])
            for _ in range(amount):
                string = string[1:] + string[0]
        elif parts[0] == 'rotate' and parts[1] == 'based':
            amount = string.find(parts[6])
            string = string[-1] + string[0:-1]
            for _ in range(amount):
                string = string[-1] + string[0:-1]
            if amount >= 4:
                string = string[-1] + string[0:-1]
    return string

def test1():
    instructions0 = open('./day21-test.input').read().strip().split('\n')
    assert solve1(instructions0,'abcde') == 'decab'
    instructions1 = open('./day21.input').read().strip().split('\n')
    assert solve1(instructions1,'abcdefgh') == 'dgfaehcb'
    assert solve2(instructions1,'fbgdceah') == 'fdhgacbe'

if __name__ == '__main__':
    print("advent of code day 21")
    instructions = open('./day21.input').read().strip().split('\n')
    print(f"part 1: {solve1(instructions,'abcdefgh')}")
    print(f"part 2: {solve2(instructions,'fbgdceah')}")

        