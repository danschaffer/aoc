#!/usr/bin/env python3
import re


def parse(file):
    rules = dict()
    lines = open(file).read().strip()
    patterns_str, messages_str = lines.split('\n\n')
    for pattern in patterns_str.split('\n'):
        (rule, branches) = pattern.split(':')
        rules[rule.strip()] = [branch.split() for branch in branches.strip().split('|')]
    messages = [message.strip() for message in messages_str.split('\n')]
    return rules, messages

def make_pattern(rules, key):
    results = []
    for branch in rules[key]:
        results0 = []
        for item in branch:
            if len(item) > 2 and item[0] == item[-1] == '"':
                results0 += [item[1:-1]]
            else:
                results0 += [make_pattern(rules, item)]
        results += [''.join(results0)]
    return '(?:' + '|'.join(results) + ')'

def part1(file):
    rules, messages = parse(file)
    pattern1 = make_pattern(rules, '0')
    return sum([1 for message in messages if re.fullmatch(pattern1,message)])

def part2(file):
    rules, messages = parse(file)
    pattern31 = make_pattern(rules, '31')
    pattern42 = make_pattern(rules, '42')
    count = max(map(len, messages))
    pattern = re.compile('|'.join(f'(?:{pattern42}){{{i + 1},}}(?:{pattern31}){{{i}}}'
    for i in range(1, (count + 1) // 2)))
    return sum(bool(re.fullmatch(pattern, text.rstrip())) for text in messages)

def test1():
    assert part1('./day19-test1.input') == 2
    assert part1('./day19-test2.input') == 2
    assert part1('./day19-test3.input') == 3
    assert part1('./day19.input') == 291

def test2():
    assert part2('./day19-test3.input') == 12
    assert part2('./day19.input') == 409

if __name__ == '__main__':
    print('day19')
    print(f"part1: {part1('./day19.input')}")
    print(f"part2: {part2('./day19.input')}")
