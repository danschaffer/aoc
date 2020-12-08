#!/usr/bin/env python3

class Day5:
    def __init__(self):
        self.lines = list()

    def load(self, file):
        self.lines = open(file).read().strip().split('\n')

    def calculate_binary(self, value):
        return int(value.replace('F','0').replace('B','1').replace('L','0').replace('R', '1'), 2)

    def calculate_seatid(self, value):
        return self.calculate_binary(value[0:7]) * 8 + self.calculate_binary(value[7:])

    def run_part1(self):
        return max([self.calculate_seatid(line) for line in self.lines])

    def run_part2(self):
        seats = sorted([self.calculate_seatid(line) for line in self.lines])
        for counter, seat in enumerate(seats):
            if counter and seat != seats[counter-1] + 1:
                return seat - 1

def test1():
    test_day5 = Day5()
    assert test_day5.calculate_binary('FBFBBFFRLR'[0:7]) == 44
    assert test_day5.calculate_binary('FBFBBFFRLR'[7:]) == 5
    assert test_day5.calculate_seatid('FBFBBFFRLR') == 357
    test_day5.load('./day5.input')
    assert test_day5.run_part1() == 888
    assert test_day5.run_part2() == 522

if __name__ == '__main__':
    print("advent of code: day5")
    day5 = Day5()
    day5.load('./day5.input')
    print(f"part 1: {day5.run_part1()}")
    print(f"part 2: {day5.run_part2()}")
