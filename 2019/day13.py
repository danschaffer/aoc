#!/usr/bin/env python

from intcode import Intcode

class Game:
    def __init__(self, data, input):
        self.intcode = Intcode(data, input)
        self.screen = {}

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

    def run_game(self):
        game.intcode.data[0] = 2
        while self.intcode.is_running():
            self.intcode.run()
            self.draw_screen()
            if (-1,0) in self.screen:
                print(f"score={self.screen[(-1,0)]}")
            move_s = input("enter move[left=-1,neutral=0,right=1]: ")
            if len(move_s) == 0:
                move = 0
            else:
                move = int(move_s)
            self.intcode.inputs = [move]

if __name__ == '__main__':
    data = [int(item) for item in open('day13.input').read().strip().split(',')]
    game = Game(data[:], [])
    game.intcode.run()
    print(game.intcode.outputs)
    print(f"part 1: {game.get_blocks()}")
    game = Game(data[:], [])
    game.run_game()
