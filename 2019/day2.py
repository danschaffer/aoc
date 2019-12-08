#!/usr/bin/env python


class Intcode:
    def __init__(self, data):
        self.data = data
        self.pointer = 0

    def run_until_halt(self):
        while self.run():
            True
        return self.data[0]

    def run(self):
        instruction = int(self.data[self.pointer])
        assert(instruction in [1, 2, 99])
        if instruction == 99:
            return False
        # add = 1 mult = 2
        if instruction == 1 or instruction == 2:
            in1 = self.data[self.pointer + 1]
            in2 = self.data[self.pointer + 2]
            out = self.data[self.pointer + 3]
            val1 = self.data[in1]
            val2 = self.data[in2]
            if instruction == 1:
                self.data[out] = val1 + val2
            elif instruction == 2:
                self.data[out] = val1 * val2
            self.pointer += 4
            return True

    def solve(self, data, answer):
        for noun in range(100):
            for verb in range(100):
                self.data = data[:]
                self.pointer = 0
                self.data[1] = noun
                self.data[2] = verb
                self.run_until_halt()
                if self.data[0] == answer:
                    return noun * 100 + verb


def test_part1():
    intcode = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    intcode.run_until_halt()
    intcode.data[3] == 70

    intcode = Intcode([1, 0, 0, 0, 99])
    intcode.run_until_halt()
    intcode.data[0] == 2

    intcode = Intcode([2, 3, 0, 3, 99])
    intcode.run_until_halt()
    intcode.data[3] == 6

    intcode = Intcode([2, 4, 4, 5, 99, 0])
    intcode.run_until_halt()
    intcode.data[5] == 9801

    intcode = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
    intcode.run_until_halt()
    intcode.data[0] == 30
    intcode.data[4] == 2


def test_part2():
    file = './day2.input'
    data = [int(num) for num in open(file).read().strip().split(',')]
    data[1] = 12
    data[2] = 2
    intcode = Intcode(data[:])
    assert(intcode.run_until_halt() == 3166704)
    assert(intcode.solve(data, 19690720) == 8018)


if __name__ == '__main__':
    file = './day2.input'
    data = [int(num) for num in open(file).read().strip().split(',')]
    data[1] = 12
    data[2] = 2
    intcode = Intcode(data[:])
    print(f"part 1: {intcode.run_until_halt()}")
    print(f"part 2: {intcode.solve(data, 19690720)}")
