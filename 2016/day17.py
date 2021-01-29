#!/usr/bin/env python
import hashlib
import heapq

def day17(passcode, part2=False):
    longest = 0
    frontier = []
    heapq.heappush(frontier, (0, ('',0,0)))
    while len(frontier):
        movelen, (moves, x, y) = heapq.heappop(frontier)
        if x == 3 and y == 3:
            if not part2:
                return moves
            else:
                longest = max(longest,movelen)
                continue
        hash = hashlib.md5(bytes(passcode + moves, 'utf-8')).hexdigest()
        if y > 0 and hash[0] in 'bcdef':
            heapq.heappush(frontier, (movelen+1, (moves+'U',x,y-1)))
        if y < 3 and hash[1] in 'bcdef':
            heapq.heappush(frontier, (movelen+1, (moves+'D',x,y+1)))
        if x > 0 and hash[2] in 'bcdef':
            heapq.heappush(frontier, (movelen+1, (moves+'L',x-1,y)))
        if x < 3 and hash[3] in 'bcdef':
            heapq.heappush(frontier, (movelen+1, (moves+'R',x+1,y)))
    return longest

def test1():
    assert day17('ihgpwlah') == 'DDRRRD'
    assert day17('kglvqrro') == 'DDUDRLRRUDRD'
    assert day17('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    assert day17('mmsxrhfx') == 'RLDUDRDDRR'

    assert day17('ihgpwlah', part2=True) == 370
    assert day17('kglvqrro', part2=True) == 492
    assert day17('ulqzkmiv', part2=True) == 830
    assert day17('mmsxrhfx', part2=True) == 590

if __name__ == '__main__':
    print("advent of code: day17")
    print(f"part1: {day17('mmsxrhfx')}")
    print(f"part2: {day17('mmsxrhfx', part2=True)}")
