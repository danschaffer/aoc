#!/usr/bin/env python3
from itertools import permutations
class Table:
    def __init__(self):
        self.people = set()
        self.happiness = {}

    def load(self, file):
        self.add_lines(open(file).read().strip().split('\n'))
        
    def add_lines(self, lines):
        for line in lines:
            self.parse(line)   

    def parse(self, line):
        if line.endswith('.'):
            line = line[:-1]
        (name1, _, change, count, _, _, _, _, _, _, name2) = line.split()
        self.people.add(name1)
        self.people.add(name2)
        happy = int(count)
        if change == 'lose':
            happy *= -1
        self.happiness.setdefault(name1, dict())[name2] = happy

    def get_best(self):
        max_happy = 0
        for ordering in permutations(self.happiness.keys()):
            happiness = sum(self.happiness[a][b]+self.happiness[b][a] for a, b in zip(ordering, ordering[1:]))
            happiness += self.happiness[ordering[0]][ordering[-1]] + self.happiness[ordering[-1]][ordering[0]]
            max_happy = max(max_happy, happiness)
        return max_happy

    def add_myself(self):
        self.happiness['me'] = {}
        for person in self.people:
            self.happiness['me'][person] = 0
            self.happiness[person]['me'] = 0
        self.people.add('me')


def test1():
    lines = [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.'
    ]
    table = Table()
    table.add_lines(lines)
    assert table.get_best() == 330

def test2():
    table = Table()
    table.load('./day13.input')
    assert table.get_best() == 709
    table.add_myself()
    assert table.get_best() == 668

if __name__ == '__main__':
    table = Table()
    table.load('day13.input')
    print(f"part 1: {table.get_best()}")
    table.add_myself()
    print(f"part 2: {table.get_best()}")
