#!/usr/bin/env python

class Day15:
    def __init__(self, inp):
        self.data = {}
        self.people = {}
        self.maxx = 0
        self.maxy = 0
        self.attackpower = 3
        self.inp = inp
        self.load(inp)

    def reset(self):
        self.data = {}
        self.people = {}
        self.load(self.inp)

    def load(self, str):
        goblin = elf = 0
        for y,line in enumerate(str.split('\n')):
            self.maxy = y+1
            self.maxx = len(line)
            for x,ch in enumerate(line):
                if ch == 'G':
                    self.people[f"G{goblin}"] = {'loc': (x,y), 'moves': 0, 'hp': 200}
                    goblin += 1
                    ch = '.'
                elif ch == 'E':
                    self.people[f"E{elf}"] = {'loc': (x,y), 'moves': 0, 'hp': 200}
                    elf += 1
                    ch = '.'
                self.data[(x,y)] = ch

    @property
    def won(self):
        goblin = sum([1 for p in self.people if p.startswith('G')])
        elf = sum([1 for p in self.people if p.startswith('E')])
        return goblin == 0 or elf == 0

    @property
    def rounds(self):
        result = 999999
        for p in self.people:
            result = min(result, p['moves'])
        return result

    @property
    def hp(self):
        return sum([p['hp'] for p in self.people])

    @property
    def next_piece(self):
        pieces = []
        for p in self.people:
            order = self.reading_order(self.people[p]['loc'])
            moves = self.people[p]['moves']
            pieces.append((p, moves, order))
        order = sorted(pieces, key=lambda i: (i[1], i[2]))
        return order[0][0]

    @property
    def locations(self):
        locs = {}
        for p in self.people:
            locs[self.people[p]['loc']] = p
        return locs
        
    def print(self):
        locs = self.locations
        for y in range(self.maxy):
            line = ''
            data = []
            for x in range(self.maxx):
                if (x,y) in locs:
                    p0 = locs[(x,y)]
                    line += p0[0]
                    data.append(str(self.people[p0]['hp']))
                else:
                    line += self.data[(x,y)]
            print(f"{line}     {' '.join(data)}")
    
    def adjacent(self, piece, enemies=None):
        if not enemies:
            enemies = self.enemies(piece)
        for move in [(piece[0]+1,piece[1]),(piece[0]-1,piece[1]),(piece[0],piece[1]-1),(piece[0],piece[1]+1)]:
            if move in enemies:
                return True
        
    def enemies(self, piece):
        return [self.people[p]['loc'] for p in self.people if p[0] != piece[0]]

    def allies(self, piece):
        return [self.people[p]['loc'] for p in self.people if p[0] == piece[0]]

    def best_move(self, piece_name):
        allies = self.allies(piece_name)
        enemies = self.enemies(piece_name)
        rowI,colI = self.people[piece_name]['loc']
        if self.adjacent((rowI,colI), enemies):
            return
        best_moves = []
        first_moves = [(rowI+1,colI),(rowI-1,colI),(rowI,colI-1),(rowI,colI+1)]
        for move in first_moves:
            if move not in self.data or self.data[move]!='.' or move in allies:
                continue
            if self.adjacent(move, enemies):
                best_moves.append((move,1,self.reading_order(move),self.reading_order(move)))
                continue
            seen = {(rowI,colI),(move)}
            r,c = move
            stack = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
            stack = [m for m in stack if (m[0],m[1]) in self.data and self.data[(m[0],m[1])]=='.' and (m[0],m[1]) not in allies]
            i = 1
            run = True
            while run:
                i+=1
                new_stack = []
                for tile in stack:
                    if tile in seen:
                        continue
                    seen.add(tile)
                    if self.adjacent(tile,enemies):
                        best_moves.append((move,i,self.reading_order(tile),self.reading_order(move)))
                        run=False
                        continue
                    r,c = tile
                    new_tiles = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                    new_stack += [m for m in new_tiles if self.data[(m[0],m[1])]=='.' and (m[0],m[1]) not in allies]
                stack =list(set(new_stack))
                if not stack:
                    run=False
        if best_moves:
            sorted_best_moves = sorted(best_moves,key=lambda i: (i[1], i[2],i[3]))
            return sorted_best_moves[0][0]

    def reading_order(self, move):
        return move[1]*self.maxx + move[0]

    def do_move(self, p, m):
        loc = self.locations
        self.people[p]['loc'] = m

    def attack(self, p):
        loc = self.people[p]['loc']
        locs = self.locations
        attacks = []
        for m in [(1,0),(-1,0),(0,1),(0,-1)]:
            attack_loc = loc[0] + m[0], loc[1] + m[1]
            if attack_loc in locs and not locs[attack_loc].startswith(p[0]):
                attacks.append((locs[attack_loc],self.people[locs[attack_loc]]['hp'],attack_loc[1]*self.maxx+attack_loc[0]))
        sorted_attacks = sorted(attacks, key=lambda i: (i[1],i[2]))
        if sorted_attacks:
            target = sorted_attacks[0][0]
            if target.startswith('G'):
                self.people[target]['hp'] = max(0, self.people[target]['hp']-self.attackpower)
            else:
                self.people[target]['hp'] = max(0, self.people[target]['hp']-3)
            if self.people[target]['hp'] == 0:
                del self.people[target]

    @property
    def round(self):
        moves = 99999
        for p in self.people:
            moves = min(moves, self.people[p]['moves'])
        return moves

    @property
    def score(self):
        points = 0
        for p in self.people:
            points += self.people[p]['hp']
        return points

    def run(self):
#        round = -1
        while not self.won:
#            if self.round > round:
#                print(f"{self.round}")
#                self.print()
#                round = self.round
            p = self.next_piece
            m = self.best_move(p)
            if m:
                self.do_move(p, m)
            self.attack(p)
            self.people[p]['moves'] += 1
#        self.print()
#        import pdb; pdb.set_trace()
        return self.round * self.score
        
    @property
    def elves(self):
        return len([p for p in self.people if p.startswith('E')])

    def run_part2(self):
        self.attackpower=4
        start_elves = self.elves
        while True:
            while not self.won:
                p = self.next_piece
                m = self.best_move(p)
                if m:
                    self.do_move(p, m)
                self.attack(p)
                self.people[p]['moves'] += 1
            if start_elves == self.elves:
                return self.round * self.score
            self.attackpower += 1
            self.reset()

def test1():
    assert Day15(t0).run() == 27730
    assert Day15(t1).run() == 36334
    assert Day15(t2).run() == 39514
    assert Day15(t3).run() == 27755
    assert Day15(t4).run() == 28944
    assert Day15(t5).run() == 18740
    assert Day15(t6).run() == 10804
    assert Day15(open('day15.input').read()).run() == 198744

def test2():
    assert Day15(t0).run_part2() == 4988
    assert Day15(t2).run_part2() == 31284
    assert Day15(t3).run_part2() == 3478
    assert Day15(t4).run_part2() == 6474
    assert Day15(t5).run_part2() == 1140
    assert Day15(t6).run_part2() == 517
    assert Day15(open('day15.input').read()).run_part2() == 66510

t0 = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

t1 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""


t2 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""


t3 = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""


t4 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""


t5 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

t6 = """###########
#G..#....G#
###..E#####
###########"""

t7 = """#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########"""

if __name__ == '__main__':
    print('advent of code: day15')
    print(f"part 1: {Day15(open('day15.input').read()).run()}")
    print(f"part 2: {Day15(open('day15.input').read()).run_part2()}")
