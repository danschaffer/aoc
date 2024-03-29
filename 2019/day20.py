#!/usr/bin/env python
import re
import networkx as nx
class DonutMaze:
    def __init__(self, maze_name, part2=False):
        self.W = 0
        self.H = 0
        self.part2=part2
        self.map = {}
        self.graph = nx.Graph()
        self.routes = {}
        self.route_names = {}
        self.start = None
        self.end = None
        self.load_map(maze_name)
        self.load_routes()

    def get_neighbors(self, node):
        neighbors = []
        x = node[0]
        y = node[1]
        for point in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if point in self.map and self.is_path(self.map[point]):
                neighbors += [point]
        return neighbors

    def solve(self):
        if self.part2:
            return self.solve_part2()
        else:
            return self.solve_part1()

    def solve_part1(self):
        nodes = {}
        for node in self.get_nodes():
            self.graph.add_node(node)
            for neighbor in self.get_neighbors(node):
                self.graph.add_edge(node, neighbor)
            if node in self.routes:
                self.graph.add_edge(node, self.routes[node])
        answer = nx.shortest_path_length(self.graph, self.start, self.end)
        return answer

    def solve_part2(self):
        nodes = {}
        for level in range(30):
            for node in self.get_nodes():
                if level != 0 and node in [self.start, self.end]:
                    continue
                node1=(node[0],node[1],level)
                self.graph.add_node(node1)
                for neighbor in self.get_neighbors(node):
                    neighbor1 = (neighbor[0],neighbor[1],level)
                    self.graph.add_edge(node1, neighbor1)
                if node in self.routes:
                    dest = self.routes[node]
                    dest1 = (dest[0],dest[1],level+1)
                    if node[0] <= 4 or node[0] >= self.W - 4 or node[1] <= 4 or node[1] >= self.H - 4:
                        self.graph.add_edge(node1,(dest[0],dest[1],level-1))
                    else:
                        self.graph.add_edge(node1,(dest[0],dest[1],level+1))
        start = (self.start[0], self.start[1], 0)
        end = (self.end[0], self.end[1], 0)
