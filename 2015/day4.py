#!/usr/bin/env python3

import hashlib

def mine_coins(input, digits=5):
    counter = 1
    answer = ''.join(['0' for _ in range(digits)])
    while True:
        if hashlib.md5(f"{input}{counter}".encode('utf-8')).hexdigest().startswith(answer):
            break
        counter +=1
    return counter


def test1():
    assert mine_coins('abcdef') == 609043

def test2():
    assert mine_coins('pqrstuv') == 1048970

def test3():
    assert mine_coins('yzbqklnj', 5) == 282749

def test4():
    assert mine_coins('yzbqklnj', 6) == 9962624

if __name__ == '__main__':
    print(f"part 1 = {mine_coins('yzbqklnj')}")
    print(f"part 2 = {mine_coins('yzbqklnj', 6)}")