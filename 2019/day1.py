#!/usr/bin/env python


def get_fuel(mass):
    return mass // 3 - 2


def solve_fuel(mass_list):
    return sum([get_fuel(int(mass)) for mass in mass_list])


def get_fuel_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel_fuel(fuel)


def solve_fuel_fuel(mass_list):
    return sum([get_fuel_fuel(int(mass)) for mass in mass_list])


def test_part1():
    assert get_fuel(12) == 2
    assert get_fuel(14) == 2
    assert get_fuel(1969) == 654
    assert get_fuel(100756) == 33583


def test_part2():
    assert get_fuel_fuel(14) == 2
    assert get_fuel_fuel(1969) == 966
    assert get_fuel_fuel(100756) == 50346


if __name__ == '__main__':
    inputs = open('day1.input').read().strip().split('\n')
    print(f"part 1: {solve_fuel(inputs)}")

    inputs = open('day1.input').read().strip().split('\n')
    print(f"part 2: {solve_fuel_fuel(inputs)}")
