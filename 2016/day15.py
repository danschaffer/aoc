#!/usr/bin/env python3

class Day15:
    def __init__(self, file):
        self.data = {}
        for line in open(file).read().strip().split('\n'):
            parts = line.split()
            self.data[int(parts[1][1:])] = (int(parts[3]), int(parts[11][0:-1]))

    def run(self):
        counter = -1
        while True:
            counter += 1
            solved = True
            for key in self.data:
                if not solved:
                    break
                positions = self.data[key][0]
                initial = self.data[key][1]
                if (initial + key + counter) % positions != 0:
                    solved = False
                    break
            if solved:
                break
        return counter

def test1():
    test_day15 = Day15('./day15-test.input')
    assert test_day15.run() == 5

def test2():
    test_day15 = Day15('./day15.input')
    assert test_day15.run() == 317371
    test_day15.data[max(test_day15.data.keys()) + 1] = (11,0)
    assert test_day15.run() == 2080951

if __name__ == '__main__':
    print("advent of code: day15")
    day15 = Day15('./day15.input')
    print(f"part 1: {day15.run()}")
    day15.data[max(day15.data.keys()) + 1] = (11,0)
    print(f"part 2: {day15.run()}")
