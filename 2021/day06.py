#!/usr/bin/env python3

class Day06:
    def __init__(self, file):
        self.data = {}
        for number in open(file).read().strip().split(','):
            self.data[int(number)] = self.data.get(int(number), 0) + 1

    def run(self, days=80):
        for day in range(days):
            data0 = {}
            for key in sorted(self.data):
                if key == 0:
                    data0[8] = self.data[key]
                    data0[6] = self.data[key]
                else:
                    data0[key-1] = self.data[key] + data0.get(key-1, 0)
            self.data = data0
        return sum([self.data[n] for n in self.data])
                
    def run_part2(self):
        return -1

def test1():
    test_day06 = Day06('./day06-test.input')
    assert test_day06.run(days=80) == 5934
    test_day06 = Day06('./day06-test.input')
    assert test_day06.run(days=256) == 26984457539

def test2():
    test_day06 = Day06('./day06.input')
    assert test_day06.run(days=80) == 360268
    test_day06 = Day06('./day06.input')
    assert test_day06.run(days=256) == 1632146183902

if __name__ == '__main__':
    print("advent of code: day06")
    day06 = Day06('./day06.input')
    print(f"part 1: {day06.run(days=80)}")
    day06 = Day06('./day06.input')
    print(f"part 2: {day06.run(days=256)}")
