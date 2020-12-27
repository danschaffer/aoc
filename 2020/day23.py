#!/usr/bin/env python3

class Cups:
    def __init__(self, name, next__=None):
        self.name = name
        self.next__ = next__

    @property
    def next(self):
        return self.next__

    @next.setter
    def next(self, next__):
        self.next__ = next__

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

def pop3(first):
    removed = first.next
    removed4 = first.next.next.next.next
    first.next = removed4
    return removed

def order1(first):
    while first.name != '1':
        first = first.next
    return ''.join(get_items(first)[1:])

def find(first, fnd):
    while first.name != str(fnd):
        first = first.next
    return first

def get_items(first):
    result = [first.name]
    item = first.next
    while item.name != first.name:
        result += [item.name]
        item=item.next
    return result

def run1(initial, moves=100):
    previous = first = Cups(initial[0])
    for cup in initial[1:]:
        current0 = Cups(cup, None)
        previous.next = current0
        previous = current0
    current0.next = first
    current = first
    for _ in range(moves):
        removed = pop3(current)
        index = int(current.name) - 1
        while str(index) not in get_items(current):
            index = index - 1
            if index < 1:
                index = 9
        insert = find(current, index)
        current = current.next
        insert0 = insert.next
        insert.next = removed
        removed.next.next.next = insert0
    return order1(current)

def run2(initial, moves=10000000):
    cycle = [int(n) for n in list(initial)] + list(range(9+1,1000000+1))
    current = cycle[0]
    max_ = max(cycle)
    cycle_dict = dict(zip(cycle, cycle[1:]))
    cycle_dict[cycle[-1]] = cycle[0]

    def pick3():
        pick = [cycle_dict[current]]
        for _ in range(2):
            pick.append(cycle_dict[pick[-1]])
        return pick

    for _ in range(moves):
        pick = pick3()
        next_ = current-1
        while next_ <= 0 or next_ in pick:
            next_ -= 1
            if next_ <= 0:
                next_ = max_
        cycle_dict[current] = cycle_dict[pick[-1]]
        cycle_dict[pick[-1]] = cycle_dict[next_]
        cycle_dict[next_] = pick[0]
        current = cycle_dict[current]

    item1 = cycle_dict[1]
    item2 = cycle_dict[item1]
    return item1 * item2

def test1():
    assert run1('389125467', 0) == '25467389'
    assert run1('389125467', 1) == '54673289'
    assert run1('389125467', 2) == '32546789'
    assert run1('389125467', 3) == '34672589'
    assert run1('389125467', 4) == '32584679'
    assert run1('389125467', 9) == '83926574'
    assert run1('389125467', 100) == '67384529'
    assert run1('284573961', 100) == '26354798'

def test2():
    assert run2('389125467') == 149245887792
    assert run2('284573961') == 166298218695

if __name__ == '__main__':
    print(f"part 1: {run1('284573961')}")
    print(f"part 2: {run2('284573961')}")
