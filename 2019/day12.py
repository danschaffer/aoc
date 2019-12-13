#!/usr/bin/env python

class Moons:
    def __init__(self, positions):
        self.positions = positions
        self.velocity = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        self.cache = []

    def calc_velocity(self, p1, p2):
        if p1 < p2:
            return 1
        if p1 > p2:
            return -1
        return 0

    def calculate_energy(self):
        total = 0
        for n in range(4):
            pot = abs(self.positions[n][0]) + abs(self.positions[n][1]) + abs(self.positions[n][2])
            kin = abs(self.velocity[n][0]) + abs(self.velocity[n][1]) + abs(self.velocity[n][2])
            total += pot * kin
        return total

    def update_position(self):
        for n in range(4):
            self.positions[n] = (self.positions[n][0] + self.velocity[n][0], self.positions[n][1] + self.velocity[n][1], self.positions[n][2] + self.velocity[n][2])

    def to_str(self):
        out = ''
        for n in range(4):
            out += f"{self.positions[n][0]}{self.positions[n][1]}{self.positions[n][2]}{self.velocity[n][0]}{self.velocity[n][1]}{self.velocity[n][2]}"
        return out

    def set_velocity(self):
        x = self.velocity[0][0] + self.calc_velocity(self.positions[0][0], self.positions[1][0]) + self.calc_velocity(self.positions[0][0], self.positions[2][0]) + self.calc_velocity(self.positions[0][0], self.positions[3][0])
        y = self.velocity[0][1] + self.calc_velocity(self.positions[0][1], self.positions[1][1]) + self.calc_velocity(self.positions[0][1], self.positions[2][1]) + self.calc_velocity(self.positions[0][1], self.positions[3][1])
        z = self.velocity[0][2] + self.calc_velocity(self.positions[0][2], self.positions[1][2]) + self.calc_velocity(self.positions[0][2], self.positions[2][2]) + self.calc_velocity(self.positions[0][2], self.positions[3][2])
        self.velocity[0] = (x, y, z)
        x = self.velocity[1][0] + self.calc_velocity(self.positions[1][0], self.positions[0][0]) + self.calc_velocity(self.positions[1][0], self.positions[2][0]) + self.calc_velocity(self.positions[1][0], self.positions[3][0])
        y = self.velocity[1][1] + self.calc_velocity(self.positions[1][1], self.positions[0][1]) + self.calc_velocity(self.positions[1][1], self.positions[2][1]) + self.calc_velocity(self.positions[1][1], self.positions[3][1])
        z = self.velocity[1][2] + self.calc_velocity(self.positions[1][2], self.positions[0][2]) + self.calc_velocity(self.positions[1][2], self.positions[2][2]) + self.calc_velocity(self.positions[1][2], self.positions[3][2])
        self.velocity[1] = (x, y, z)
        x = self.velocity[2][0] + self.calc_velocity(self.positions[2][0], self.positions[0][0]) + self.calc_velocity(self.positions[2][0], self.positions[1][0]) + self.calc_velocity(self.positions[2][0], self.positions[3][0])
        y = self.velocity[2][1] + self.calc_velocity(self.positions[2][1], self.positions[0][1]) + self.calc_velocity(self.positions[2][1], self.positions[1][1]) + self.calc_velocity(self.positions[2][1], self.positions[3][1])
        z = self.velocity[2][2] + self.calc_velocity(self.positions[2][2], self.positions[0][2]) + self.calc_velocity(self.positions[2][2], self.positions[1][2]) + self.calc_velocity(self.positions[2][2], self.positions[3][2])
        self.velocity[2] = (x, y, z)
        x = self.velocity[3][0] + self.calc_velocity(self.positions[3][0], self.positions[0][0]) + self.calc_velocity(self.positions[3][0], self.positions[1][0]) + self.calc_velocity(self.positions[3][0], self.positions[2][0])
        y = self.velocity[3][1] + self.calc_velocity(self.positions[3][1], self.positions[0][1]) + self.calc_velocity(self.positions[3][1], self.positions[1][1]) + self.calc_velocity(self.positions[3][1], self.positions[2][1])
        z = self.velocity[3][2] + self.calc_velocity(self.positions[3][2], self.positions[0][2]) + self.calc_velocity(self.positions[3][2], self.positions[1][2]) + self.calc_velocity(self.positions[3][2], self.positions[2][2])
        self.velocity[3] = (x, y, z)

def test_1():
    positions = [
        (-1, 0, 2),
        (2, -10, -7),
        (4, -8, 8),
        (3, 5, -1)
    ]
    moons = Moons(positions)
    moons.set_velocity()
    moons.update_position()
    assert(moons.velocity[0] == ( 3, -1, -1))
    assert(moons.velocity[1] == ( 1,  3,  3))
    assert(moons.velocity[2] == (-3,  1, -3))
    assert(moons.velocity[3] == (-1, -3,  1))

def test_2():
    positions = [
        (-1, 0, 2),
        (2, -10, -7),
        (4, -8, 8),
        (3, 5, -1)
    ]
    moons = Moons(positions)
    for _ in range(10):
        moons.set_velocity()
        moons.update_position()
    assert moons.calculate_energy() == 179

def test_3():
    positions = [
        (-8, -10, 0),
        (5, 5, 10),
        (2, -7, 3),
        (9, -8, -3)
    ]
    moons = Moons(positions)
    for _ in range(100):
        moons.set_velocity()
        moons.update_position()
    assert moons.calculate_energy() == 1940

def test_4():
    positions = [
        (-8, -10, 0),
        (5, 5, 10),
        (2, -7, 3),
        (9, -8, -3)
    ]
    moons = Moons(positions)
    steps = 0
    while True:
        moons.set_velocity()
        moons.update_position()
        if {'p':{moons.positions},'v':{moons.velocity}} in self.cache:
            print("done in {steps}")
            break
        steps += 1

if __name__ == '__main__':
    positions = [
        (-4, -9, -3),
        (-13, -11, 0),
        (-17, -7, 15),
        (-16, 4, 2)
    ]
    moons = Moons(positions)
    for _ in range(1000):
        moons.set_velocity()
        moons.update_position()
    print(f"input 1: {moons.calculate_energy()}")

    positions = [
        (-8, -10, 0),
        (5, 5, 10),
        (2, -7, 3),
        (9, -8, -3)
    ]
    moons = Moons(positions)
    steps = 0
    while True:
        moons.set_velocity()
        moons.update_position()
#        print(moons.to_str())
        if moons.to_str() in moons.cache:
            print(f"done in {steps}")
            break
        steps += 1
        moons.cache += [moons.to_str()]
        if (steps % 10000) == 0:
            print(steps)
