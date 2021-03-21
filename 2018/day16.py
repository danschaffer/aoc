#!/usr/bin/env python3

class Machine:
    def __init__(self, registers=[0,0,0,0]):
        self.registers=registers
        self.instructions = {
            'addr': self.addr,
            'addi': self.addi,
            'mulr': self.mulr,
            'muli': self.muli,
            'banr': self.banr,
            'bani': self.bani,
            'borr': self.borr,
            'bori': self.bori,
            'gtir': self.gtir,
            'gtri': self.gtri,
            'gtrr': self.gtrr,
            'eqir': self.eqir,
            'eqri': self.eqri,
            'eqrr': self.eqrr,
            'setr': self.setr,
            'seti': self.seti,
        }
        self.instruction_map = {
            0: self.borr,
            1: self.seti,
            2: self.mulr,
            3: self.eqri,
            4: self.banr,
            5: self.bori,
            6: self.bani,
            7: self.gtri,
            8: self.addr,
            9: self.muli,
            10: self.addi,
            11: self.eqrr,
            12: self.gtir,
            13: self.eqir,
            14: self.setr,
            15: self.gtrr,
        }
    
    def set_registers(self, new_registers):
        self.registers = new_registers

    def run(self, instruction, a, b, c):
        if type(instruction) == int:
            self.instruction_map[instruction](a,b,c)
        else:
            self.instructions[instruction](a,b,c)

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        if a > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def gtri(self, a, b, c):
        if self.registers[a] > b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def gtrr(self, a, b, c):
        if self.registers[a] > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqir(self, a, b, c):
        if a == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqri(self, a, b, c):
        if self.registers[a] == b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqrr(self, a, b, c):
        if self.registers[a] == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

def part1(data):
    threeormore = 0
    for lines in data.split('\n\n'):
        before, line, after = lines.split('\n')
        parts = before.split()
        before_registers = [int(parts[1][1:-1]), int(parts[2][:-1]), int(parts[3][:-1]), int(parts[4][:-1])]
        instructions = [int(n) for n in line.split()]
        parts = after.split()
        after_registers = [int(parts[1][1:-1]), int(parts[2][:-1]), int(parts[3][:-1]), int(parts[4][:-1])]
        if count(before_registers, instructions, after_registers) >= 3:
            threeormore += 1
    return threeormore

def count(before, instructions, after):
    _, a, b, c = instructions
    result = 0
    machine = Machine()
    for instruction in machine.instructions:
        machine.set_registers(before[:])
        machine.run(instruction, a, b, c)
        if after == machine.registers:
            result += 1
    return result

def count2(before, instructions, after):
    _, a, b, c = instructions
    result = 0
    matched = None
    machine = Machine()
    for instruction in machine.instructions:
        if machine.instructions[instruction] in machine.instruction_map.values():
            continue
        machine.set_registers(before[:])
        machine.run(instruction, a, b, c)
        if after == machine.registers:
            result += 1
            matched = instruction
    return result, matched

def solve2(data):
    for lines in data.split('\n\n'):
        result = 0
        before, line, after = lines.split('\n')
        parts = before.split()
        before_registers = [int(parts[1][1:-1]), int(parts[2][:-1]), int(parts[3][:-1]), int(parts[4][:-1])]
        instructions = [int(n) for n in line.split()]
        parts = after.split()
        after_registers = [int(parts[1][1:-1]), int(parts[2][:-1]), int(parts[3][:-1]), int(parts[4][:-1])]
        result, matched = count2(before_registers, instructions, after_registers)
        if result == 1:
            print(f"found match: {instructions[0]} {matched}")
    return result

def part2(data):
    lines = data.split('\n')
    code = []
    for line in lines:
        if line == '':
            continue
        parts = line.split()
        code.append([int(parts[0]),int(parts[1]),int(parts[2]),int(parts[3])])
    instruction_pointer = 0
    machine = Machine()
    while instruction_pointer < len(code):
        code1 = code[instruction_pointer]
        machine.run(code1[0], code1[1], code1[2], code1[3])
        instruction_pointer += 1
    return machine.registers[0]

def test1():
    assert part1('Before: [3, 2, 1, 1]\n9 2 1 2\nAfter:  [3, 2, 2, 1]') == 1
    data = open('./day16.input').read().split('\n\n\n')
    assert part1(data[0]) == 588
    assert part2(data[1]) == 627

if __name__ == '__main__':
    print("advent of code: day16")
    data = open('./day16.input').read().split('\n\n\n')
    print(f"part 1: {part1(data[0])}")
#    solve2(part1(data[0]))
    print(f"part 2: {part2(data[1])}")
