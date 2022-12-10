#!/usr/bin/env python3
import sys
class Day10:
    def __init__(self, file):
        self.regs = []
        self.noops = []
        self.data = open(file).readlines()
        for n, line in enumerate(self.data):
            line = line.strip()
            parts = line.split()
            if len(parts) == 1:
                self.noops.append(n)
            else:
                self.regs.append(int(parts[1]))

    def get_strength(self, n):
        answer = 1
        ctr = 0
        sigctr = 0
        index = 0
        while ctr < n:
            if index in self.noops:
                ctr += 1
            else:
                if ctr + 2 < n:
                    answer += self.regs[sigctr]
                    sigctr += 1
                ctr += 2
            index += 1
        return answer

    def run_part1(self):
        answer = 0
        for signal in [20, 60, 100, 140, 180, 220]:
            answer += signal * self.get_strength(signal)
        return answer

    def run_part2(self):
        output = ""
        cycle = 1
        x = 1
        index = 0
        while cycle < 240:
            if abs(((cycle - 1) % 40) - x) <= 1:
                output += "#"
            else:
                output += "."
            cycle += 1
            if self.data[index].strip() != 'noop':
                if abs(((cycle - 1) % 40) - x) <= 1:
                    output += "#"
                else:
                    output += "."
                cycle += 1
                x += int(self.data[index].split()[1])
            index += 1
            print(f"{cycle}: cycle {index} index x {x}")
            print(output)
            print(self.data[index].strip())
        return output[0:40] + '\n' + output[40:80] + '\n' + output[80:120] + '\n' + output[120:160] + '\n' + output[160:200] + '\n' + output[200:240] + '\n'
            
def test1():
    test_day10 = Day10('./day10-test.input')
    assert test_day10.run_part1() == 13140

def test2():
    test_day10 = Day10('./day10.input')
    assert test_day10.run_part1() == 11220

if __name__ == '__main__':
    print("advent of code: day10")
    file = './day10-test.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day10 = Day10(file)
    print(f"part 1: {day10.run_part1()}")
    print(f"part 2: \n{day10.run_part2()}") # BZPAJELK
