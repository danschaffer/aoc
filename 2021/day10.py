#!/usr/bin/env python3

class Day10:
    def __init__(self, file):
        self.lines = open(file).readlines()

    def run(self):
        syntax = {'}':'{',']':'[',')':'(','>':'<','}':'{','[':']','(':')','<':'>'}
        opener = ['{','[','<','(']
        sightings = {'}':0, ']':0, ')':0, '>':0}
        points = {'}':1197,']':57,')':3,'>':25137}
        autototal = []
        autopoints = {'{':3,'[':2,'(':1,'<':4}
        for line in self.lines:
            line = line.strip()
            opens = []
            corrupted = False
            for ch in line:
                if ch in opener:
                    opens.append(ch)
                elif opens[-1] == syntax[ch]:
                    opens.pop(-1)
                else:
                    sightings[ch] += 1
                    corrupted = True
                    break
            if corrupted == False:
                autoscore = 0
                while len(opens) > 0:
                    autoscore = (autoscore * 5) + autopoints[opens[-1]]
                    opens.pop(-1)
                autototal.append(autoscore)

        part1 = sum([sightings[n]*points[n] for n in sightings])
        part2 = sorted(autototal)[len(autototal)//2]
        return part1,part2


def test1():
    part1,part2 = Day10('./day10-test.input').run()
    assert part1 == 26397
    assert part2 == 288957

def test2():
    part1,part2 = Day10('./day10.input').run()
    assert part1 == 367227
    assert part2 == 3583341858

if __name__ == '__main__':
    print("advent of code: day10")
    part1,part2 = Day10('./day10.input').run()
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
