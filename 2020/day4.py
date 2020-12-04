#!/usr/bin/env python3
import re
class Day4:
    def __init__(self):
        self.lines = []

    def load(self, file):
        self.lines = open(file).read().strip().split('\n') + [""]

    def matches_fields1(self, data):
        fields = sorted(data.keys())
        if fields == ['byr','cid','ecl','eyr','hcl','hgt','iyr','pid'] or fields == ['byr','ecl','eyr','hcl','hgt','iyr','pid']:
            return True
        return False

    def matches_fields2(self, data):
        for key in data.keys():
            value = data[key]
            if not self.is_valid_field(key, value):
                return False
        return True

    def is_valid_field(self, key, value):
        if key == 'byr':
            if value.isdigit() and int(value) >= 1920 and int(value) <= 2002:
                return True
        elif key == 'iyr':
            if value.isdigit() and int(value) >= 2010 and int(value) <= 2020:
                return True
        elif key == 'eyr':
            if value.isdigit() and int(value) >= 2020 and int(value) <= 2030:
                return True
        elif key == 'hgt':
            if value.endswith('cm'):
                value1 = value[:-2]
                if value1.isdigit() and int(value1) >= 150 and int(value1) <= 193:
                    return True
            if value.endswith('in'):
                value1 = value[:-2]
                if value1.isdigit() and int(value1) >= 59 and int(value1) <= 76:
                    return True
        elif key == 'hcl':
            return not re.match('#[a-f0-9]{6}$', value) is None
        elif key == 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            return len(value) == 9 and value.isdigit()
        elif key == 'cid':
            return True
        return False

    def run(self, part2=False):
        count = 0
        data = {}
        line = ""
        for line in self.lines:
            if line.strip() == "":
                if self.matches_fields1(data) and (not part2 or self.matches_fields2(data)):
                    count +=1
                data = {}
            else:
                for token in line.split():
                    key,value = token.split(":")
                    data[key] = value
        return count

def test1():
    test_day4 = Day4()
    test_day4.load('./day4-test.input')
    assert test_day4.run() == 2

    assert test_day4.is_valid_field('byr', '2002')
    assert not test_day4.is_valid_field('byr', '2003')

    assert test_day4.is_valid_field('hgt', '60in')
    assert test_day4.is_valid_field('hgt', '190cm')
    assert not test_day4.is_valid_field('hgt', '190in')
    assert not test_day4.is_valid_field('hgt', '190')

    assert test_day4.is_valid_field('hcl', '#123abc')
    assert not test_day4.is_valid_field('hcl', '#123abz')
    assert not test_day4.is_valid_field('hcl', '123abc')

    assert test_day4.is_valid_field('ecl', 'brn')
    assert not test_day4.is_valid_field('ecl', 'wat')

    assert test_day4.is_valid_field('pid', '000000001')
    assert not test_day4.is_valid_field('pid', '01234567890')

def test2():
    test_day4 = Day4()
    test_day4.load('./day4-test2.input')
    assert test_day4.run(part2=True) == 4

def test3():
    test_day4 = Day4()
    test_day4.load('./day4.input')
    assert test_day4.run() == 226
    assert test_day4.run(part2=True) == 160


if __name__ == '__main__':
    day4 = Day4()
    day4.load('./day4.input')
    print(f"part 1: {day4.run()}")
    print(f"part 2: {day4.run(part2=True)}")
