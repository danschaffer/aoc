#!/usr/bin/env python3

class Day07:
    def __init__(self, file):
        self.data = {}
        for line in open(file).read().strip().split('\n'):
            parts = line.split()
            name = parts[0]
            value = int(parts[1][1:-1])
            children = []
            if len(parts) > 3:
                children = ''.join(parts[3:]).split(',')
            self.data[name] = {'parent':None, 'children':children, 'value':value}
        for name in self.data:
            for child in self.data[name]['children']:
                self.data[child]['parent'] = name

    def write_dot(self, file):
        source = 'digraph day7 {\nrankdir=LR;\n'
        for item in self.data:
            value = self.data[item]['value']
            total_value = self.get_value(item)
            source += f'{item} [label="{item} {value} {total_value}"];\n'
        for item in self.data:
            for child in self.data[item]['children']:
                source += f'{item}->{child};\n'
        source += '}\n'
        open(file,'w').write(source)

    def get_root(self):
        for name in self.data:
            if self.data[name]['parent'] is None:
                return name

    def get_value(self, node):
        result = self.data[node]['value']
        for child in self.data[node]['children']:
            result += self.get_value(child)
        return result

def test1():
    test_day07_test = Day07('./day07-test.input')
    assert test_day07_test.get_root() == 'tknk'
    test_day07_test.write_dot('./day07-test.dot')  # ugml was 68, should be 60
    # write to png, dot -Tpng ./day07-test.dot > day07-test.png

    test_day07 = Day07('./day07.input')
    assert test_day07.get_root() == 'qibuqqg'

if __name__ == '__main__':
    print("advent of code: day07")
    day07 = Day07('./day07.input')
    print(f"part 1: {day07.get_root()}")
    day07.write_dot('./day07.dot') # egbzge was 1086 should be 1079, parent wknuyhc, dwggjb
    # write to png, dot -Tpng ./day07.dot > day07.png
    