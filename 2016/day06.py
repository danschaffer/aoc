#!/usr/bin/env python3

def run(file, part2=False):
    lines = open(file).read().strip().split('\n')
    data = [{} for _ in range(len(lines[0]))]
    for line in lines:
        for index, letter in enumerate(line):
            if letter not in data[index]:
                data[index][letter] = 1
            else:
                data[index][letter] += 1
    password = ''
    for eachdata in data:
        password += sorted(eachdata.items(), key=lambda x: x[1], reverse=(not part2))[0][0]
    return password

def test1():
    assert run('./day06-test.input') == 'easter'
    assert run('./day06-test.input', part2=True) == 'advent'

if __name__ == '__main__':
    print("advent of code: day06")
    print(f"part 1: {run('./day06.input')}")
    print(f"part 2: {run('./day06.input', part2=True)}")
