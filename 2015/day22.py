#!/usr/bin/env python3

class GameSpells:
    def __init__(self, boss=71, damage=10, me=50, mana=500):
        self.boss = boss
        self.damage = damage
        self.me = me
        self.mana = mana
        self.cache = []
        self.solutions = []

    def solve_bfs(self, hard=False):
        self.cache = [(0, self.boss, self.me, self.mana, 0, 0, 0, 1)]
        while len(self.cache) > 0:
            armor = 0
            (spent, boss, me, mana, shield, poison, recharge, myturn) = self.cache.pop()
            if shield > 0:
                shield -= 1
                armor = 7
            if poison > 0:
                poison -= 1
                boss -= 3
            if recharge > 0:
                recharge -= 1
                mana += 101
            if boss <= 0:
                self.solutions += [spent]
                continue
            if hard and myturn == 1:
                me = me - 1
            if me <= 0:
                continue
            if myturn == 1:
                if mana < 53:
                    continue
                if mana >= 53: # missle
                    spent1 = spent + 53
                    mana1 = mana - 53
                    boss1 = boss - 3
                    self.cache += [(spent1, boss1, me, mana1, shield, poison, recharge, 0)]
                if mana >= 73: # drain
                    spent1 = spent + 73
                    mana1 = mana - 73
                    boss1 = boss - 2
                    me1 = me + 2
                    self.cache += [(spent1, boss1, me1, mana1, shield, poison, recharge, 0)]
                if shield == 0 and mana >= 113: # shield
                    spent1 = spent + 113
                    mana1 = mana - 113
                    shield1 = 6
                    self.cache += [(spent1, boss, me, mana1, shield1, poison, recharge, 0)]
                if poison == 0 and mana >= 173: # poison
                    spent1 = spent + 173
                    mana1 = mana - 173
                    poison1 = 6
                    self.cache += [(spent1, boss, me, mana1, shield, poison1, recharge, 0)]
                if recharge == 0 and mana >= 229: # recharge
                    spent1 = spent + 229
                    mana1 = mana - 229
                    recharge1 = 5
                    self.cache += [(spent1, boss, me, mana1, shield, poison, recharge1, 0)]
            else:
                bossdamage = self.damage - armor
                me = me - bossdamage
                self.cache += [(spent, boss, me, mana, shield, poison, recharge, 1)]
        return min(self.solutions)

if __name__ == '__main__':
    game = GameSpells()
    print(f"part 1: {game.solve_bfs()}")
    game = GameSpells()
    print(f"part 2: {game.solve_bfs(hard=True)}")