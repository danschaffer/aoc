#!/usr/bin/env python3

def day25(data, start='A', steps=6):
    slot = 0
    values = {0:0}
    current = start
    for n in range(steps):
#        if n % 100000 == 0:
#            print(f"{n}/{steps}")
        state = data[current]
        if slot not in values:
            values[slot] = 0
        if values[slot] == 0:
            values[slot] = state[0]
            slot = slot + state[1]
            current = state[2]
        else:
            values[slot] = state[3]
            slot = slot + state[4]
            current = state[5]
    return sum([values[key] for key in values])

def test1():
    test_data = {
        'A': (1,1,'B',0,-1,'B'),
        'B': (1,-1,'A',1,1,'A'),
    }
    assert day25(test_data) == 3

    data = {
        'A': (1,1,'B',0,-1,'E'),
        'B': (1,-1,'C',0,1,'A'),
        'C': (1,-1,'D',0,1,'C'),
        'D': (1,-1,'E',0,-1,'F'),
        'E': (1,-1,'A',1,-1,'C'),
        'F': (1,-1,'E',1,1,'A'),
    }
    assert day25(data, steps=12386363) == 4385

if __name__ == '__main__':
    print("advent of code: day25")
    data = {
        'A': (1,1,'B',0,-1,'E'),
        'B': (1,-1,'C',0,1,'A'),
        'C': (1,-1,'D',0,1,'C'),
        'D': (1,-1,'E',0,-1,'F'),
        'E': (1,-1,'A',1,-1,'C'),
        'F': (1,-1,'E',1,1,'A'),
    }
    print(f"part 1: {day25(data, start='A', steps=12386363)}")
