#!/usr/bin/env python3

class Day8:
    def __init__(self, program, verbose=False):
        self.program = program
        self.verbose = verbose
        self.acc = 0
        self.inptr = 0
        self.log = set()
        self.count = 0

    def execute(self):
        line = self.program[self.inptr]
        (instruction, parameter1) = line.split()
        parameter1 = int(parameter1)
        if instruction == 'acc':
            self.acc += parameter1
            self.inptr += 1
        elif instruction == 'jmp':
            self.inptr += parameter1
        elif instruction == 'nop':
            self.inptr += 1
        else:
            assert False, f"unknown instruction {instruction}"
        self.count += 1
        if self.inptr in self.log:
            return False
        self.log.add(self.inptr)
        return True

    def run(self):
        if self.verbose:
            print(f"{self.program[self.count]} {self.inptr} {self.acc}")
        while self.execute():
            if self.verbose:
                print(f"{self.program[self.count]} {self.inptr} {self.acc}")
            if self.inptr == len(self.program):
                break
        return self.acc

    def run_part1(self):
        return self.run()

def load(file):
    return open(file).read().strip().split('\n')

def run_part2(file):
    program = open(file).read().strip().split('\n')
    for index, line in enumerate(program):
        (instruction, parameter1) = line.split()
        parameter1 = int(parameter1)
        program1 = program[:]
        if instruction == 'nop' and parameter1 > 0:
            program1[index] = f"jmp {parameter1}"
            newday = Day8(program1)
            newday.run()
            if newday.inptr == len(program1):
                return newday.acc
        elif instruction == 'jmp':
            program1[index] = f"nop {parameter1}"
            newday = Day8(program1)
            newday.run()
            if newday.inptr == len(program1):
                return newday.acc

def test1():
    test_day8 = Day8(load('./day8-test.input'))
    assert test_day8.run_part1() == 5
    assert run_part2('./day8-test.input') == 8

def test2():
    test_day8 = Day8(load('./day8.input'))
    assert test_day8.run_part1() == 1501
    assert run_part2('./day8.input') == 509

if __name__ == '__main__':
    print("advent of code: day8")
    day8 = Day8(load('./day8.input'))
    print(f"part 1: {day8.run_part1()}")
    print(f"part 2: {run_part2('./day8.input')}")
