#!/usr/bin/env python
import copy
import heapq
import itertools
import time

class KeyDict(object):
    def __init__(self, key, moves, dct):
        self.key = key
        self.moves = moves
        self.dct = dct

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return '{0.__class__.__name__}(key={0.key}, moves={0.moves}, dct={0.dct})'.format(self)

def load(file):
    data = {}
    max_x = 0
    for line in open(file).read().strip().split('\n')[2:]:
        parts = line.split()
        names = parts[0].split('-')
        name = (int(names[1][1:]), int(names[2][1:]))
        max_x = max(max_x, name[0])
        size = int(parts[1][:-1])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        data[name] = (size,used,avail,False)
    data[(max_x,0)] = (data[(max_x,0)][0],data[(max_x,0)][1],data[(max_x,0)][2],True)
    return data

def solve1(file):
    solutions = 0
    data = load(file)
    for pair1, pair2 in itertools.permutations(data, 2):
        if data[pair1][1] == 0:
            continue
        if data[pair2][2] > data[pair1][1]:
            solutions += 1
    return solutions

def get_hole(data):
    for (x,y) in data:
        if data[(x,y)][1] == 0:
            return (x,y)

def get_moves(loc,data):
    (x,y) = loc
    moves= []
    if (x-1,y) in data and data[(x-1,y)][2]>0:
        moves.append((x-1,y))
    if (x+1,y) in data and data[(x+1,y)][2]>0:
        moves.append((x+1,y))
    if (x,y-1) in data and data[(x,y-1)][2]>0:
        moves.append((x,y-1))
    if (x,y+1) in data and data[(x,y+1)][2]>0:
        moves.append((x,y+1))
    return moves

def solve2(file):
    data = load(file)
    max_x = 0
    max_y = 0
    hole = None
    for (x,y) in data:
        max_x = max(x,max_x)
        max_y = max(y,max_y)
        if data[(x,y)][1] == 0:
            hole=(x,y)

    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            value = data[(x,y)][1]
            if x == 0 and y == 0:
                line += 'O'
            elif x == max_x and y == 0:
                line += 'G'
            elif value == 0:
                line += '_'
            elif (x-1,y) in data and value > data[(x-1,y)][0] or (x+1,y) in data and value > data[(x+1,y)][0] or (x,y-1) in data and value > data[(x,y-1)][0] or (x,y+1) in data and value > data[(x,y+1)][0]:
                line += '#'
            else:
                line += '.'
#        print(line)

    dest = (max_x-1,0)
    dist = abs(hole[0] - max_x - 1) + abs(hole[1])
    frontier = []
    heapq.heappush(frontier,KeyDict(dist, [], data))
    visited = [hole]
    while frontier:
        keydict = heapq.heappop(frontier)
        data = keydict.dct
        moves = keydict.moves
        hole = get_hole(data)
        for move in get_moves(hole,data):
            if move in visited:
                continue
            visited.append(move)
            data0 = copy.deepcopy(data)
            data0[hole] = (data[hole][0],data[move][1],data[hole][0]-data[move][1],False)
            data0[move] = (data[move][0],0,data[move][0],True)
            moves0 = moves[:] + [move]
            dist = abs(hole[0] - max_x - 1) + abs(hole[1])
            if dist == 0:
                break
            heapq.heappush(frontier,KeyDict(dist, moves0, data0))
    return len(moves) + 5*(max_x-1)



def test1():
    assert solve1('./day22-test.input') == 5
    assert solve1('./day22.input') == 1038
    assert solve2('./day22-test.input') == 7
    assert solve2('./day22.input') == 252

if __name__ == '__main__':
    print("advent of code day 22")
    print(f"part 1: {solve1('./day22.input')}")
    start = time.time()
    print(f"part 2: {solve2('./day22.input')} {round(time.time()-start,1)}s")
