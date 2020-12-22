#!/usr/bin/env python3

class Day22:
    def __init__(self,file):
        (lines1, lines2) = open(file).read().strip().split('\n\n')
        self.deck1 = [int(card) for card in lines1.split('\n')[1:]]
        self.deck2 = [int(card) for card in lines2.split('\n')[1:]]

    def play_round(self):
        card1 = self.deck1.pop(0)
        card2 = self.deck2.pop(0)
        if card1 > card2:
            self.deck1 += [card1, card2]
        else:
            self.deck2 += [card2, card1]

    def run(self):
        while len(self.deck1) > 0 and len(self.deck2) > 0:
            self.play_round()

    def score(self):
        cards = self.deck1 + self.deck2
        return sum([(count+1) * card for count, card in enumerate(reversed(cards))])

    def run_part1(self):
        self.run()
        return self.score()

    def run_part2(self):
        return -1

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run_part1() == 306
    assert test_day22.run_part2() == -1

def test2():
    test_day22 = Day22('./day22.input')
    assert test_day22.run_part1() == 33010
    assert test_day22.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22('./day22.input')
    print(f"part 1: {day22.run_part1()}")
    print(f"part 2: {day22.run_part2()}")
