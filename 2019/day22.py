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

# https://topaz.github.io/paste/#XQAAAQAgBQAAAAAAAAAzHIoib6pENkSmUIKIED8dy140D1lKWSMhNhZz+hjKgIgfJKPuwdqIBP14lxcYH/qI+6TyUGZUnsGhS4MQYaEtf9B1X3qIIO2JSejFjoJr8N1aCyeeRSnm53tWsBtER8F61O2YFrnp7zwG7y303D8WR4V0eGFqtDhF/vcF1cQdZLdxi/WhfyXZuWC+hs8WQCBmEtuId6/G0PeMA1Fr78xXt96Um/CIiLCievFE2XuRMAcBDB5We73jvDO95Cjg0CF2xgF4yt3v4RB9hmxa+gmt6t7wRI4vUIGoD8kX2k65BtmhZ7zSZk1Hh5p1obGZ6nuuFIHS7FpuSuv1faQW/FuXlcVmhJipxi37mvPNnroYrDM3PFeMw/2THdpUwlNQj0EDsslC7eSncZQPVBhPAHfYojh/LlqSf4DrfsM926hSS9Fdjarb9xBYjByQpAxLDcmDCMRFH5hkmLYTYDVguXbOCHcY+TFbl+G/37emZRFh/d+SkeGqbFSf64HJToM2I7N2zMrWP7NDDY5FWehD5gzKsJpEg34+sG7x2O82wO39qBlYHcYg1Gz4cLBrH1K1P+KWvEdcdj/NBtrl6yftMlCu6pH4WTGUe9oidaiRuQZOGtw71QsTQUuhpdoWO4mEH0U9+CiPZCZLaQolFDSky1J9nDhZZHy3+ETcUeDOfSu+HI3WuKC0AtIRPdG8B9GhtxZQKAx+5kyi/ek7A2JAY9SjrTuvRADxx5AikbHWXIsegZQkupAc2msammSkwY8dRMk0ilf5vh6kR0jHNbSi0g0KJLCJfqggeX24fKk5Mdh8ULZXnMfMZOmwEGfegByYbu91faLijfW4hoXCB1nlsWTPZEw2PCZqqhl9oc1q25H2YkkvKLxEZWl6a9eFuRzxhB840I1zdBjUVgfKd9/V4VdodzU2Z2e+VEh7RbJjQNFC/rG8dg==
def day22p2(infile):
    n = 119315717514047
    c = 2020

    a,b = 1,0
    for l in open(infile).readlines():
        if l == 'deal into new stack\n':
            la, lb = -1, -1
        elif l.startswith('deal with increment '):
            la, lb = int(l[len('deal with increment '):]), 0
        elif l.startswith('cut '):
            la, lb = 1, -int(l[len('cut '):])
        a = (la * a) % n
        b = (la * b + lb) % n

    M = 101741582076661
    def inv(a,n): return pow(a, n-2, n)

    Ma = pow(a, M, n)
    Mb = (b * (Ma - 1) * inv(a-1,n)) % n
    return ((c-Mb) * inv(Ma,n)) % n


if __name__ == '__main__':
    deck = Deck(10007)
    commands = open('./day22.input').read().strip().split('\n')
    deck.parse_commands(commands)
    print(f"part 1: {deck.cards.index(2019)}")  # 3324
    print(f"part 2: {day22p2('./day22.input')}")