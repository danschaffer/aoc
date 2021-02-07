#!/usr/bin/env python

def find_distance(goal_steps):
    cache=set()
    cache.add((0,0))
    location=(0,0)
    direction=0
    moves=[(0,-1),(1,0),(0,1),(-1,0)]  # move left
    steps=1
    while steps < goal_steps:
        if (location[0]+moves[(direction+1)%4][0],location[1]+moves[(direction+1)%4][1]) not in cache:
            direction=(direction+1)%4
        location=(location[0]+moves[direction][0], location[1]+moves[direction][1])
        cache.add(location)
        steps += 1
    return abs(location[0]) + abs(location[1])

def find_sums(goal):
    cache={}
    cache[(0,0)] = 1
    location=(0,0)
    direction=0
    moves=[(0,-1),(1,0),(0,1),(-1,0)]  # move left
    allmoves=[(0,-1),(1,0),(0,1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]  # move left
    while True:
        if (location[0]+moves[(direction+1)%4][0],location[1]+moves[(direction+1)%4][1]) not in cache:
            direction=(direction+1)%4
        location=(location[0]+moves[direction][0], location[1]+moves[direction][1])
        result = sum([cache.get((location[0]+direction[0],location[1]+direction[1]),0) for direction in allmoves])
        cache[location]=result
        if result >= goal:
            return result

def test():
    assert find_distance(1) == 0
    assert find_distance(12) == 3
    assert find_distance(23) == 2
    assert find_distance(1024) == 31
    assert find_distance(325489) == 552
    assert find_sums(800) == 806
    assert find_sums(325489) == 330785

if __name__ == '__main__':
    print("advent of code day 3")
    print(f"part 1: {find_distance(325489)}")
    print(f"part 2: {find_sums(325489)}")