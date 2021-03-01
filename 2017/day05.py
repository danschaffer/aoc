#!/usr/bin/env python3
import time
def day5_part1(file):
    data=[int(line) for line in open(file).read().strip().split('\n')]
    pointer = 0
    counter = 0
    while pointer >= 0 and pointer < len(data):
        next = pointer + data[pointer]
        data[pointer] += 1
        pointer = next
        counter += 1
    return counter

def day5_part2(file):
    data=[int(line) for line in open(file).read().strip().split('\n')]
    pointer = 0
    counter = 0
    while pointer >= 0 and pointer < len(data):
        next = pointer + data[pointer]
        if data[pointer] >= 3:
            data[pointer] -= 1
        else:
            data[pointer] += 1
        pointer = next
        counter += 1
    return counter

def test1():
    assert day5_part1('./day05-test.input') == 5
    assert day5_part2('./day05-test.input') == 10

if __name__ == '__main__':
    print(f"advent of code: day05")
    print(f"part 1: {day5_part1('./day05.input')}")
    start = time.time()
    print(f"part 2: {day5_part2('./day05.input')} {round(time.time()-start,1)}s")
