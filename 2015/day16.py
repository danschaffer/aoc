#!/usr/bin/env python

class AuntSue:
    def __init__(self):
        self.data = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1,
        }
    def run(self, file, part2=False):
        matches = []
        for line in open(file).read().strip().split('\n'):
            (_, number, field1, value1, field2, value2, field3, value3) = line.split()
            number = int(number[:-1])
            field1 = field1[:-1]
            value1 = int(value1[:-1])
            field2 = field2[:-1]
            value2 = int(value2[:-1])
            field3 = field3[:-1]
            value3 = int(value3)
            if self.matches(field1, value1, part2) and self.matches(field2, value2, part2) and self.matches(field3, value3, part2):
                matches += [number]
        assert len(matches) == 1
        return matches[0]

    def matches(self, field, value, part2=False):
        if part2 and (field == 'cats' or field == 'trees'):
            return value > self.data[field]
        if part2 and (field == 'pomeranians' or field == 'goldfish'):
            return value < self.data[field]
        return self.data[field] == value

def test1():
    sue = AuntSue()
    assert sue.run('./day16.input') == 373
    assert sue.run('./day16.input', part2=True) == 260

if __name__ == '__main__':
    sue = AuntSue()
    print(f"part 1: {sue.run('./day16.input')}")
    print(f"part 2: {sue.run('./day16.input', part2=True)}")
