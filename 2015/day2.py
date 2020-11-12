#!/usr/bin/env python

def get_wrapping_list(wrap_list):
    return sum([get_wrapping(wrap) for wrap in wrap_list])

def get_wrapping(dimensions):
    dims = sorted([int(n) for n in dimensions.split('x')])
    return 2 * dims[0] * dims[1] + 2 * dims[1] * dims[2] + 2 * dims[0] * dims[2] + dims[0] * dims[1]

def get_ribbon_list(wrap_list):
    return sum([get_ribbon(wrap) for wrap in wrap_list])

def get_ribbon(dimensions):
    dims = sorted([int(n) for n in dimensions.split('x')])
    return dims[0] + dims[0] + dims[1] + dims[1] + dims[0] * dims[1] * dims[2]

def test_1():
    assert get_wrapping('2x3x4') == 58
    assert get_wrapping('1x1x10') == 43
    assert get_wrapping_list(['2x3x4', '1x1x10']) == 101

def test_2():
    assert get_ribbon('2x3x4') == 34
    assert get_ribbon('1x1x10') == 14
    assert get_ribbon_list(['2x3x4', '1x1x10']) == 48

if __name__ == '__main__':
    data = open('./day2.input').read().strip().split('\n')
    print(f"part 1: {get_wrapping_list(data)}")
    print(f"part 2: {get_ribbon_list(data)}")
