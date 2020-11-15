#!/usr/bin/env python3
import json

class Accounting:
    def __init__(self):
        self.sum = 0

    def load_file(self, file):
        data = json.loads(open(file).read())
        self.parse(data)

    def load(self, line):
        data = json.loads(line)
        self.parse(data)

    def load_file2(self, file):
        data = json.loads(open(file).read())
        self.parse_part2(data)

    def load2(self, line):
        data = json.loads(line)
        self.parse_part2(data)

    def parse(self, obj):
        if type(obj) == int:
            self.sum += obj
        elif type(obj) == str:
            pass
        elif type(obj) == list:
            for item in obj:
                self.parse(item)
        elif type(obj) == dict:
            for key in obj.keys():
                self.parse(obj[key])
        else:
            assert False, f"unknown type {type(obj)} on {obj}"

    def parse_part2(self, obj):
        if type(obj) == int:
            self.sum += obj
        elif type(obj) == str:
            pass
        elif type(obj) == list:
            for item in obj:
                self.parse_part2(item)
        elif type(obj) == dict:
            if "red" not in obj.values():
                for key in obj.keys():
                    self.parse_part2(obj[key])
        else:
            assert False, f"unknown type {type(obj)} on {obj}"

def test1():
    account = Accounting()
    account.load("[1,2,3]")
    assert account.sum == 6
    account.sum = 0
    account.load('{"a":2,"b":4}')
    assert account.sum == 6
    account.sum = 0
    account.load('{"a":2,"b":4}')
    assert account.sum == 6
    account.sum = 0
    account.load('[[[3]]]')
    assert account.sum == 3
    account.sum = 0
    account.load('{"a":{"b":4},"c":-1}')
    assert account.sum == 3
    account.sum = 0
    account.load('{"a":[-1,1]}')
    assert account.sum == 0
    account.sum = 0
    account.load('[-1,{"a":1}]')
    assert account.sum == 0
    account.sum = 0
    account.load('{}')
    assert account.sum == 0
    account.sum = 0
    account.load('[]')
    assert account.sum == 0
    account.sum = 0

    account.load2('[1,{"c":"red","b":2},3]')
    assert account.sum == 4

def test2():
    account = Accounting()
    account.load_file('./day12.input')
    assert account.sum == 156366
    account.sum = 0
    account.load_file2('./day12.input')
    assert account.sum == 96852

if __name__ == '__main__':
    account = Accounting()
    account.load_file('./day12.input')
    print(f"part 1: {account.sum}")

    account2 = Accounting()
    account2.load_file2('./day12.input')
    print(f"part 2: {account2.sum}")
