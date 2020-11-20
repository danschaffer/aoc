#!/usr/bin/env python3

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

def build_rules(rules, start, destination):
    data = {start: 0}
    while destination not in data.keys():
        next_key = sorted(data.keys(), key=len)[0]
        print(f"{next_key} {len(data)}")
        moves = data[next_key]
        del data[next_key]
        for key in apply_rules(rules, next_key):
            if key not in data.keys():
                data[key] = moves + 1
    return data[destination]

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
    rules, data = parse(open('./day19.input').read().strip().split('\n'))
    print(f"part 1: {len(apply_rules(rules, data))}")
#    print(f"part 2: {len(build_rules(rules, 'e', data))}")
