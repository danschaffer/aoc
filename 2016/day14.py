#!/usr/bin/env python
import hashlib
import os
class Day14:
    def __init__(self, salt, part2=False):
        self.salt = salt
        self.part2 = part2
        if part2:
            self.cache = f"./cache{salt}2.txt"
        else:
            self.cache = f"./cache{salt}1.txt"
        self.cachedata = {}
        if os.path.exists(self.cache):
            for line in open(self.cache).read().strip().split('\n'):
                parts = line.split()
                self.cachedata[int(parts[0])] = parts[1]
        else:
            for n in range(25000):
                if n % 1000 == 0:
                    print(n)
                self.cachedata[n] = self.get_hash(n)

    def get_hash(self, index):
        if index in self.cachedata:
            return self.cachedata[index]
        hash_ = hashlib.md5(bytes(self.salt + str(index), 'utf-8')).hexdigest()
        if self.part2:
            for _ in range(2016):
                hash_ = hashlib.md5(bytes(hash_, 'utf-8')).hexdigest()
        return hash_

    def create_cache(self, num=25000):
        for counter in range(num):
            if counter % 100 == 0:
                print(counter)
            hash_ = hashlib.md5(bytes(self.salt + str(counter), 'utf-8')).hexdigest()
            if self.part2:
                for _ in range(2016):
                    hash_ = hashlib.md5(bytes(hash_, 'utf-8')).hexdigest()
            with open(self.cache,'a') as file:
                file.write(f"{counter} {hash_}\n")

    def has_in_next(self, index, string, amount):
        for counter in range(amount):
            hash_ = self.get_hash(index+counter+1)
            if string*5 in hash_:
                return True
        return False

    def has_three(self, value):
        for idx in range(len(value) - 2):
            if len({value[idx + i] for i in range(3)}) == 1:
                return value[idx]
        return None

    def run(self):
        index = 0
        matches = 0
        while True:
            hash_ = self.get_hash(index)
            result = self.has_three(hash_)
            if result and self.has_in_next(index, result, 1000):
                matches += 1
#                print(f"{matches} {index} {result}")
                if matches == 64:
                    break
            index += 1
        return index

def test1():
    day14_test1 = Day14('abc', part2=False)
    assert day14_test1.run() == 22728
    day14_test2 = Day14('abc', part2=True)
    assert day14_test2.run() == 22551

def test2():
    day14_test1 = Day14('ihaygndm', part2=False)
    assert day14_test1.run() == 15035 
    day14_test2 = Day14('ihaygndm', part2=True)
    assert day14_test2.run() == 19968

if __name__ == '__main__':
    print("advent of code day 15")
    day14_test1 = Day14('ihaygndm', part2=False)
#    day14_test.create_cache()
    print(f"part 1 test: {day14_test1.run()}")
    day14_test2 = Day14('ihaygndm', part2=True)
#    day14_test.create_cache()
    print(f"part 1 test: {day14_test2.run()}")
