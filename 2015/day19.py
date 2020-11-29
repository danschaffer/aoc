#!/usr/bin/env python3
from queue import PriorityQueue
import random
import sys

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

def apply_rules_2(rules, data):
    results = set()
    for rule in rules:
        (key,value) = rule
        index = 0
        while data.find(key, index) > -1:
            index = data.find(key, index)
            results.add(data[0:index] + value + data[index+len(key):])
            index += len(key)
    return results

def build_rules(rules, goal, start):
    frontier = PriorityQueue()
    frontier.put((len(start), 0 ,start))
    best = sys.maxsize
    while True:
        (_, moves, state) = frontier.get()
        best = min(best, len(state))
        print(f"{moves} {best} {state}")
        if state == goal:
            break
        rules1 = list(apply_rules(rules, state))
        random.shuffle(rules1)
        for newstate in rules1:
            newweight = moves + 1 + len(newstate)
#            newweight = moves + 1
            frontier.put((newweight, (moves+1), newstate))
    return moves

def count(str, fnd):
    index = 0
    cnt = 0
    while str.find(fnd, index) > -1:
        cnt += 1
        index = str.find(fnd, index) + len(fnd)
    return cnt

def countEle(str):
    cnt = 0
    for ch in range(len(str)):
        if str[ch] >= 'A' and str[ch] <= 'Z':
            cnt += 1
    return cnt

def find_count(start):
    rn = count(start, 'Rn')
    ar = count(start, 'Ar')
    y = count(start, 'Y')
    ln = countEle(start)
    return ln - (rn + ar) - 2*y - 1

def parse(lines):
    rules = []
    rules2 = []
    data = ''
    for line in lines:
        if line.find('=>') > -1:
            (rule1, _, rule2) = line.split()
            rules += [(rule1, rule2)]
            rules2 += [(rule2, rule1)]
        elif line == '':
            continue
        else:
            data = line
    return rules, rules2, data

def test1():
    rules, _, data = parse([
    'H => HO',
    'H => OH',
    'O => HH',
    'HOH'
    ])
    assert len(apply_rules(rules, data)) == 4

    rules, _, data = parse([
    'e => H',
    'e => O',
    'H => HO',
    'H => OH',
    'O => HH'
    ])
    assert build_rules(rules, 'HOH', 'e') == 3
    assert build_rules(rules, 'HOHOHO', 'e') == 6

def test2():
    rules, _, data = parse(open('./day19.input').read().strip().split('\n'))
    assert len(apply_rules(rules, data)) == 576
    assert find_count(data) == 207
    
if __name__ == '__main__':
    rules, rules2, start = parse(open('./day19.input').read().strip().split('\n'))
    print(f"part 1: {len(apply_rules(rules, start))}")
#    print(f"part 2: {build_rules(rules2, 'e', start)}")
    print(f"part 2: {find_count(start)}")
