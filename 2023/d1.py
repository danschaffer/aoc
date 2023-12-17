#!/usr/bin/env python
import sys

nums1=['1','2','3','4','5','6','7','8','9']
nums2=['one','two','three','four','five','six','seven','eight','nine']
def calibrate(items, line):
    matches = []
    for ct in range(len(line)):
        for itemset in items:
            for idx, name in enumerate(itemset):
                if line[ct:].startswith(name):
                    matches.append(str(idx+1))
                    break
    if matches == []:
        matches += ['0']                
    return int(matches[0] + matches[-1])

if len(sys.argv) > 1:
    indata = open(sys.argv[1]).read()
else:
    indata = sys.stdin.read()

res1=0
res2=0
for line in indata.split():
    res1 += calibrate([nums1], line)
    res = calibrate([nums1, nums2], line)
    res2 += res
print("day1")
print(f"part 1: {res1}")
print(f"part 2: {res2}")
