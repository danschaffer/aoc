#!/usr/bin/env python3
import itertools


class Game:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.combinations = self.build_combinations()
        self.weapons = {
            'dagger': (8, 4),
            'shortsword': (10, 5),
            'warhammer': (25, 6),
            'longsword': (40, 7),
            'greataxe': (74, 8),
        }
        self.armor = {
            'leather': (13, 1),
            'chainmail': (31, 2),
            'splintmail': (53, 3),
            'bandedmail': (75, 4),
            'platemail': (102, 5),
        }
        self.rings = {
            'damage1': (25,1,0),
            'damage2': (50,2,0),
            'damage3': (100,3,0),
            'defense1': (20,0,1),
            'defense2': (40,0,2),
            'defense3': (80,0,3),
        }

    def build_combinations(self):
        weapon_armor_combinations = []
        for weapon0 in itertools.combinations(['dagger','shortsword','warhammer','longsword','greataxe'], 1):
            weapon_armor_combinations += [[weapon0[0]]]
        for weapon0 in itertools.combinations(['dagger','shortsword','warhammer','longsword','greataxe'], 1):
            for armor0 in itertools.combinations(['leather','chainmail','splintmail','bandedmail','platemail'], 1):
                weapon_armor_combinations += [[weapon0[0], armor0[0]]]
        combinations = weapon_armor_combinations[:]
        for wa0 in weapon_armor_combinations:
            for ring0 in itertools.combinations(['damage1','damage2','damage3','defense1','defense2','defense3'],1):
                combinations += [wa0 + [ring0[0]]]
        for wa0 in weapon_armor_combinations:
            for ring0 in itertools.combinations(['damage1','damage2','damage3','defense1','defense2','defense3'],2):
                combinations += [wa0 + [ring0[0],ring0[1]]]
        return combinations

    def find_lowest_win(self, boss, my_hp):
        wins = []
        for inventory in self.combinations:
            cost = self.cost_inventory(inventory)
            damage, armor = self.parse_inventory(inventory)
            me = {'hp': my_hp, 'damage': damage, 'armor': armor}
            winner = self.do_round(me, boss)
            if self.verbose:
                print(f"{cost} {inventory} me: {me} boss: {boss} {winner}")
            if winner == 'me':
                wins += [cost]
        return min(wins)

    def find_highest_loss(self, boss, my_hp):
        losses = []
        for inventory in self.combinations:
            cost = self.cost_inventory(inventory)
            damage, armor = self.parse_inventory(inventory)
            me = {'hp': my_hp, 'damage': damage, 'armor': armor}
            winner = self.do_round(me, boss)
            if self.verbose:
                print(f"{cost} {inventory} me: {me} boss: {boss} {winner}")
            if winner == 'boss':
                losses += [cost]
        return max(losses)

    def cost_inventory(self, inventory):
        cost = 0
        for item in inventory:
            if item in self.weapons.keys():
                cost += self.weapons[item][0]
            elif item in self.armor.keys():
                cost += self.armor[item][0]
            elif item in self.rings.keys():
                ring = self.rings[item]
                cost += ring[0]
        return cost

    def parse_inventory(self, inventory):
        damage = 0
        armor = 0
        for item in inventory:
            if item in self.weapons.keys():
                damage += self.weapons[item][1]
            elif item in self.armor.keys():
                armor += self.armor[item][1]
            elif item in self.rings.keys():
                ring = self.rings[item]
                damage += ring[1]
                armor += ring[2]
        return damage, armor

    def do_round(self, me, boss):
        bosshp = boss['hp']
        mehp = me['hp']
        while True:
            damage1 = max(1, me['damage'] - boss['armor'])
            bosshp -= damage1
            if self.verbose:
                print(f"The player deals {me['damage']} - {boss['armor']} = {damage1} damage; the boss goes down to {bosshp} hit points.")
            if bosshp <= 0:
                return 'me'
            damage2 = max(1, boss['damage'] - me['armor'])
            mehp -= damage2
            if self.verbose:
                print(f"The boss deals {boss['damage']} - {me['armor']} = {damage2} damage; the player goes down to {mehp} hit points.")
            if mehp <= 0:
                return 'boss'

def test1():
    me = {'hp': 8, 'damage': 5, 'armor': 5}
    boss = {'hp': 12, 'damage': 7, 'armor': 2}
    game = Game(True)
    assert game.do_round(me, boss) == 'me'

def test2():
    boss = {'hp': 109, 'damage': 8, 'armor': 2}
    game = Game()
    assert(game.find_lowest_win(boss, 100) == 111)
    assert(game.find_highest_loss(boss, 100) == 188)

if __name__ == '__main__':
    boss = {'hp': 109, 'damage': 8, 'armor': 2}
    game = Game()
    print(f"part 1: {game.find_lowest_win(boss, 100)}")
    print(f"part 2: {game.find_highest_loss(boss, 100)}")
