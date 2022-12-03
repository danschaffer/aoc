#!/usr/bin/env python3
import sys
class Day03:
    def __init__(self, file):
        self.file = file

    @staticmethod
    def get_score(chs):
        answer = 0
        for ch in chs:
            if ord(ch) >= ord('a'):
                answer += ord(ch) - ord('a') + 1
            else:
                answer += ord(ch) - ord('A') + 27
        return answer

    def run(self):
        answer1 = answer2 = 0
        lines2 = []
        for line in open(self.file).readlines():
            line = line.strip()
            lines2.append(line)
            if len(lines2) == 3:
                diffs = set(lines2[0]).intersection(lines2[1]).intersection(lines2[2])
                answer2 += Day03.get_score(diffs)
                lines2 = []
            answer1 += Day03.get_score(set(line[0:len(line)//2]).intersection(line[len(line)//2:]))
        return answer1, answer2

def test1():
    answer1, answer2 = Day03('./day03-test.input').run()
    assert answer1 == 157
    assert answer2 == 70

def test2():
    answer1, answer2 = Day03('./day03.input').run()
    assert answer1 == 7967
    assert answer2 == 2716

if __name__ == '__main__':
    print("advent of code: day03")
    file = './day03.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    answer1, answer2 = Day03(file).run()
    print(f"part 1: {answer1}")
    print(f"part 2: {answer2}")
