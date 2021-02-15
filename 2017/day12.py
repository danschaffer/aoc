#!/usr/bin/env python3
class Day12:
    def __init__(self, file):
        self.data = {}
        for line in open(file).read().strip().split('\n'):
            parts = line.split()
            source = int(parts[0])
            connections = [int(connection.strip()) for connection in (''.join(parts[2:])).split(',')]
            self.data[source] = connections

    def get_group(self, item=0):
        visited = [item]
        frontier = self.data[item][:]
        while frontier:
            source = frontier.pop()
            if source in visited:
               continue
            visited.append(source)
            frontier += self.data[source]
        return (visited)

    def get_groups(self):
        groups = 0
        found = []
        for item in self.data:
            if item in found:
                continue
            found += self.get_group(item)
            groups += 1
        return groups

def test1():
    assert len(Day12('./day12-test.input').get_group(0)) == 6
    assert Day12('./day12-test.input').get_groups() == 2

    assert len(Day12('./day12.input').get_group(0)) == 128
    assert Day12('./day12.input').get_groups() == 209


if __name__ == '__main__':
    print("advent of code: day12")
    day12 = Day12('./day12.input')
    print(f"part 1: {len(day12.get_group(0))}")
    print(f"part 2: {day12.get_groups()}")
