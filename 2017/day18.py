#!/usr/bin/env python3

class Day18:
    def __init__(self, file, verbose=True):
        self.lines = open(file).read().strip().split('\n')
        self.verbose = verbose
        self.instruction_pointer = 0
        self.registers = {}
        self.lastsound = 0
        self.instructions = {
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'mod': self.mod,
            'snd': self.snd,
            'rcv': self.rcv,
            'jgz': self.jgz,
        }
        for n in range(26):
            self.registers[chr(ord('a')+n)] = 0

    def run(self):
        result = None
        while result is None:
            parts = self.lines[self.instruction_pointer].split()
            result = self.instructions[parts[0]](parts[1:])
        return result

    def set(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] = value
        if self.verbose:
            print(f"set {args[0]} = {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def add(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] += value
        if self.verbose:
            print(f"add {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def mul(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] *= value
        if self.verbose:
            print(f"mul {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def mod(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] %= value
        if self.verbose:
            print(f"mod {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def snd(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        self.lastsound = value
        if self.verbose:
            print(f"snd {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def rcv(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        if self.verbose:
            print(f"recv {value} {self.show_registers()}")
        self.instruction_pointer += 1
        if value > 0:
            return self.lastsound

    def jgz(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        if self.verbose:
            print(f"jgz {args[0]} {value} {self.show_registers()}")
        if self.registers[args[0]] > 0:
            self.instruction_pointer += value
        else:
            self.instruction_pointer += 1

    def show_registers(self):
        result = '['
        for register in self.registers:
            if self.registers[register] > 0:
                result += f"{register}={self.registers[register]} "
        return result + ']'

def test1():
    test_day18 = Day18('./day18-test.input')
    assert test_day18.run() == 4

    day18 = Day18('./day18.input')
    assert day18.run() == 3188

if __name__ == '__main__':
    print("advent of code: day18")

    day18 = Day18('./day18.input')
    print(f"part 1: {day18.run()}")
