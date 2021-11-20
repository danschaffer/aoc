#!/usr/bin/env python
print("advent of code: day 21")
seen = set()
CS = set()
final = None

C = 1250634
D = 65536
while True:
    E = D % 256
    C += E
    C = (C%(2**24) * 65899) % (2**24)
    if D < 256:
        if not CS:
            print(f"part 1: {C}")
        if C not in CS:
            final = C
        CS.add(C)
        D = C | (2**16)
        if D in seen:
            print(f"part 2: {final}")
            break
        seen.add(D)
        C = 1250634
        continue
    D = D//256