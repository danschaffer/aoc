#!/usr/bin/env python
import itertools
def day2p1(file):
    result = 0
    for line in open(file).read().strip().split('\n'):
        numbers=[int(number) for number in line.split()]
        result+= max(numbers) - min(numbers)
    return result

def day2p2(file):
    result = 0
    for line in open(file).read().strip().split('\n'):
        numbers=[int(number) for number in line.split()]
        for combination in itertools.permutations(numbers,2):
            if combination[0] % combination[1] == 0:
                result += combination[0] // combination[1]
    return result

def test1():
    assert day2p1('day02-test.input') == 18
    assert day2p1('day02.input') == 44216
    assert day2p2('day02-test2.input') == 9
    assert day2p2('day02.input') == 320

if __name__ == '__main__':
    print('advent of code day 2')
    print(f"part 1: {day2p1('./day02.input')}")
    print(f"part 2: {day2p2('./day02.input')}")
