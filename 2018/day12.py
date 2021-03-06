#!/usr/bin/env python3

class Day12:
    def __init__(self, file):
        self.rules = {}
        for line in open(file).readlines():
            if line.startswith('initial state:'):
                self.initial = line.split()[2]
                continue
            if line.strip() == '':
                continue
            parts = line.split()
            self.rules[parts[0]] = parts[2]

    def run1(self, generations=20):
        offset=4
        state = '.'*offset + self.initial + '.'*20
#        print(f"{0:-2} {self.count(state):-4} {state}")
        for gen in range(generations):
            state0 = '..' 
            for n in range(len(state)-5):
                if state[n:n+5] not in self.rules:
                    state0 += '.'
                else:
                    state0 += self.rules[state[n:n+5]]
            state = state0 + '.'*4
#            print(f"{gen+1:-2} {self.count(state):-4} {state}")
        return self.count(state)

    def count(self, state, offset=4):
        result = 0
        for n in range(len(state)):
            if state[n] == '#':
                result += n-offset
        return result

def test1():
    test_day12 = Day12('./day12-test.input')
    assert test_day12.run1() == 325

    day12 = Day12('./day12.input')
    assert day12.run1() == 1696

    day12 = Day12('./day12.input')
    result = day12.run1(150)  # increases by 14 each time
    result += (50000000000 - 150)*36
    assert result == 1799999999458

if __name__ == '__main__':
    print("advent of code: day12")
    day12 = Day12('./day12.input')
    print(f"part 1: {day12.run1()}")

    day12 = Day12('./day12.input')
    result = day12.run1(150)  # increases by 14 each time
    result += (50000000000 - 150)*36
    print(f"part 1: {result}")
