#!/usr/bin/env python

import sys
As, Bs, Cs = [],[],[]
lines = open('day24.input').read().split('\n')
for n,line in enumerate(lines):
    if n % 18 == 5:
        As.append(int(line.split()[2]))
    if n % 18 == 15:
        Bs.append(int(line.split()[2]))
    if n % 18 == 4:
        Cs.append(int(line.split()[2]))

import itertools as it

# testing tools (not needed for the actual solution)

def forward(A, B, C, z, w):
    "this is what a single block does"
    z1 = z//C
    if w == z % 26 + A:
        return z1
    else:
        return 26 * z1 + w + B

def forward_all(ws,As=As,Bs=Bs,Cs=Cs,z=0):
    "the whole program"
    for A,B,C,w in zip(As,Bs,Cs,ws):
        z = forward(A,B,C,z,w)
    return z

# solution starts here
  
def backward(A, B, C, z2, w):
    """The possible values of z before a single block
    if the final value of z is z2 and w is w"""
    zs = []
    x = z2 - w - B
    if x % 26 == 0:
        zs.append(x//26 * C)
    if 0 <= w-A < 26:
        z0 = z2 * C
        zs.append(w-A+z0)
        
    return zs

def solve(part,As=As,Bs=Bs,Cs=Cs):
    zs = {0}
    result = {}
    if part == 1:
        ws = range(1,10)
    else:
        ws = range(9,0,-1)
    for A,B,C in zip(As[::-1],Bs[::-1],Cs[::-1]):
        #print(len(zs))
        newzs = set()
        for w,z in it.product(ws,zs):
            z0s = backward(A,B,C,z,w)
            for z0 in z0s:
                newzs.add(z0)
                result[z0] = (w,) + result.get(z, ())
        zs = newzs
    return ''.join(str(digit) for digit in result[0])


def test1():
    assert solve(1) == '99394899891971'
    assert solve(2) == '92171126131911'


if __name__ == '__main__':
    print("advent of code: day24")
    print(f"part 1: {solve(1)}")
    print(f"part 2: {solve(2)}")
