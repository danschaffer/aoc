#!/usr/bin/env python
import sys
red=12
green=13
blue=14
res1=0
res2=0

def parse(line):
    r1 = 0
    g1 = 0
    b1 = 0
    r2 = 999
    g2 = 999
    b2 = 999
    id = int(line.split(':')[0].split()[1])
    rest = line.split(':')[1]
    for item1 in rest.split(';'):
        for item2 in item1.split(','):
            num, type = item2.split()
            if type == 'red':
                r1 = max(r1,int(num))
            if type == 'green':
                g1 = max(g1,int(num))
            if type == 'blue':
                b1 = max(b1,int(num))
    return id, r1, g1, b1

if len(sys.argv) > 1:
    indata = open(sys.argv[1]).read()
else:
    indata = sys.stdin.read()

for line in indata.split('\n'):
    id, red1, green1, blue1 = parse(line)
    if red1<=red and blue1<=blue and green1<=green:
        res1+=id
    res2 += red1 * green1 * blue1
print("day2")
print(f"part 1: {res1}")
print(f"part 2: {res2}")