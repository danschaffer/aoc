#!/usr/bin/env python
import sys

def part1(data):
    result = 1
    for time,dist in data:
        wins = 0
        for t in range(time):
            dist1 = t * (time-t)
            if dist1 > dist:
                wins += 1
        result = result * wins
    return result

def part2(data):
    time = int(''.join([str(time) for time,_ in data]))
    dist = int(''.join([str(dist) for _,dist in data]))
    j = 0
    count = 0
    for t in range(time):
        dist1 = t * (time-j)
        if dist1 > dist:
            count += 1
        j += 1
    return count

if __name__ == '__main__':
    if len(sys.argv) > 1:
        indata = open(sys.argv[1]).read().strip()
    else:
        indata = sys.stdin.read().strip()
    data = [(int(n),int(indata.split('\n')[1].split()[i+1])) for i,n in enumerate(indata.split('\n')[0].split()[1:])]
    print("day 6")
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")
