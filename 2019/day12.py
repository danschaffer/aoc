#!/usr/bin/env python

class Moon:
    def __init__(self, coords):
        self.pos = [int(x) for x in coords]
        self.vel = [0, 0, 0]

def energy(moons):
    return sum([sum(map(abs, m.pos)) * sum(map(abs, m.vel)) for m in moons])

def lcm(x, y):
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y

def test_1():
    moons_coord = [
        (-1, 0, 2),
        (2, -10, -7),
        (4, -8, 8),
        (3, 5, -1)
    ]
    moons = [Moon(m) for m in moons_coord]
    for t in range(10):
        for moon in moons:
            for other_moon in moons:
                for i in range(3):
                    if moon.pos[i] < other_moon.pos[i]:
                        moon.vel[i] += 1
                    elif moon.pos[i] > other_moon.pos[i]:
                        moon.vel[i] += -1
        for moon in moons:
            for i in range(3):
                moon.pos[i] += moon.vel[i]
    assert energy(moons) == 179

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

if __name__ == '__main__':
#    moons_coord = [
#        (-1, 0, 2),
#        (2, -10, -7),
#        (4, -8, 8),
#        (3, 5, -1)
#    ]
    moons_coord = [
        (-4, -9, -3),
        (-13, -11, 0),
        (-17, -7, 15),
        (-16, 4, 2)
    ]
    moons = [Moon(m) for m in moons_coord]
#    for t in range(10):
    for t in range(1000):
        for moon in moons:
            for other_moon in moons:
                for i in range(3):
                    if moon.pos[i] < other_moon.pos[i]:
                        moon.vel[i] += 1
                    elif moon.pos[i] > other_moon.pos[i]:
                        moon.vel[i] += -1
        for moon in moons:
            for i in range(3):
                moon.pos[i] += moon.vel[i]
    print(f"part 1: {energy(moons)}")

    moons = [Moon(m) for m in moons_coord]
    x_states, y_states, z_states = set(), set(), set()
    while True:
        for moon in moons:
            for other_moon in moons:
                for i in range(3):
                    if moon.pos[i] < other_moon.pos[i]:
                        moon.vel[i] += 1
                    elif moon.pos[i] > other_moon.pos[i]:
                        moon.vel[i] += -1
        for moon in moons:
            for i in range(3):
                moon.pos[i] += moon.vel[i]
        x_state = tuple((m.pos[0], m.vel[0]) for m in moons)
        y_state = tuple((m.pos[1], m.vel[1]) for m in moons)
        z_state = tuple((m.pos[2], m.vel[2]) for m in moons)
        if x_state in x_states and y_state in y_states and z_state in z_states:
            break
        x_states.add(x_state)
        y_states.add(y_state)
        z_states.add(z_state)
    print(f"part 2: {lcm(len(x_states), lcm(len(y_states), len(z_states)))}")