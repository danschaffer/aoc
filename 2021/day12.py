#!/usr/bin/env python3

class Day12:
    def __init__(self, file):
        self.data = {}
        for line in open(file).readlines():
            line = line.strip()
            node1, node2 = line.split('-')
            if node1 != 'end' and node2 != 'start':
                if node1 not in self.data:
                    self.data[node1] = []
                self.data[node1].append(node2)
            if node1 != 'start' and node2 != 'end':
                if node2 not in self.data:
                    self.data[node2] = []
                self.data[node2].append(node1)
 
    def run(self, node='start', visited=set(), part2=False):
        if node == 'end':
            return 1
        if node == 'start' and visited:
            return 0
        if node.islower() and node in visited:
            if part2:
                part2 = False
            else:
                return 0
        visited = visited | {node}
        answer = 0
        for n in self.data[node]:
            answer += self.run(n, visited, part2)
        return answer

def test1():
    assert Day12('./day12-test1.input').run() == 10
    assert Day12('./day12-test2.input').run() == 19
    assert Day12('./day12-test3.input').run() == 226
    assert Day12('./day12-test1.input').run(part2=True) == 36
    assert Day12('./day12-test2.input').run(part2=True) == 103
    assert Day12('./day12-test3.input').run(part2=True) == 3509

def test2():
    assert Day12('./day12.input').run() == 4707
    assert Day12('./day12.input').run(part2=True) == 130493

if __name__ == '__main__':
    print("advent of code: day12")
    print(f"part 1: {Day12('./day12.input').run()}")
    print(f"part 2: {Day12('./day12.input').run(part2=True)}")
