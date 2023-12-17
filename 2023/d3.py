#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    indata = open(sys.argv[1]).read()
else:
    indata = sys.stdin.read()

data = {}
parts = []
gears = []
parts_coords = {}

for y, line in enumerate(indata.split('\n')):
    part_num = ''
    part_loc = []
    for x, ch in enumerate(line):
        if ch == '*':
            gears += [(x,y)]
        data[(x,y)] = ch
        if ch in ['0','1','2','3','4','5','6','7','8','9']:
            part_num += ch
            part_loc += [(x,y)]
        if ch not in ['0','1','2','3','4','5','6','7','8','9'] and len(part_num) > 0:
            parts += [{'num': int(part_num), 'loc': part_loc}]
            for loc in part_loc:
                parts_coords[loc] = (int(part_num), y)
            part_num = ''
            part_loc = []
    if len(part_num) > 1:
        parts += [{'num': int(part_num), 'loc': part_loc}]
        for loc in part_loc:
            parts_coords[loc] = (int(part_num),y)
        part_num = ''
        part_loc = []

def part1():
    result = 0
    for part in parts:
        found = False
        num = part['num']
        for digit in part['loc']:
            for neighbor in [(-1,-1), (-1,0), (-1,1), (1,0), (1,1), (1,-1), (0,-1), (0,1)]:
                neighbor1 = (digit[0]+neighbor[0], digit[1]+neighbor[1])
                if neighbor1 in data and data[neighbor1] in ['*','#','$','+','/','@','-','=','&','%']:
                    result += num
                    found = True
                    break
            if found:
                break
    return result

def part2():
    result = 0
    for gear in gears:
        matches = set()
        for neighbor in [(-1,-1), (-1,0), (-1,1), (1,0), (1,1), (1,-1), (0,-1), (0,1)]:
            gear1 = (gear[0] + neighbor[0], gear[1] + neighbor[1])
            if gear1 in parts_coords:
                matches.add(parts_coords[gear1])
        
        if len(matches) == 2:
            result += list(matches)[0][0] * list(matches)[1][0]
    return result

print("day3")
print(f"part 1: {part1()}")
print(f"part 2: {part2()}")