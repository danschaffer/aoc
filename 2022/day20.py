#!/usr/bin/env python3
import sys
class Day20:
    def __init__(self, file):
        self.numbers = [int(line.strip()) for line in open(file).readlines()]

    def run_part1(self):
        newlist = self.numbers[:]
        origlist = self.numbers[:]
        for number in origlist:
            fnd = newlist.index(number)
            print(f"{number} {newlist} {fnd+number}")
            insert_pt = (fnd + number) % len(newlist)
            newlist.remove(number)
            newlist.insert(insert_pt, number)
        print(f"{number} {newlist}")
        return newlist[1000%len(newlist)] + newlist[2000%len(newlist)] + newlist[3000%len(newlist)]

    def run_part2(self):
        return -1

#def test1():
#    test_day20 = Day20('./day20-test.input')
#    assert test_day20.run_part1() == 3
#    assert test_day20.run_part2() == -1

#def test2():
#    test_day20 = Day20('./day20.input')
#    assert test_day20.run_part1() == -1
#    assert test_day20.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day20")
    file = './day20.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day20 = Day20(file)
    print(f"part 1: {day20.run_part1()}")
    print(f"part 2: {day20.run_part2()}")
