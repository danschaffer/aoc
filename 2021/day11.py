#!/usr/bin/env python3

class Day11:
    def __init__(self, file):
        self.data = {}
        for y, line in enumerate(open(file).readlines()):
            for x, char in enumerate(line.strip()):
                self.data[(x,y)] = int(char)
                self.maxx = len(line)
        self.maxy = y+1

    def step(self):
        flash_count = 0
        flashq = []
        for item in self.data:
            self.data[item] += 1
            if self.data[item] > 9:
                flashq.append(item)
                flash_count += 1
        while len(flashq):
            x,y = flashq.pop()
            self.data[(x,y)] = 0
            for neighbor in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                if neighbor in self.data and self.data[neighbor] > 0:
                    self.data[neighbor] += 1
                if neighbor in self.data and self.data[neighbor] > 9 and neighbor not in flashq:
                    flash_count += 1
                    flashq.append(neighbor)
        return flash_count

    def print_board(self):
        for y in range(self.maxy):
            line = ''
            for x in range(self.maxx):
                line += str(self.data[(x,y)])
            print(line)

    def run_part1(self):
        return sum([self.step() for _ in range(100)])

    def run_part2(self):
        counter = 0
        while True:
            counter += 1
            result = self.step()
            if result == 100:
                return counter

def test1():
    assert Day11('./day11-test.input').run_part1() == 1656
    assert Day11('./day11-test.input').run_part2() == 195

def test2():
    assert Day11('./day11.input').run_part1() == 1601
    assert Day11('./day11.input').run_part2() == 368

if __name__ == '__main__':
    print("advent of code: day11")
    print(f"part 1: {Day11('./day11.input').run_part1()}")
    print(f"part 2: {Day11('./day11.input').run_part2()}")
