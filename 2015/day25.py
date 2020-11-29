#!/usr/bin/env python3

def find_value(find_row, find_column, start, first, second):
    row = 1
    column = 1
    value = start
    max_row = 1
    while True:
        if row == find_row and column == find_column:
            break
        value = value * first % second
        row -= 1
        column += 1
        if row == 0:
            max_row += 1
            row = max_row
            column = 1
    return value

def test1():
    assert find_value(1, 1, 20151125, 252533, 33554393) == 20151125
    assert find_value(2, 1, 20151125, 252533, 33554393) == 31916031
    assert find_value(1, 2, 20151125, 252533, 33554393) == 18749137
    assert find_value(2, 2, 20151125, 252533, 33554393) == 21629792
    assert find_value(6, 6, 20151125, 252533, 33554393) == 27995004

if __name__ == '__main__':
    print(f"part 1: {find_value(3010, 3019, 20151125, 252533, 33554393)}")
