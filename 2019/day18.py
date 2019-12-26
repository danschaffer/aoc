#!/usr/bin/env python
import re
import time
class Vault:
    def __init__(self, text):
        self.keys = []
        self.key_locations = {}
        self.map = {}
        self.doors = {}
        self.paths = {}
        self.cache = []
        self.parse_map(text.strip())
        self.start = time.time()

    def collect_keys(self, moves):
        keys = []
        for move in moves:
            key = self.map[move]
            if self.is_key(key) and key not in keys:
                keys += [key]
        return keys

    def keys_left(self, keys):
        keys_left = self.keys[:]
        for key in keys:
            keys_left.remove(key)
        return keys_left

    def valid_path(self, moves):
        keys = []
        for move in moves:
            object = self.map[move]
            if self.is_key(object):
                keys += [object]
            if self.is_door(object) and object.lower() not in keys:
                return False
        return True

    def cache_hit(self, keys):
        if ''.join(keys) in self.cache:
            return False
        self.cache += [''.join(keys)]
        return True

    def find_location(self, object):
        if object in self.key_locations:
            return self.key_locations[object]
        for pos in self.map:
            if self.map[pos] == object:
                self.key_locations[object] = pos
                return pos

    def is_key(self, object):
        return not re.search('[a-z]', object) is None

    def is_door(self, object):
        return not re.search('[A-Z]', object) is None

    def find_keys(self):
        if self.keys == []:
            keys = []
            for point in self.map:
                if self.is_key(self.map[point]):
                    keys += [self.map[point]]
            self.keys = list(sorted(keys))
        return self.keys

    def show_time(self):
        out = ''
        secs = time.time() - self.start
        if secs // 60 // 60 > 0:
            out += f"{secs // 60 // 60}h"
        out += f"{secs % 3600 // 60}m{round(secs%60,0)}s"
        return out

    def find_path(self, start, goal):
        paths = [{'loc': start, 'moves': [], 'doors': []}]
        cache = []
        doors = []
        while len(paths) > 0:
            move = paths[0]
            paths.remove(paths[0])
            if move['loc'] == goal:
                return move
            if self.is_door(self.map[move['loc']]):
                move['doors'] = move['doors'][:] + [self.map[move['loc']].lower()]
            cache += [move['loc']]
            moves = self.add_moves(move)
            for move in moves:
                if move['loc'] not in cache:
                    paths = paths[:] + [move]
            paths.sort(key=lambda move: len(move['moves']))

    def print_move(self, move, message=''):
        moves = move['moves']
        keys = move['keys']
        position = move['loc']
        print(f"{message} moves={moves} position={position} keys={keys}")

    def add_if_valid(self, position):
        if position['loc'] in self.map:
            return [position]
        return []

    def add_moves(self, position):
        moves = [] + \
        self.add_if_valid({'loc': (position['loc'][0] - 1, position['loc'][1]), 'moves': position['moves'] + [(position['loc'][0] - 1, position['loc'][1])], 'doors': position['doors']}) +\
        self.add_if_valid({'loc': (position['loc'][0] + 1, position['loc'][1]), 'moves': position['moves'] + [(position['loc'][0] + 1, position['loc'][1])], 'doors': position['doors']}) +\
        self.add_if_valid({'loc': (position['loc'][0], position['loc'][1] - 1), 'moves': position['moves'] + [(position['loc'][0], position['loc'][1] - 1)], 'doors': position['doors']}) +\
        self.add_if_valid({'loc': (position['loc'][0], position['loc'][1] + 1), 'moves': position['moves'] + [(position['loc'][0], position['loc'][1] + 1)], 'doors': position['doors']})
        return moves

    def map_all_keys(self):
        self.paths = {}
        keys = self.find_keys() + ['@']
        print(f"looking for paths for {len(keys)}")
        for k1 in keys:
            start = time.time()
            self.paths[k1] = {}
            for k2 in keys:
                if k1 == k2:
                    continue
                self.paths[k1][k2] = self.find_path(self.find_location(k1), self.find_location(k2))
            print(f"found path {k1} = {round(time.time()-start, 1)}s")

    def update_keys(self, path, keys_left):
        keys = []
        for key in path['doors']:
            if key in keys_left:
                keys += [key]
        path['doors'] = keys

    def shortest_key(self, paths):
        shortest = len(paths[0]['keys'])
        for path in paths:
            if len(path['keys']) < shortest:
                shortest = len(path['keys'])
        return shortest

    def run(self):
        current = '@'
        keys = self.find_keys()
        self.map_all_keys()
        paths = [{'current': '@', 'keys': [], 'moves': []}]
        best = None
        lastbest = None
        counter = 0
        start = time.time()
        print(f"0 {self.show_time()}")
        while self.shortest_key(paths) < len(keys):
            if len(paths[0]['keys']) == len(keys):
                if not best or len(paths[0]['moves']) < best:
                    best = len(paths[0]['moves'])
                    print(f"{counter} paths={len(paths)} best={best} keys={paths[0]['keys']}")
            paths.sort(key=lambda e: (-1 * len(e['keys']), len(e['moves'])))
            n = 0
            while len(paths[n]['keys']) == len(keys) and n < len(paths):
                if best is not None and len(paths[n]['moves']) > best:
                    paths.remove(paths[n])
                else:
                    n += 1
            if n == len(paths):
                return len(paths[0]['moves'])
            path0 = paths[n]
            paths.remove(path0)
            for key in self.keys_left(path0['keys']):
                path1 = self.paths[path0['current']][key]
                moves = path0['moves'][:] + path1['moves'][:]
                keys1 = self.collect_keys(moves)
                new_path = {'current':key, 'keys': keys1, 'moves': moves}
                if self.valid_path(moves) and self.cache_hit(keys1):
                    paths += [new_path]
            counter += 1
            if counter % 5000 == 0:
                print(f"{counter} {len(paths)} {round(time.time()-start,1)}s {self.show_time()}")
                start = time.time()
        return len(paths[0]['moves'])

    def parse_map(self, text):
        y = 0
        for line in text.split('\n'):
            x = 0
            for item in list(line):
                if re.search('[A-Za-z.@]', item):
                    self.map[(x,y)] = item
                x += 1
            y += 1


