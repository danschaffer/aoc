#!/usr/bin/env python
import time
def day15(a,b,afactor=16807,bfactor=48271,remainder=2147483647,iterations=40000000, part2=False):
    count = 0
    for _ in range(iterations):
        a = (a * afactor) % remainder
        if part2:
            while a % 4 != 0:
                a = (a * afactor) % remainder

        b = (b * bfactor) % remainder
        if part2:
            while b % 8 != 0:
                b = (b * bfactor) % remainder

        if a & 0xFFFF == b & 0xFFFF:
            count += 1
    return count

def test1():
    assert day15(65, 8921, iterations=5) == 1
    assert day15(65, 8921) == 588
    assert day15(65, 8921, iterations=5000000, part2=True) == 309
    
    assert day15(591,393) == 619
    assert day15(591,393, iterations=5000000, part2=True) == 290

if __name__ == '__main__':
    print("advent of code day 15")
    start = time.time()
    print(f"part 1: {day15(591,393)} {round(time.time()-start,1)}s")
    start = time.time()
    print(f"part 1: {day15(591,393,part2=True,iterations=5000000)} {round(time.time()-start,1)}s")  # 66s
