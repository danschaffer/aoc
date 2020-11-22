#!/usr/bin/env python3
from itertools import combinations
import sys

class Sleigh:
    def __init__(self, weights=[]):
        self.weights = weights
        self.combinations = []
        self.smallest1 = []

    def load(self, file):
        self.weights = [int(number) for number in open(file).read().strip().split('\n')]

    def make_combinations3(self):
        for count1 in range(1, 8):
            groups1 = combinations(self.weights, count1)
            for group1 in groups1:
                if sum(group1) == sum(self.weights) / 3:
                    self.combinations += [(list(group1))]

    def make_combinations4(self):
        for count1 in range(1, 8):
            groups1 = combinations(self.weights, count1)
            for group1 in groups1:
                if sum(group1) == sum(self.weights) / 4:
                    self.combinations += [(list(group1))]

    def find_smallest1(self):
        smallest = sys.maxsize
        for combination in self.combinations:
            smallest = min(smallest, len(combination))
        for combination in self.combinations:
            if len(combination) == smallest:
                self.smallest1 += [combination]

    def find_smallest_qe(self):
        smallest_qe = sys.maxsize
        for smallest in self.smallest1:
            qe = 1
            for item in smallest:
                qe = qe * item
            smallest_qe = min(smallest_qe, qe)
        return smallest_qe

    def run3(self):
        self.make_combinations3()
        self.find_smallest1()
        return self.find_smallest_qe()

    def run4(self):
        self.make_combinations4()
        self.find_smallest1()
        return self.find_smallest_qe()

def test1():
    sleigh = Sleigh(list(range(1,5+1)) + list(range(7,11+1)))
    assert sleigh.run3() == 99
    assert sleigh.run4() == 44

def test2():
    sleigh = Sleigh()
    sleigh.load('./day24.input')
    assert sleigh.run3() == 11266889531
    assert sleigh.run4() == 77387711

if __name__ == '__main__':
    sleigh = Sleigh()
    sleigh.load('./day24.input')
    print(f"part 1: {sleigh.run3()}")
    print(f"part 2: {sleigh.run4()}")
