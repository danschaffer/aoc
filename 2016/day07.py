#!/usr/bin/env python3

def is_line_valid(line,part2=False):
    index = 0
    strings0 = []
    strings1 = []
    while line.find('[',index) > -1:
        index0 = line.find('[',index)
        strings0.append(line[index:index0])
        index1 = line.find(']', index)
        strings1.append(line[index0+1:index1])
        index = index1 + 1
    strings0.append(line[index:])
    if not part2:
        is_valid = False
        for string in strings1:
            if is_string_valid1(string):
                is_valid = True
                break
        if is_valid:
            return False
        for string in strings0:
            if is_string_valid1(string):
                return True
        return False
    else:
        for string in strings0:
            abas = get_aba(string)
            for aba in abas:
                if get_bab(aba) in strings1:
                    return True
        return False

def get_bab(string):
    return string[1]+string[0]+string[1]

def get_aba(string):
    results = []
    for index in range(len(string)-2):
        if string[index] == string[index+2]:
            results.append(string[index:index+2])
    return results

def is_string_valid1(string):
    result=False
    for index in range(len(string)-3):
        if string[index]+string[index+1] == string[index+3]+string[index+2] and string[index] != string[index+1]:
            result=True
    return result

def run_part1(file):
    return sum([1 for line in open(file).read().strip().split('\n') if is_line_valid(line)])

def run_part2(file):
    return sum([1 for line in open(file).read().strip().split('\n') if is_line_valid(line,part2=True)])

def test1():
    assert is_line_valid('abba[mnop]qrst')
    assert is_line_valid('abcd[bddb]xyyx') is False
    assert run_part1('./day07-test.input') == 2
    assert run_part1('./day07.input') == 105
    assert run_part2('./day07-test2.input') == 3

if __name__ == '__main__':
    print("advent of code: day07")
    print(f"part 1: {run_part1('./day07.input')}")
    print(f"part 2: {run_part2('./day07.input')}")
