#!/usr/bin/env python3

def day4(file, part2=False):
    result=0
    for line in open(file).read().strip().split('\n'):
        cache=set()
        valid=True
        for word in line.split():
            if part2:
                word = ''.join(sorted(word))
            if word in cache:
                valid=False
                break
            else:
                cache.add(word)
        if valid:
            result+=1
    return result

def test1():
    assert day4('./day04-test.input') == 2
    assert day4('./day04.input') == 337
    assert day4('./day04.input', part2=True) == 231

if __name__ == '__main__':
    print("advent of code: day04")
    print(f"part 1: {day4('./day04.input')}")
    print(f"part 2: {day4('./day04.input',part2=True)}")
