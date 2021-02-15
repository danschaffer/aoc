#!/usr/bin/env python3
import os

def get_distance(location):
    x,y,z = location
    return (abs(x) + abs(y) + abs(z) ) // 2

def day11(data):
    if os.path.exists(data):
        data = open(data).read().strip()
    moves = data.split(',')
    location = (0,0,0)
    furthest = 0
    for move in moves:
        x,y,z=location
        if move == 'n':
            location = (x+1,y-1,z)
        elif move == 's':
            location = (x-1,y+1,z)
        elif move == 'nw':
            location = (x+1,y,z-1)
        elif move == 'ne':
            location = (x,y-1,z+1)
        elif move == 'sw':
            location = (x,y+1,z-1)
        elif move == 'se':
            location = (x-1,y,z+1)
        furthest = max(furthest, get_distance(location))
    distance = get_distance(location)
    return distance, furthest

def test1():
    assert day11('ne,ne,ne') == (3,3)
    assert day11('ne,ne,sw,sw') == (0,2)
    assert day11('ne,ne,s,s') == (2,2)
    assert day11('se,sw,se,sw,sw') == (3,3)
    assert day11('./day11.input') == (818,1596)

if __name__ == '__main__':
    print("advent of code: day11")
    distance, furthest = day11('./day11.input')
    print(f"part 1: {distance}")
    print(f"part 2: {furthest}")
