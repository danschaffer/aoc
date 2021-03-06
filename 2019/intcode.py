#!/usr/bin/env python

class Intcode:
    '''
        ABCDE
        DE two digit opcode
        C mode of 1st parameter
        B mode of 2nd parameter
        A mode of 3rd parameter

        0 position mode (default if omitted)
        1 immediate mode
        2 relative mode

        inputs get popped from inputs
        outputs pushes to outputs
    '''
    def __init__(self, data, inputs=[], name='', verbose=False, manual_input=False):
        self.data_raw = data
        self.pointer = 0
        self.base = 0
        self.inputs = inputs
        self.name = name
        self.verbose = verbose
        self.manual_input = manual_input

        self.outputs = []
        self.params = []
        self.instruction = None
        self.instruction_s = 0
        self.data = {}
        for n in range(len(self.data_raw)):
            self.data[n] = self.data_raw[n]
        self.instruction_table = {
            1:  'add',           # val1 val2 out
            2:  'mult',          # val1 val2 out
            3:  'input',         # val1
            4:  'output',        # val1
            5:  'jump-if-true',  # condition jmp
            6:  'jump-if-false', # condition jmp
            7:  'less-than',     # val1 val2 jmp
            8:  'equals',        # val1 val2 jmp
            9:  'adjust-base',   # value
            99: 'halt'           # (no args)
        }

    def write_memory(self, file):
        f = open(file, 'w')
        for n in sorted(self.data.keys()):
            f.write(f"{n} {self.data[n]}\n")

    def parse_instruction(self):
        self.params = []
        while len(self.instruction_s) < 5:
            self.instruction_s = '0' + self.instruction_s
        code = int(self.instruction_s[3:])
        assert code in self.instruction_table.keys(), f"unknown instruction {code}"
        self.instruction = self.instruction_table[code]

    def resolve_param(self, number):
        value = self.check_data(self.pointer + number)
        if number == 3 and self.instruction_s[0] == '2' or number == 2 and self.instruction_s[1] == '2' or number == 1 and self.instruction_s[2] == '2':
            value = self.check_data(self.base + value)
        elif number == 3 and self.instruction_s[0] == '0' or number == 2 and self.instruction_s[1] == '0' or number == 1 and self.instruction_s[2] == '0':
            value = self.check_data(value)
        return value

    def is_running(self):
        return self.data[self.pointer] != 99

    def run(self):
        while self.run_instruction():
            True

    def check_data(self, n):
        if n not in self.data:
            self.data[n] = 0
        return self.data[n]

    def run_instruction(self):
        self.check_data(self.pointer)
        self.instruction_s = str(self.data[self.pointer])
        self.parse_instruction()
        # 1 == add
        if self.instruction == 'add':  # 01
            if self.instruction_s[0] == '2':
                value = self.check_data(self.pointer + 3)
                self.data[self.base + value] = self.resolve_param(1) + self.resolve_param(2)
            else:
                self.data[self.data[self.pointer + 3]] = self.resolve_param(1) + self.resolve_param(2)
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1)} {self.resolve_param(2)}")
            self.pointer += 4
            return True
        # 2 == mult
        elif self.instruction == 'mult':  # 02
            if self.instruction_s[0] == '2':
                value = self.check_data(self.pointer + 3)
                self.data[self.base + value] = self.resolve_param(1) * self.resolve_param(2)
            else:
                self.data[self.data[self.pointer + 3]] = self.resolve_param(1) * self.resolve_param(2)
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1)} {self.resolve_param(2)}")
            self.pointer += 4
            return True
        # 3 = input
        elif self.instruction == 'input':  # 03
            if self.manual_input:
                self.inputs = [int(input("enter input: ").strip())]
            if len(self.inputs) == 0:
                return False
            if self.instruction_s[2] == '2':
                value = self.check_data(self.pointer + 1)
                self.data[self.base + value] = self.inputs[0]
            else:
                self.data[self.data[self.pointer + 1]] = self.inputs[0]
            self.inputs = self.inputs[1:]
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} ({self.data[self.pointer + 1]}){self.data[self.data[self.pointer + 1]]}")
            self.pointer += 2
            return True
        # 4 = output
        elif self.instruction == 'output':  # 04
            self.outputs += [self.resolve_param(1)]
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1):3}")
            self.pointer += 2
            return True
        # 5 = jump-if-true
        elif self.instruction == 'jump-if-true':  # 05
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1)} {self.resolve_param(2)}")
            if self.resolve_param(1) != 0:
                self.pointer = self.resolve_param(2)
            else:
                self.pointer += 3
        # 6 = jump-if-false
            return True
        elif self.instruction == 'jump-if-false':  # 06
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1)} {self.resolve_param(2)}")
            if self.resolve_param(1) == 0:
                self.pointer = self.resolve_param(2)
            else:
                self.pointer += 3
            return True
        # 7 = less than
        elif self.instruction == 'less-than':  # 07
            if self.resolve_param(1) < self.resolve_param(2):
                if self.instruction_s[0] == '2':
                    value = self.check_data(self.pointer + 3)
                    self.data[self.base + value] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 1
            else:
                if self.instruction_s[0] == '2':
                    value = self.check_data(self.pointer + 3)
                    self.data[self.base + value] = 0
                else:
                    self.data[self.data[self.pointer + 3]] = 0
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.data[self.pointer+1]}[{self.resolve_param(1)}] {self.data[self.pointer+2]}[{self.resolve_param(2)}] {self.data[self.pointer + 3]}[{self.data[self.data[self.pointer + 3]]}]")
            self.pointer += 4
            return True
        # 8 = equals
        elif self.instruction == 'equals':  # 08
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.resolve_param(1)} {self.resolve_param(2)} {self.data[self.pointer + 3]}")
            if self.resolve_param(1) == self.resolve_param(2):
                if self.instruction_s[0] == '2':
                    value = self.check_data(self.pointer + 3)
                    self.data[self.base + value] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 1
            else:
                if self.instruction_s[0] == '2':
                    value = self.check_data(self.pointer + 3)
                    self.data[self.base + value] = 0
                else:
                    self.data[self.data[self.pointer + 3]] = 0
            self.pointer += 4
            return True
        # 9 = adjust-base
        elif self.instruction == 'adjust-base':  # 09
            self.base += self.resolve_param(1)
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5} {self.data[self.pointer+1]}[{self.resolve_param(1)}]  base={self.base}")
            self.pointer += 2
            return True
        # 99 = halt
        if self.instruction == 'halt':  # 99
            if self.verbose:
                print(f"{self.name} {self.pointer:3} {self.instruction:13} {self.instruction_s:5}")
            return False

