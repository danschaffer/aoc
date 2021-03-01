#!/usr/bin/env python
import binascii
from collections import deque

def knot_hash(inputs, length=256):
    sizes = [ord(n) for n in inputs] + [17, 31, 73, 47, 23]
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

def knot_hash_binary(inputs):
    hash = knot_hash(inputs)
    result=bin(int(hash,16))[2:]
    while len(result) != 128:
        result = f"0{result}"
    return result

def get_grid(inputs):
    grid = []
    for n in range(128):
        grid.append(knot_hash_binary(f"{inputs}-{n}"))
    return grid

def count_grid(inputs):
    count = 0
    for line in get_grid(inputs):
        count += sum([1 for ch in line if ch == '1'])
    return count

def count_regions(inputs):
    data = []
    grids = get_grid(inputs)
    for row,line in enumerate(grids):
        for col, ch in enumerate(line):
            if ch == '1':
                data.append((col,row))
    regions = 0
    while data:
        frontier = []
        item = data[0]
        frontier.append(item)
        data.remove(item)
        region = []
        while frontier:
            item = frontier.pop()
            region.append(item)
            left = (item[0]-1,item[1])
            if left in data:
                data.remove(left)
                frontier.append(left)
            right = (item[0]+1,item[1])
            if right in data:
                data.remove(right)
                frontier.append(right)
            up = (item[0],item[1]-1)
            if up in data:
                data.remove(up)
                frontier.append(up)
            down = (item[0],item[1]+1)
            if down in data:
                data.remove(down)
                frontier.append(down)
        regions +=1
    return regions

def test1():
    assert (count_grid('flqrgnkx')) == 8108
    assert (count_regions('flqrgnkx')) == 1242

    assert (count_grid('uugsqrei')) == 8194
    assert (count_regions('uugsqrei')) == 1141

if __name__ == '__main__':
    print("advent of code day 14")
    print(f"part 1: {count_grid('uugsqrei')}")
    print(f"part 2: {count_regions('uugsqrei')}")
