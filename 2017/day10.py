#!/usr/bin/env python
from collections import deque

def part1(sizes, length=256):
    sizes = [int(n) for n in sizes.split(',')]
    queue = deque(list(range(length)))
    pos = 0
    skip = 0
    for size in sizes:
        queue.rotate(-pos)
        queue_list = list(queue)
        queue_list[:size] = reversed(queue_list[:size])
        queue = deque(queue_list)
        queue.rotate(pos)
        pos = (pos + size + skip) % length
        skip += 1
    return queue[0] * queue[1]

def part2(sizes, length=256):
    sizes = [ord(n) for n in sizes] + [17, 31, 73, 47, 23]
    queue = deque(list(range(length)))
    pos = 0
    skip = 0
    for _ in range(64):
        for size in sizes:
            queue.rotate(-pos)
            queue_list = list(queue)
            queue_list[:size] = reversed(queue_list[:size])
            queue = deque(queue_list)
            queue.rotate(pos)
            pos = (pos + size + skip) % length
            skip += 1
    result = ''
    for block in range(0, length, 16):
        hash = 0
        for n in list(queue)[block : block+16]:
            hash = hash ^ n
        hex0 = hex(hash)[2:]
        if len(hex0) == 1:
            hex0 = '0' + hex0
        result += hex0
    return result

def test1():
    assert part1('3, 4, 1, 5', 5) == 12

if __name__ == '__main__':
    print('advent of code day 10')
    print(f"part 1: {part1('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70')}")
    print(f"part 2: {part2('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70')}")