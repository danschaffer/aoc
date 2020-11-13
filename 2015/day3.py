#!/usr/bin/env python3

class HousePresents:
    def __init__(self, input):
        self.input = input
        self.data = {(0,0): 1}
        self.location = (0, 0)

    def deliver(self):
        for move in list(self.input):
            self.update_location(move)
            if self.location not in self.data:
                self.data[self.location] = 1
            else:
                self.data[self.location] += 1

    def run(self):
        self.deliver()
        return len(self.data.keys())

    def update_location(self, move):
        assert move in ['^','v','<','>']
        if move == '^':
            self.location = (self.location[0], self.location[1] + 1)
        elif move == 'v':
            self.location = (self.location[0], self.location[1] - 1)
        elif move == '>':
            self.location = (self.location[0] + 1, self.location[1])
        else:
            self.location = (self.location[0] - 1, self.location[1])

def part1(input):
    return HousePresents(input).run()

def part2(input):
    santa = ''
    robot_santa = ''
    for ch in range(len(input)):
        if ch % 2 == 0:
            santa += input[ch]
        else:
            robot_santa += input[ch]
    santa1 = HousePresents(santa)
    santa1.deliver()
    santa2 = HousePresents(robot_santa)
    santa2.deliver()
    santa1.data.update(santa2.data)
    return len(santa1.data.keys())

def test1():
    assert part1('') == 1
    assert part2('') == 1

def test2():
    assert part1('^') == 2
    assert part1('^') == 2

def test3():
    assert part1('^>v<') == 4
    assert part2('^>v<') == 3

def test4():
    assert part1('^v^v^v^v^v') == 2
    assert part2('^v^v^v^v^v') == 11

def test5():
    input = open('day3.input').read().strip()
    assert part1(input) == 2565
    assert part2(input) == 2639

if __name__ == '__main__':
    input = open('day3.input').read().strip()
    print(f"part 1 = {part1(input)}")
    print(f"part 2 = {part2(input)}")
