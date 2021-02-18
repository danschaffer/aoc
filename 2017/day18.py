#!/usr/bin/env python3

class Day18:
    def __init__(self, file, verbose=False, id=0, part2=False):
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
        if part2:
            self.instructions['snd'] = self.snd2
            self.instructions['rcv'] = self.rcv2
        for n in range(26):
            self.registers[chr(ord('a')+n)] = 0
        self.registers['p'] = id
        self.id = id
        self.send_queue = []
        self.receive_queue = None
        self.send_count = 0

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
            print(f"[{self.id}]set {args[0]} = {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def add(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] += value
        if self.verbose:
            print(f"[{self.id}]add {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def mul(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] *= value
        if self.verbose:
            print(f"[{self.id}]mul {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def mod(self, args):
        value = args[1]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.registers[args[0]] %= value
        if self.verbose:
            print(f"[{self.id}]mod {args[0]} {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def snd(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        self.lastsound = value
        if self.verbose:
            print(f"[{self.id}]snd {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def rcv(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        if self.verbose:
            print(f"[{self.id}]recv {value} {self.show_registers()}")
        self.instruction_pointer += 1
        if value > 0:
            return self.lastsound

    def snd2(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.send_queue.append(value)
        self.send_count += 1
        if self.verbose:
          print(f"[{self.id}]snd {value} {self.show_registers()}")
        self.instruction_pointer += 1

    def rcv2(self, args):
        if len(self.receive_queue) > 0:
            self.registers[args[0]] = int(self.receive_queue.pop(0))
        else:
            if self.verbose:
                print(f"[{self.id}]recv {args[0]} {self.show_registers()} returning, empty receive queue")
            return 1
        if self.verbose:
            print(f"[{self.id}]recv {args[0]} {self.show_registers()}")
        self.instruction_pointer += 1

    def jgz(self, args):
        value = args[1]
        if value in self.registers:
            value = int(self.registers[value])
        else:
            value = int(value)
        if self.verbose:
            print(f"[{self.id}]jgz {args[0]} {value} {self.show_registers()}")
        value1 = args[0]
        if value1 not in self.registers:
            value1 = int(value1)
        else:
            value1 = self.registers[value1]
        if value1 > 0:
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

def test2():
    day18_0 = Day18('./day18.input', id=0, part2=True,verbose=False)
    day18_1 = Day18('./day18.input', id=1, part2=True,verbose=False)
    day18_0.receive_queue = day18_1.send_queue
    day18_1.receive_queue = day18_0.send_queue

    while True:
        day18_0.run()
        day18_1.run()
        if len(day18_0.send_queue) == 0 and len(day18_1.send_queue) == 0:
            break
    assert day18_1.send_count == 7112

if __name__ == '__main__':
    print("advent of code: day18")

    day18 = Day18('./day18.input')
    print(f"part 1: {day18.run()}")

    day18_0 = Day18('./day18.input', id=0, part2=True,verbose=False)
    day18_1 = Day18('./day18.input', id=1, part2=True,verbose=False)
    day18_0.receive_queue = day18_1.send_queue
    day18_1.receive_queue = day18_0.send_queue

    while True:
        day18_0.run()
        day18_1.run()
        if len(day18_0.send_queue) == 0 and len(day18_1.send_queue) == 0:
            break
    print(f"part 2: {day18_1.send_count}")
