#!/usr/bin/env python

import argparse
import sys

class GameConsole:
    def __init__(self, file=None, verbose=False, stop_on_loop=False):
        self.inst_ptr = 0
        self.verbose = verbose
        self.stop_on_loop = stop_on_loop
        self.accumulator = 0
        self.program = list()
        self.loops = set()
        if file:
            self.program = open(file).read().strip().split('\n')
        self.instructions = {
            'nop': GameConsole.nop,
            'jmp': GameConsole.jmp,
            'acc': GameConsole.acc
        }

    def run(self):
        while self.inst_ptr < len(self.program):
            if self.stop_on_loop:
                if self.inst_ptr in self.loops:
                    break
                self.loops.add(self.inst_ptr)
            instr, param1 = self.program[self.inst_ptr].split()
            self.instructions[instr](self, param1)
        return self.accumulator

    def nop(self, param1):
        if self.verbose:
            print(f"nop {param1} acc:{self.accumulator} ip:{self.inst_ptr}")
        self.inst_ptr += 1

    def acc(self, param1):
        self.accumulator += int(param1)
        if self.verbose:
            print(f"acc {param1} acc:{self.accumulator} ip:{self.inst_ptr}")
        self.inst_ptr += 1

    def jmp(self, param1):
        if self.verbose:
            print(f"jmp {param1} acc:{self.accumulator} ip:{self.inst_ptr}")
        self.inst_ptr += int(param1)

def test1():
    assert GameConsole('./day8.input', stop_on_loop=True).run() == 1501
    assert GameConsole('./day8.input.solution').run() == 509

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game Console')
    parser.add_argument('--verbose', action='store_true', help='verbose output')
    parser.add_argument('--stop_loop', action='store_true', help='stops when ip repeats')
    parser.add_argument('file', help='input file')
    pargs = parser.parse_args()
    if len(sys.argv) == 0:
        print(f"{sys.argv[0]} <file>")
        sys.exit(1)
    print(f"acc: {GameConsole(file=pargs.file, verbose=pargs.verbose, stop_on_loop=pargs.stop_loop).run()}")
