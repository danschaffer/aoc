#!/usr/bin/env python3
import sys
import math
class Day11:
    def __init__(self, file):
        self.data = []
        lines = [line.strip() for line in open(file).readlines()]
        for i in range(len(lines)//7 + 1):
            items = []
            for item in lines[i*7+1].split()[2:]:
                if item.endswith(','):
                    item = item[0:-1]
                items.append(int(item))
            operations = lines[i*7+2].split()[4:]
            if operations[1] == 'old':
                op = '^2'
                op1 = 0
            else:
                op = operations[0]
                op1 = int(operations[1])
            divisible = int(lines[i*7+3].split()[3])
            throw_true = int(lines[i*7+4].split()[5])
            throw_false = int(lines[i*7+5].split()[5])
            self.data.append({'items':items,'op':op,'op1': op1, 'divisible':divisible,'throw_true': throw_true, 'throw_false': throw_false, 'inspected': 0})

    @staticmethod
    def do_operation(item, op, op1):
        if op == '+':
            result = item + op1
        elif op == '*':
            result = item * op1
        else:
            result = item * item
        return result

    def run_part1(self):
        for _ in range(20):
            for monkey in self.data:
                while monkey['items']:
                    monkey['inspected'] += 1
                    item = monkey['items'].pop(0)
                    worry = Day11.do_operation(item, monkey['op'], monkey['op1']) // 3
                    if worry % monkey['divisible'] == 0:
                        self.data[monkey['throw_true']]['items'].append(worry)
                    else:
                        self.data[monkey['throw_false']]['items'].append(worry)
        inspected = [monkey['inspected'] for monkey in self.data]
        inspected.sort(reverse=True)
        return inspected[0] * inspected[1]

    def run_part2(self):
        base = 1
        for monkey in self.data:
            base *= math.lcm(monkey['divisible'])
        for n in range(10_000):
            for monkey in self.data:
                while monkey['items']:
                    monkey['inspected'] += 1
                    item = monkey['items'].pop(0)
                    worry = Day11.do_operation(item, monkey['op'], monkey['op1'])
                    worry = worry % base
                    if worry % monkey['divisible'] == 0:
                        self.data[monkey['throw_true']]['items'].append(worry)
                    else:
                        self.data[monkey['throw_false']]['items'].append(worry)
        inspected = [monkey['inspected'] for monkey in self.data]
        inspected.sort(reverse=True)
        return inspected[0] * inspected[1]

def test1():
    test_day11 = Day11('./day11-test.input')
    assert test_day11.run_part1() == 10605
    test_day11 = Day11('./day11-test.input')
    assert test_day11.run_part2() == 2713310158

def test2():
    test_day11 = Day11('./day11.input')
    assert test_day11.run_part1() == 120056
    test_day11 = Day11('./day11.input')
    assert test_day11.run_part2() == 21816744824

if __name__ == '__main__':
    print("advent of code: day11")
    file = './day11.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day11 = Day11(file)
    print(f"part 1: {day11.run_part1()}")
    day11 = Day11(file)
    print(f"part 2: {day11.run_part2()}")
