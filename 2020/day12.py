#!/usr/bin/env python3

def part1(lines):
    north = 0
    east = 0
    direction = 'E'
    for line in lines:
        op = line[0]
        amount = int(line[1:])
#        print(f"{op}{amount} north:{north} east:{east} direction:{direction}")
        if op == 'L':
            amounts = [0, 270, 180, 90]
            dirs = ['N','E','S','W']
            direction = dirs[(dirs.index(direction) + amounts.index(amount)) % 4]
        elif op == 'R':
            amounts = [0,90,180,270]
            dirs = ['N','E','S','W']
            direction = dirs[(dirs.index(direction) + amounts.index(amount)) % 4]
        elif op == 'F':
            if direction == 'E':
                east += amount
            elif direction == 'W':
                east -= amount
            elif direction == 'N':
                north += amount
            elif direction == 'S':
                north -= amount
        elif op == 'N':
            north += amount
        elif op == 'S':
            north -= amount
        elif op == 'E':
            east += amount
        elif op == 'W':
            east -= amount
#        print(f"{op}{amount} north:{north} east:{east} direction:{direction}")
    return abs(north) + abs(east)

def part2(lines):
    north = 0
    east = 0
    way_north = 1
    way_east = 10
    for line in lines:
        op = line[0]
        amount = int(line[1:])
#        print(f"{op}{amount} north:{north} east:{east} way_north:{way_north} way_east:{way_east}")
        if op == 'N':
            way_north += amount
        elif op == 'S':
            way_north -= amount
        elif op == 'E':
            way_east += amount
        elif op == 'W':
            way_east -= amount
        elif op == 'F':
            east = east + amount * way_east
            north = north + amount * way_north
        elif op == 'R':
            if amount == 90:
                way_east1 = way_north
                way_north1 = way_east * -1
            elif amount == 180:
                way_east1 = way_east * -1
                way_north1 = way_north * -1
            elif amount == 270:
                way_east1 = way_north * -1
                way_north1 = way_east
            way_east = way_east1
            way_north = way_north1
        elif op == 'L':
            if amount == 90:
                way_east1 = way_north * -1
                way_north1 = way_east
            elif amount == 180:
                way_east1 = way_east * -1
                way_north1 = way_north * -1
            elif amount == 270:
                way_east1 = way_north
                way_north1 = way_east * -1
            way_east = way_east1
            way_north = way_north1
#        print(f"{op}{amount} north:{north} east:{east} way_north:{way_north} way_east:{way_east}")
    return abs(north) + abs(east)

def test1():
    assert part1(['F10','N3','F7','R90','F11']) == 25
    assert part2(['F10','N3','F7','R90','F11']) == 286

def test2():
    data = open('./day12.input').read().strip().split('\n')
    assert part1(data) == 882
    assert part2(data) == 28885

if __name__ == '__main__':
    print("advent of code: day12")
    data = open('./day12.input').read().strip().split('\n')
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")
