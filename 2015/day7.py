#!/usr/bin/env python3

class Circuit:
    def __init__(self):
        self.data = {}
        self.statements = {}

    def load(self, file):
        self.parse(open(file).read().split('\n'))

    def get_tokens(self, lst):
        tokens = []
        for tok in lst:
            if tok.isalpha():
                tokens += [tok]
        return tokens

    def has_all(self, tokens):
        for token in tokens:
            if token not in self.data.keys():
                return False
        return True

    def parse_line(self, line):
        tokens = line.split()
        if tokens[1] == '->':
            self.statements[line] = self.get_tokens([tokens[0]])
        elif tokens[1] == 'AND':
            self.statements[line] = self.get_tokens([tokens[0], tokens[2]])
        elif tokens[1] == 'OR':
            self.statements[line] = self.get_tokens([tokens[0], tokens[2]])
        elif tokens[1] == 'LSHIFT':
            self.statements[line] = self.get_tokens([tokens[0], tokens[2]])
        elif tokens[1] == 'RSHIFT':
            self.statements[line] = self.get_tokens([tokens[0], tokens[2]])
        elif tokens[0] == 'NOT':
            self.statements[line] = self.get_tokens([tokens[1]])

    def parse(self, lines):
        for line in lines:
            self.parse_line(line)
        while len(self.statements.keys()) > 0:
            for statement in self.statements.keys():
                if self.has_all(self.statements[statement]):
                    self.process_line(statement)
                    self.statements.pop(statement)
                    break

    def get_value(self, key):
        if key in self.data.keys():
            return self.data[key]
        elif key.isalpha():
            assert False, f"not value for {key}"
        else:
            return int(key)

    def show_values(self):
        for value in self.data.keys():
            print(f"{value}: {self.data[value]}")
    
    def process_line(self, line):
        tokens = line.split()
        if tokens[1] == '->':
            self.data[tokens[2]] = self.get_value(tokens[0])
        elif tokens[1] == 'AND':
            self.data[tokens[4]] = (self.get_value(tokens[0]) & self.get_value(tokens[2])) % pow(2, 16)
        elif tokens[1] == 'OR':
            self.data[tokens[4]] = (self.get_value(tokens[0]) | self.get_value(tokens[2])) % pow(2, 16)
        elif tokens[1] == 'LSHIFT':
            self.data[tokens[4]] = (self.get_value(tokens[0]) << self.get_value(tokens[2])) % pow(2, 16)
        elif tokens[1] == 'RSHIFT':
            self.data[tokens[4]] = (self.get_value(tokens[0]) >> self.get_value(tokens[2])) % pow(2, 16)
        elif tokens[0] == 'NOT':
            self.data[tokens[3]] = ~self.get_value(tokens[1]) % pow(2, 16)
        else:
            assert False, f"could not parse {line}"

def test1():
    circuit = Circuit()
    circuit.process_line('123 -> x')
    assert circuit.get_value('x') == 123
    circuit.process_line('456 -> y')
    assert circuit.get_value('y') == 456
    circuit.process_line('x AND y -> d')
    assert circuit.get_value('d') == 72
    circuit.process_line('x OR y -> e')
    assert circuit.get_value('e') == 507
    circuit.process_line('x LSHIFT 2 -> f')
    assert circuit.get_value('f') == 492
    circuit.process_line('y RSHIFT 2 -> g')
    assert circuit.get_value('g') == 114
    circuit.process_line('NOT x -> h')
    assert circuit.get_value('h') == 65412
    circuit.process_line('NOT y -> i')
    assert circuit.get_value('i') == 65079

def test2():
    circuit = Circuit()
    circuit.load('day7.input')
    assert circuit.get_value('a') == 46065
    circuit.data = {'b': 46065}
    circuit.load('day7.input')
    assert circuit.get_value('a') == 14134

if __name__ == '__main__':
    circuit = Circuit()
    circuit.load('day7.input')
    a = circuit.get_value('a')
    print(f"part 1: {a}")
    circuit.data = {'b': a}
    circuit.load('day7.input')
    print(f"part 2: {circuit.get_value('a')}")
