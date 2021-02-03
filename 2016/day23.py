#!/usr/bin/env python
import time
class Day23:
    def __init__(self, file, verbose=False):
        self.verbose = verbose
        self.instructions = {
            'cpy': self.cpy,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz,
            'tgl': self.tgl,
            'nop': self.nop,
            'mul': self.mul
        }
        self.instruction_pointer = 0
        self.executions = 0
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}
        self.lines = open(file).read().strip().split('\n')
        self.lines_original = self.lines[:]

    def tgl(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        target_value = self.instruction_pointer + value
        if target_value < 0 or target_value >= len(self.lines):
            if self.verbose:
                print(f"{self.instruction_pointer} tgl {args[0]} {self.registers} target {target_value} not in lines")
        else:
            target = self.lines[target_value].split()
            if len(target) == 2:
                if target[0] == 'inc':
                    target[0] = 'dec'
                else:
                    target[0] = 'inc'
            else:
                if target[0] == 'jnz':
                    target[0] = 'cpy'
                else:
                    target[0] = 'jnz'
            self.lines[self.instruction_pointer + value] = ' '.join(target)
            if self.verbose:
                print(f"{self.instruction_pointer} tgl {args[0]} {self.registers} {self.lines[self.instruction_pointer + value]}")
        self.instruction_pointer += 1

    def mul(self, args):
        num1 = args[0]
        num2 = args[1]
        if num1 in self.registers:
            num1 = self.registers[num1]
        else:
            value = int(num1)
        if num2 in self.registers:
            num2 = self.registers[num2]
        else:
            value = int(num2)
        target = args[2]
        self.registers[target] = num1 * num2
        if self.verbose:
            print(f"{self.instruction_pointer} mul {num1} {num2} {target} {self.registers}")
        self.instruction_pointer += 1

    def nop(self, args):
        if self.verbose:
            print(f"{self.instruction_pointer} nop {self.registers}")
        self.instruction_pointer += 1

    def cpy(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        dest = args[1]
        if dest not in self.registers:
            if self.verbose:
                print("f{self.instruction_pointer} cpy {args[0]} {args[1]} register not found")
        else:
            self.registers[dest] = value
            if self.verbose:
                print(f"{self.instruction_pointer} cpy {args[0]} {args[1]} {self.registers}")
        self.instruction_pointer += 1

    def inc(self, args):
        register = args[0]
        if register not in self.registers:
            if self.verbose:
                print(f"{self.instruction_pointer} inc {register} register not found")
        else:
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
        if args[1] not in self.registers:
            value = int(args[1])
        else:
            value = self.registers[args[1]]
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
            self.executions += 1
            if self.executions % 100000 == 0:
                print(f"{self.executions} {self.instruction_pointer} {self.registers}")
        return self.registers['a']

    def reset(self):
        self.lines = self.lines_original[:]
        self.instruction_pointer = 0
        self.executions = 0
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}

def test1():
    test_day23 = Day23('./day12-test.input')
    assert test_day23.run() == 42
    test_day23.reset()
    assert test_day23.run(part2=True) == 42

if __name__ == '__main__':
    print("advent of code: day23")
    day23 = Day23('./day23.input')
    day23.registers['a'] = 7
    print(f"part 1: {day23.run()}")
    day23.reset()
    day23.registers['a'] = 12
    print(f"part 2: {day23.run()}")
