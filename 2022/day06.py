#!/usr/bin/env python3
import os
import sys
class Day06:
    def __init__(self, file):
        self.data = file
        if os.path.exists(file):
            self.data = open(file).read().strip()

    def run_part1(self):
        for i in range(len(self.data)-4):
            if len(set(self.data[i:i+4])) == 4:
                return i+4

    def run_part2(self):
        for i in range(len(self.data)-14):
            if len(set(self.data[i:i+14])) == 14:
                return i+14

def test1():
    for test,answer1, answer2 in [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb',7,19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz',5,23),
        ('nppdvjthqldpwncqszvftbrmjlhg',6,23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',10,29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',11,26),
    ]:
        assert Day06(test).run_part1() == answer1
        assert Day06(test).run_part2() == answer2

def test2():
    test_day06 = Day06('./day06.input')
    assert test_day06.run_part1() == 1282
    assert test_day06.run_part2() == 3513

if __name__ == '__main__':
    print("advent of code: day06")
    file = './day06.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day06 = Day06(file)
    print(f"part 1: {day06.run_part1()}")
    print(f"part 2: {day06.run_part2()}")
