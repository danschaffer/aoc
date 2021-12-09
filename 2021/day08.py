#!/usr/bin/env python3

class Day08:
    def __init__(self, file):
        self.file = file

    def run_part1(self):
        answer = 0
        for line in open(self.file).readlines():
            _, output = line.split('|')
            answer += sum([1 for digit in output.split() if len(digit) in [2, 4, 3, 7]])
        return answer

    def matches(self, s1, s2):
        return sum([1 for s in s2 if s in s1])

    def run_part2(self):
        answer = 0
        for line in open(self.file).readlines():
            seeds, output = line.split('|')
            seeds = seeds.split()
            output = output.split()
            numbers = {}
            sorted_seeds = sorted(seeds, key=lambda x: len(x))
            sorted_output = [''.join(sorted(s)) for s in output]
            sorted_seeds = [''.join(sorted(s)) for s in sorted_seeds]
            numbers[1] = sorted_seeds[0]
            numbers[7] = sorted_seeds[1]
            numbers[4] = sorted_seeds[2]
            numbers[8] = sorted_seeds[9]
            if self.matches(sorted_seeds[3],sorted_seeds[0]) == 2:
                numbers[3] = sorted_seeds[3]
                if self.matches(sorted_seeds[4], sorted_seeds[2]) == 2:
                    numbers[2] = sorted_seeds[4]
                    numbers[5] = sorted_seeds[5]
                else:
                    numbers[2] = sorted_seeds[5]
                    numbers[5] = sorted_seeds[4]
            elif self.matches(sorted_seeds[4],sorted_seeds[0]) == 2:
                numbers[3] = sorted_seeds[4]
                if self.matches(sorted_seeds[3], sorted_seeds[2]) == 2:
                    numbers[2] = sorted_seeds[3]
                    numbers[5] = sorted_seeds[5]
                else:
                    numbers[2] = sorted_seeds[5]
                    numbers[5] = sorted_seeds[3]
            else:
                numbers[3] = sorted_seeds[5]
                if self.matches(sorted_seeds[3], sorted_seeds[2]) == 2:
                    numbers[2] = sorted_seeds[3]
                    numbers[5] = sorted_seeds[4]
                else:
                    numbers[2] = sorted_seeds[4]
                    numbers[5] = sorted_seeds[3]

            if self.matches(sorted_seeds[6], sorted_seeds[0]) != 2:
                numbers[6] = sorted_seeds[6]
                if self.matches(sorted_seeds[7], numbers[5]) == 5:
                    numbers[9] = sorted_seeds[7]
                    numbers[0] = sorted_seeds[8]
                else:
                    numbers[9] = sorted_seeds[8]
                    numbers[0] = sorted_seeds[7]
            elif self.matches(sorted_seeds[7], sorted_seeds[0]) != 2:
                numbers[6] = sorted_seeds[7]
                if self.matches(sorted_seeds[6], numbers[5]) == 5:
                    numbers[9] = sorted_seeds[6]
                    numbers[0] = sorted_seeds[8]
                else:
                    numbers[9] = sorted_seeds[8]
                    numbers[0] = sorted_seeds[6]
            else:
                numbers[6] = sorted_seeds[8]
                if self.matches(sorted_seeds[7], numbers[5]) == 5:
                    numbers[9] = sorted_seeds[7]
                    numbers[0] = sorted_seeds[6]
                else:
                    numbers[9] = sorted_seeds[6]
                    numbers[0] = sorted_seeds[7]
            number_key = {}
            for i in range(10):
                number_key[numbers[i]] = i
            number = 0
            for n in range(4):
                number += number_key[sorted_output[n]] * 10**(3-n)
            answer += number
        return answer

def test1():
    test_day08 = Day08('./day08-test.input')
    assert test_day08.run_part1() == 26
    assert test_day08.run_part2() == 61229

def test2():
    test_day08 = Day08('./day08.input')
    assert test_day08.run_part1() == 514
    assert test_day08.run_part2() == 1012272

if __name__ == '__main__':
    print("advent of code: day08")
    day08 = Day08('./day08.input')
    print(f"part 1: {day08.run_part1()}")
    print(f"part 2: {day08.run_part2()}")
