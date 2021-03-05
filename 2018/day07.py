#!/usr/bin/env python
import networkx as nx
from string import ascii_uppercase
class Day07:
    def __init__(self, file):
        self.graph = nx.DiGraph()

        for line in open(file).readlines():
            parts = line.split()
            self.graph.add_edge(parts[1],parts[7])

    def run_part1(self):
        return ''.join(nx.lexicographical_topological_sort(self.graph))

    def run_part2(self, workers=5, base_time=60):
        for node in self.graph.nodes:
            self.graph.nodes[node]['work'] = base_time + 1 + ord(node) - ord('A')
        time = 0
        while self.graph.nodes:
            available_nodes = [node for node in self.graph.nodes if self.graph.in_degree(node) == 0]  
            available_nodes.sort(key=lambda node: self.graph.nodes[node]['work'])
            for worker, node in zip(range(workers), available_nodes):
                self.graph.nodes[node]['work'] -= 1
                if self.graph.nodes[node]['work'] == 0:
                    self.graph.remove_node(node)
            time += 1
        return time

def test1():
    test_day07 = Day07('./day07-test.input')
    assert test_day07.run_part1() == 'CABDFE'
    assert test_day07.run_part2(workers=2, base_time=0) == 16

    day07 = Day07('./day07.input')
    assert day07.run_part1() == 'OUGLTKDJVBRMIXSACWYPEQNHZF'
    assert day07.run_part2() == 929

if __name__ == '__main__':
    print("advent of code: day07")
    day07 = Day07('./day07.input')
    print(f"part 1: {day07.run_part1()}")
    print(f"part 2: {day07.run_part2()}")
