#!/usr/bin/env python


class Wires:
    def __init__(self, data1, data2):
        self.data = []
        self.add_data(data1)
        self.add_data(data2)

    def man_dist(self, pair):
        return abs(pair[0]) + abs(pair[1])

    def find_best(self):
        data1 = self.data[0]
        data2 = self.data[1]
        matches = []
        for d1 in data1:
            for d2 in data2:
                if d1[0] == d2[0] and d1[1] == d2[1]:
                    d1 = (d1[0], d1[1], d1[2] + d2[2])
                    print(f"match {d1} dist={self.man_dist(d1)} steps={d1[2]}")
                    matches += [d1]
                    break
        matches1 = []
        matches2 = []
        for match in matches:
            matches1 += [self.man_dist(match)]
            matches2 += [match[2]]
        matches1 = sorted(matches1)
        matches2 = sorted(matches2)
        return matches1[0], matches2[0]

    def add_data(self, items):
        x = 0
        y = 0
        data = []
        steps = 0
        for item in items:
            dir = item[0]
            assert dir in ['R', 'L', 'U', 'D']
            num = int(item[1:])
            if dir == 'R':
                for n in range(num):
                    steps += 1
                    x += 1
                    data += [(x, y, steps)]
            elif dir == 'L':
                for n in range(num):
                    steps += 1
                    x -= 1
                    data += [(x, y, steps)]
            elif dir == 'U':
                for n in range(num):
                    steps += 1
                    y += 1
                    data += [(x, y, steps)]
            elif dir == 'D':
                for n in range(num):
                    steps += 1
                    y -= 1
                    data += [(x, y, steps)]
        self.data += [data]


def test_wires_man():
    wire1 = ['R8', 'U5', 'L5', 'D3']
    wire2 = ['U7', 'R6', 'D4', 'L4']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[0] == 6)

    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[0] == 159)

    wire1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[0] == 135)


def test_wires_steps():
    wire1 = ['R8', 'U5', 'L5', 'D3']
    wire2 = ['U7', 'R6', 'D4', 'L4']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[1] == 30)

    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[1] == 610)

    wire1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    wires = Wires(wire1, wire2)
    assert(wires.find_best()[1] == 410)


if __name__ == '__main__':
    lines = open('./day3.input').read().split('\n')
    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')
    wires = Wires(wire1, wire2)
    man, steps = wires.find_best()
    print(f"part 1: {man} shortest manhattan distance ")
    print(f"part 2: {steps} shortest steps ")