#        for i,path in enumerate(nx.shortest_path(self.graph, start, end)):
#            print(f"{i} {path}")
        answer = nx.shortest_path_length(self.graph, start, end)
        return answer

    def get_nodes(self):
        nodes = []
        for item in self.map.keys():
            if self.is_path(self.map[item]):
                nodes += [item]
        return nodes

    def is_path(self, letter):
        return letter == '.'

    def is_route(self, letter):
        return not re.search('[A-Z]', letter) is None

    def find_paths(self, point):
        paths = []
        items = []
        (x,y) = point
        if (x-1,y) in self.map:
            if self.is_path(self.map[(x-1,y)]):
                paths += [(x-1,y)]
            if self.is_route(self.map[(x-1,y)]):
                items += self.map[(x-1,y)]
        if (x+1,y) in self.map:
            if self.is_path(self.map[(x+1,y)]):
                paths += [(x+1,y)]
            if self.is_route(self.map[(x+1,y)]):
                items += self.map[(x+1,y)]
        if (x,y+1) in self.map:
            if self.is_path(self.map[(x,y+1)]):
                paths += [(x,y+1)]
            if self.is_route(self.map[(x,y+1)]):
                items += self.map[(x,y+1)]
        if (x,y-1) in self.map:
            if self.is_path(self.map[(x,y-1)]):
                paths += [(x,y-1)]
            if self.is_route(self.map[(x,y-1)]):
                items += self.map[(x,y-1)]
        return paths, items

    def load_routes(self):
        points1 = {}
        for point in self.map:
            item = self.map[point]
            if self.is_route(item):
                paths, items = self.find_paths(point)
                points1[point] = (paths, items)
        for point in points1:
            if points1[point][0]:
                if point[0] > points1[point][0][0][0] or point[1] > points1[point][0][0][1]:
                    name = self.map[point] + points1[point][1][0]
                else:
                    name = points1[point][1][0] + self.map[point]
                path = points1[point][0][0]
                if name not in self.route_names:
                    self.route_names[name] = []
                self.route_names[name] += [path]
        for route_name in self.route_names.keys():
            route = self.route_names[route_name]
            if route_name == 'AA':
                self.start = route[0]
            elif route_name == 'ZZ':
                self.end = route[0]
            else:
                self.routes[route[0]] = route[1]
                self.routes[route[1]] = route[0]

    def load_map(self, maze_name):
        map_str = self.get_maze(maze_name)
        y = 1
        for line in map_str.split('\n'):
            self.W = max(self.W, len(line.strip()))
            x = 1
            for item in list(line):
                if self.is_route(item) or self.is_path(item):
                    self.map[(x,y)] = item
                x += 1
            y += 1
        self.H = y

    def get_maze(self, name):
        mazes = {
            'maze1': """
         A
         A
  #######.#########
  #######.........#
  #######.#######.#
  #######.#######.#
  #######.#######.#
  #####  B    ###.#
BC...##  C    ###.#
  ##.##       ###.#
  ##...DE  F  ###.#
  #####    G  ###.#
  #########.#####.#
DE..#######...###.#
  #.#########.###.#
FG..#########.....#
  ###########.#####
             Z
             Z
""",
            'maze2': """
                   A
                   A
  #################.#############
  #.#...#...................#.#.#
  #.#.#.###.###.###.#########.#.#
  #.#.#.......#...#.....#.#.#...#
  #.#########.###.#####.#.#.###.#
  #.............#.#.....#.......#
  ###.###########.###.#####.#.#.#
  #.....#        A   C    #.#.#.#
  #######        S   P    #####.#
  #.#...#                 #......VT
  #.#.#.#                 #.#####
  #...#.#               YN....#.#
  #.###.#                 #####.#
DI....#.#                 #.....#
  #####.#                 #.###.#
ZZ......#               QG....#..AS
  ###.###                 #######
JO..#.#.#                 #.....#
  #.#.#.#                 ###.#.#
  #...#..DI             BU....#..LF
  #####.#                 #.#####
YN......#               VT..#....QG
  #.###.#                 #.###.#
  #.#...#                 #.....#
  ###.###    J L     J    #.#.###
  #.....#    O F     P    #.#...#
  #.###.#####.#.#####.#####.###.#
  #...#.#.#...#.....#.....#.#...#
  #.#####.###.###.#.#.#########.#
  #...#.#.....#...#.#.#.#.....#.#
  #.###.#####.###.###.#.#.#######
  #.#.........#...#.............#
  #########.###.###.#############
           B   J   C
           U   P   P
""", 'maze3': """
                                     S         N       I         Y       A     F
                                     D         C       J         J       C     W
  ###################################.#########.#######.#########.#######.#####.#####################################
  #.......#.#...#.....#...#.....#.........#...#.....#.#.......#...#...........#.....#.................#.#...#.#.#.#.#
  ###.###.#.###.#####.#.#.#####.###.#####.#.#.#.#.###.#.#########.###.###.#######.###.#####.###.###.###.###.#.#.#.#.#
  #...#.#...#.#...#.#...#.#.........#.....#.#.#.#...#.....#.#.....#.#...#.#.#.#.#.......#.#.#.#.#.#.#.#.#...#.#.....#
  #.###.#.###.###.#.###.###.###.#####.#####.#.###.#####.#.#.#####.#.###.###.#.#.#.#.#####.###.###.###.#.###.#.#.#####
  #.#...#.....................#.#.#.......#.#.........#.#.#.......#.....#.......#.#...#.#...#.#.#.#.......#.....#.#.#
  #####.###.#.###.###.#.#.#.#.###.#######.#.#############.#.###.###.#.#.#####.#.#.#####.#.###.#.#.#.###.#.#####.#.#.#
  #.........#.#...#...#.#.#.#.#.#.#.......#.#.......#.....#.#.#.#...#.#.#.#...#...#.#.....#...#.....#.#.#.#.....#...#
  #.#.#######.#############.###.#.###.#.#.#.#.###.#.#.#.#.#.#.#####.#####.###.#####.#.#####.#####.###.#########.#.#.#
  #.#.#...#...#.#.#...........#.......#.#.#.#.#.#.#.#.#.#.#.#...#.....#.....#.....#.....#...#.....#...#...........#.#
  ###.###.###.#.#.#######.#####.###.#######.#.#.#.#####.###.#.###.###.###.#######.#.#.#####.###.#.#.#.#######.#######
  #.#...#.#...#.#...#.#.......#.#...#.#.#.....#.#.....#...#.....#.#...#.#.....#.#...#...........#.#.#.#...#.......#.#
  #.#####.#####.#.#.#.###.#########.#.#.#.###.###.#######.#.#.#######.#.###.###.#.###.#.#.###.###.#.###.#####.#.###.#
  #...#...........#...#.#.#.#.#.#.....#.#...#.#.....#.#.#.#.#.#.........#.........#...#.#...#...#.#...#.#.....#.#...#
  #.#######.#####.###.#.###.#.#.#####.#.#.#######.#.#.#.#.###.###.#.###.#.#.#.#.#.###.#######.#####.###.#######.#.#.#
  #.....#...#.#...#.............#.#.....#.#...#...#.#.....#.#...#.#.#.#.#.#.#.#.#...#...#.............#.#.#...#...#.#
  #.#########.#####.#######.###.#.#.#########.###.###.###.#.#.#.###.#.#####.#######.###.###.#.#.#.#####.#.#.###.#####
  #.#.#.#.#...#.#.#.#.......#.#.....#.....#.........#.#...#...#...#...#.#.......#.#.#.#.#...#.#.#.#.#.#.#...#.......#
  #.#.#.#.###.#.#.#####.#.#.#.#####.#.#.#######.#.###.###.#.#.#.###.###.###.#####.###.#.###########.#.#.#.#.###.###.#
  #.#...#.....#...#.#...#.#...#.#...#.#.....#...#...#.#...#.#.#.#.#...#.#.#.#.#...#...#.#.....#.#.......#.#...#.#...#
  #.###.#.#######.#.#######.###.###.#.###.#######.#####.###.#.#.#.#.###.#.#.#.#.###.#######.###.#.#####.###.###.#####
  #...........#.......#.#.#.#.........#.#...#.#.....#.....#.#.#.#...#.#.#...#...#...#...#.#...#.#.#...#...#...#.....#
  ###.###.###########.#.#.###.###.#.###.#.###.###.#######.#.#######.#.#.###.#.#.#.#.#.###.#.###.#####.#.###.###.#.###
  #.....#...#.#.#.......#.#.#.#...#...#...#...#.#.#.......#.#.......#.#.#.....#.#.#.#...#.....#...#...#...#...#.#.#.#
  ###.#######.#.###.#####.#.#####.#.###.#####.#.#.#.#.#####.###.#.#.#.#.###.###.#.###.###.#.#.#.#####.###.#.###.###.#
  #.#.....#.#.#...#...#...#.......#.#.#.....#.#...#.#...#.....#.#.#.......#...#.....#.....#.#...#.#...#.#.#.#.#.#.#.#
  #.#.###.#.#.###.#.###.#########.###.###.###.#.#.#.#.#.###.#.###.#######.#######.###.#.#.#######.#.###.#.#.#.#.#.#.#
  #.#...#.#...#.#...#.#...#.#...#...#.......#...#.#.#.#.#...#...#.#.......#...........#.#.#...#...#.#.#.....#.......#
  #.#.#######.#.#.#.#.#.###.#.#######.###########.#.#######.#######.###########.#############.###.#.#.###.###.###.###
  #...#...#.....#.#.#...#.#.#.#      S           N P       R       Y           M        #.#.#.#...#...#.#...#.#.....#
  ###.#.#####.#.###.###.#.#.#.#      J           D S       A       J           F        #.#.#.#.###.###.#.#######.###
  #.#.#.#.#.#.#...........#.#.#                                                         #.......#.........#.........#
  #.#.#.#.#.#####.###.#####.#.#                                                         #.#####.#.###.###.#.#####.###
  #...#...#...#.#.#.#.#.#.#...#                                                         #.....#.....#.#.#.....#......KQ
  ###.###.#.###.#.#.#.#.#.#.###                                                         #####.###.#####.#.###########
  #.#.....#.....#.#.....#.....#                                                         #.......#.#.#.#.#...#.......#
  #.###.#######.#####.#.#.#.###                                                         #.#####.###.#.#.#.#.#######.#
  #.#...#.#...#.....#.#.#.#...#                                                       SC..#...#.#.#.#.#.#.#.#.#.#.#.#
  #.###.#.#.#####.###.#.#.#.###                                                         ###.#####.#.#.#.#####.#.#.#.#
ZB....#.#...#.........#...#....UX                                                       #.....#...........#.......#..SJ
  #.###.###.#####.###.#.#######                                                         #.#.#.#.#.#####.###.###.#.#.#
  #.................#.#.#.#...#                                                       UI..#.#...#.#...#.#.#.#.#.#...#
  #.#.###.#####.###.#.###.#.###                                                         ###.#.#######.#.#.#.#.#####.#
  #.#.#.#.#.#.#...#.#.#.#.....#                                                         #.#.#...#.........#.#...#...#
  #.#.#.###.#.#########.#.###.#                                                         #.#.#######.#####.#.###.#####
  #.#.#.#.#.#...#.......#.#...#                                                         #.#.#.....#.#.#.......#...#.#
  #####.#.#.#.#.#######.#.#.###                                                         #.#####.#####.#########.###.#
  #.#.#...#...#...#.#.....#...#                                                         #...#.....#...............#..RA
  #.#.#.###.#####.#.###.#.#.#.#                                                         #.#.#.#.###.#############.#.#
JA..............#.......#.#.#..SD                                                     NC..#...#.#.....#.....#...#.#.#
  #####.###.#.###.#############                                                         #.###.#.###.#####.#####.#.#.#
UJ....#.#...#.#...#...#.#......JL                                                       #...#.#.#.............#.....#
  #.#####.#######.#.#.#.#.###.#                                                         #######.#.#.###.#############
  #.....#.#.....#.#.#...#...#..FW                                                       #.........#.#.#.#.#.#...#...#
  #.#########.#####.###.#.#####                                                         #.###########.###.#.###.###.#
YM....#...#.#.........#.......#                                                         #.#...........#.....#........ND
  #.#.#.#.#.#.#####.###.#######                                                         ###.#########.#.###.#.#.#####
  #.#...#.......#.....#.....#.#                                                         #.#.........#...#.#...#.#.#.#
  #######.###.###.###########.#                                                         #.#########.#####.#.#.###.#.#
  #.....#...#.#.#.#.....#.#...#                                                       YT..........#.#...#...#...#...#
  #.###.#######.###.#####.###.#                                                         ###.###.###.#.###.#########.#
  #...#...#...#.#.....#.#......XQ                                                       #.#.#.........#...#...#...#.#
  #.###.###.#.#.#.#.#.#.#.#.#.#                                                         #.#.#.#######.#####.###.###.#
  #.#...#...#...#.#.#.#.#.#.#.#                                                       OY..#.#.#...#.#.#.#.....#.#...#
  #.#.###.#.###.###.#.#.#####.#                                                         #.#####.###.###.###.#.#.#.#.#
MF..#.....#.#.......#.........#                                                         #...#...............#.....#..YT
  #.###.#.#####.#.###########.#                                                         #.#####.#####.#######.###.#.#
  #...#.#.#.#.#.#.#.#.......#.#                                                         #...#...#.#...#.#.......#.#.#
  #.#######.#.#####.###.###.###                                                         #.#.#.###.###.#.#.###.#.#####
  #.#.....#.....#...#...#.....#                                                         #.#.......#.....#.#...#.#...#
  #####.###.#####.###.#.#.###.#                                                         ###.###.#####.#############.#
LE......#.#.#.#.#...#.#.#.#...#                                                         #.#...#.#.#.#...#...#.....#..XQ
  #.#.#.#.#.#.#.###.#.#######.#                                                         #.#######.#.###.###.###.#.#.#
  #.#.#...............#.#...#..YM                                                     ZB....#...#.#...#.#.....#.#...#
  #####################.#.#####                                                         #.#####.#.###.#####.###.###.#
  #.....#...............#.....#                                                         #.#...#...#.......#...#...#.#
  #.###.#.#########.###.#.###.#                                                         #.#.#####.###.#####.#.###.###
  #.#.#.#...#.......#...#...#..LE                                                       #...................#.....#.#
  #.#.#.###.###.###.#.#####.###                                                         ###########################.#
  #...#...#...#.#...#.#...#...#                                                         #.#.........................#
  ###.###.#.###.###.#.#.#.#.###                                                         #.#.#.###.#.#.###.###.###.#.#
YL......#...#.#.#...#...#.....#                                                         #.#.#.#.#.#.#.#.....#...#.#.#
  ###.#######.###.#####.###.#.#                                                         #.###.#.#.###.###.#########.#
  #.......#.#.....#.#...#...#.#                                                       JQ..#.#...#.#...#.....#.......#
  ###.###.#.###.###.###.#.#.###                                                         #.#.###.###.###.###.###.#.###
  #.....#...#...#.......#.#.#.#                                                         #.........#.#...#.....#.#....JL
  ###.#########.#####.#######.#    Y         A   I           M       U   K     J        #.#.###.#####.###.#########.#
  #.........#.....#.....#.....#    L         C   J           V       J   Q     A        #.#.#...#.....#...#.#.......#
  #.###.#.#####.#############.#####.#########.###.###########.#######.###.#####.#########.#####.#####.###.#.#####.###
  #...#.#...#.....#.......#.#.........#.#.#.#...#.....#.......#.........#.....#.........#...#.#...#...#.....#...#...#
  #####.#.#.#######.#####.#.#.###.#.###.#.#.#.#####.#######.#.#.#.#####.###.#.#######.#######.#.#.#.###.###.###.#.###
  #.....#.#...#...#...#.#.#...#.#.#.#.........#.....#.......#.#.#...#...#...#.#.#.....#.#...#...#.#...#.#...#.......#
  ###.#.#####.###.#.###.#.###.#.#.###.###.#######.#######.###.#.#######.###.#.#.#####.#.###.#.#.#######.###.###.###.#
  #...#.....#...#...#.......#.#.....#.#...#.....#.#...#.....#.#.#.....#...#.#.....#.........#.#.......#.#.....#.#.#.#
  #.#.#.#####.#######.#.#.#####.#.#######.#.#.###.#.#.#.#.#####.#.#.#######.#.###.###.###.###########.#.#.###.###.#.#
  #.#.#...#...#.....#.#.#.......#...#.......#.#.#...#.#.#...#.#...#.....#...#...#.#.#.#.#.#...#...#...#.#.#.#.#.....#
  ###.#.#.#########.#######.#####.#.###.#####.#.#####.#.#####.#####.#######.#.#####.#.#.###.#.#.#####.#####.#######.#
  #...#.#.#.................#...#.#.#...#.#.#...#...#.#.#.....#.#.......#...#.#.....#.......#.#.....#.#...#.........#
  #.###.#####.###.###.#.#.#.###.#.#####.#.#.#.###.#.#.#.#.#.###.#.#.#.#######.#####.#.###.#.#####.#####.###.###.#.#.#
  #.#.....#...#.....#.#.#.#.#.......#...#.....#...#...#...#.#.....#.#.#.....#.#...#.....#.#...............#...#.#.#.#
  ###.#.#######.#####.#####.###.#.#########.###.#.###.#.#####.#.#######.#.###.#.#####.###.#.#.#.#.###.#.###########.#
  #.#.#...#.....#.......#...#.#.#.#.#.....#...#.#...#.#.#...#.#.#.#.#.#.#.........#.#...#.#.#.#.#...#.#.......#.....#
  #.#.#.#.#####.#.#####.#.###.###.###.#.###.#.#.#######.#.#.###.#.#.#.###.#.#.#.###.#.###.###.###############.###.#.#
  #.#.#.#.#.....#.#...#.#.#.....#.....#...#.#.#.#.#.....#.#.....#...#.....#.#.#...#.....#.#.#...........#.#.....#.#.#
  #.###.#####.###.###.#.#.#.###.#.#.###.#.###.#.#.###.#.#####.#.#.###.#.###.###.###.#.#####.#####.#.#.###.#########.#
  #.......#.#.#.#.#.....#.#.#.#.#.#.#...#.#...#.....#.#.#...#.#.#...#.#.#.....#...#.#.#.......#...#.#...........#...#
  ###.#.#.#.###.#.###.#######.#.#####.#######.###.#####.#.#####.#.#####.#.#.#.#.#.###.#.#.#.###.###.###.###.#####.#.#
  #...#.#...#.....#...#.#.#.#.#...#...#.#.#...#...#.#.....#...#...#.#.#.#.#.#.#.#.#.....#.#...#.#...#...#...#.#...#.#
  ###.###.###.#.#.#####.#.#.#.###.#.###.#.#.#.#.#.#.###.###.###.#.#.#.#####.#########.###############.#.#####.###.#.#
  #...#.#.#...#.#.#.#.#.#.#.#...........#.#.#.#.#...#.....#.....#.#.#.....#.#...#.....#.#.#...#.#.#.#.#...#.......#.#
  ###.#.#####.#####.#.#.#.#.#.#######.###.###.#.#######.###.#.#.###.#.#####.#.#######.#.#.#.###.#.#.#######.#.###.#.#
  #.#.#...#.#.#.#.............#.#.#...#.......#.......#.#.#.#.#.#.#...#.......#.#.#.#...................#.#.#...#.#.#
  #.###.###.###.#######.###.###.#.#.#########.#.#######.#.#####.#.#.#####.#####.#.#.#.###.###############.#####.#####
  #.........#.........#.#.....#.....#.....#.#.#...#.#.#...#.....#...#.#...#...#.#...#.#.#.......#.#...#...#.....#...#
  #####.###.###.#####.#####.#####.#######.#.#.###.#.#.###.#####.#.#.#.#.###.#.#.#.#.#.#.#.#######.#.###.#.#####.#.###
  #.....#.......#.............#...........#...#.......#...#.......#.#.......#...#.#.....#...............#.#.........#
  #################################.###.###.#.#######.###.#######.###########.#####.#################################
                                   A   U   Z M       S   P       U           J     O
                                   A   X   Z V       C   S       I           Q     Y         """,
"maze4": """
             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                     
"""
        }
        return mazes[name]

def test_maze1():
    donutmaze = DonutMaze('maze1')
    assert donutmaze.solve() == 23
    donutmaze = DonutMaze('maze2')
    assert donutmaze.solve() == 58
    donutmaze = DonutMaze('maze3')
    steps = donutmaze.solve() == 526

def test_maze2():
    donutmaze = DonutMaze('maze3')
    steps = donutmaze.solve(part2=True) == 6292
    donutmaze = DonutMaze('maze4')
    steps = donutmaze.solve(part2=True) == 396


if __name__ == '__main__':
    donutmaze = DonutMaze('maze3')
    print(f"part 1: {donutmaze.solve()}")
    donutmaze = DonutMaze('maze3', part2=True)
    print(f"part 0: {donutmaze.solve()}")
