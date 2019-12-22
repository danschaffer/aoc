#!/usr/bin/env python

class Deck:
    def __init__(self, size, decks=1):
        self.cards = []
        for _ in range(decks):
            self.cards += list(range(size))

    def deal_new_stack(self):
        self.cards = list(reversed(self.cards))
        return self.cards

    def deal_with_increment(self, n):
        newdeck = {}
        count = 0
        while len(newdeck) != len(self.cards):
            newdeck[count * n % len(self.cards)] = self.cards[count]
            count += 1
        for card in range(len(self.cards)):
            self.cards[card] = newdeck[card]
        return self.cards

    def cut(self, n):
        self.cards = self.cards[n:] + self.cards[0:n]
        return self.cards

    def parse(self, command):
        if command == 'deal into new stack':
            self.deal_new_stack()
        elif command.startswith('cut'):
            self.cut(int(command.split(' ')[-1]))
        elif command.startswith('deal with increment'):
            self.deal_with_increment(int(command.split(' ')[-1]))
        else:
            print(f"unknown command {command}")

    def parse_commands(self, commands):
        for command in commands:
            self.parse(command)

def test1():
    deck = Deck(10)
    assert deck.deal_new_stack() == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    deck = Deck(10)
    assert deck.cut(3) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

    deck = Deck(10)
    assert deck.cut(-4) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

    deck = Deck(10)
    assert deck.deal_with_increment(3) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

    deck = Deck(10)
    assert deck.deal_with_increment(7) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

def test2():
    deck = Deck(10)
    commands = ['deal with increment 7', 'deal into new stack', 'deal into new stack']
    deck.parse_commands(commands)
    assert deck.cards == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

    deck = Deck(10)
    commands = ['cut 6', 'deal with increment 7', 'deal into new stack']
    deck.parse_commands(commands)
    assert deck.cards == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]

    deck = Deck(10)
    commands = ['deal with increment 7', 'deal with increment 9', 'cut -2']
    deck.parse_commands(commands)
    assert deck.cards == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

    deck = Deck(10)
    commands = ['deal into new stack', 'cut -2', 'deal with increment 7', 'cut 8', 'cut -4', 'deal with increment 7', 'cut 3', 'deal with increment 9', 'deal with increment 3', 'cut -1']
    deck.parse_commands(commands)
    assert deck.cards == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

if __name__ == '__main__':
    deck = Deck(10007)
    commands = open('./day22.input').read().strip().split('\n')
    deck.parse_commands(commands)
    print(f"part 1: {deck.cards.index(2019)}")  # 3324