def test_1():
    vault = Vault("""
#########
#b.A.@.a#
#########
""")
    assert vault.is_door('@') is False
    assert vault.is_key('@') is False
    assert vault.find_location('@') == (5, 1)
    assert vault.find_location('a') == (7, 1)
    path = vault.find_path(vault.find_location('@'), vault.find_location('a'))
    assert path['doors'] == []
    assert path['moves'] == [(6,1), (7,1)]
    path = vault.find_path(vault.find_location('@'), vault.find_location('b'))
    assert path['doors'] == ['a']
    assert path['moves'] == [(4,1), (3,1), (2,1), (1,1)]
    assert vault.find_keys() == ['a', 'b']
    assert vault.run() == 8

def test_2():
    vault = Vault("""
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""")
    result = vault.run()
    assert result == 86


# def test_3():
#     vault = Vault("""
# #################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################
# """)
#     result = vault.run()
#     assert result == 136

def test_4():
    vault = Vault("""
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""")
    result = vault.run()
    assert result == 132

def test_5():
    vault = Vault("""
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""")
    result = vault.run()
    assert result == 81

if __name__ == '__main__':
    vault = Vault("""
#################################################################################
#..f....#...........#.....#.........#m..#.........#.#.......#...............#...#
#.#.###.#########.#.#.###.#.#.#####.#.#.#Q#.#####.#.#.###.###.#V#####.#####.#.#C#
#.#...#...........#t#.#.#...#.#...#.#.#.#.#.#.......#.#.#.....#.....#.#...#...#.#
#####.###############.#.#####.#.#.###.#.#.#.#########.#.###########.###.#.#####.#
#.....#...............#...#.#...#...#.#.#.#.........#.#...........#.....#.#...#e#
#.###.#.###############.#.#.#######.#I#.#.#########.#.###########.#####.#.#.#.#.#
#...#.#...#.....#.......#.....#.G.#.#.#.#.#.......#.#.....#.......#...#.#...#.#.#
###.#.###.#.#.#.###.###########.#.#.#.#.#.#####.#.#.#####.#.#.#####.#.#######.#.#
#...#.#...#.#.#...#.#...#.....#b#.#...#.#.......#.#.........#.#.....#.#...#...#.#
#.#####.###.#.###.#.#.#.#.###.#.#.#####.#########.#############.#####.#.#.#.###.#
#.......#.#.#...#.Z.#.#.B.#.....#.....#.#.......#.....#.........#.#.....#...#...#
#.#######.#.###.#####.#.#############.#M#.#.#########.#.#########.#.#############
#.#.......#...#.#.....#u#...K.......#.#.#.#...........#...#.........#...........#
#.###.###.#.###.#.#####.#.#####.###.#.#.#.#############.#.#.#########.#########.#
#...#...#...#...#.U.#...#.#..j#...#.#g..#.......#...R.#.#.#.....#.....#.......#.#
###.#######.#.#####.#####.#.#.###.#.#############.###.#.#.#######.#########.###.#
#.#.......#.#.....#..k....#.#.#d..#.#...#.........#...#.#.........#.#.......#...#
#.#######.#.#####.#####.###.#.#####.#.#.#.#########.###.#########.#.#.#.#####.#.#
#.....#...#.#.....#.H.#.#...#.S...#.D.#.#...#.....#.#...#.#.....#.#...#..a#...#.#
#.#.#.#.#####.#####.#.#.#.#######.#####.###.#.###.#.###.#.#.###.#.#.#####.#.###.#
#.#.#.#...#...#...#.#.#.#.#.....#.....#s#...#...#.#...#...#...#.#.#...#...#.#...#
###.#.###.#.###.#.#.#####J###.#######.#.#.#######.###.###.#####.#.#.###.#.#.#.###
#...#.#...#.#...#.#.#.....#...#.....#...#.#...#.....#.#...#...#.#.#.#...#.#.#...#
#.#####.###.#.###.#.###.###.###.#.#.#####.#.#.#.###.#.###.###.#.#.###.###.#.###.#
#.....#...#...#...#....h#...#...#.#.#...#...#.#.#.#.#...#.....#.#.....#...#.#.#.#
#.###.###.#.###.###########.#.###.#.###.#####.#.#.#.###.#######.#######.###.#.#.#
#.#.#.....#.#...#.....#...#...#.#.#.....#...#...#...#.#...#.....#.......#.#.#..p#
#.#.#########.###.#.#.#.#.###.#.#.#####.#.#######.###.###.#.###########.#.#.###.#
#.#.#.......#.....#.#...#...#...#.#...#.#.......#.#.#...#.#.......#...#.#.#...#.#
#.#.#.###.#.#.#####.#######.#####.###.#.#.#####.#.#.#.#.#.#######.#.#.#.#.###.#.#
#.#...#...#.#.....#.......#.....#...#...#.....#.#.#...#.#...#...#...#.#.#.#...#.#
#.#####.###.#####.#######.#####.###.#.###.#####.#.#####.#.###.#.#####.#.#.#.###.#
#...N.#.#.#.#.....#.......#...#.....#.#.#.#...#.#.......#.....#.......#...#...#.#
#####.#.#.#.#.#####.#######.#########.#.###.#.#.#######.#####################.#.#
#...#...#...#.....#.......#.#...#.....#.#...#.....#...X.#.....Y.#...#...W.....#.#
###.#####.#######.#######.#.#.#.#.#####.#.#########.#########.#.###.#.#.#######.#
#...#.....#...#.....#...#.#.#.#...#.....#.#.....#...#...#...#.#...#...#.#.#.....#
#.###.#####.#.#######.#.#.#.#.#######.#.#.#.###.#.###.#.#.#.#.###.#####.#.#.#####
#.........A.#.........#...#..x........#.......#.......#...#...#.........#.......#
#######################################.@.#######################################
#.O.......#.............#.......#.....................#...........#...#...#.#...#
###.#####.#######.#####.###.#.#.#.#####.#.#.#########.#######.###.#.#.#.#.#.#.#.#
#...#...#.......#.#..y....#.#.#.#.#...#.#.#.#.....#.........#...#.#.#...#.#.#.#.#
#.#####.#######.#.#.#####.###.#.#.#.#.#.###.#.###.#########.###.#.#.#####.#.#.#.#
#.#...#.......#.#.#.#...#.....#...#.#.#.#...#...#...#.....#.....#.#...#.#.#...#.#
#.#.#.#####.###.#.###.#.#############.#.#.#####.###.#.###.#######.###.#.#.#####.#
#..r#.#...#.....#.#.L.#.#...#...#.....#.#.........#.#.#...#.....#.....#.#.#..n..#
#####.#.#.###.###.#.###.#.#.#.#.###.###.#.#######.#.#.#.###.###.#######.#.#.#####
#...#...#...#..w..#.#.#.#.#.#.#...#...#.#...#...#.#...#...#.#...#.....#...#.....#
#.#.#######.#######.#.#.#.#.#.###.###.#.###.#.#.#######.#.#.#.#####.###.###.###.#
#.#...#...#.....#...#.#...#.....#...#.#.#.#.#.#.......#.#...#.#...#.#...#...#...#
###.#.#.#######.#.###.#########.###.#.#.#.#.#.#######.#.#####.#.#.#.#.#####.#.###
#...#...#...#.P.#.#...#.#.....#.#...#.#.#...#.#.#...#.#...#o#...#.#...#...#.#...#
#.#####.#.#.#.###.#.#.#.#.###.###.###.#.#.###.#.#.#.#.###.#.#####.#.###.#.#.###.#
#.....#.#.#.#.....#.#...#...#.....#...#.#...#.#...#.#.#.....#.....#.#...#.#...#.#
#.###.#.#.#.#######.#######.#########.#.#####.#.###.#.#.#####.#####.#.###.#.###.#
#.#.#.#.#.#...#.#.....#.....#...#...#.#.#.....#.#.#.#.#.#.....#...#.#...#.#.#...#
#.#.#.###.#.#.#.#.###.#.#####.#.#.#.#.#.#.#####.#.#.#.###.#####.###.###.#.###.###
#.#.#.E...#.#.#...#...#...#...#...#...#.#.....#.#.#.......#.........#..l#...#...#
#.#.#######.#.#####.###.#.#.#.#####.###.#####.#.#.#########.###.#####.#####.###.#
#.#.......#.#.....#.#.#.#.#.#.#...#.#...#.....#.#.#.....#...#.#.#...#.#...#.....#
#.#.#####.#.#####.#.#.#.#.###.#.#.###.###.#####.#.#.###.#####.#.#.#.#.###.#####.#
#.#.#.....#.#.......#.#.#.#...#.#.#...#.#.#.....#.#.#.#.....#.#...#...#...#.....#
#.#.#.#####.#.#######.#.#.#.###.#.#.###.#.#.#####.#.#.#####.#.#########.###.#####
#.#.#...#...#.#..q#...#.#.#.....#.#.#...#.#.#.....#.#.....#.#.......#...#...#...#
#.#.#.###.###.#.#.#.#####.#.#####.#.###.#.#.#.#.###.###.#.#.#######.#.#.#.#####.#
#.#.#.#...#.#...#.#.......#.....#.#...#.#.#...#.#v..#...#.#...#.....#.#.#.#...#.#
#.#.#.#.###.#.#################.#.###.#.#.###.###.###.#######.#.#####.###.#.#.#.#
#...#.#...#...#.............#...#...#.#.#...#.#...#.........#...#.......#...#...#
#.#####.#.#####.#.###########.#####.#.#.#.#.###.###########.#####.#####.#######.#
#.#...#.#.#.....#.....#.......#.....#.#.#.#...#.#...............#.#...#.......#.#
###.#.###.#.#########.#.#######.#####.#.#.###.#.#.#.#############.###.#####.###.#
#...#...#.#.#.........#.#.....#.....#.#.#.#...#.#.#....c..........#.....#.#.....#
#.#####.#.#.#.#########.#.#.#.#####.#.#.###.###.#.#################.###.#.#######
#.....#...#z#.......#...#.#.#...#.#.#.#.#...#...#.....#.....#...#...#.#.#.......#
#.###.#####.#######.#.###.#.###.#.#.#.#.#.###.#######.###.#.#.#.#.###.#.#T#.###.#
#...#.....#...#...#...#...#...#...#.#.#.#...#.#...#...#...#.#.#...#.#...#.#.#.#.#
###.#####.###.#.#.###########.###.#.#.#.#.#.#.#.###.###.###.#.#####.#F#####.#.#.#
#.......#.......#.............#...#.....#.#...#.........#.....#.............#i..#
#################################################################################""")
#     vault = Vault("""
# #################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################
# """)
    result = vault.run()
    print(result)
