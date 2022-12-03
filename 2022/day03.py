#!/usr/bin/env python3

class Day03:
    def __init__(self, file):
        self.file = file

    @staticmethod
    def get_score(ch):
        if ord(ch) >= ord('a'):
            return ord(ch) - ord('a') + 1
        else:
            return ord(ch) - ord('A') + 27

    def run_part1(self):
        answer = 0
        for line in open(self.file).readlines():
            line = line.strip()
            s1 = line[0:len(line)//2]
            s2 = line[len(line)//2:]
            for ch in set(s1).intersection(s2):
                answer += self.get_score(ch)
        return answer

    def run_part2(self):
        answer = 0
        lines = []
        for line in open(self.file).readlines():
            lines.append(line.strip())
        for ct in range(len(lines)//3):
            line1 = lines[ct*3 + 0]
            line2 = lines[ct*3 + 1]
            line3 = lines[ct*3 + 2]
            diffs = set(line1).intersection(line2).intersection(line3)
            for ch in diffs:
                answer += self.get_score(ch)
        return answer

def test1():
    test_day03 = Day03('./day03-test.input')
    assert test_day03.run_part1() == 157
    assert test_day03.run_part2() == 70

def test2():
    test_day03 = Day03('./day03.input')
    assert test_day03.run_part1() == 7967
    assert test_day03.run_part2() == 2716

if __name__ == '__main__':
    print("advent of code: day03")
    day03 = Day03('./day03.input')
    print(f"part 1: {day03.run_part1()}")
    print(f"part 2: {day03.run_part2()}")
