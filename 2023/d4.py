#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    indata = open(sys.argv[1]).read()
else:
    indata = sys.stdin.read()

def part1():
    result = 0
    for line in indata.split('\n'):
        _, data = line.split(':')
        winning_, mine_ = data.split('|')
        winning=[int(num) for num in winning_.strip().split()]
        mine=[int(num) for num in mine_.strip().split()]
        wins = sum([1 for num in mine if num in winning])
        if wins > 0:
            result += 2 ** (wins-1)
    return result

def part2():
    result = 0
    wins = []
    states = []
    for line in indata.split('\n'):
        _, data = line.split(':')
        winning_, mine_ = data.split('|')
        winning=[int(num) for num in winning_.strip().split()]
        mine=[int(num) for num in mine_.strip().split()]
        wins.append(sum([1 for num in mine if num in winning]))
        states.append(1)
    def next_state():
        for n in range(len(states)):
            if states[n] > 0:
                return n
        return -1
    while True:
        n = next_state()
        if n == -1:
            break
        result += 1
        states[n] -= 1
        for ct in range(wins[n]):
            if n + ct + 1 < len(states):
                states[n + ct + 1] += 1
    return result


print("day04")
print(f"part 1: {part1()}")
print(f"part 1: {part2()}")
