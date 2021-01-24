#!/usr/bin/env python
import time
class Day12:
    def __init__(self, file, verbose=False):
        self.verbose = verbose
        self.reset()
        self.instructions = {
            'cpy': self.cpy,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz
        }
        self.lines = open(file).read().strip().split('\n')

    def cpy(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        dest = args[1]
        self.registers[dest] = value
        if self.verbose:
            print(f"{self.instruction_pointer} cpy {args[0]} {args[1]} {self.registers}")
        self.instruction_pointer += 1

    def inc(self, args):
        register = args[0]
        self.registers[register] += 1
        if self.verbose:
            print(f"{self.instruction_pointer} inc {register} {self.registers}")
        self.instruction_pointer += 1

    def dec(self, args):
        register = args[0]
        self.registers[register] -= 1
        if self.verbose:
            print(f"{self.instruction_pointer} dec {register} {self.registers}")
        self.instruction_pointer += 1

    def jnz(self, args):
        register = args[0]
        if args[0] not in self.registers:
            register_value = int(args[0])
        else:
            register_value = self.registers[args[0]]
        value = int(args[1])
        if self.verbose:
            print(f"{self.instruction_pointer} jnz {register} {value} {self.registers}")
        if register_value != 0:
            self.instruction_pointer += value
        else:
            self.instruction_pointer += 1

    def run(self, part2=False):
        if part2:
            self.registers['c'] = 1
        while self.instruction_pointer < len(self.lines):
            parts = self.lines[self.instruction_pointer].split()
            function = parts[0]
            args = parts[1:]
            self.instructions[function](args)
        return self.registers['a']

    def reset(self):
        self.instruction_pointer = 0
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}

def test1():
    test_day12 = Day12('./day12-test.input')
    assert test_day12.run() == 42
    test_day12.reset()
    assert test_day12.run(part2=True) == 42

def test2():
    test_day12 = Day12('./day12.input')
    assert test_day12.run() == 318009
    test_day12.reset()
    assert test_day12.run(part2=True) == 9227663

if __name__ == '__main__':
    print("advent of code: day12")
    day12 = Day12('./day12.input')
    start = time.time()
    print(f"part 1: {day12.run()} {round(time.time()-start,1)}s")
    day12.reset()
    print(f"part 2: {day12.run(part2=True)} {round(time.time()-start,1)}s")
