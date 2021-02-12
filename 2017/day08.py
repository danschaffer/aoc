#!/usr/bin/env python3

class Day08:
    def __init__(self, file):
        self.registers = {}
        self.lines = open(file).read().strip().split('\n')

    def run(self):
        highest = 0
        for line in self.lines:
            tokens = line.split()
            register = tokens[0]
            operation = tokens[1]
            value = int(tokens[2])
            condition_register = tokens[4]
            condition_operation = tokens[5]
            condition_value = int(tokens[6])
            condition = False
            if condition_operation == '>' and self.registers.get(condition_register,0) > condition_value:
                condition = True
            elif condition_operation == '>=' and self.registers.get(condition_register,0) >= condition_value:
                condition = True
            elif condition_operation == '<' and self.registers.get(condition_register,0) < condition_value:
                condition = True
            elif condition_operation == '<=' and self.registers.get(condition_register,0) <= condition_value:
                condition = True
            elif condition_operation == '==' and self.registers.get(condition_register,0) == condition_value:
                condition = True
            elif condition_operation == '!=' and self.registers.get(condition_register,0) != condition_value:
                condition = True
            if not condition:
                continue
            if register not in self.registers:
                self.registers[register] = 0
            if operation == 'inc':
                self.registers[register] += value
            elif operation == 'dec':
                self.registers[register] -= value
            highest = max(highest, max(self.registers.values()))
        return max(self.registers.values()), highest

def test1():
    largest_test,highest_test = Day08('./day08-test.input').run()
    assert largest_test == 1
    assert highest_test == 10

    largest,highest = Day08('./day08.input').run()
    assert largest == 4888
    assert highest == 7774

if __name__ == '__main__':
    print("advent of code: day08")
    largest,highest = Day08('./day08.input').run()
    print(f"part 1: {largest}")
    print(f"part 2: {highest}")
