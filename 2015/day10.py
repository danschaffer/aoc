#!/usr/bin/env python3

class LookAndSay:
    def __init__(self, value):
        self.value = value

    def do_round(self):
        index = 0
        newvalue = ''
        while index < len(self.value):
            ctr = 0
            while index + ctr < len(self.value) and self.value[index] == self.value[index + ctr]:
                ctr += 1
            newvalue += f"{ctr}{self.value[index]}"
            index += ctr
        self.value = newvalue

    def do_rounds(self, n):
        for _ in range(n):
            self.do_round()

    def get_value(self):
        return self.value

    def get_len(self):
        return len(self.value)

def test1():
    look = LookAndSay('1')
    look.do_round()
    assert look.get_value() == '11'
    look.do_round()
    assert look.get_value() == '21'
    look.do_round()
    assert look.get_value() == '1211'
    look.do_round()
    assert look.get_value() == '111221'

def test2():
    look = LookAndSay('1113122113')
    look.do_rounds(40)
    assert look.get_len() == 360154
    look.do_rounds(10)
    assert look.get_len() == 5103798

if __name__ == '__main__':
    look = LookAndSay('1113122113')
    look.do_rounds(40)
    print(f"part 1: {look.get_len()}")
    look.do_rounds(10)
    print(f"part 2: {look.get_len()}")
