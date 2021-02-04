#!/usr/bin/env python
import time
class Day25:
    def __init__(self, file, verbose=False):
        self.verbose = verbose
        self.instructions = {
            'cpy': self.cpy,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz,
            'out': self.out,
            'nop': self.nop,
            'mul': self.mul
        }
        self.instruction_pointer = 0
        self.executions = 0
        self.output = []
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}
        self.lines = open(file).read().strip().split('\n')

    def out(self, args):
        value = args[0]
        if value in self.registers:
            value = self.registers[value]
        else:
            value = int(value)
        self.output.append(value)
#        print(value,end='')
        if self.verbose:
            print(f"{self.instruction_pointer} out {args[0]} {self.registers} {value}")
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

    def run(self):
        while self.instruction_pointer < len(self.lines):
            parts = self.lines[self.instruction_pointer].split()
            function = parts[0]
            args = parts[1:]
            self.instructions[function](args)
            self.executions += 1
            for index,value in enumerate(self.output):
                if value != index % 2:
                    return None
            if self.executions > 100000:
                break
        return self.registers['a']

    def reset(self):
        self.instruction_pointer = 0
        self.executions = 0
        self.output = []
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}

if __name__ == '__main__':
    print("advent of code: day25")
    day25 = Day25('./day25.input')
    counter = 0
    result = None
    while result is None:
        day25.registers['a'] = counter
        result = day25.run()
        str0 = ''
        if result is None:
            #for value in day25.output:
            #    str0 += str(value)
            #print(f"{counter} {str0}")
            counter += 1
        day25.reset()
    print(f"part 1: {counter}")
