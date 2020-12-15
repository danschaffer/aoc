#!/usr/bin/env python3
import os
def run_part1(numbers, rounds):
    if os.path.exists(numbers):
        numbers = [int(number) for number in open(numbers).read().strip().split(',')]
    else:
        numbers = [int(number) for number in numbers.split(',')]
    while len(numbers) < rounds:
        last = numbers[-1]
        try:
            match = numbers[::-1][1:].index(last)
        except:
            match = -1
        numbers += [(match+1)]
    return numbers[-1]

def run_part2():
    return -1

def test1():
    assert run_part1('0,3,6', 4) == 0
    assert run_part1('0,3,6', 5) == 3
    assert run_part1('0,3,6', 6) == 3
    assert run_part1('0,3,6', 7) == 1
    assert run_part1('0,3,6', 8) == 0
    assert run_part1('0,3,6', 9) == 4
    assert run_part1('0,3,6', 10) == 0
    assert run_part1('1,3,2', 2020) == 1
    assert run_part1('./day15.input', 2020) == 1025

if __name__ == '__main__':
    print("advent of code: day15")
    print(f"part 1: {run_part1('./day15.input', 2020)}")
