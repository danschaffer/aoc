#!/usr/bin/env python3

def precedence(op, part2=False):
    if op == '+':
        return 2 if part2 else 1
    if op == '*':
        return 1
    if op == '*':
        return 1
    return 0

def applyOp(term1, term2, op):
    if op == '+':
        return term1 + term2
    elif op == '*':
        return term1 * term2

def calculate(line, part2=False):
    terms, ops = list(), list()

    def combine():
        term1, term2 = terms.pop(), terms.pop()
        op = ops.pop()
        terms.append(applyOp(term1, term2, op))

    for ch in "".join(line.strip().split()):
        if ch.isdigit():
            terms.append(int(ch))
        elif ch == '(':
            ops.append(ch)
        elif ch == ')':
            while len(ops) > 0 and ops[-1] != '(':
                combine()
            ops.pop()
        elif ch in ['+','*']:
            while len(ops) > 0 and precedence(ops[-1], part2) >= precedence(ch, part2):
                combine()
            ops.append(ch)
    while len(ops) > 0:
        combine()
    return terms[-1]

def test1():
    assert calculate('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert calculate('2 * 3 + (4 * 5)') == 26
    assert calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    assert calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    assert calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

def test2():
    assert calculate('2 * 3 + (4 * 5)', part2=True) == 46
    assert calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)', part2=True) == 1445
    assert calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', part2=True) == 669060
    assert calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', part2=True) == 23340

def test3():
    lines0 = open('./day18.input').read().strip().split('\n')
    assert sum([calculate(line) for line in lines0]) == 36382392389406
    assert sum([calculate(line,part2=True) for line in lines0]) == 381107029777968

if __name__ == '__main__':
    print("day18")
    lines = open('./day18.input').read().strip().split('\n')
    p1 = sum([calculate(line) for line in lines])
    print(f"part1: {p1}")
    p2 = sum([calculate(line,part2=True) for line in lines])
    print(f"part1: {p2}")