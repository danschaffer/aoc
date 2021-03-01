#!/usr/bin/env python

class Day21:
    def __init__(self, infile):
        self.rules = {}
        self.start = '.#./..#/###'
        for line in open(infile).readlines():
            parts = line.split(' => ')
            key = parts[0].strip()
            value = parts[1].strip()
            for rots in range(4):
                for flips in range(2):
                    transformed = self.to_grid(key)
                    for _ in range(rots):
                        transformed = self.rot(transformed)
                    for _ in range(flips):
                        transformed = self.flip(transformed)
                    self.rules[self.to_str(transformed)] = value

    def to_grid(self, s):
        return list(map(list, s.split("/")))

    # rot 90 deg
    def rot(self, grid):
        n = len(grid)
        o = [[None]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                o[i][j] = grid[~j][i]
        return o

    def flip(self, grid):
        return list(map(reversed, grid))

    def to_str(self, s):
        return "/".join("".join(x) for x in s)

    def count(self, s):
        return sum([1 for ch in self.to_str(s) if ch == '#'])

    def iteration(self, grid):
        length = len(grid)
        if length % 2 == 0:
            newlength = length // 2 * 3
            split = 2
            newsplit = 3
        else:
            newlength = length
            newlength = length // 3 * 4
            split = 3
            newsplit = 4
        out = [[None]*newlength for _ in range(newlength)]
        for i in range(0, length // split):
            for j in range(0, length // split):
                si = i * split
                sj = j * split
                g = [row[sj:sj+split] for row in grid[si:si+split]]
                s = self.to_str(g)
                transf = self.to_grid(self.rules[s])

                ei = i * newsplit
                ej = j * newsplit
                for a in range(newsplit):
                    for b in range(newsplit):
                        out[ei+a][ej+b] = transf[a][b]
        return out
    def run(self, iterations=5):
        grid = self.to_grid(self.start)
        for _ in range(iterations):
            grid = self.iteration(grid)
        return self.count(grid)

def test1():
    assert Day21('./day21-test.input').run(2) == 12
    assert Day21('./day21.input').run(5) == 110
    assert Day21('./day21.input').run(18) == 1277716

if __name__ == '__main__':
    print("advent of code: day21")
    print(f"part 1: {Day21('./day21.input').run(5)}")
    print(f"part 2: {Day21('./day21.input').run(18)}")
