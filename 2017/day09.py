#!/usr/bin/env python3
import os
def day9(input, part2=False):
    if os.path.exists(input):
        input = open(input).read().strip()
    pointer = 0
    level = 0
    total = 0
    garbage_total = 0
    garbage = False
    while pointer < len(input):
        if garbage and input[pointer] == '>':
                garbage = False
        elif not garbage and input[pointer] == '{':
            level += 1
            total += level
        elif not garbage and input[pointer] == '}':
            level -= 1
        if input[pointer] == '!':
            pointer += 1
        elif garbage:
            garbage_total += 1
        if not garbage and input[pointer] == '<':
            garbage = True

        pointer += 1
    if part2:
        return garbage_total
    else:
        return total

def test1():
    assert day9('{}') == 1
    assert day9('{{{}}}') == 6
    assert day9('{{},{}}') == 5
    assert day9('{<{},{},{{}}>}') == 1
    assert day9('{<a>,<a>,<a>,<a>}') == 1
    assert day9('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert day9('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert day9('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
    assert day9('./day09.input') == 23588

    assert day9('<>',part2=True) == 0
    assert day9('<random characters>',part2=True) == 17
    assert day9('<<<<>',part2=True) == 3
    assert day9('<{!>}>',part2=True) == 2
    assert day9('<!!>',part2=True) == 0
    assert day9('<!!!>>',part2=True) == 0
    assert day9('<{o"i!a,<{i<a>',part2=True) == 10
    assert day9('./day09.input', part2=True) == 10045

if __name__ == '__main__':
    print("advent of code: day09")
    print(f"part 1: {day9('./day09.input')}")
    print(f"part 2: {day9('./day09.input', part2=True)}")
