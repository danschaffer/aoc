#!/usr/bin/env python3
import functools
import json
import sys
class Day13:
    def __init__(self, file):
        self.data =open(file).read()

    @staticmethod
    def compare(item1, item2):
        if type(item1) == list and type(item2) != list:
            item2 = [item2]
        if type(item2) == list and type(item1) != list:
            item1 = [item1]
        if type(item1) == list:
            result = 0
            for n in range(max(len(item1), len(item2))):
                if len(item1) == n:
                    return -1
                if len(item2) == n:
                    return 1
                result += Day13.compare(item1[n], item2[n])
                if result != 0:
                    return result
        else:
            if item1 == item2:
                return 0
            elif item1 < item2:
                return -1
            else:
                return 1
        return result

    def run_part1(self):
        answer = 0
        for n, section in enumerate(self.data.split('\n\n')):
            line1, line2 = section.split('\n')
            line1 = json.loads(line1)
            line2 = json.loads(line2)
            if Day13.compare(line1, line2) < 0:
                answer += n + 1
        return answer

    def run_part2(self):
        data = self.data + '\n[[2]]\n[[6]]'
        items = [json.loads(item) for item in data.split('\n') if item != '']
        sorted_items = sorted(items, key=functools.cmp_to_key(Day13.compare))
        return (sorted_items.index([[2]])+1) * (sorted_items.index([[6]])+1)

def test1():
    test_day13 = Day13('./day13-test.input')
    assert test_day13.run_part1() == 13
    assert test_day13.run_part2() == 140

def test2():
    test_day13 = Day13('./day13.input')
    assert test_day13.run_part1() == 5684
    assert test_day13.run_part2() == 22932

if __name__ == '__main__':
    print("advent of code: day13")
    file = './day13.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day13 = Day13(file)
    print(f"part 1: {day13.run_part1()}")
    print(f"part 2: {day13.run_part2()}")
