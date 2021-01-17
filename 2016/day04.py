#!/usr/bin/env python3

def is_real_room(line):
    data = {}
    line0, checksum = line.split('[')
    checksum = checksum[:-1]
    tokens = line0.split('-')
    sector = int(tokens[-1])
    letters = ''.join(tokens[:-1])
    for letter in letters:
        if letter not in data:
            data[letter] = 1
        else:
            data[letter] += 1
    data0 = {}
    for key in data:
        if data[key] not in data0:
            data0[data[key]] = []
        data0[data[key]].append(key)
    keys = sorted(data0.keys(), reverse=True)
    actual_checksum = ''
    for key in keys:
        actual_checksum += ''.join(sorted(data0[key]))
    if checksum == actual_checksum[0:5]:
        return sector
    else:
        return 0

def decrypt_name(line):
    line0, checksum = line.split('[')
    checksum = checksum[:-1]
    tokens = line0.split('-')
    sector = int(tokens[-1])
    name = '-'.join(tokens[0:-1])
    decrypted = ''
    for ch in name:
        if ch == '-':
            decrypted += ' '
        else:
            letter = ord(ch) - 97
            decrypted += chr(97+(letter + sector) % 26)
    return decrypted

def part1():
    return sum([is_real_room(line) for line in open('./day04.input').read().strip().split('\n')])

def part2():
    for line in open('./day04.input').read().strip().split('\n'):
        if is_real_room(line) > 0:
            name = decrypt_name(line)
            if 'northpole' in name:
                answer = line.split('[')[0].split('-')[-1]
                # print(f'{line} {decrypt_name(line)}')
                return int(answer)

def test1():
    assert is_real_room('aaaaa-bbb-z-y-x-123[abxyz]') == 123
    assert is_real_room('a-b-c-d-e-f-g-h-987[abcde]') == 987
    assert is_real_room('not-a-real-room-404[oarel]') == 404
    assert is_real_room('totally-real-room-200[decoy]') == 0
    assert is_real_room('qzmt-zixmtkozy-ivhz-343[zimth]') == 343
    assert decrypt_name('qzmt-zixmtkozy-ivhz-343[zimth]') == 'very encrypted name'
    assert part1() == 361724
    assert part2() == 482

if __name__ == '__main__':
    print("day4")
    print(f"part1 : {part1()}")
    print(f"part2 : {part2()}")