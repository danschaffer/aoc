#!/usr/bin/env python3
import time
class Day13:
    def __init__(self, file):
        self.data = {}
        for line in open(file).read().strip().split('\n'):
            parts = line.split(':')
            depth = int(parts[0].strip())
            range = int(parts[1].strip())
            self.data[depth] = range

    def is_caught(self, n , delay=0):
        return n in self.data.keys() and (n + delay) % (2 * (self.data[n] - 1)) == 0

    def get_severity(self):
        total = 0
        for n in range(max(self.data)+1):
            if self.is_caught(n):
                total += n * self.data[n]
        return total

    def get_delay(self):
        delay = 0
        passed = False
        while not passed:
            for n in range(max(self.data)+1):
                if self.is_caught(n, delay):
                    delay += 1
                    break
                if n == max(self.data):
                    passed=True
        return delay

def test1():
    test_day13 = Day13('./day13-test.input')
    assert test_day13.get_severity() == 24
    assert test_day13.get_delay() == 10
    day13 = Day13('./day13.input')
    assert day13.get_severity() == 1528
    assert day13.get_severity() == 1528
    

if __name__ == '__main__':
    print("advent of code: day13")
    day13 = Day13('./day13.input')
    print(f"part 1: {day13.get_severity()}")
    start = time.time()
    print(f"part 2: {day13.get_delay()} {round(time.time()-start, 1)}s")
