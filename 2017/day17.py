#!/usr/bin/env python
import time
from collections import deque

def day17(steps=3,times=2017):
    deq = deque([0])
    for n in range(1,times+1):
        deq.rotate(-1*steps-1)
        deq.appendleft(n)
    deq.popleft()
    return deq.popleft()

def day17_p2(steps=312):
    deq = deque([0])
    for n in range(1,50000001):
        deq.rotate(-1*steps-1)
        deq.appendleft(n)
    return deq[deq.index(0)+1]

def test1():
    assert day17(steps=3) == 638
    assert day17(steps=312) == 772

if __name__ == '__main__':
    print('advent of code: day 17')
    print(f"part 1: {day17(steps=312)}")
    start = time.time()
    print(f"part 2: {day17_p2(steps=312)} {round(time.time()-start, 1)}s")

