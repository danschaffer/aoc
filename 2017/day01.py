#!/usr/bin/env python
import os
def day1(digits, part2=False):
    if os.path.exists(digits):
        digits=open(digits).read().strip()
    result = 0
    for index,item in enumerate(digits):
        if part2:
            other = digits[(index+len(digits)//2) % len(digits)]
        else:
            other = digits[index-1]
        if digits[index] == other:
            result += int(item)
    return result

def test1():
    assert(day1('1122')) == 3
    assert(day1('1111')) == 4
    assert(day1('1234')) == 0
    assert(day1('91212129')) == 9

if __name__ == '__main__':
    print('advent of code day1')
    print(f"part 1: {day1('day01.input')}")
    print(f"part 2: {day1('day01.input',part2=True)}")