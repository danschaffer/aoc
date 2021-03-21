#!/usr/bin/env python3

class Machine:
    def __init__(self, lines, registers=[0,0,0,0,0,0]):
        self.registers=registers
        self.lines=lines
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
    def set_registers(self, new_registers):
        self.registers = new_registers

    def run(self, part2=False):
        max_cycles = 0
        if part2:
            self.registers[0] = 1
            max_cycles = 1000
        parts = self.lines[0].split()
        assert parts[0] == '#ip'
        ip_register = int(parts[1])
        ip = self.registers[ip_register]
        program = []
        cycles = 0
        for line in self.lines[1:]:
            parts = line.split()
            program.append([parts[0],int(parts[1]),int(parts[2]),int(parts[3])])
        while ip >=0 and ip < len(program):
            self.registers[ip_register] = ip
            before = self.registers[:]
            prog = program[ip]
            self.instructions[prog[0]](prog[1], prog[2], prog[3])
#            print(f"{ip} {before} {self.lines[ip]} {self.registers}")
            ip = self.registers[ip_register] + 1
            cycles += 1
            if max_cycles and cycles >= max_cycles:
                break
        return self.registers

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

def test1():
    machine = Machine(open('./day19-test.input').read().split('\n'))
    assert machine.run()[0] == 6

if __name__ == '__main__':
    print("advent of code: day19")
    machine = Machine(open('./day19.input').read().split('\n'))
    print(f"part 1: {machine.run()[0]}")
    machine.registers=[0,0,0,0,0,0]
    registers = machine.run(part2=True)
    n = max(registers)
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    print(f"part 2: {total}")
