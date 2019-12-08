#!/usr/bin/env python

class Map:
    def __init__(self, lines):
        self.lines = lines
        self.map = {'COM': None}
        self.load()

    def load(self):
        for line in self.lines:
            tokens = line.split(')')
            self.map[tokens[1]] = tokens[0]

    def count(self, key):
        moves = 0
        current = key
        while self.map[current]:
            moves += 1
            current = self.map[current]
        return moves

    def count_all(self):
        moves = 0
        for key in self.map.keys():
            moves += self.count(key)
        return moves

    def get_path(self, item):
        items = []
        while self.map[item]:
            items += [self.map[item]]
            item = self.map[item]
        return items

    def orbiting(self, item1, item2):
        items1 = self.get_path(item1)
        items2 = self.get_path(item2)
        items = []
        for item in items2:
            if item not in items1:
                items += [item]
        for item in items1:
            if item not in items2:
                items += [item]
        return len(items)

def test_1():
    lines = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L'
    ]
    map = Map(lines)
    assert map.count('COM') == 0
    assert map.count('D') == 3
    assert map.count('L') == 7
    assert map.count_all() == 42

def test_2():
    lines = open('./day6.input').read().strip().split('\n')
    map = Map(lines)
    assert map.count_all() == 241064

def test_3():
    lines = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
        'K)YOU',
        'I)SAN'
    ]
    map = Map(lines)
    assert(map.orbiting('YOU', 'SAN') == 4)

def test_4():
    lines = open('./day6.input').read().strip().split('\n')
    map = Map(lines)
    assert map.orbiting('YOU', 'SAN') == 418

if __name__ == '__main__':
    test_3()
    lines = open('./day6.input').read().strip().split('\n')
    map = Map(lines)
    print(f"part 1: {map.count_all()}")
    print(f"part 2: {map.orbiting('YOU', 'SAN')}")
