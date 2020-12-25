#!/usr/bin/env python3

class Day25:
    def __init__(self, card, door):
        self.card = card
        self.door = door
        self.card_loopsize = 0
        self.door_loopsize = 0

    def find_loop(self, goal):
        start = 1
        key = 7
        loop = 0
        while start != goal:
            start = (start * key) % 20201227
            loop += 1
        return loop

    def calculate_loop(self, key, loop):
        result = 1
        for _ in range(loop):
            result = (result * key) % 20201227
        return result

    def run(self):
        self.card_loopsize = self.find_loop(self.card)
        self.door_loopsize = self.find_loop(self.door)
        return self.calculate_loop(self.door, self.card_loopsize)
#        return self.calculate_loop(self.card, self.door_loopsize)

def test1():
    test_day25 = Day25(5764801, 17807724)
    assert test_day25.run() == 14897079
    test_day25a = Day25(12232269, 19452773)
    assert test_day25a.run() == 354320

if __name__ == '__main__':
    print("advent of code: day25")
    day25 = Day25(12232269, 19452773)
    print(f"part 1: {day25.run()}")
