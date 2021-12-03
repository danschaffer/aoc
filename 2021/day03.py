#!/usr/bin/env python3

class Day03:
    def __init__(self, file):
        self.lines = []
        self.data = []
        for line in open(file).readlines():
            self.length = len(line)
            self.lines.append(line)
            self.data.append(int(line,2))

    def run_part1(self):
        gamma = 0
        epsilon = 0
        for i in range(self.length):
            count = 0
            for j in range(len(self.data)):
                count += self.data[j] >> i & 1
            if count >= len(self.data) / 2:
                gamma = gamma | 1 << i
            else:
                epsilon = epsilon | 1 << i
        return gamma * epsilon

    def run_part2(self):
        oxygen = self.data[:]
        co2 = self.data[:]
        for i in range(self.length):
            count = 0
            oxygen2 = []
            i0 = self.length - i - 1
            for j in range(len(oxygen)):
                count += oxygen[j] >> i0 & 1
            if count >= len(oxygen) / 2:
                for j in range(len(oxygen)):
                    if oxygen[j] >> i0 & 1 == 1:
                        oxygen2.append(oxygen[j])
            else:
                for j in range(len(oxygen)):
                    if oxygen[j] >> i0 & 1 == 0:
                        oxygen2.append(oxygen[j])
            oxygen = oxygen2
            if len(oxygen) == 1:
                break
        for i in range(self.length):
            count = 0
            co22 = []
            i0 = self.length - i - 1
            for j in range(len(co2)):
                count += co2[j] >> i0 & 1
            if count >= len(co2) / 2:
                for j in range(len(co2)):
                    if co2[j] >> i0 & 1 == 0:
                        co22.append(co2[j])
            else:
                for j in range(len(co2)):
                    if co2[j] >> i0 & 1 == 1:
                        co22.append(co2[j])
            co2 = co22
            if len(co2) == 1:
                break
        return oxygen[0] * co2[0]

def test1():
    test_day03 = Day03('./day03-test.input')
    assert test_day03.run_part1() == 198
    assert test_day03.run_part2() == 230

def test2():
    test_day03 = Day03('./day03.input')
    assert test_day03.run_part1() == 2648450
    assert test_day03.run_part2() == 2845944

if __name__ == '__main__':
    print("advent of code: day03")
    day03 = Day03('./day03.input')
    print(f"part 1: {day03.run_part1()}")
    print(f"part 2: {day03.run_part2()}")
