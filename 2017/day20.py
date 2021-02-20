#!/usr/bin/env python3

class Day20:
    def __init__(self,file):
        self.data=[]
        for line in open(file).readlines():
            parts = line.split('>')
            x0,y0,z0 = parts[0][3:].strip().split(',')
            x1,y1,z1 = parts[1][5:].strip().split(',')
            x2,y2,z2 = parts[2][5:].strip().split(',')
            self.data.append({'p':(int(x0),int(y0),int(z0)),'v':(int(x1),int(y1),int(z1)),'a':(int(x2),int(y2),int(z2))})

    def get_closest(self):
        distances = []
        for n,item in enumerate(self.data):
            man_dist = abs(item['p'][0])+abs(item['p'][1])+abs(item['p'][2])
#            print(f"{n} {man_dist}")
            distances.append(man_dist)
        smallest = min(distances)
        return distances.index(smallest)

    def do_move(self, n):
        item = self.data[n]
        item['v'] = (item['v'][0] + item['a'][0], item['v'][1] + item['a'][1], item['v'][2] + item['a'][2])
        item['p'] = (item['p'][0] + item['v'][0], item['p'][1] + item['v'][1], item['p'][2] + item['v'][2])

    def remove_collisions(self):
        positions = set()
        dup_positions = []
        removals = []
        for item in self.data:
            if item['p'] in positions and item['p'] not in dup_positions:
                dup_positions.append(item['p'])
            else:
                positions.add(item['p'])
        for dup in dup_positions:
            for item in self.data:
                if item['p'] == dup:
                    removals.append(item)
        for removal in removals:
            self.data.remove(removal)
        return len(removals)

    def run1(self):
        for move in range(100):
            for item in range(len(self.data)):
                self.do_move(item)
        return self.get_closest()

    def run2(self):
        self.remove_collisions()
        for move in range(100):
            for item in range(len(self.data)):
                self.do_move(item)
            removed = self.remove_collisions()
        return len(self.data)

def test1():
    day20 = Day20('./day20.input')
    assert day20.run1() == 172
    day20 = Day20('./day20.input')
    assert day20.run2() == 502


if __name__ == '__main__':
    print("advent of code: day20")
    day20 = Day20('./day20.input')
    print(f"part 1: {day20.run1()}")
    day20 = Day20('./day20.input')
    print(f"part 2: {day20.run2()}")
