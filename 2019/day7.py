#!/usr/bin/env python
import itertools
class Intcode:
    '''
        ABCDE
        DE two digit opcode
        C mode of 1st parameter
        B mode of 2nd parameter
        A mode of 3rd parameter
        0 position mode (default if omitted)
        1 immediate mode

        opcodes
        01 - add p1 + p2 result in p3
        02 - mult p1 * p2 result in p3
        03 - input to p1
        04 - output from p1
        05 -

        inputs get popped from inputs
        outputs pushes to outputs
    '''
    def __init__(self, data, inputs=[1]):
        self.data = data
        self.pointer = 0
        self.inputs = inputs
        self.outputs = []
        self.params = []
        self.instruction = None
        self.instruction_s = 0
        self.instruction_table = {
            1:  'add',           # val1 val2 out
            2:  'mult',          # val1 val2 out
            3:  'input',         # val1
            4:  'output',        # val1
            5:  'jump-if-true',  # condition jmp
            6:  'jump-if-false', # condition jmp
            7:  'less-than',     # val1 val2 jmp
            8:  'equals',        # val1 val2 jmp
            99: 'halt'          # (no args)
        }

    def parse_instruction(self):
        self.params = []
        while len(self.instruction_s) < 5:
            self.instruction_s = '0' + self.instruction_s
        code = int(self.instruction_s[3:])
        assert code in self.instruction_table.keys(), f"unknown instruction {instruction}"
        self.instruction = self.instruction_table[code]

    def resolve_param(self, number):
        value = self.data[self.pointer + number]
        if number == 3 and self.instruction_s[0] == '0' or number == 2 and self.instruction_s[1] == '0' or number == 1 and self.instruction_s[2] == '0':
            value = self.data[value]
        return value

    def is_running(self):
        return self.data[self.pointer] != 99

    def run(self):
        while self.run_instruction():
            True

    def run_instruction(self):
        self.instruction_s = str(self.data[self.pointer])
        self.parse_instruction()
        if self.instruction == 'halt':  # 99
            return False
        # 3 = input
        elif self.instruction == 'input':  # 03
            if len(self.inputs) == 0:
                return False
            self.data[self.data[self.pointer + 1]] = self.inputs[0]
            self.inputs = self.inputs[1:]
            self.pointer += 2
            return True
        # 4 = output
        elif self.instruction == 'output':  # 04
            self.outputs += [self.resolve_param(1)]
            self.pointer += 2
            return True
        # 5 = jump-if-true
        elif self.instruction == 'jump-if-true':  # 05
            if self.resolve_param(1) != 0:
                self.pointer = self.resolve_param(2)
            else:
                self.pointer += 3
        # 6 = jump-if-false
            return True
        elif self.instruction == 'jump-if-false':  # 06
            if self.resolve_param(1) == 0:
                self.pointer = self.resolve_param(2)
            else:
                self.pointer += 3
            return True
        # 7 = less than
        elif self.instruction == 'less-than':  # 07  does 10007 works?
            if self.resolve_param(1) < self.resolve_param(2):
                if self.instruction_s[0] == '1':
                    self.data[self.pointer + 3] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 1
            else:
                if self.instruction_s[0] == '1':
                    self.data[self.pointer + 3] = 0
                else:
                    self.data[self.data[self.pointer + 3]] = 0
            self.pointer += 4
            return True
        # 8 = equals
        elif self.instruction == 'equals':  # 08 does 10008 work?
            if self.resolve_param(1) == self.resolve_param(2):
                if self.instruction_s[0] == '1':
                    self.data[self.pointer + 3] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 1
            else:
                if self.instruction_s[0] == '1':
                    self.data[self.pointer + 3] = 0
                else:
                    self.data[self.data[self.pointer + 3]] = 0
            self.pointer += 4
            return True
        # 1 == add
        elif self.instruction == 'add':  # 01
            self.data[self.data[self.pointer + 3]] = self.resolve_param(1) + self.resolve_param(2)
            self.pointer += 4
            return True
        # 2 == mult
        elif self.instruction == 'mult':  # 02
            self.data[self.data[self.pointer + 3]] = self.resolve_param(1) * self.resolve_param(2)
            self.pointer += 4
            return True

