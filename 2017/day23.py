#!/usr/bin/env python3

class Day23:
    def __init__(self, file, verbose=False, part2=False):
        self.data = {}
        self.lines = open(file).readlines()
        self.verbose = verbose
        self.part2 = part2
        self.instruction_pointer = 0
        self.registers = {}
        self.instructions = {
            'set': self.set,
            'sub': self.sub,
            'mul': self.mul,
            'jnz': self.jnz,
        }
        for n in range(8):
            self.registers[chr(ord('a')+n)] = 0
        if part2:
            self.registers['a'] = 1

    def run(self):
        while self.instruction_pointer < 11:
            parts = self.lines[self.instruction_pointer].split()
            result = self.instructions[parts[0]](parts[1:])
        if not self.part2:
            result = (self.registers['b'] - self.registers['e']) * (self.registers['b'] - self.registers['d'])
        else:
            result = 0
            for b in range(self.registers['b'], self.registers['c']+1, 17):
                if any(b % d == 0 for d in range(2, int(b**0.5))):
                    result += 1
        return result

    def set(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] = value
        if self.verbose:
            print(f"[{self.instruction_pointer}]set {args[0]} = {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def sub(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] -= value
        if self.verbose:
            print(f"[{self.instruction_pointer}]sub {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def mul(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] *= value
        if self.verbose:
            print(f"[{self.instruction_pointer}]mul {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def jnz(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        amount = args[1]
        if amount in self.registers:
            amount = self.registers[amount]
        else:
            amount = int(amount)
        if value != 0:
            newip = self.instruction_pointer + amount
        else:
            newip = self.instruction_pointer + 1
        if self.verbose:
            print(f"[{self.instruction_pointer}]jnz {args[0]} {value} newip={newip} {self.show_registers()}")
        self.instruction_pointer = newip

    def show_registers(self):
        result = '['
        for register in self.registers:
            if self.registers[register] > 0:
                result += f"{register}={self.registers[register]} "
        return result + ']'

def test1():
    test_day23 = Day23('./day23.input')
    assert test_day23.run() == 8281
    test_day23 = Day23('./day23.input', part2=True)
    assert test_day23.run() == 911

if __name__ == '__main__':
    print("advent of code: day23")
    day23 = Day23('./day23.input')
    print(f"part 1: {day23.run()}")
    day23 = Day23('./day23.input', part2=True)
    print(f"part 2: {day23.run()}")
