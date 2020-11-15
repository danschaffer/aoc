#!/usr/bin/env python3

import sys
from itertools import permutations

class Distances:
    def __init__(self):
        self.places = set()
        self.distances = {}

    def add_line(self, line):
        (source, _, dest, _, distance) = line.split()
        self.places.add(source)
        self.places.add(dest)
        self.distances.setdefault(source, dict())[dest] = int(distance)
        self.distances.setdefault(dest, dict())[source] = int(distance)

    def find_shortest(self):
        shortest = sys.maxsize
        for items in permutations(self.places):
            dist = map(lambda x, y: self.distances[x][y], items[:-1], items[1:])
            shortest = min(shortest, sum(dist))
        return shortest

    def find_longest(self):
        longest = 0
        for items in permutations(self.places):
            dist = map(lambda x, y: self.distances[x][y], items[:-1], items[1:])
            longest = max(longest, sum(dist))
        return longest

    def load(self, file):
        for line in open(file).read().strip().split('\n'):
            self.add_line(line)

def test1():
    distances = Distances()
    distances.add_line('London to Dublin = 464')
    distances.add_line('London to Belfast = 518')
    distances.add_line('Dublin to Belfast = 141')
    assert distances.find_shortest() == 605
    assert distances.find_longest() == 982

def test2():
    distances = Distances()
    distances.load('./day9.input')
    assert distances.find_shortest() == 141
    assert distances.find_longest() == 736

if __name__ == '__main__':
    distances1 = Distances()
    distances1.load('./day9.input')
    print(f"part 1 = {distances1.find_shortest()}")
    print(f"part 2 = {distances1.find_longest()}")
