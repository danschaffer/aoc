#!/usr/bin/env python
import time
class Day18:
    def __init__(self, tiles, rows):
        self.tiles = tiles
        self.rows = rows

    def next_tile(self, row, index):
        if index < 1:
            test = '.' + row[0:2]
        elif index == len(row) - 1:
            test = row[index-1] + '..'
        else:
            test = row[index-1:index+2]
        if test in ['^^.','.^^','^..','..^']:
            return '^'
        else:
            return '.'

    def next_row(self, row):
        return ''.join([self.next_tile(row, index) for index in range(len(row))])

    def run(self):
        total = 0
        tiles = self.tiles
        for ch in tiles:
            if ch == '.':
                total += 1
        for _ in range(self.rows-1):
            tiles = self.next_row(tiles)
            for ch in tiles:
                if ch == '.':
                    total += 1
        return total

def test1():
    assert Day18('..^^.', 3).run() == 6
    assert Day18('.^^.^.^^^^', 10).run() == 38

def test2():
    tiles = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
    assert Day18(tiles, 40).run() == 1963
    assert Day18(tiles, 400000).run() == 20009568

if __name__ == '__main__':
    print("advent of code day 18")
    tiles = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
    print(f"part 1: {Day18(tiles,40).run()}")
    start = time.time()
    print(f"part 2: {Day18(tiles,400000).run()} {round(time.time()-start,1)}s")
 