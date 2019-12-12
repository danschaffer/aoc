#!/usr/bin/env python

from intcode import Intcode

class HullPaintingRobot:
    def __init__(self, data, input):
        self.intcode = Intcode(data, input)
        self.dir = 0
        self.dirs = ['up', 'right', 'down', 'left']
        self.position = (0, 0)
        self.positions = {}

    def move(self, turn):
        assert turn in [0, 1]
        if turn == 0:
            self.dir = (self.dir - 1) % 4
        elif turn == 1:
            self.dir = (self.dir + 1) % 4
        x = self.position[0]
        y = self.position[1]
        if self.dir == 0: # up
            self.position = (x, y-1)
        elif self.dir == 1:  # right
            self.position = (x+1, y)
        elif self.dir == 2: # down
            self.position = (x, y+1)
        elif self.dir == 3: # left
            self.position = (x-1, y)

    def run(self):
        while self.intcode.is_running():
            self.intcode.run()
            assert self.intcode.inputs == []
            assert len(self.intcode.outputs) == 2
            color = self.intcode.outputs[0]
            turn = self.intcode.outputs[1]
            print(f"at {self.position} got color={color} turn={turn}")
            self.positions[self.position] = color
            self.move(turn)
            if self.position not in self.positions:
                current = 0
            else:
                current = self.positions[self.position]
            self.intcode.outputs = []
            self.intcode.inputs = [current]
        print("done")
        return len(self.positions)

    def show_message(self):
        first = list(self.positions.keys())[0]
        minx = first[0]
        miny = first[1]
        maxx = first[0]
        maxy = first[1]
        for position in self.positions:
            minx = min(minx, position[0])
            miny = min(miny, position[1])
            maxx = max(maxx, position[0])
            maxy = max(maxy, position[1])
        output = ''
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                if (x, y) not in self.positions or self.positions[(x,y)] == 0:
                    output += ' '
                else:
                    output += '#'
            output += '\n'
        return output


if __name__ == '__main__':
    data = [int(item) for item in open('day11.input').read().strip().split(',')]
    robot = HullPaintingRobot(data[:], [0])
    print(f"part 1: {robot.run()}")
    robot = HullPaintingRobot(data[:], [1])
    robot.run()
    print(f"part 2: \n{robot.show_message()}")
