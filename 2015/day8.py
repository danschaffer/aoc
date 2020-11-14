#!/usr/bin/env python3

class Whitespace:
    def __init__(self):
        self.literal = 0
        self.inmemory = 0

    def parse_part1(self, str):
        self.literal += len(str)
        assert str.startswith('"') and str.endswith('"'), f"bad line '{str}'"
        str = str[1:-1]
        while str.find('\\\\') > -1:
            index = str.find('\\\\')
            str = str[0:index] + 'X' + str[index+2:]
        while str.find('\\"') > -1:
            index = str.find('\\"')
            str = str[0:index] + 'X' + str[index+2:]
        while str.find('\\x') > -1:
            index = str.find('\\x')
            str = str[0:index] + 'X' + str[index+4:]
        self.inmemory += len(str)

    def parse_part2(self, str):
        self.literal += len(str)
        str = '\\' + str.replace('\\', '\\\\').replace('"', '\\"') + '\\'
        self.inmemory += len(str)

    def load_part1(self, file):
        for line in open(file).read().strip().split('\n'):
            self.parse_part1(line)

    def load_part2(self, file):
        for line in open(file).read().strip().split('\n'):
            self.parse_part2(line)

    def get_value(self):
        return self.literal - self.inmemory

def test1():
    whitespace1 = Whitespace()
    inp1 = '""'
    whitespace1.parse_part1(inp1)
    assert whitespace1.literal == 2
    assert whitespace1.inmemory == 0
    whitespace2 = Whitespace()
    whitespace2.parse_part1('"abc"')
    assert whitespace2.get_value() == 2
    whitespace3 = Whitespace()
    whitespace3.parse_part1('"a\\\\a"')
    assert whitespace3.inmemory == 3
    whitespace4 = Whitespace()
    whitespace4.parse_part1('"a\\"a"')
    assert whitespace4.inmemory == 3
    whitespace5 = Whitespace()
    whitespace5.parse_part1('"a\\x27a"')
    assert whitespace5.inmemory == 3

def test2():
    whitespace = Whitespace()
    whitespace.load_part1('./day8.input')
    assert whitespace.get_value() == 1371

def test3():
    whitespace = Whitespace()
    whitespace.load_part2('./day8.input')
    assert whitespace.inmemory - whitespace.literal == 2117

if __name__ == '__main__':
    whitespace1 = Whitespace()
    whitespace1.load_part1('./day8.input')
    print(f"part 1 : {whitespace1.get_value()}")

    whitespace2 = Whitespace()
    whitespace2.load_part2('./day8.input')
    print(f"part 2 : {whitespace2.inmemory - whitespace2.literal}")
