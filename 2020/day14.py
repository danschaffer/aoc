#!/usr/bin/env python3
from itertools import product
class Day14:
    def __init__(self, file):
        self.lines = open(file).read().strip().split('\n')

    def set_bit(self, value, bit):
        return value | (1<<bit)

    def clear_bit(self, value, bit):
        return value & ~(1<<bit)

    def run_part1(self):
        mem = {}
        mask = ''
        for line in self.lines:
            instr, param = line.split('=')
            instr = instr.strip()
            param = param.strip()
            if instr == 'mask':
                mask = param
            else:
                index0 = int(instr.split('[')[1][:-1])
                value = int(param)
                for index, bit in enumerate(mask[::-1]):
                    if bit == 'X':
                        continue
                    elif bit == '0':
                        value = self.clear_bit(value, index)
                    else:
                        value = self.set_bit(value, index)
                mem[index0] = value
        return sum(mem.values())

    def run_part2(self):
        memory = {}
        mask = ''
        for line in self.lines:
            instr, param = line.split('=')
            instr = instr.strip()
            param = param.strip()
            if instr == 'mask':
                mask = param
                masks = []
                counter = mask.find('X')
                while counter > -1 and counter < len(mask):
                    masks += [len(mask) - counter - 1]
                    counter = mask.find('X', counter+1)
            else:
                mem = int(instr.split('[')[1][:-1])
                value = int(param)
                for index,char in enumerate(mask[::-1]):
                    if char == '1':
                        mem = self.set_bit(mem, index)
                for replacements in product([0,1],repeat=len(masks)):
                    mem0 = mem
                    for index,replace in enumerate(list(replacements)):
                        if replace == 0:
                            mem0=self.clear_bit(mem0, masks[index])
                        else:
                            mem0=self.set_bit(mem0, masks[index])
                    memory[mem0] = value
        return sum(memory.values())

def test1():
    test1_day14 = Day14('./day14-test1.input')
    assert test1_day14.run_part1() == 165
    test2_day14 = Day14('./day14-test2.input')
    assert test2_day14.run_part2() == 208

def test2():
    test_day14 = Day14('./day14.input')
    assert test_day14.run_part1() == 14925946402938
    assert test_day14.run_part2() == 3706820676200

if __name__ == '__main__':
    print("advent of code: day14")
    day14 = Day14('./day14.input')
    print(f"part 1: {day14.run_part1()}")
    print(f"part 2: {day14.run_part2()}")
