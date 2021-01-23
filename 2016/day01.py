#!/usr/bin/env python3
def day1(line,part2=False):
    locations = []
    location = (0,0)
    locations.append(location)
    direction = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for move in line.split(','):
        move = move.strip()
        if move[0] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        amount = int(move[1:])
        for _ in range(amount):
            location = (location[0]+directions[direction][0], location[1]+directions[direction][1])
            if part2:
                if location in locations:
                    return abs(location[0]) + abs(location[1])
                locations.append(location)
    return abs(location[0]) + abs(location[1])

def test1():
    assert day1('R2, L3') == 5
    assert day1('R2, R2, R2') == 2
    assert day1('R5, L5, R5, R3') == 12
    assert day1(open('./day01.input').read()) == 239

    assert day1('R8, R4, R4, R8',part2=True) == 4
    assert day1(open('./day01.input').read(), part2=True) == 141

if __name__ == '__main__':
    print("advent of code: day1")
    print(f"part 1: {day1(open('./day01.input').read())}")
    print(f"part 2: {day1(open('./day01.input').read(), part2=True)}")
