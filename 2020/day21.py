#!/usr/bin/env python3

class Day21:
    def __init__(self, file):
        self.data = {}
        self.foods = []
        self.lines = open(file).read().strip().split('\n')
        for line in self.lines:
            foods, allergens = line[:-1].split('(contains')
            self.foods += [food.strip() for food in foods.split()]
            for allergen in allergens.split(','):
                if allergen.strip() not in self.data:
                    self.data[allergen.strip()] = []
                self.data[allergen.strip()].append([food.strip() for food in foods.split()])

        self.allergens = {}

    def run(self):
        def intersect(lst1, lst2):
            return [value for value in lst1 if value in lst2]

        for allergen in self.data:
            merge = self.data[allergen][0]
            for lst in self.data[allergen][1:]:
                merge = intersect(merge, lst)
            self.allergens[allergen] = merge
        while True:
            done = True
            for allergen in self.allergens:
                if len(self.allergens[allergen]) > 1:
                    done = False
                    break
            if done:
                break
            for allergen in self.allergens:
                if len(self.allergens[allergen]) == 1:
                    remove_ = self.allergens[allergen][0]
                    for allergen0 in self.allergens:
                        if allergen == allergen0:
                            continue
                        if remove_ in self.allergens[allergen0]:
                            self.allergens[allergen0].remove(remove_)
            removes = [self.allergens[allergen][0] for allergen in self.allergens]
            for remove_ in removes:
                while remove_ in self.foods:
                    self.foods.remove(remove_)
        allergens_list = []
        for key in sorted(self.allergens):
            allergens_list.append(self.allergens[key][0])
        return len(self.foods), ','.join(allergens_list)

def test1():
    test_day21 = Day21('./day21-test.input')
    part1_, part2_ = test_day21.run()
    assert part1_ == 5
    assert part2_ == 'mxmxvkd,sqjhc,fvjkl'

def test2():
    test_day21 = Day21('./day21.input')
    part1_, part2_ = test_day21.run()
    assert part1_ == 2020
    assert part2_ == 'bcdgf,xhrdsl,vndrb,dhbxtb,lbnmsr,scxxn,bvcrrfbr,xcgtv'

if __name__ == '__main__':
    print("advent of code: day21")
    day21 = Day21('./day21.input')
    part1, part2 = day21.run()
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
