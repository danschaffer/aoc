#!/usr/bin/env python3
import networkx as nx

class Day22:
    def __init__(self, depth, target, corner):
        self.depth = depth
        self.target = target
        self.corner = corner
        self.grid = {}

    def generate_grid(self):
        for y in range(0, self.corner[1] + 1):
            for x in range(0, self.corner[0] + 1):
                if (x, y) in [(0, 0), self.target]:
                    geo = 0
                elif x == 0:
                    geo = y * 48271
                elif y == 0:
                    geo = x * 16807
                else:
                    geo = self.grid[(x-1, y)][1] * self.grid[(x, y-1)][1]
                ero = (geo + self.depth) % 20183
                risk = ero % 3
                self.grid[(x, y)] = (geo, ero, risk)

    def dijkstra(self):
        rocky, wet, narrow = 0, 1, 2
        torch, gear, neither = 0, 1, 2
        valid_items = {rocky: (torch, gear), wet: (gear, neither), narrow: (torch, neither)}
        graph = nx.Graph()
        for y in range(0, self.corner[1] + 1):
            for x in range(0, self.corner[0] + 1):
                items = valid_items[self.grid[(x, y)][2]]
                graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x <= self.corner[0] and 0 <= new_y <= self.corner[1]:
                        new_items = valid_items[self.grid[(new_x, new_y)][2]]
                        for item in set(items).intersection(set(new_items)):
                            graph.add_edge((x, y, item), (new_x, new_y, item), weight=1)
        return nx.dijkstra_path_length(graph, (0, 0, torch), (self.target[0], self.target[1], torch))

    def part1(self):
        self.generate_grid()
        return sum(v[2] for v in self.grid.values())

    def part2(self):
        self.generate_grid()
        return self.dijkstra()

def test1():
    assert Day22(510,(10,10),(10,10)).part1() == 114
    assert Day22(7305,(13,734),(13,734)).part1() == 10204

def test2():
    assert Day22(510,(10,10),(15,15)).part2() == 45
    assert Day22(7305,(13,734),(25,1100)).part2() == 1004

if __name__ == '__main__':
    print("advent of code day 22")
    print(f"part 1: {Day22(7305,(13,734),(13,734)).part1()}")
    print(f"part 2: {Day22(7305,(13,734),(25,1100)).part2()}")
