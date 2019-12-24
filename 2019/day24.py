#!/usr/bin/env python

class Eris:
    def __init__(self, input):
        self.input = input
        self.data = []
        self.time = 0
        self.load(input)

    def load(self, input):
        data = {}
        input = input.strip()
        y = 0
        for line in input.strip().split('\n'):
            x = 0
            for item in list(line):
                if item == '.':
                    data[(x,y)] = 0
                else:
                    data[(x,y)] = 1
                x += 1
            y += 1
        self.data += [data]

    def neighbors(self, x, y, data):
        count = 0
        if (x - 1, y) in data and data[(x-1,y)] == 1:
            count += 1
        if (x + 1, y) in data and data[(x+1,y)] == 1:
            count += 1
        if (x, y - 1) in data and data[(x,y-1)] == 1:
            count += 1
        if (x, y + 1) in data and data[(x,y+1)] == 1:
            count += 1
        return count

    def tick(self):
        data0 = self.data[-1]
        data1 = {}
        for y in range(5):
            for x in range(5):
                if data0[(x,y)] == 1:
                    if self.neighbors(x,y, data0) in [1]:
                        data1[(x,y)] = 1
                    else:
                        data1[(x,y)] = 0
                else:
                    if self.neighbors(x,y, data0) in [1, 2]:
                        data1[(x,y)] = 1
                    else:
                        data1[(x,y)] = 0
        return data1

    def get_biodiversity(self, data):
        count = 0
        for y in range(5):
            for x in range(5):
                if data[(x,y)] == 1:
                    count += 2 ** (y * 5 + x)
        return count

    def get_repeat(self):
        while (True):
            data0 = self.tick()
            if data0 in self.data:
                break
            self.data += [data0]
        return data0

    def tostring(self, data):
        result = ""
        for y in range(5):
            for x in range(5):
                if data[(x,y)] == 1:
                    result += '#'
                else:
                    result += '.'
            result += '\n'
        return result

def test1():
    eris = Eris("""
....#
#..#.
#..##
..#..
#....
""")
    data1 = eris.tick()
    assert eris.tostring(data1).strip() == """#..#.
####.
###.#
##.##
.##..
    """.strip()
    data0 = eris.get_repeat()
    print(eris.tostring(data0))
    assert eris.get_biodiversity(data0) == 2129920


if __name__ == '__main__':
    data = """
###.#
..#..
#..#.
#....
.#.#.
"""
    eris = Eris(data)
    result = eris.get_biodiversity(eris.get_repeat())
    print(f"part 1: {result}")
