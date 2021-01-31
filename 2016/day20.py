#!/usr/bin/env python

def solve(file, part2=False):
    data = []
    results = 0
    for line in open(file).read().strip().split('\n'):
        parts = line.split('-')
        data.append((int(parts[0]), int(parts[1])))
    data.sort()
    ip = 0
    counter = 0
    while ip < 4294967295: 
        lower, upper = data[counter]
        if ip >= lower:
            if ip <= upper:
                ip = upper + 1
                continue
            counter += 1
        else:
            if not part2:
                return ip
            ip += 1
            results += 1
    return results

def test1():
    assert solve('./day20.input') == 32259706
    assert solve('./day20.input', part2=True) == 113

if __name__ == '__main__':
    print(f"part 1: {solve('./day20.input')}")
    print(f"part 2: {solve('./day20.input', part2=True)}")
        