#!/usr/bin/env python

def part1(file):
  boxids = open(file).read().split('\n')
  twos = 0
  threes = 0
  for boxid in boxids:
    frequencies = {}
    for id in boxid:
      if id in frequencies:
        frequencies[id] += 1
      else:
        frequencies[id] = 1
    hastwo = False
    hasthree = False
    for key in frequencies:
      if frequencies[key] == 2:
        hastwo = True
      if frequencies[key] == 3:
        hasthree = True
    if hastwo:
      twos += 1
    if hasthree:
      threes += 1
  return twos * threes

def showdiffs(a, b):
  diffs = 0
  first = -1
  for n in range(len(a)):
    if a[n] != b[n]:
      diffs += 1
      if first == -1:
        first = n
  return diffs, first

def part2(file):
  boxids = open(file).read().split('\n')
  solutions = []
  for n0 in range(len(boxids)):
    for n1 in range(len(boxids)):
      diffs, n = showdiffs(boxids[n0], boxids[n1])
      if diffs == 1:
        answer = boxids[n0][0:n-1] + boxids[n0][n+1:]
        if answer not in solutions:
          solutions += [answer]
        else:
          return answer

def test1():
  assert part1('./day02.input') == 9633
  assert part2('./day02.input') == 'lujnogabetmsydyfcovzixaw'

if __name__ == '__main__':
  print('advent of code: day 02')
  print(f"part1: {part1('./day02.input')}")
  print(f"part2: {part2('./day02.input')}")
