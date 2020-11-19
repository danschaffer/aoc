#!/usr/bin/env python3
import math
import time
def find_divisors_1(number):
    results = []
    for index in range(1, number+1):
        if number % index == 0:
            results += [index]
    return results

def find_divisors_2(number):
    results = []
    index = 1
    while index < math.sqrt(number):
        if number % index == 0:
            if number // index == index:
                results += [index]
            else:
                results += [number // index, index]
        index += 1
    return results

def sum_denoms10(number):
    return 10 * sum(find_divisors_2(number))

def calculate_lowest(answer):
    index = 1
    calc = 0
    while calc < answer:
        index += 1
        calc = sum_denoms10(index)
#        print(f"{index} {calc}")
    return index

def calculate_lowest_2(answer):
    index = 1
    calc = 0
    while calc < answer:
        index += 1
        divisors = find_divisors_2(index)
        divisors2 = []
        for div0 in divisors:
            if div0 * 50 >= index:
                divisors2 += [div0]
        calc = 11 * sum(divisors2)
#        print(f"{index} {calc} {divisors}")
    return index

def test1():
    assert calculate_lowest(29000000) == 665280
    assert calculate_lowest_2(29000000) == 705600

if __name__ == '__main__':
    start = time.time()
    print(f"part 1: {calculate_lowest(29000000)} time: {round(time.time() - start)}s")
    start = time.time()
    print(f"part 1: {calculate_lowest_2(29000000)} time: {round(time.time() - start)}s")
