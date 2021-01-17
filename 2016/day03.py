#!/usr/bin/env python3

def is_valid_triangle(line):
    sides=[int(side) for side in line.split()]
    return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

def count_triangles1(file):
    return sum([1 for line in open(file).read().strip().split('\n') if is_valid_triangle(line)])

def count_triangles2(file):
    result = 0
    lines = open(file).read().strip().split('\n')
    for count in range(len(lines)//3):
        line1 = lines[count*3+0].split()
        line2 = lines[count*3+1].split()
        line3 = lines[count*3+2].split()
        if is_valid_triangle(f"{line1[0]} {line2[0]} {line3[0]}"):
            result += 1
        if is_valid_triangle(f"{line1[1]} {line2[1]} {line3[1]}"):
            result += 1
        if is_valid_triangle(f"{line1[2]} {line2[2]} {line3[2]}"):
            result += 1
    return result

def test1():
    assert is_valid_triangle('5 10 25') is False
    assert count_triangles1('./day03.input') == 982
    assert count_triangles2('./day03.input') == 1826

if __name__ == '__main__':
    print("advent of code: day3")
    print(f"part1: {count_triangles1('./day03.input')}")
    print(f"part2: {count_triangles2('./day03.input')}")
