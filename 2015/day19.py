#!/usr/bin/env python3
from queue import PriorityQueue
import time

def apply_rules(rules, data):
    results = set()
    for rule in rules:
        (key,value) = rule
        index = 0
        while data.find(key, index) > -1:
            index = data.find(key, index)
            results.add(data[0:index] + value + data[index+len(key):])
            index += len(key)
    return results

def measure(state, goal):
    count = len(goal)
    if len(state) > len(goal):
        return count + 99
    for index in range(len(state)):
        if state[index] == goal[index]:
            count -= 1
    return count

def get_time(secs):
    result = ""
    if secs > 60 * 60:
        secs = secs % 60



def build_rules(rules, start, goal):
    frontier = PriorityQueue()
    frontier.put((len(goal),0,len(goal),'e'))
    count = 0
    start = time.time()
    while True:
        (weight, moves, difference, state) = frontier.get()
        print(f"{weight} {moves} {difference} {len(state)} {count} {get_time(time.time() - start)}")
        if state == goal:
            break
        for newstate in apply_rules(rules, state):
            difference = measure(newstate, goal)
            newweight = moves+1 + difference
            frontier.put((newweight, (moves+1), difference, newstate))
            count += 1
    return moves

def parse(lines):
    rules = []
    data = ''
    for line in lines:
        if line.find('=>') > -1:
            (rule1, _, rule2) = line.split()
            rules += [(rule1, rule2)]
        elif line == '':
            continue
        else:
            data = line
    return rules, data

def test1():
    rules, data = parse([
    'H => HO',
    'H => OH',
    'O => HH',
    'HOH'
    ])
    assert len(apply_rules(rules, data)) == 4

    rules, data = parse([
    'e => H',
    'e => O',
    'H => HO',
    'H => OH',
    'O => HH'
    ])
    assert build_rules(rules, 'e', 'HOH') == 3
    assert build_rules(rules, 'e', 'HOHOHO') == 6

def test2():
    rules, data = parse(open('./day19.input').read().strip().split('\n'))
    assert len(apply_rules(rules, data)) == 576

if __name__ == '__main__':
    rules, goal = parse(open('./day19.input').read().strip().split('\n'))
#    print(f"part 1: {len(apply_rules(rules, goal))}")
#    print(f"{len(goal)} {goal}")
    print(f"part 2: {len(build_rules(rules, 'e', goal))}")
