#!/usr/bin/env python
import math
import time
def white_elephant1(number):
    data = [1 for _ in range(number)]
    target = active = 0
    while data[active] != number:
        target = (active + 1) % number
        while data[target] == 0:
            target = (target+1) % number
        data[active] += data[target]
        data[target] = 0
        active = target
        active = (active + 1) % number
        while data[active] == 0:
            active = (active + 1) % number
    return active+1

def white_elephant2(number):
    data = [n+1 for n in range(number)]
    active = 1
    while len(data) > 1:
        target = data[(data.index(active) + len(data) // 2) % len(data)]
        print(f"{active} {target} {len(data)}")
        data.remove(target)
        nactive = data.index(active) + 1
        if nactive == len(data):
            active = data[0]
        else:
            active = data[nactive]
    return active

def white_elephant3(number):
    l = math.floor(math.log(number, 3))
    k = number - 3**l
    if k == 0:
        return number
    if l == 1 or k <= (3**l):
        return k
    else:
        return 3**l + 2*(k-3**l)

def test1():
    assert white_elephant1(5) == 3
    assert white_elephant1(3018458) == 1842613
    assert white_elephant2(5) == 2
    assert white_elephant3(5) == 2
    assert white_elephant3(3018458) == 1424135

if __name__ == '__main__':
    print("advent of code day 19")
    start = time.time()
    print(f"part 1: {white_elephant1(3018458)} {round(time.time()-start, 1)}s")
    print(f"part 2: {white_elephant3(3018458)}")
