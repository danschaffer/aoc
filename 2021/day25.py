#!/usr/bin/env python3

class Day25:
    def __init__(self, file):
        self.data = {}
        self.downs = set()
        self.rights = set()
        for y,line in enumerate([line.strip() for line in open(file).readlines()]):
            for x, ch in enumerate(line):
                self.data[(x,y)] = ch
                if ch == 'v':
                    self.downs.add((x,y))
                elif ch == '>':
                    self.rights.add((x,y))

    def print_map(self):
        maxx,maxy = max(self.data)
        for y in range(0,maxy+1):
            line = ''
            for x in range(0, maxx+1):
                line += self.data[(x,y)]
            print(line)

    def run(self):
        rounds = 0
        rights = self.rights
        downs = self.downs
        maxx, maxy = max(self.data)
        while True:
#            print(rounds)
#            self.print_map()
            madeMove = False
            data1 = {}
            rights1 = set()
            for orig in rights:
                dest = (orig[0]+1,orig[1])
                if dest[0] > maxx:
                    dest = (0, dest[1])
                if dest not in rights and dest not in downs:
                    rights1.add(dest)
                    madeMove = True
                else:
                    rights1.add(orig)
            rights = rights1
            downs1 = set()
            for orig in downs:
                dest = (orig[0],orig[1]+1)
                if dest[1] > maxy:
                    dest = (dest[0], 0)
                if dest not in rights and dest not in downs:
                    downs1.add(dest)
                    madeMove = True
                else:
                    downs1.add(orig)
            downs = downs1
            self.data = {}
            for x in range(maxx+1):
                for y in range(maxy+1):
                    if (x,y) in rights:
                        self.data[(x,y)] = '>'
                    elif (x,y) in downs:
                        self.data[(x,y)] = 'v'
                    else:
                        self.data[(x,y)] = '.'
            rounds += 1
            if madeMove == False:
                break
        return rounds

def test1():
    test_day25 = Day25('./day25-test.input')
    assert test_day25.run() == 58

def test2():
    test_day25 = Day25('./day25.input')
    assert test_day25.run() ==498

if __name__ == '__main__':
    print("advent of code: day25")
    day25 = Day25('./day25.input')
    print(f"part 1: {day25.run()}")