def test_intcode():
    intcode = Intcode([1002, 5, 2, 5, 99, 33], [], verbose=True)  # mult
    intcode.run()
    assert(intcode.data[5] == 66)

    intcode = Intcode([1001, 5, 2, 5, 99, 33], [], verbose=True)  # add
    intcode.run()
    assert(intcode.data[5] == 35)

    intcode = Intcode([3, 3, 99, 0], [1], verbose=True)  # input
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([4, 3, 99, 11], [], verbose=True)  # output
    intcode.run()
    assert(intcode.outputs == [11])

    intcode = Intcode([104, 3, 99, 11], [], verbose=True)  # output
    intcode.run()
    assert(intcode.outputs == [3])

    intcode = Intcode([104, 3, 99, 11], [], verbose=True)  # output
    intcode.run()
    assert(intcode.outputs == [3])

    intcode = Intcode([1105, 1, 4, 99, 104, 1, 99], [], verbose=True)  # jump if true
    intcode.run()
    assert(intcode.outputs == [1])

    intcode = Intcode([5, 7, 8, 99, 104, 1, 99, 1, 4], [], verbose=True)  # jump if true
    intcode.run()
    assert(intcode.outputs == [1])

    intcode = Intcode([1106, 0, 4, 99, 104, 1, 99], [], verbose=True)  # jump if false
    intcode.run()
    assert(intcode.outputs == [1])

    intcode = Intcode([6, 7, 8, 99, 104, 1, 99, 0, 4], [], verbose=True)  # jump if false
    intcode.run()
    assert(intcode.outputs == [1])

    intcode = Intcode([1107, 0, 1, 3, 99], [], verbose=True)  # less than
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([7, 5, 6, 3, 99, 0, 1], [], verbose=True)  # less than
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([7, 5, 6, 3, 99, 1, 1], [], verbose=True)  # less than
    intcode.run()
    assert(intcode.data[3] == 0)

    intcode = Intcode([1107, 1, 1, 3, 99], [], verbose=True)  # less than
    intcode.run()
    assert(intcode.data[3] == 0)

    intcode = Intcode([1108, 1, 1, 3, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([1108, 0, 1, 3, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 0)

    intcode = Intcode([8, 5, 6, 3, 99, 1, 1], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([8, 5, 6, 3, 99, 1, 0], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 0)

    intcode = Intcode([1, 5, 6, 3, 99, 5, 3], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 8)

    intcode = Intcode([1101, 10, 5, 3, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 15)

    intcode = Intcode([1101, 10, 5, 3, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 15)
    intcode = Intcode([2, 5, 6, 3, 99, 5, 3], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 15)

    intcode = Intcode([1102, 10, 5, 3, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.data[3] == 50)

    intcode = Intcode([109, 100, 99], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.base == 100)

    intcode = Intcode([9, 3, 99, 100], [], verbose=True)  # equals
    intcode.run()
    assert(intcode.base == 100)

if __name__ == '__main__':
    import sys
    data = [int(n) for n in open(sys.argv[1]).read().strip().split(',')]
    intcode = Intcode(data, verbose=True, manual_input=True)
    intcode.run()
    print(intcode.outputs)
