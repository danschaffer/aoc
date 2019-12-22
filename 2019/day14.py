#!/usr/bin/env python
import math
import sys
class Fuel:
    def __init__(self, lines):
        self.recipes = {}
        for line in lines:
            self.parse(line)

    def parse(self, line):
        formula = line.split('=>')
        outputs = formula[1].strip().split(' ')
        self.recipes[outputs[1]] = {'amount': int(outputs[0]), 'inputs': {}}
        inputs = formula[0].strip().split(',')
        for input in inputs:
            tokens1 = input.strip().split(' ')
            self.recipes[outputs[1]]['inputs'][tokens1[1]] = int(tokens1[0])

    def run(self, amount=1):
        orders = [{'name': 'FUEL', 'amount': amount}]
        supply = {}
        ores = 0
        while orders:
            order = orders.pop()
            if order['name'] == 'ORE':
                ores += order['amount']
            elif order['amount'] <= supply.get(order['name'], 0):
                supply[order['name']] -= order['amount']
            else:
                amount_needed = order['amount'] - supply.get(order['name'], 0)
                recipe = self.recipes[order['name']]
                batches = math.ceil(amount_needed / recipe['amount'])
                for ingredient in recipe['inputs']:
                    orders += [{'name': ingredient, 'amount': recipe['inputs'][ingredient] * batches}]
                leftover_amount = batches * recipe['amount'] - amount_needed
                supply[order['name']] = leftover_amount
        return ores

    def run_bsearch(self, goal=10**12):
        low = 0
        high = goal
        while low < high -1:
            mid = low + (high - low) // 2
            answer = self.run(mid)
            if answer > goal:
                high = mid
            else:
                low = mid
        return low

def test1():
    data = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""
    fuel = Fuel(data.strip().split('\n'))
    assert fuel.run() == 31

def test2():
    data = """
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""
    fuel = Fuel(data.strip().split('\n'))
    assert fuel.run() == 165

def test3():
    data = """
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
    """
    fuel = Fuel(data.strip().split('\n'))
    assert fuel.run() == 13312
    assert fuel.run_bsearch() == 82892753

def test4():
    data = """
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
"""
    fuel = Fuel(data.strip().split('\n'))
    assert fuel.run() == 180697
    assert fuel.run_bsearch() == 5586022

def test5():
    data = """
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
    """
    fuel = Fuel(data.strip().split('\n'))
    assert fuel.run() == 2210736
    assert fuel.run_bsearch() == 460664

if __name__ == '__main__':
    data = """
1 HJDM, 1 BMPDP, 8 DRCX, 2 TCTBL, 1 KGWDJ, 16 BRLF, 2 LWPB, 7 KDFQ => 6 ZSPL
1 PVRCK, 3 RSLR, 4 JBZD => 6 LCHRC
10 FCBVC, 1 TSJSJ, 20 SQCQ => 9 PNQLP
1 MBVL => 6 TSZJ
1 HWGQF => 4 ZSLVH
1 TBDSC, 13 TSZJ => 1 HRZH
1 RSLR, 1 LJWM => 3 RSFJR
1 VMZFB => 2 MBVL
4 DSTHJ, 2 TSZJ, 13 MBVL => 4 ZWLGK
1 MKTZ, 18 RVFJB, 1 RSLR, 2 HRZH, 14 ZWLGK, 4 RJFTV => 1 ZCVL
6 KDFQ, 1 PNQLP, 1 HRZH => 9 DLPMH
1 DSVT, 22 DRCX, 18 RJFTV, 2 MKTZ, 13 FVZBX, 15 SLTNZ, 7 ZSLVH => 5 GWJC
2 JZSJ, 3 ZSLVH, 6 HNRXC => 8 RJFTV
1 TSZJ => 7 GFVG
5 VMZFB => 4 JBZD
1 PBFZ, 23 JBZD, 2 LJWM => 1 TSJSJ
7 ZPQD => 7 VMZFB
2 LCHRC => 8 PXHK
2 TSZJ, 1 KCXMF, 1 FKJGC => 6 HWGQF
4 PBFZ => 1 FCBVC
1 GMWHM, 4 JQBKW => 8 SQCQ
5 SHMP => 5 PVRCK
10 KCXMF => 3 DRCX
15 VMZFB, 2 RSFJR => 6 KDFQ
35 HNRXC => 2 CJLG
8 MKTZ, 1 FCBVC, 12 HJDM => 9 BRLF
171 ORE => 8 GMWHM
8 RVFJB, 3 CJLG, 9 SLTNZ => 3 LWPB
1 PXHK, 2 RSFJR => 3 FVZBX
1 CJLG, 1 HRZH, 10 MKTZ => 8 KGWDJ
1 RSFJR => 3 FKJGC
1 NXCZM, 31 FKJGC => 2 MKTZ
18 XLWBP => 6 MBLWL
22 HNRXC => 8 FTGK
3 KGWDJ, 1 MLBJ, 5 HJDM => 7 DSVT
9 KDFQ => 5 NXCZM
2 RVFJB, 4 LGDKL, 1 PXHK => 5 CVTR
1 RSFJR, 6 GMWHM, 20 TSJSJ => 9 LGDKL
5 KCXMF => 9 RBDP
6 GWJC, 16 ZCVL, 29 JZSJ, 1 ZSPL, 35 MBLWL, 30 BWFRH, 2 MSFDB, 13 BMPDP, 11 FTGK, 1 ZWLGK => 1 FUEL
6 GFVG, 2 TVQP => 8 HJDM
1 CJLG, 13 PBFZ => 6 JZSJ
3 CVTR => 3 BMPDP
16 FPKMV, 1 ZSLVH => 8 MSFDB
9 JBZD, 12 LCHRC => 8 TBDSC
133 ORE => 3 LJWM
107 ORE => 7 SHMP
1 KDFQ, 1 LJWM => 9 FPKMV
3 PXHK => 4 BWFRH
123 ORE => 4 JQBKW
2 FVZBX, 1 JZSJ => 8 XLWBP
117 ORE => 2 ZPQD
7 NXCZM => 7 HNRXC
1 MLBJ, 22 RSLR => 8 KCXMF
2 TBDSC => 8 RVFJB
1 KDFQ, 23 DSTHJ => 7 SLTNZ
3 RSFJR => 6 MLBJ
5 PVRCK, 2 SQCQ => 9 RSLR
1 LGDKL, 17 MBVL, 6 PNQLP => 5 TVQP
3 RBDP => 6 TCTBL
1 DLPMH, 1 GFVG, 3 MBVL => 2 DSTHJ
21 VMZFB, 2 LJWM => 1 PBFZ
    """
    fuel = Fuel(data.strip().split('\n'))
    print(f"part 1: {fuel.run(1)}")
    print(f"part 2: {fuel.run_bsearch()}")
