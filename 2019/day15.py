#!/usr/bin/env python

import pickle
import os
from intcode import Intcode

class Oxygen:
    # 1-north,2-south,3-east,4-west
    def __init__(self, data):
        self.intcode = Intcode(data, input)
        self.pos = (0,0)
        self.screen = {(0,0): 0}
        self.moves = 0

    def do_move(self, move):
        import pdb; pdb.set_trace()
        if move == 'n':
            inputs = [1]
            dest = (self.pos[0], self.pos[1] - 1)
        elif move == 's':
            inputs = [2]
            dest = (self.pos[0], self.pos[1] + 1)
        elif move == 'w':
            inputs = [3]
            dest = (self.pos[0] - 1, self.pos[1])
        elif move == 'e':
            inputs = [4]
            dest = (self.pos[0] + 1, self.pos[1])
        self.intcode.inputs = inputs
        self.intcode.outputs = []
        self.intcode.run()
        output = self.intcode.outputs
        assert output == [1]
        self.pos == dest

    def check_moves(self):
        moves = []
        orig = self.pos
        for move in ['n', 's', 'w', 'e']:
            opp = ''
            if move == 'n':
                inputs = [1]
                dest = (self.pos[0], self.pos[1] - 1)
                opp = 's'
            elif move == 's':
                inputs = [2]
                dest = (self.pos[0], self.pos[1] + 1)
                opp = 'n'
            elif move == 'w':
                inputs = [3]
                dest = (self.pos[0] - 1, self.pos[1])
                opp = 'e'
            elif move == 'e':
                inputs = [4]
                dest = (self.pos[0] + 1, self.pos[1])
                opp = 'w'
            self.intcode.inputs = inputs
            self.intcode.outputs = []
            self.intcode.run()
            output = self.intcode.outputs
            if output == [0]:
                self.screen[dest] = 1
            elif output == [1]:
                import pdb; pdb.set_trace()
                self.screen[dest] = 0
                moves += [move]
                self.do_move(opp)
                self.intcode.outputs = []
            elif output == [2]:
                self.screen[dest] = 2
                moves += [move]
                self.do_move(opp)
                self.intcode.outputs = []
        return moves

    def run_auto(self):
        self.draw_screen()
        lastmove = None
        while True:
            self.draw_screen()
            moves = self.check_moves()
            move1 = moves[0]
            if lastmove == move1 and len(moves) > 1:
                move1 = moves[1]
            self.do_move(move1)

    def run_manual(self):
        self.draw_screen()
        inputs = []
        move=input("move n,s,e,w: ")
        if move == 'n':
            inputs = [1]
            dest = (self.pos[0], self.pos[1] - 1)
        elif move == 's':
            inputs = [2]
            dest = (self.pos[0], self.pos[1] + 1)
        elif move == 'w':
            inputs = [3]
            dest = (self.pos[0] - 1, self.pos[1])
        elif move == 'e':
            inputs = [4]
            dest = (self.pos[0] + 1, self.pos[1])
        self.intcode.inputs = inputs
        self.intcode.outputs = []
        self.intcode.run()
        output = self.intcode.outputs
        print(f"returned {output}")
        if output == [0]:
            self.screen[dest] = 1
        elif output == [1]:
            self.screen[dest] = 0
            self.pos = dest
            self.moves += 1
        elif output == [2]:
            self.screen[dest] = 2
            self.pos = dest
            self.moves += 1
        self.save()

    def save(self):
        save = {'pos':self.pos,'board':self.screen,'data':self.intcode.data, 'ip': self.intcode.pointer}
        with open('./day15.pickle','wb') as f:
            pickle.dump(save, f)

    def load(self):
        with open('./day15.pickle', 'rb') as f:
            data = pickle.load(f)
        self.pos = data['pos']
        self.screen = data['board']
        self.intcode.data = data['data']
        self.intcode.pointer = data['ip']

    def draw_screen(self):
        minx = 0
        maxx = 0
        miny = 0
        maxy = 0
        for point in self.screen.keys():
            if point[0] < minx:
                minx = point[0]
            elif point[0] > maxx:
                maxx = point[0]
            if point[1] < miny:
                miny = point[1]
            elif point[1] > maxy:
                maxy = point[1]
        screen = ""
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x,y) not in self.screen:
                    screen += ' '
                elif (x,y) == self.pos:
                    screen += 'D'
                elif (x,y) == (0,0):
                    screen += 'H'
                elif self.screen[(x,y)] == 0:
                    screen += '.'
                elif self.screen[(x,y)] == 1:
                    screen += '#'
                elif self.screen[(x,y)] == 2:
                    screen += 'X'
            screen += '\n'
        print(f"pos: {self.pos} moves: {self.moves}\n{screen}")


if __name__ == '__main__':
    name = 'day15.input'
    contents = open(name).read().strip()
    if contents.startswith("["):
        contents = contents[1:]
    if contents.endswith("]"):
        contents = contents[:-1]
    data = [int(item.strip()) for item in contents.split(',')]
    game = Oxygen(data[:])
    if os.path.exists('./day15.pickle'):
        game.load()
    game.run_auto()
#    while True:
#        game.run_manual()
