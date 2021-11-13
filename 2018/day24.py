#!/usr/bin/env python


class Day24:
    """
    immune system
    infection
 
    - army has groups, groups have units
    - fight until only one army has units remaining
    - unit have hp, have attack damage
    - attack type, initiative, weakness, immunity
    - units=18 hp=729 weak=fire immune=cold, attack=8 initiative=10
    - effective power = units * attack
    - target select and attacking
    - target selection
      - group chooses one target
      - group decr power, if tie higher initiative
      - target most damage, if tie largest power then highest initiative
    - attacking
      - group deals damage, order decreasing initiative
      - if immune 0 damage
      - if weakness double damage

    type=immune u=17 hp=5390 weak=radiation, blugdeoning, attack=4507 fire , initiative=2
    type=immune u=989 hp=1274 weak=bludgeoning, slashing immune=fire attack=25 slashing initiative=3
    type=infection u=801 hp=4706 weak=radiation, attack=116 bludeoning, ini=1
    type=infection u=4485 hp=2961 weak=fire,cold immune=radiation damage=12 slashing init=4



    """
    def __init__(self, file, boost=0):
        self.armies = []
        self.taken = []
        self.boost = boost
        self.load(file)

    def load(self, file):
        for line in open(file).readlines():
            if line.strip() == '':
                continue
            toks=line.split()
            if toks[0] == 'Immune':
                num = 1
                type = 'immune'
                continue
            if toks[0] == 'Infection:':
                num = 1
                type = 'infection'
                continue
            ct = 0
            immune=[]
            weak=[]
            for ct,tok in enumerate(toks):
                if tok.startswith('('):
                    toks[ct] = tok[1:]
                if tok.endswith(')') or tok.endswith(',') or tok.endswith(';'):
                    toks[ct] = tok[:-1]
            for ct,tok in enumerate(toks):
                if tok == 'units':
                    units = int(toks[ct-1])
                if tok == 'hit':
                    hit = int(toks[ct-1])
                if tok == 'attack':
                    attack = int(toks[ct+3])
                    if type == 'immune':
                        attack += self.boost
                    attacktype = toks[ct+4]
                if tok == 'initiative':
                    initiative = int(toks[ct+1])
                if tok == 'weak':
                    ct0 = ct + 2
                    while toks[ct0] in ['slashing','radiation','bludgeoning','fire','cold']:
                        weak.append(toks[ct0])
                        ct0 += 1
                if tok == 'immune':
                    ct0 = ct + 2
                    while toks[ct0] in ['slashing','radiation','bludgeoning','fire','cold']:
                        immune.append(toks[ct0])
                        ct0 += 1
            power = units * attack
            self.armies.append({'num': num, 'type':type, 'units':units, 'hit':hit, 'weak':weak, 'immune':immune, 'ini': initiative, 'attack': attack, 'attacktype': attacktype, 'power': power})
            num += 1

    def get_damage(self, attacker, enemy):
        if attacker['attacktype'] in enemy['immune']:
            return 0
        damage = attacker['attack'] * attacker['units']
        if attacker['attacktype'] in enemy['weak']:
            damage *= 2
        return damage
        
    def get_attack_enemy(self, attacker):
        attack_list = []
        for enemy in self.armies:
            if enemy['type'] != attacker['type']:
                if enemy['units'] == 0 or attacker['attacktype'] in enemy['immune']:
                    continue
                ini = enemy['ini']
                power = enemy['power']
                damage = attacker['attack'] * attacker['units']
                if attacker['attacktype'] in enemy['weak']:
                    damage *= 2
                attack_list += [(enemy, damage, power, ini)]
        sorted_attack_list = sorted(attack_list, key=lambda element: (element[1], element[2], element[3]), reverse=True)
        item = 0
        while item < len(sorted_attack_list):
            if sorted_attack_list[item][0] not in self.taken:
                self.taken.append(sorted_attack_list[item][0])
                return sorted_attack_list[item]
            item += 1

    def get_all_attacks(self):
        attacks = {}
        sorted_armies = sorted(self.armies, key = lambda i: (i['power'], i['ini']), reverse=True)
        for army in sorted_armies:
            target = self.get_attack_enemy(army)
            if target:
                attacks[(army['type'], army['num'], army['ini'])] = target
        return attacks

    def check_won(self):
        units=[0,0]
        infect = 0
        for army in self.armies:
            if army['type'] == 'immune':
                units[0] += army['units']
#                print(f"Immune System: Group {army['num']} contains {army['units']} units")
            else:
                units[1] += army['units']
#                print(f"Infection    : Group {army['num']} contains {army['units']} units")
        if units[0] == 0:
            return units[1], 'infection'
        elif units[1] == 0:
            return units[0], 'immune'
        else:
            return -1, None

    def get_army(self, num, type):
        for army in self.armies:
            if army['num'] == num and army['type'] == type:
                return army

    def kill(self, army, units):
        army['units'] -= units
        army['power'] = army['units'] * army['attack']

    def attack(self, key, enemy):
        type, num, ini = key
        attacker = self.get_army(num, type)
        damage = self.get_damage(attacker, enemy[0])
        enemy0 = self.get_army(enemy[0]['num'], enemy[0]['type'])
        killed = min(damage // enemy0['hit'], enemy0['units'])
        if killed > 0:
#            print(f"{attacker['type']} {attacker['num']} attacks {enemy[0]['type']} {enemy[0]['num']} killing {killed} units")
            self.kill(enemy0, killed)

    def run(self):
        while True:
            amount, winner = self.check_won()
            if winner:
                return winner, amount
            self.taken = []
            attacks = self.get_all_attacks()
            sorted_attacks = sorted(attacks.keys(), key=lambda element: (element[2]), reverse=True)
            for key in sorted_attacks:
                self.attack(key, attacks[key])

def test1():
    assert Day24('day24-test.input').run() == ('infection', 5216)
    assert Day24('day24-test.input', boost=1570).run() == ('immune', 51)
    assert Day24('day24.input').run()[1] == 13331
    assert Day24('day24.input', boost=33).run() == ('immune', 7476)

if __name__ == '__main__':
    print('advent of code 2018: day 24')
    print(f"part 1: {Day24('day24.input').run()[1]}")
    print(f"part 1: {Day24('day24.input', boost=33).run()}")
