#!/usr/bin/env python3

class Day8:
    def __init__(self, width=50, height=6):
        self.width = width
        self.height = height
        self.data = {}
        for x in range(self.width):
            for y in range(self.height):
                self.data[(x,y)] = '.'

    def load(self, file):
        for line in open(file).read().strip().split('\n'):
            tokens = line.split()
            if tokens[0] == 'rect':
                x, y = tokens[1].split('x')
                for x0 in range(int(x)):
                    for y0 in range(int(y)):
                        self.data[(x0,y0)] = '#'
            elif tokens[0] == 'rotate' and tokens[1] == 'column':
                col = int(tokens[2].split('=')[1])
                by = int(tokens[4])
                newdata = self.data.copy()
                for h in range(self.height):
                    newdata[(col,(h+by)%self.height)] = self.data[(col,h)]
                self.data = newdata
            elif tokens[0] == 'rotate' and tokens[1] == 'row':
                row = int(tokens[2].split('=')[1])
                by = int(tokens[4])
                newdata = self.data.copy()
                for w in range(self.width):
                    newdata[((w+by)%self.width),row] = self.data[(w,row)]
                self.data = newdata

    def print_grid(self):
        for row in range(self.height):
            line = ''
            for column in range(self.width):
                line += self.data[(column,row)]
            print(line)

    def get_lit(self):
        return sum([1 for point in self.data if self.data[point] == '#'])

    def run_part1(self):
        return self.get_lit()

def test1():
    test_day8 = Day8(7,3)
    test_day8.load('./day08-test.input')
    assert test_day8.run_part1() == 6
    test_day8 = Day8()
    test_day8.load('./day08.input')
    assert test_day8.run_part1() == 128
    

if __name__ == '__main__':
    print("advent of code: day8")
    day8 = Day8()
    day8.load('./day08.input')
    print(f"part 1: {day8.run_part1()}")
    print(f"part 2:")
    day8.print_grid()  # EOARGPHYAO
