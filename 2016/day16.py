#!/usr/bin/env python
import time
def step1(a):
    b = a[::-1].replace('0','x').replace('1','0').replace('x','1')
    return a + '0' + b

def checksum(s):
    while len(s) % 2 == 0:
        index = 0
        s0 = ''
        while index < len(s):
            if s[index] == s[index+1]:
                s0 += '1'
            else:
                s0 += '0'
            index += 2
        s = s0
    return s

def day16(s, length_):
    while len(s) < length_:
        s = step1(s)
    s = s[:length_]
    s = checksum(s)
    return s

def test1():
    assert step1('1') == '100'
    assert step1('0') == '001'
    assert step1('11111') == '11111000000'
    assert step1('111100001010') == '1111000010100101011110000'
    assert checksum('110010110100') == '100'
    assert day16('10000', 20) == '01100'

def test2():
    assert day16('11100010111110100', 272) == '10100011010101011'
    assert day16('11100010111110100', 35651584) == '01010001101011001'

if __name__ == '__main__':
    print("advent of code: day16")
    print(f"part1: {day16('11100010111110100', 272)}")
    start = time.time()
    print(f"part2: {day16('11100010111110100', 35651584)} {round(time.time()-start,1)}s")