class Amplifier:
    def __init__(self, code):
        self.code = code

    def run_one(self, inputs):
        intcode_a = Intcode(self.code[:], [inputs[0], 0])
        intcode_a.run()
        intcode_b = Intcode(self.code[:], [inputs[1], intcode_a.outputs[0]])
        intcode_b.run()
        intcode_c = Intcode(self.code[:], [inputs[2], intcode_b.outputs[0]])
        intcode_c.run()
        intcode_d = Intcode(self.code[:], [inputs[3], intcode_c.outputs[0]])
        intcode_d.run()
        intcode_e = Intcode(self.code[:], [inputs[4], intcode_d.outputs[0]])
        intcode_e.run()
        return intcode_e.outputs[0]

    def run_two(self, inputs):
        intcode_a = Intcode(self.code[:], [inputs[0], 0])
        intcode_b = Intcode(self.code[:], [inputs[1]])
        intcode_c = Intcode(self.code[:], [inputs[2]])
        intcode_d = Intcode(self.code[:], [inputs[3]])
        intcode_e = Intcode(self.code[:], [inputs[4]])
        while intcode_a.is_running() and intcode_b.is_running() and intcode_c.is_running() and intcode_a.is_running() and intcode_d.is_running() and intcode_e.is_running():
            intcode_a.run()
            if intcode_b.is_running() and len(intcode_a.outputs) > 0:
                intcode_b.inputs += intcode_a.outputs
                intcode_a.outputs = []
            intcode_b.run()
            if intcode_c.is_running() and len(intcode_b.outputs) > 0:
                intcode_c.inputs += intcode_b.outputs
                intcode_b.outputs = []
            intcode_c.run()
            if intcode_d.is_running() and len(intcode_c.outputs) > 0:
                intcode_d.inputs += intcode_c.outputs
                intcode_c.outputs = []
            intcode_d.run()
            if intcode_e.is_running() and len(intcode_d.outputs) > 0:
                intcode_e.inputs += intcode_d.outputs
                intcode_d.outputs = []
            intcode_e.run()
            if intcode_a.is_running() and len(intcode_e.outputs) > 0:
                intcode_a.inputs += intcode_e.outputs
                intcode_e.outputs = []
        return intcode_e.outputs[0]

    def run_perm_one(self):
        result = 0
        for phase in itertools.permutations(list(range(5))):
            result = max(result, self.run_one([phase[0], phase[1], phase[2], phase[3], phase[4]]))
        return result

    def run_perm_two(self):
        result = 0
        for phase in itertools.permutations(list(range(5, 10))):
            result = max(result, self.run_two([phase[0], phase[1], phase[2], phase[3], phase[4]]))
        return result

def test_intcode():
    intcode = Intcode([1002, 5, 2, 5, 99, 33], [])  # mult
    intcode.run()
    assert(intcode.data[5] == 66)

    intcode = Intcode([1001, 5, 2, 5, 99, 33], [])  # add
    intcode.run()
    assert(intcode.data[5] == 35)

    intcode = Intcode([3, 3, 99, 0], [1])  # input
    intcode.run()
    assert(intcode.data[3] == 1)

    intcode = Intcode([4, 3, 99, 11], [])  # output
    intcode.run()
    assert(intcode.outputs == [11])

    intcode = Intcode([104, 3, 99, 11], [])  # output
    intcode.run()
    assert(intcode.outputs == [3])

    intcode = Intcode([104, 3, 99, 11], [])  # output
    intcode.run()
    assert(intcode.outputs == [3])

    intcode = Intcode([1105, 1, 4, 99, 104, 1, 99], [])  # jump if true
    intcode.run()
    assert(intcode.outputs == [1])

    intcode = Intcode([5, 7, 8, 99, 104, 1, 99, 1, 4], [])  # jump if true
    intcode.run()
    assert(intcode.outputs == [1])

def test_amplifier1():
    amplifier = Amplifier([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    assert amplifier.run_one([4,3,2,1,0]) == 43210

    amplifier = Amplifier([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
    assert amplifier.run_one([0,1,2,3,4]) == 54321

    amplifier = Amplifier([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
    assert amplifier.run_one([1,0,4,3,2]) == 65210

def test_part1():
    with open('./in7.txt') as f:
        input = [int(item) for item in f.read().strip().split(',')]
        amplifier= Amplifier(input)
        assert amplifier.run_perm_one() == 262086

def test_amplifier2():
    amplifier = Amplifier([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
    assert amplifier.run_two([9,8,7,6,5]) == 139629729

    amplifier = Amplifier([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10])
    assert amplifier.run_two([9,7,8,5,6]) == 18216

def test_part2():
    with open('./in7.txt') as f:
        input = [int(item) for item in f.read().strip().split(',')]
        amplifier= Amplifier(input)
        assert amplifier.run_perm_two() == 5371621

if __name__ == '__main__':
    with open('./day7.input') as f:
        input = [int(item) for item in f.read().strip().split(',')]

        amplifier = Amplifier(input)
        result = amplifier.run_perm_one()
        print(f"part 1: {result}")

        amplifier = Amplifier(input)
        result = amplifier.run_perm_two()
        print(f"part 2: {result}")
