#!/usr/bin/env python

class Day15:
    def __init__(self, filename):
        self.data = {}
        for y, line in enumerate(open(filename).read().split('\n')):
            for x, ch in enumerate(line):
                if ch == 'O':
                    self.start=(x,y)
                    self.data[(x,y)] = '.'
                elif ch == '.':
                    self.data[(x,y)] = '.'
        self.size = (x+1,y+1)

    def neighbors(self, point):
        points = []
        x , y = point
        for point1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if point1 in self.data and self.data[point1] == '.':
                points.append(point1)
        return points

    def run(self):
        count = -1
        points = [self.start]
        while points:
            count += 1
            points1 = []
            while points:
                point=points.pop()
                self.data[point] = 'O'
                points1 += self.neighbors(point)
            points = points1
            print(count)
            self.drawscreen()
#            import pdb; pdb.set_trace()
        return count

    def drawscreen(self):
        x1,y1 = self.size
        for y in range(y1):
            line = ''
            for x in range(x1):
                if (x,y) not in self.data:
                    line += '#'
                else:
                    line += self.data[(x,y)]
            print(line)

if __name__ == '__main__':
    day15 = Day15('day15.map')
    print(f"day15 part 2: {day15.run()}")
