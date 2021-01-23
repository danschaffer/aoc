#!/usr/bin/env python3

def calculate_code(file, start, data):
    location = start
    lines = open(file).read().strip().split('\n')
    moves = {
        'U': (0,-1),
        'D': (0,1),
        'L': (-1,0),
        'R': (1,0),
    }
    code = ''
    for line in lines:
        for move in line:
            locx = location[0] + moves[move][0]
            locy = location[1] + moves[move][1]
            if (locx,locy) in data:
                location = (locx, locy)
        code += data[location]
    return code

def part1(file):
    start=(1,1)
    data={
        (0,0): '1',
        (1,0): '2',
        (2,0): '3',
        (0,1): '4',
        (1,1): '5',
        (2,1): '6',
        (0,2): '7',
        (1,2): '8',
        (2,2): '9',
    }
    return calculate_code(file, start, data)

def part2(file):
    start=(0,2)
    data={
        (2,0): '1',
        (1,1): '2',
        (2,1): '3',
        (3,1): '4',
        (0,2): '5',
        (1,2): '6',
        (2,2): '7',
        (3,2): '8',
        (4,2): '9',
        (1,3): 'A',
        (2,3): 'B',
        (3,3): 'C',
        (2,4): 'D',
    }
    return calculate_code(file, start, data)

def test1():
    assert part1('./day02-test.input') == '1985'
    assert part2('./day02-test.input') == '5DB3'

    assert part1('./day02.input') == '48584'
    assert part2('./day02.input') == '563B6'

if __name__ == '__main__':
    print("advent of code: day2")
    print(f"part 1: {part1('./day02.input')}")
    print(f"part 2: {part2('./day02.input')}")
