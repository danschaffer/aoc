#!/usr/bin/env python3
import json
class Day18:
    def __init__(self, file):
        self.data = []
        for line in open(file).readlines():
            self.data.append(json.loads(line.strip()))
    
    def unflatten(self, data, depth0=0):
        result = []
        _, depth = data[0]
        if depth > depth0:
            result.append(self.unflatten(data,depth0+1))
        elif depth < depth0:
            return result
        else:
            item,_ = data.pop(0)
            result.append(item)
        _, depth = data[0]
        if depth > depth0:
            result.append(self.unflatten(data,depth0+1))
        elif depth < depth0:
            return result
        else:
            item,_ = data.pop(0)
            result.append(item)
        return result


    def flatten(self, data, depth=0):
        result = []
        first, second = data
        if type(first) == list:
            result += self.flatten(first, depth + 1)
        else:
            result.append([first, depth])
        if type(second) == list:
            result += self.flatten(second, depth + 1)
        else:
            result.append([second, depth])
        return result

    def add(self, number1, number2):
        return [number1, number2]

    def reduce(self, data):
        data_flat = self.flatten(data)
        while True:
            explode = self.check_explode(data_flat)
            split = self.check_split(data_flat)
            if explode == -1 and split == -1:
                break
            if explode > -1:
                self.explode(data_flat, explode)
            else:
                self.split(data_flat, split)
        newdata = self.unflatten(data_flat)
        return newdata

    def check_explode(self, data):
        for index,data in enumerate(data):
            if data[1] > 3:
                return index
        return -1

    def check_split(self, data):
        for index,data in enumerate(data):
            if data[0] > 9:
                return index
        return -1

    def explode(self, data, index):
        if index > 0:
            data[index-1][0] += data[index][0]
        if index < len(data)-2:
            data[index+2][0] += data[index+1][0]
        level=data[index][1]
        data.pop(index)
        data.pop(index)
        data.insert(index,[0,level-1])

    def split(self, data, index):
        item, level = data[index]
        data.pop(index)
        data.insert(index,[item//2,level+1])
        data.insert(index+1,[item//2+item%2,level+1])

    def magnitude(self, number):
        left, right = number
        if type(left) is list:
            left = self.magnitude(left)
        if type(right) is list:
            right = self.magnitude(right)
        return 3*left + 2*right

    def run_part1(self):
        number = self.data[0]
        for i in range(1,len(self.data)):
            number = self.add(number, self.data[i])
            number = self.reduce(number)
        return self.magnitude(number)

    def run_part2(self):
        largest = 0
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if i == j:
                    continue
                sum0 = self.add(self.data[i], self.data[j])
                sum0 = self.reduce(sum0)
                magnitude = self.magnitude(sum0)
                largest = max(largest, magnitude)
        return largest

def test1():
    test_day18 = Day18('./day18-test.input')
    assert test_day18.magnitude([9,1]) == 29
    assert test_day18.magnitude([[1,2],[[3,4],5]]) == 143
    assert test_day18.magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    assert test_day18.magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
    assert test_day18.magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
    assert test_day18.magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
    assert test_day18.magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

    assert test_day18.reduce([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
    assert test_day18.reduce([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
    assert test_day18.reduce([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
    assert test_day18.reduce([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]

    assert test_day18.reduce(test_day18.add([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

    assert Day18('./day18-test1.input').run_part1() == 445
    assert Day18('./day18-test2.input').run_part1() == 791
    assert Day18('./day18-test3.input').run_part1() == 1137
    assert Day18('./day18-test4.input').run_part1() == 3488
    assert Day18('./day18-test5.input').run_part1() == 4140
    assert Day18('./day18-test.input').run_part2() == 3993

def test2():
    test_day18 = Day18('./day18.input')
    assert test_day18.run_part1() == 4145
    assert test_day18.run_part2() == 4855

if __name__ == '__main__':
    print("advent of code: day18")
    day18 = Day18('./day18.input')
    print(f"part 1: {day18.run_part1()}")
    print(f"part 2: {day18.run_part2()}")
