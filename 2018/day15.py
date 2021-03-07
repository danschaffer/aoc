#!/usr/bin/env python

class Day15:
    def __init__(self, file):
        self.objects={}
        self.data=[]
        self.goblin = 0
        self.elf = 0
        for row,line in enumerate(open(file).readlines()):
            for col,ch in enumerate(line):
                if ch == 'G':
                    self.data.append((col,row))
                    self.objects[f"G{self.goblin}"] = {'loc':(col,row),'hp':200, 'type':'goblin'}
                    self.goblin += 1
                elif ch == 'E':
                    self.data.append((col,row))
                    self.objects[f"E{self.goblin}"] = {'loc':(col,row),'hp':200, 'type':'elf'}
                    self.elf += 1
                elif ch == '.': 
                    self.data.append((col,row))

    def keys(self):
        return sorted(list(self.objects.keys()),key=lambda x: self.objects[x]['loc'][1]*100+self.objects[x]['loc'][0])

def test1():
    day15 = Day15('./day15-test.input')
    assert day15.keys() == ['G0', 'E1', 'G1', 'G2', 'G3', 'E4']

if __name__ == '__main__':
    print('advent of code 2018 day 15')
#    day15 = Day15('./day15.input')
    day15 = Day15('./day15.input')
    print(f"goblin : {day15.goblin}")
    print(f"elf    : {day15.elf}")
