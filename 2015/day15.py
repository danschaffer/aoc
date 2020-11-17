#!/usr/bin/env python3
class Recipes:
    def __init__(self):
        self.ingredients = []

    def load(self, lines):
        for line in lines:
            self.parse(line)

    def parse(self, line):
        (name, _, capacity, _, durability, _, flavor, _, texture, _, calories) = line.split()
        name = name[:-1]
        capacity = int(capacity[:-1])
        durability = int(durability[:-1])
        flavor = int(flavor[:-1])
        texture = int(texture[:-1])
        calories = int(calories)
        self.ingredients += [(name, capacity, durability, flavor, texture, calories)]

    def solve2_part1(self):
        highscore = 0
        (_, capacity0, durability0, flavor0, texture0, calories0) = self.ingredients[0]
        (_, capacity1, durability1, flavor1, texture1, calories1) = self.ingredients[1]
        for ct0 in range(101):
            for ct1 in range(100):
                count = 0
                if ct0 + ct1 == 100:
                    count = 1
                capacity = max(0, ct0 * capacity0 + ct1 * capacity1)
                durability = max(0, ct0 * durability0 + ct1 * durability1)
                flavor = max(0, ct0 * flavor0 + ct1 * flavor1)
                texture = max(0, ct0 * texture0 + ct1 * texture1)
                score = count * capacity * durability * flavor * texture
                if score > 0:
                    print(f"{ct0} {ct1} {capacity} {durability} {flavor} {texture} {score}")
                highscore = max(score, highscore)
        return highscore

    def solve2_part2(self):
        highscore = 0
        (_, capacity0, durability0, flavor0, texture0, calories0) = self.ingredients[0]
        (_, capacity1, durability1, flavor1, texture1, calories1) = self.ingredients[1]
        for ct0 in range(101):
            for ct1 in range(100):
                count = 0
                if ct0 + ct1 == 100:
                    count = 1
                capacity = max(0, ct0 * capacity0 + ct1 * capacity1)
                durability = max(0, ct0 * durability0 + ct1 * durability1)
                flavor = max(0, ct0 * flavor0 + ct1 * flavor1)
                texture = max(0, ct0 * texture0 + ct1 * texture1)
                calories = ct0 * calories0 + ct1 * calories1
                if calories == 500:
                    calories = 1
                else:
                    calories = 0
                score = count * capacity * durability * flavor * texture * calories
                if score > 0:
                    print(f"{ct0} {ct1} {capacity} {durability} {flavor} {texture} {calories} {score}")
                highscore = max(score, highscore)
        return highscore

    def solve4_part1(self):
        highscore = 0
        (_, capacity0, durability0, flavor0, texture0, calories0) = self.ingredients[0]
        (_, capacity1, durability1, flavor1, texture1, calories1) = self.ingredients[1]
        (_, capacity2, durability2, flavor2, texture2, calories2) = self.ingredients[2]
        (_, capacity3, durability3, flavor3, texture3, calories3) = self.ingredients[3]
        for ct0 in range(101):
            for ct1 in range(100):
                for ct2 in range(100):
                    for ct3 in range(100):
                        count = 0
                        if ct0 + ct1 + ct2 + ct3 == 100:
                            count = 1
                        capacity = max(0, ct0 * capacity0 + ct1 * capacity1 + ct2 * capacity2 + ct3 * capacity3)
                        durability = max(0, ct0 * durability0 + ct1 * durability1 + ct2 * durability2 + ct3 * durability3)
                        flavor = max(0, ct0 * flavor0 + ct1 * flavor1 + ct2 * flavor2 + ct3 * flavor3)
                        texture = max(0, ct0 * texture0 + ct1 * texture1 + ct2 * texture2 + ct3 * texture3)
                        score = count * capacity * durability * flavor * texture
                        highscore = max(score, highscore)
                        if score > 0:
                            print(f"{ct0} {ct1} {ct2} {ct3} {capacity} {durability} {flavor} {texture} {score}")
        return highscore

    def solve4_part2(self):
        highscore = 0
        (_, capacity0, durability0, flavor0, texture0, calories0) = self.ingredients[0]
        (_, capacity1, durability1, flavor1, texture1, calories1) = self.ingredients[1]
        (_, capacity2, durability2, flavor2, texture2, calories2) = self.ingredients[2]
        (_, capacity3, durability3, flavor3, texture3, calories3) = self.ingredients[3]
        for ct0 in range(101):
            for ct1 in range(101):
                for ct2 in range(101):
                    for ct3 in range(101):
                        if ct0 + ct1 + ct2 + ct3 == 100:
                            count = 1
                        else:
                            count = 0
                        _calories = ct0 * calories0 + ct1 * calories1 + ct2 * calories2 + ct3 * calories3
                        if _calories == 500:
                            calories = 1
                        else:
                            calories = 0
                        capacity = max(0, ct0 * capacity0 + ct1 * capacity1 + ct2 * capacity2 + ct3 * capacity3)
                        durability = max(0, ct0 * durability0 + ct1 * durability1 + ct2 * durability2 + ct3 * durability3)
                        flavor = max(0, ct0 * flavor0 + ct1 * flavor1 + ct2 * flavor2 + ct3 * flavor3)
                        texture = max(0, ct0 * texture0 + ct1 * texture1 + ct2 * texture2 + ct3 * texture3)
                        score = count * capacity * durability * flavor * texture * calories
                        highscore = max(score, highscore)
                        if score > 0:
                            print(f"{ct0} {ct1} {ct2} {ct3} {capacity} {durability} {flavor} {texture} {_calories} {score}")
        return highscore

def test1():
    recipes0 = Recipes()
    recipes0.load([
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ])
    print(f"part 1: {recipes0.solve2_part1()}")
    print(f"part 2: {recipes0.solve2_part2()}")
    assert recipes0.solve2_part1() == 62842880
    assert recipes0.solve2_part2() == 57600000

    recipes1 = Recipes()
    recipes1.load([
        'Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3',
        'Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3',
        'Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8',
        'Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'
    ])
#    assert recipes1.solve4_part1() == 21367368
#    assert recipes3.solve4_part2() == 1766400

if __name__ == '__main__':
    recipes = Recipes()
    recipes.load([
        'Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3',
        'Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3',
        'Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8',
        'Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'
    ])
    print(f"part 1: {recipes.solve4_part1()}")
    print(f"part 2: {recipes.solve4_part2()}")
