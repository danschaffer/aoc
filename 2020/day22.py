#!/usr/bin/env python3

class Day22:
    def __init__(self,deck1=None, deck2=None):
        self.deck1 = deck1
        self.deck2 = deck2
        self.cache = []

    def load(self, file):
        (lines1, lines2) = open(file).read().strip().split('\n\n')
        self.deck1 = [int(card) for card in lines1.split('\n')[1:]]
        self.deck2 = [int(card) for card in lines2.split('\n')[1:]]
        self.cache = []

    def run(self):
        while len(self.deck1) > 0 and len(self.deck2) > 0:
            card1 = self.deck1.pop(0)
            card2 = self.deck2.pop(0)
            if card1 > card2:
                self.deck1 += [card1, card2]
            else:
                self.deck2 += [card2, card1]
            self.cache.append([self.deck1, self.deck2])
        if len(self.deck2) == 0:
            return 1
        else:
            return 2

    def score(self):
        cards = self.deck1 + self.deck2
        return sum([(count+1) * card for count, card in enumerate(reversed(cards))])

    def run_part1(self):
        self.run()
        cards = self.deck1 + self.deck2
        return sum([(count+1) * card for count, card in enumerate(reversed(cards))])

    def run_part2(self):
        while len(self.deck1) > 0 and len(self.deck2) > 0:
            if ([self.deck1, self.deck2]) in self.cache:
                return 1
            self.cache.append([self.deck1[:], self.deck2[:]])
            card1 = self.deck1.pop(0)
            card2 = self.deck2.pop(0)
            if len(self.deck1) >= card1 and len(self.deck2) >= card2:
                if Day22(self.deck1[:][0:card1], self.deck2[:][0:card2]).run_part2() == 1:
                    self.deck1 += [card1, card2]
                else:
                    self.deck2 += [card2, card1]
            else:
                if card1 > card2:
                    self.deck1 += [card1, card2]
                else:
                    self.deck2 += [card2, card1]
        if len(self.deck2) == 0:
            return 1
        else:
            return 2

def test1():
    test_day22 = Day22()
    test_day22.load('./day22-test.input')
    assert test_day22.run_part1() == 306
    test_day22.load('./day22-test.input')
    test_day22.run_part2()
    assert test_day22.score() == 291
    test_day22.load('./day22-test2.input')
    test_day22.run_part2()
    assert test_day22.score() == 369

def test2():
    test_day22 = Day22()
    test_day22.load('./day22.input')
    assert test_day22.run_part1() == 33010
    test_day22.load('./day22.input')
    result = test_day22.run_part2()
    assert result == 1
    assert sum([(count+1) * card for count,card in enumerate(reversed(test_day22.deck1))]) == 32769

if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22()
    day22.load('./day22.input')
    print(f"part 1: {day22.run_part1()}")
    day22.load('./day22.input')
    RESULT = day22.run_part2()
    if RESULT == 1:
        score = sum([(count+1) * card for count,card in enumerate(reversed(day22.deck1))])
    else:
        score = sum([(count+1) * card for count,card in enumerate(reversed(day22.deck2))])
    print(f"part 2: {score}")
