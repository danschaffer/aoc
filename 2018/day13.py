#!/usr/bin/env python3

class Day13:
    def __init__(self, file):
        self.data = {}
        self.carts = []
        for row,line in enumerate(open(file).readlines()):
            for column, char in enumerate(line):
                if char == '>':
                    self.data[column,row] = '-'
                    self.carts.append(((column,row),(1,0),'l',True))
                elif char == '<':
                    self.data[column,row] = '-'
                    self.carts.append(((column,row),(-1,0),'l',True))
                elif char == '^':
                    self.data[column,row] = '|'
                    self.carts.append(((column,row),(0,-1),'l',True))
                elif char == 'v':
                    self.data[column,row] = '|'
                    self.carts.append(((column,row),(0,1),'l',True))
                elif char != ' ' and char != '\n':
                    self.data[column,row] = char
    
    def check_collisions(self):
        positions = set()
        for cart in self.carts:
            if cart[0] in positions:
                return True
            positions.add(cart[0])

    def remove_collisions(self):
        positions = set()
        collisions = []
        removals = []
        for cart in self.carts:
            if cart[3] is False:
                continue
            if cart[0] in positions:
                collisions.append(cart[0])
            else:
                positions.add(cart[0])
        for n,cart in enumerate(self.carts):
            if cart[3] == True and cart[0] in collisions:
                self.carts[n] = (cart[0],cart[1],cart[2],False)

    def change_direction(self,loc, dir, turn):
        if self.data[loc] == '+':
            if turn == 'l' and dir == (-1,0):
                turn = 's'
                dir = (0,1)
            elif turn == 'l' and dir == (1,0):
                turn = 's'
                dir = (0,-1)
            elif turn == 'l' and dir == (0,-1):
                turn = 's'
                dir = (-1,0)
            elif turn == 'l' and dir == (0,1):
                turn = 's'
                dir = (1,0)
            elif turn == 's':
                turn = 'r'
            elif turn == 'r' and dir == (-1,0):
                turn = 'l'
                dir = (0,-1)
            elif turn == 'r' and dir == (1,0):
                turn = 'l'
                dir = (0,1)
            elif turn == 'r' and dir == (0,-1):
                turn = 'l'
                dir = (1,0)
            elif turn == 'r' and dir == (0,1):
                turn = 'l'
                dir = (-1,0)
        elif self.data[loc] == '/':
            if dir == (-1,0):
                dir = (0,1)
            elif dir == (1,0):
                dir = (0,-1)
            elif dir == (0,-1):
                dir = (1,0)
            elif dir == (0,1):
                dir = (-1,0)
        elif self.data[loc] == '\\':
            if dir == (-1,0):
                dir = (0,-1)
            elif dir == (1,0):
                dir = (0,1)
            elif dir == (0,-1):
                dir = (-1,0)
            elif dir == (0,1):
                dir = (1,0)
        return dir, turn

    def run_part1(self):
        while True:
            self.carts.sort(key=lambda x:x[0][1]*100+x[0][0])
            for n,cart in enumerate(self.carts):
                loc, dir, turn, _ = cart
                loc = (loc[0]+dir[0],loc[1]+dir[1])
                dir,turn = self.change_direction(loc,dir,turn)
                self.carts[n] = (loc, dir, turn, True)
                if self.check_collisions():
                    return loc

    def done(self):
        exists = 0
        coord = None
        for cart in self.carts:
            if cart[3] is True:
                exists += 1
                coord = cart[0]
        if exists == 1:
            return coord

    def run_part2(self):
        tick = 0
        while True:
            tick += 1
            self.carts.sort(key=lambda x:x[0][1]*100+x[0][0])
            for n,cart in enumerate(self.carts):
                loc, dir, turn, crashed = cart
                if not crashed:
                    continue
                loc = (loc[0]+dir[0],loc[1]+dir[1])
                dir,turn = self.change_direction(loc,dir,turn)
                self.carts[n] = (loc, dir, turn, crashed)
                self.remove_collisions()
            if self.done() is not None:
                return self.done()

def test1():
    test_day13 = Day13('./day13-test.input')
    assert test_day13.run_part1() == (7,3)
    test_day13 = Day13('./day13-test2.input')
    assert test_day13.run_part2() == (6,4)

    test_day13 = Day13('./day13.input')
    assert test_day13.run_part1() == (143,43)
    test_day13 = Day13('./day13.input')
    assert test_day13.run_part2() == (116,125)

if __name__ == '__main__':
    print("advent of code: day13")
    day13 = Day13('./day13.input')
    print(f"part 1: {day13.run_part1()}")
    print(f"part 2: {day13.run_part2()}")
