#!/usr/bin/env python3
import sys

class Day07:
    def __init__(self, file):
        self.data = {'/':0}
        cwd = []
        for line in open(file).readlines():
            tokens = line.strip().split()
            if line.startswith('$'):
                if line.startswith('$ cd'):  # ignore $ ls
                    if tokens[2] == '..':
                        cwd.pop()
                    else:
                        cwd.append(tokens[2])
            elif line.startswith('dir'):
                self.data['/'.join(cwd+[tokens[1]])] = 0
            else:
                value = int(tokens[0])
                for i in range(1, len(cwd)+1):
                    self.data['/'.join(cwd[0:i])] += value

    def run_part1(self):
        # find sum of all sizes < 100k
        return sum([self.data[name] for name in self.data if self.data[name] <= 100000])

    def run_part2(self):
        # total 70000000, need unused 30000000
        freespace = 70000000 - self.data['/']
        smallest = 70000000
        for value in self.data.values():
            if freespace + value > 30000000 and value < smallest:
                smallest = value
        return smallest

def test1():
    test_day07 = Day07('./day07-test.input')
    assert test_day07.run_part1() == 95437
    assert test_day07.run_part2() == 24933642

def test2():
    test_day07 = Day07('./day07.input')
    assert test_day07.run_part1() == 1350966
    assert test_day07.run_part2() == 6296435

if __name__ == '__main__':
    print("advent of code: day07")
    file = './day07.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day07 = Day07(file)
    print(f"part 1: {day07.run_part1()}")
    print(f"part 2: {day07.run_part2()}")
