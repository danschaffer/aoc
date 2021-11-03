#!/usr/bin/env python

import networkx as nx


class Day20:
    def __init__(self, str):     
        self.maze = nx.Graph()
        pos = {0}
        stack = []
        starts, ends = {0}, set()
        for s in str:
            if s == '|':
                ends.update(pos)
                pos = starts
            elif s in 'NSEW':
                direction = {'N': 1, 'S': -1, 'E': 1j, 'W': -1j}[s]
                self.maze.add_edges_from((p,p+direction) for p in pos)
                pos = {p+direction for p in pos}
            elif s == '(':
                stack.append((starts, ends))
                starts, ends = pos, set()
            elif s == ')':
                pos.update(ends)
                starts, ends = stack.pop()
        
    def part1(self):
        lengths = nx.algorithms.shortest_path_length(self.maze, 0)
        return max(lengths.values())

    def part2(self):
        lengths = nx.algorithms.shortest_path_length(self.maze, 0)
        return sum(1 for length in lengths.values() if length >= 1000)

def test1():
    assert Day20('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$').part1() == 23
    assert Day20('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$').part1() == 31

if __name__ == '__main__':
    print('day20')
    day20 = Day20(open('day20.input').read())
    print(f"part 1: {day20.part1()}")
    print(f"part 2: {day20.part2()}")

