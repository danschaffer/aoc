#!/usr/bin/env python3

import networkx as nx
class Day22:
    def __init__(self, depth, target_x, target_y):
        self.depth = depth
        self.target_x = target_x
        self.target_y = target_y
        self.table = {}

    def print_board(self):
        for y in range(self.target_y+1):
            line = ''
            for x in range(self.target_x+1):
                line += ['.','=','|'][self.table[(x,y)]%3]
            print(line)
        print('')

    def run_part1(self):
        answer = 0
        for x in range(self.target_x+1):
            for y in range(self.target_y+1):
                if x == 0:
                    geo_index = y * 48271
                elif y == 0:
                    geo_index = x * 16807
                elif (x,y) == (self.target_x, self.target_y):
                    geo_index = 0
                else:
                    geo_index = self.table[(x-1,y)] * self.table[(x,y-1)]
                erosion_level = (geo_index + self.depth) % 20183
                self.table[(x,y)] = erosion_level
                answer += erosion_level % 3
        return answer

    def run_part2(self, x, y):
        rocky, wet, narrow = 0,1,2
        torch, gear, neither = 0,1,2
        graph = nx.Graph()
        for x in range(x+1):
            for y in range(y+1):
                risk = self.table[(x,y)] % 3
                if risk == rocky:
                    graph.add_edge((x,y,torch),(x,y,gear),weight=7)
                elif risk == wet:
                    graph.add_edge((x,y,gear),(x,y,neither),weight=7)
                else:
                    graph.add_edge((x,y,torch),(x,y,neither),weight=7)
                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    newx,newy = x+dx, y+dy
                    if newx < 0 or newx > x or newy < 0 or newy > y:
                        continue
                    risk = self.table[(newx,newy)] % 3
                    if risk == rocky:
                        graph.add_edge((x,y,gear), (newx,newy,gear),weight=1)
                        graph.add_edge((x,y,torch), (newx,newy,torch),weight=1)
                    elif risk == wet:
                        graph.add_edge((x,y,gear), (newx,newy,gear),weight=1)
                        graph.add_edge((x,y,neither), (newx,newy,neither),weight=1)
                    else:
                        graph.add_edge((x,y,torch), (newx,newy,torch),weight=1)
                        graph.add_edge((x,y,neither), (newx,newy,neither),weight=1)
        for i,path in enumerate(nx.dijkstra_path(graph,(0,0,torch),(x,y,torch))):
            print(f"{i} {path}")
        return nx.dijkstra_path_length(graph,(0,0,torch),(x,y,torch))

    def get_distance(self, loc, goal):
        return abs(loc[0] - goal[0]) + abs(loc[1] - goal[1])

def test1():
    assert Day22(510,(10,10)).run_part1() == 114

def test2():
    assert Day22(7305,(13,734)).run_part1() == 10204

if __name__ == '__main__':
    print("advent of code: day22")
    d = Day22(7305,13,734)
    print(f"part 1: {d.run_part1()}")
    print(f"part 2: {d.run_part2(13,734)}")

