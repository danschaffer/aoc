#!/usr/bin/env python3
import sys

def dec_to_snafu(num):
    result = 0
    for n,ch in enumerate(num[::-1]):
        result += 5**n * {'0':0,'1':1,'2':2,'-':-1,'=':-2}[ch]
    return result

def snafu_to_dec(num):
    result = ''
    while num:
        result = str(num % 5) + result
        num //= 5
    while True:
        if result.startswith('3') or result.startswith('4'):
            result = '0' + result
        ind3 = result.find('3')
        ind4 = result.find('4')
        if max(ind3,ind4) == -1:
            break
        if ind3 > -1 and ind4 > -1:
            ind = min(ind3,ind4)
        elif ind3 == -1:
            ind = ind4
        else:
            ind = ind3
        nextc = '=-0123'
        ch0 = nextc[nextc.index(result[ind-1])+1]
        if result[ind] == '3':
            ch1 = '='
        else:
            ch1 = '-'
        result = result[0:ind-1] + ch0 + ch1 + result[ind+1:]
    return result

def parse_file(file):
    result = 0
    lines = open(file).read().split('\n')
    for line in lines:
        result += dec_to_snafu(line)
    return result

def test1():
    assert parse_file('./day25-test.input') == 4890
    assert snafu_to_dec(7) == '12'
    assert snafu_to_dec(20) == '1-0'
    assert snafu_to_dec(12345) == '1-0---0'
    assert snafu_to_dec(314159265) == '1121-1110-1=0'
    assert snafu_to_dec(4890) == '2=-1=0'

def test2():
    assert parse_file('./day25.input') == 30223327868980
    assert snafu_to_dec(30223327868980) == '2=0=02-0----2-=02-10'

if __name__ == '__main__':
    print("advent of code: day25")
    file = './day25.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    print(f"part 1: {snafu_to_dec(parse_file(file))}")
