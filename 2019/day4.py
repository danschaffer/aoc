#!/usr/bin/env python


class Password:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.passwords = 0

    def run1(self):
        self.passwords = 0
        for number in range(self.lower, self.upper + 1):
            if self.has_double(number) and self.increases(number):
                self.passwords += 1
        return self.passwords

    def run2(self):
        self.passwords = 0
        for number in range(self.lower, self.upper + 1):
            if self.has_double_2(number) and self.increases(number):
                self.passwords += 1
        return self.passwords

    def has_double_2(self, number):
        number = str(number)
        item = 0
        while item < len(number) - 1:
            if number[item] == number[item + 1]:
                if item >= len(number) - 2 or number[item + 2] != number[item]:
                    return True
                else:
                    digit = number[item]
                    item += 1
                    while item < len(number) and number[item] == digit:
                        item += 1
            else:
                item += 1
        return False

    def has_double(self, number):
        number = str(number)
        for item in range(len(number) - 1):
            if number[item] == number[item + 1]:
                return True
        return False

    def increases(self, number):
        number = str(number)
        last = int(str(number)[0])
        number = str(number)
        for digit in list(number):
            if last > int(digit):
                return False
            last = int(digit)
        return True


def test_has_double():
    p = Password(138241, 674034)
    assert(p.has_double(111111) is True)
    assert(p.has_double(111122) is True)
    assert(p.has_double(112233) is True)
    assert(p.has_double(123456) is False)


def test_has_double_2():
    p = Password(138241, 674034)
    assert(p.has_double_2(111111) is False)
    assert(p.has_double_2(111122) is True)
    assert(p.has_double_2(112233) is True)
    assert(p.has_double_2(123456) is False)
    assert(p.increases(111111) is True)
    assert(p.increases(123456) is True)
    assert(p.increases(123450) is False)


def test_increases():
    p = Password(138241, 674034)
    assert(p.increases(111111) is True)
    assert(p.increases(123456) is True)
    assert(p.increases(123450) is False)


def test_runs():
    p = Password(138241, 674034)
    assert(p.run1() == 1890)
    assert(p.run2() == 1277)


if __name__ == '__main__':
    print(f"part 1: {Password(138241, 674034).run1()}")
    print(f"part 2: {Password(138241, 674034).run2()}")
