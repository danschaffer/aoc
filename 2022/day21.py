#!/usr/bin/env python3
import sys
class Day21:
    def __init__(self, file):
        self.data = {}
        for line in open(file).readlines():
            line = line.strip()
            parts = line.split()
            terminal = parts[0][:-1]
            if len(parts) == 2:
                result = int(parts[1])
                self.data[terminal] = result
            else:
                self.data[terminal] = parts[1:]

    def solve1(self, terminal):
        if type(self.data[terminal]) == int:
            return self.data[terminal]
        node1, op, node2 = self.data[terminal]
        if op == '+':
            return self.solve1(node1) + self.solve1(node2)
        elif op == '-':
            return self.solve1(node1) - self.solve1(node2)
        elif op == '*':
            return self.solve1(node1) * self.solve1(node2)
        elif op == '/':
            return self.solve1(node1) // self.solve1(node2)
        else:
            assert False, f"unknown operation {op}!"

    def run_part1(self):
        return self.solve1("root")

    def run_part2(self):
        return -1

def test1():
    test_day21 = Day21('./day21-test.input')
    assert test_day21.run_part1() == 152
    assert test_day21.run_part2() == -1

def test2():
    test_day21 = Day21('./day21.input')
    assert test_day21.run_part1() == 118565889858886
    assert test_day21.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day21")
    file = './day21.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day21 = Day21(file)
    print(f"part 1: {day21.run_part1()}")
    print(f"part 2: {day21.run_part2()}")
