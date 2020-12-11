#!/usr/bin/env python3
class Day11:
    def __init__(self, file):
        self.data = {}
        lines = open(file).read().strip().split('\n')
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                if char == 'L':
                    self.data[(column, row)] = 0
        self.rowmax = len(lines)
        self.colmax = len(lines[0])

    def count(self):
        return sum([1 for key in self.data if self.data[key] == 1])

    def count_neighbors(self, point):
        column, row = point
        total = 0
        if (column - 1, row) in self.data and self.data[(column-1,row)] == 1:
            total += 1
        if (column + 1, row) in self.data and self.data[(column+1,row)] == 1:
            total += 1
        if (column, row-1) in self.data and self.data[(column,row-1)] == 1:
            total += 1
        if (column, row+1) in self.data and self.data[(column,row+1)] == 1:
            total += 1
        if (column - 1, row - 1) in self.data and self.data[(column-1,row-1)] == 1:
            total += 1
        if (column - 1, row + 1) in self.data and self.data[(column-1,row+1)] == 1:
            total += 1
        if (column + 1, row + 1) in self.data and self.data[(column+1,row+1)] == 1:
            total += 1
        if (column + 1, row - 1) in self.data and self.data[(column+1,row-1)] == 1:
            total += 1
        return total

    def count_neighbors2(self, point):
        column, row = point
        total = 0
        for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
            column1 = column + dx
            row1 = row + dy
            while 0 <= row1 < self.rowmax and 0 <= column1 < self.colmax and (column1, row1) not in self.data.keys():
                column1 += dx
                row1 += dy
            if (column1, row1) in self.data and self.data[(column1, row1)] == 1:
                total += 1
        return total


    def next(self):
        data1 = {}
        for point in self.data:
            data1[point] = self.data[point]
            neighbors = self.count_neighbors(point)
            if self.data[point] == 0 and neighbors == 0:
                data1[point] = 1
            elif neighbors >= 4:
                data1[point] = 0
        self.data = data1

    def next2(self):
        data1 = {}
        for point in self.data:
            data1[point] = self.data[point]
            neighbors = self.count_neighbors2(point)
            if self.data[point] == 0 and neighbors == 0:
                data1[point] = 1
            elif neighbors >= 5:
                data1[point] = 0
        self.data = data1

    def run_part1(self):
        last = -1
        while last != self.count():
            last = self.count()
            self.next()
        return self.count()

    def run_part2(self):
        last = -1
        while last != self.count():
            last = self.count()
            self.next2()
        return self.count()

def test1():
    test_day11a = Day11('./day11-test.input')
    assert test_day11a.run_part1() == 37
    test_day11b = Day11('./day11-test.input')
    assert test_day11b.run_part2() == 26

def test2():
    test_day11a = Day11('./day11.input')
    assert test_day11a.run_part1() == 2368
    test_day11b = Day11('./day11.input')
    assert test_day11b.run_part2() == 2124

if __name__ == '__main__':
    print("advent of code: day11")
    day11 = Day11('./day11.input')
    print(f"part 1: {day11.run_part1()}")
    day11b = Day11('./day11.input')
    print(f"part 2: {day11b.run_part2()}")
