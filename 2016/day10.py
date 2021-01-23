#!/usr/bin/env python

class Day10:
    def __init__(self, file, goal):
        self.bots = {}
        self.outputs = {}
        self.lines = open(file).read().strip().split('\n')
        self.goal = goal

    def run(self, part2=False):
        for line in self.lines:
            parts = line.split()
            if parts[0] == 'value':
                self.lines.remove(line)
                bot = int(parts[-1])
                value = int(parts[1])
                if bot not in self.bots:
                    self.bots[bot] = []
                self.bots[bot].append(value)
                self.bots[bot].sort()
        while sum([len(self.bots[bot]) for bot in self.bots]) > 0:
            for line in self.lines:
                parts = line.split()
                bot = int(parts[1])
                if bot in self.bots and len(self.bots[bot]) >= 2:
                    self.bots[bot].sort()
                    if not part2 and self.bots[bot] == self.goal:
                        return bot
                    low = self.bots[bot][0]
                    high = self.bots[bot][1]
                    self.bots[bot] = self.bots[bot][2:]
                    lowdest = int(parts[6])
                    if parts[5] == 'bot':
                        if lowdest not in self.bots:
                            self.bots[lowdest] = []
                        self.bots[lowdest].append(low)
                    else:
                        if lowdest not in self.outputs:
                            self.outputs[lowdest] = []
                        self.outputs[lowdest].append(low)
                    highdest = int(parts[-1])
                    if parts[10] == 'bot':
                        if highdest not in self.bots:
                            self.bots[highdest] = []
                        self.bots[highdest].append(high)
                    else:
                        if highdest not in self.outputs:
                            self.outputs[highdest] = []
                        self.outputs[highdest].append(high)
        return self.outputs[0][0] * self.outputs[1][0] * self.outputs[2][0]

def test1():
    day10a = Day10('day10-test.input', [2, 5])
    assert day10a.run() == 2

    day10b = Day10('day10.input', [17, 61])
    assert day10b.run() == 157
    assert day10b.run(part2=True) == 1085

if __name__ == '__main__':
    day10 = Day10('day10.input', [17, 61])
    print(f"part 1: {day10.run()}")
    print(f"part 2: {day10.run(part2=True)}")