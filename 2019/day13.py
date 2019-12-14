#!/usr/bin/env python

import sys
from intcode import Intcode

class Game:
    def __init__(self, data, input):
        self.intcode = Intcode(data, input)
        self.screen = {}
        self.rounds = 0

    def find_obj(self, obj):
        for coord in self.screen.keys():
            if self.screen[coord] == obj:
                return coord

    def get_blocks(self):
        pieces = []
        blocks = 0
        for n in range(len(game.intcode.outputs)):
            if n % 3 == 2:
                pieces += [game.intcode.outputs[n]]
        for n in range(len(pieces)):
            if pieces[n] == 2:
                blocks += 1
        return blocks

    def draw_screen(self):
        outputs = self.intcode.outputs
        self.intcode.outputs = []
        index = 0
        while index < len(outputs):
            x = outputs[index]
            y = outputs[index + 1]
            item = outputs[index + 2]
            index += 3
            self.screen[(x,y)] = item
        screen = ""
        for y in range(25):
            for x in range(41):
                if (x,y) not in self.screen or self.screen[(x,y)] == 0:
                    screen += ' '
                elif self.screen[(x,y)] == 1:
                    screen += 'w'
                elif self.screen[(x,y)] == 2:
                    screen += 'b'
                elif self.screen[(x,y)] == 3:
                    screen += 'p'
                elif self.screen[(x,y)] == 4:
                    screen += 'o'
            screen += '\n'
        print(f"\n{screen}")

    def run_game(self, manual=False):
        game.intcode.data[0] = 2
        last_move = ' '
        score = 0
        while self.intcode.is_running():
            self.rounds += 1
            self.intcode.run()
            self.draw_screen()
            ball = self.find_obj(4)
            paddle = self.find_obj(3)
            score = self.screen[(-1,0)]
            if (-1,0) in self.screen:
                print(f"score={score} rounds={self.rounds} ball={ball} paddle={paddle}")

            if manual:
                move_s = input("enter move[left=-1,,neutral=0,right=1.]: ")
                if len(move_s) == 0:
                    move_s = last_move
                if move_s == ',':
                    move = -1
                elif move_s == '.':
                    move = 1
                elif move_s == ' ':
                    move = 0
                elif move_s == 's':
                    name = f"day13-{self.rounds}"
                    data = [self.intcode.data[n] for n in self.intcode.data]
                    open(name, 'w').write(str(data))
                    print(f"wrote file {name}")
                    continue
                else:
                    continue
                last_move = move_s
            else:
                if ball[0] < paddle[0]:
                    move = -1
                elif ball[0] > paddle[0]:
                    move = 1
                else:
                    move = 0
                self.intcode.inputs = [move]
        return score


if __name__ == '__main__':
    name = 'day13.input'
    if len(sys.argv) > 1:
        name = sys.argv[1]
    contents = open(name).read().strip()
    if contents.startswith("["):
        contents = contents[1:]
    if contents.endswith("]"):
        contents = contents[:-1]
    data = [int(item.strip()) for item in contents.split(',')]
    game = Game(data[:], [])
    game.intcode.run()
    print(game.intcode.outputs)
    part1 = game.get_blocks()
    game = Game(data[:], [])
    part2 = game.run_game()
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
