#!/usr/bin/env python3
from collections import deque
import os
class Day16:
    def __init__(self, data, positions=None):
        if positions is None:
            self.positions=[chr(ord('a')+n) for n in range(16)]
        else:
            self.positions = positions.split(',')
        if os.path.exists(data):
            data = open(data).read().strip()
        self.instructions = data.split(',')

    def run(self, start=None):
        if not start:
            start = self.positions[:]
            pos = start[:]
        else:
            pos = list(start)
        for instruction in self.instructions:
            if instruction[0] == 's':
                amount = int(instruction[1:])
                pos1 = deque(pos)
                pos1.rotate(amount)
                pos=list(pos1)
            elif instruction[0] == 'x':
                slots = instruction[1:].split('/')
                index0 = int(slots[0])
                index1 = int(slots[1])
                item = pos[index0]
                pos[index0] = pos[index1]
                pos[index1] = item
            elif instruction[0] == 'p':
                slots = instruction[1:].split('/')
                index0 = pos.index(slots[0])
                index1 = pos.index(slots[1])
                item = pos[index0]
                pos[index0] = pos[index1]
                pos[index1] = item
        return ''.join(pos)

    def repeat(self, iterations=1000000000):
        pos0 = ''.join(self.positions)
        cache = [pos0]
        cycle = 0
        while True:
            pos1 = self.run(pos0)
            cycle += 1
            if pos1 in cache:
                break
            cache.append(pos1)
            pos0 = pos1
        offset = iterations % cycle
        return cache[offset]
        
def test1():
    day16_test=Day16('s1,x3/4,pe/b', 'a,b,c,d,e')
    assert day16_test.run() == 'baedc'

    day16=Day16('./day16.input')
    assert day16.run() == 'dcmlhejnifpokgba'
    assert day16.repeat() == 'ifocbejpdnklamhg'

if __name__ == '__main__':
    print("advent of code: day16")
    day16 = Day16('./day16.input')

    print(f"part 1: {day16.run()}")
    print(f"part 2: {day16.repeat()}")
