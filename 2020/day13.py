#!/usr/bin/env python3
import math
from math import gcd
from itertools import count
import os
def run_part1(file):
    goal, line = open(file).read().strip().split('\n')
    goal=int(goal)
    targets=[int(token) for token in line.split(',') if token!='x']
    matches={}
    for target in targets:
        counter=1
        while counter*target<goal:
            counter+=1
        matches[counter*target] = target
    best=min(matches.keys())
    return (best-goal)*matches[best]

def run_part2(file):
    def lcm(a,b):
        return a * b // gcd(a,b)
    line = file
    if os.path.exists(file):
        _, line = open(file).read().strip().split('\n')
    targets = []
    for counter, item in enumerate(line.split(',')):
        if item !='x':
            targets += [(counter, int(item))]
    time_, step_ = targets[0]
    for delta, period in targets[1:]:
        for time_ in count(time_, step_):
            if (time_ + delta) % period == 0:
                break
        step_ = lcm(step_, period)
    return time_

def test1():
    assert run_part1('./day13-test.input') == 295
    assert run_part1('./day13.input') == 115

def test2():
    assert run_part2('2,3') == 2
    assert run_part2('17,x,13,19') == 3417
    assert run_part2('67,7,59,61') == 754018
    assert run_part2('67,x,7,59,61') == 779210
    assert run_part2('67,x,7,59,61') == 779210
    assert run_part2('67,7,x,59,61') == 1261476
    assert run_part2('1789,37,47,1889') == 1202161486
    assert run_part2('./day13-test.input') == 1068781
    assert run_part2('./day13.input') == 756261495958122

if __name__ == '__main__':
    print("advent of code: day13")
    print(f"part 1: {run_part1('./day13.input')}")
    print(f"part 2: {run_part2('./day13.input')}")
