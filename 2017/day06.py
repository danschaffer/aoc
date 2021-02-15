#!/usr/bin/env python3


def day6(data, part2=False):
    current = [int(n) for n in data.split()]
    cache=[]
    moves = 0
    goal = None
    while True:
        if goal is not None and goal == current:
            break
        if current in cache:
            if not part2:
                break
            moves = 0
            cache = []
            goal = current[:]
        cache.append(current[:])
        highest = max(current)
        index = current.index(highest)
        current[index] = 0
        while highest > 0:
            index = (index + 1) % len(current)
            current[index] += 1
            highest -= 1
        moves += 1
    return moves

def test1():
    assert day6('0 2 7 0') == 5
    assert day6('0 2 7 0',part2=True) == 4

    assert day6('5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6') == 5042
    assert day6('5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6', part2=True) == 1086

if __name__ == '__main__':
    print("advent of code: day06")
    print(f"part 1: {day6('5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6')}")
    print(f"part 2: {day6('5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6', part2=True)}")
