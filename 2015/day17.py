#!/usr/bin/env python
from itertools import combinations
import sys

containers = [int(n) for n in open('./day17.input').read().strip().split()]
container_combinations = []
for index in range(len(containers)):
    container_combinations += combinations(containers, index)
matches = 0
matches_smallest = 0
smallest = sys.maxsize
for container in container_combinations:
    if sum(container) == 150:
        smallest = min(smallest, len(container))
        matches += 1
for container in container_combinations:
    if sum(container) == 150 and len(container) == smallest:
        matches_smallest += 1
print(f"part 1: {matches}")
print(f"part 2: {matches_smallest}")
assert matches == 1304
assert matches_smallest == 18
