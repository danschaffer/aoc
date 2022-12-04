#!/usr/bin/env python3
import sys
class Day04:
    def __init__(self, file):
        self.data = [line.strip() for line in open(file).readlines()]

    @staticmethod
    def parse_line(line):
        def parse_section(section):
            first, second = section.split('-')
            return set(range(int(first), int(second)+1))
        section1, section2 = line.split(',')
        return parse_section(section1), parse_section(section2)

    def run(self):
        answer1 = answer2 = 0
        for line in self.data:
            set1, set2 = Day04.parse_line(line)
            ilen = len(set1.intersection(set2))
            if ilen in [len(set1),len(set2)]:
                answer1 += 1
            if ilen:
                answer2 += 1
        return answer1, answer2

def test1():
    answer1, answer2 = Day04('./day04-test.input').run()
    assert answer1 == 2
    assert answer2 == 4

def test2():
    answer1, answer2 = Day04('./day04.input').run()
    assert answer1 == 305
    assert answer2 == 811

if __name__ == '__main__':
    print("advent of code: day04")
    file = './day04.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    answer1, answer2 = Day04(file).run()
    print(f"part 1: {answer1}")
    print(f"part 2: {answer2}")
