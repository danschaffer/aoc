#!/usr/bin/env python3

class Machine:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.registers = {'a':0, 'b':0}
        self.ip = 0
        self.lines = []

    def load(self, file):
        self.add_lines(open(file).read().strip().split('\n'))

    def add_lines(self, lines):
        self.lines = lines

    def run(self):
        while self.ip < len(self.lines):
            self.run_line()

    def run_line(self):
        newip = self.ip + 1
        tokens = self.lines[self.ip].split()
        if tokens[0] == 'inc':
            self.registers[tokens[1]] += 1
        elif tokens[0] == 'tpl':
            self.registers[tokens[1]] *= 3
        elif tokens[0] == 'hlf':
            self.registers[tokens[1]] = self.registers[tokens[1]] // 2
        elif tokens[0] == 'jmp':
            value = int(tokens[1])
            newip = self.ip + value
        elif tokens[0] == 'jie':
            register = tokens[1][:-1]
            value = int(tokens[2])
            if self.registers[register] % 2 == 0:
                newip = self.ip + value
        elif tokens[0] == 'jio':
            register = tokens[1][:-1]
            value = int(tokens[2])
            if self.registers[register] == 1:
                newip = self.ip + value
        else:
            assert False, f"Uknown instruction {tokens[0]}"
        if self.verbose:
            print(f"{self.ip} {self.lines[self.ip]} {newip} {self.registers}")
        self.ip = newip

def test1():
    machine = Machine()
    machine.add_lines([
        'inc a',
        'jio a, +2',
        'tpl a',
        'inc a',
    ])
    machine.run()
    assert machine.registers['a'] == 2

def test2():
    machine = Machine()
    machine.load('./day23.input')
    machine.run()
    assert machine.registers['b'] == 255
    machine.registers = {'a':1, 'b':0}
    machine.ip = 0
    machine.run()
    assert machine.registers['b'] == 334

if __name__ == '__main__':
    machine = Machine()
    machine.load('./day23.input')
    machine.run()
    print(f"part 1: {machine.registers['b']}")
    machine.registers = {'a':1, 'b':0}
    machine.ip = 0
    machine.run()
    print(f"part 2: {machine.registers['b']}")
