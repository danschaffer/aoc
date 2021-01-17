#!/usr/bin/env python3
import hashlib
def get_password_part1(seed):
    password = ''
    num = 0
    for _ in range(8):
        while hashlib.md5((seed + str(num)).encode('utf-8')).hexdigest().startswith('00000') == False:
            num += 1
        password += hashlib.md5((seed + str(num)).encode('utf-8')).hexdigest()[5]
        num += 1
    return password

def get_password_part2(seed):
    password = '        '
    num = 0
    while ' ' in password:
        while hashlib.md5((seed + str(num)).encode('utf-8')).hexdigest().startswith('00000') == False:
            num += 1
        index = hashlib.md5((seed + str(num)).encode('utf-8')).hexdigest()[5]
        char = hashlib.md5((seed + str(num)).encode('utf-8')).hexdigest()[6]
        if index.isdigit() and int(index) < 8 and password[int(index)] == ' ':
            password = password[0:int(index)] + char + password[int(index)+1:]
        num += 1
#        print(f'{index} {char} {password}')
    return password

def test1():
    assert get_password_part1('abc') == '18f47a30'
    assert get_password_part1('reyedfim') == 'f97c354d'
    assert get_password_part2('abc') == '05ace8e3'
    assert get_password_part2('reyedfim') == '863dde27'

if __name__ == '__main__':
    print("advent of code: day05")
    print(f"part 1: {get_password_part1('reyedfim')}")
    print(f"part 2: {get_password_part2('reyedfim')}")
