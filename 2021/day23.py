#!/usr/bin/env python
import heapq
class Day23:
    def __init__(self, file, part2=False):
        self.puzzle = self.read_input(file, part2)

    def read_input(self, file, part2):
        lines = []
        for line in open(file).read().split('\n'):
            data = [c for c in line if c in 'ABCD.']
            if data:
                lines.append(''.join(data))
        if part2:
            lines.insert(2, 'DCBA')
            lines.insert(3, 'DBAC')
        return ''.join(lines)

    @staticmethod
    def can_leave_room(puzzle, room_pos):
        for a in room_pos:
            if puzzle[a] == '.':
                continue
            return a

    @staticmethod
    def blocked(a, b, puzzle):
        step = 1 if a<b else -1
        for pos in range(a+step, b+step, step):
            if puzzle[pos] != '.': return True

    @staticmethod
    def get_possible_parc_pos(a, parc, puzzle):
        for b in [pos for pos in parc if puzzle[pos] == '.']:
            if Day23.blocked(a,b,puzzle): continue
            yield b

    @staticmethod
    def move(a,b,puzzle):
        p = list(puzzle)
        p[a], p[b] = p[b], p[a]
        return ''.join(p)

    @staticmethod
    def can_enter_room(a,b,amphi, puzzle,room_pos):
        for pos in room_pos:
            if puzzle[pos] == '.': best_pos = pos
            elif puzzle[pos] != amphi: return False
        if not Day23.blocked(a,b,puzzle): return best_pos

    @staticmethod
    def possible_moves(puzzle, parc, stepout, target):
        for a in [pos for pos in parc if puzzle[pos] != '.']:
            amphi = puzzle[a]
            if (b:=Day23.can_enter_room(a, stepout[amphi], amphi, puzzle, target[amphi])):
                yield a,b
        for room in 'ABCD':
            if not (a:=Day23.can_leave_room(puzzle, target[room])): continue
            for b in Day23.get_possible_parc_pos(stepout[room], parc, puzzle):
                yield a,b

    def run(self):
        puzzle = self.puzzle
        energy = dict(A=1, B=10, C=100, D=1000)
        parc = [0,1,3,5,7,9,10]
        stepout = dict(A=2, B=4, C=6, D=8)
        target = {r: range(ord(r)-54, len(puzzle),4) for r in 'ABCD'}
        targetI = {v:key for key,val in target.items() for v in val}
        solution = '.'*11+'ABCD'*((len(puzzle)-11)//4)
        heap, seen = [(0,puzzle)], {puzzle:0}
        while heap:
            cost, state = heapq.heappop(heap)
            if state == solution: return cost
            for a,b in Day23.possible_moves(state, parc, stepout, target):
                p,r = (a,b) if a < b else (b,a)
                distance = abs(stepout[targetI[r]]-p) + (r-7)//4
                new_cost = cost + distance * energy[state[a]]
                moved = Day23.move(a,b,state)
                if seen.get(moved,999999) <= new_cost: continue
                seen[moved] = new_cost
                heapq.heappush(heap,(new_cost, moved))

def test1():
    assert Day23('day23-test.input').run() == 12521

def test2():
    assert Day23('day23.input').run() == 18051

def test3():
    assert Day23('day23-test.input', part2=True).run() == 44169

def test4():
    assert Day23('day23.input', part2=True).run() == 50245

if __name__ == '__main__':
    print("advent of code: day23")
    day23 = Day23('./day23.input')
    print(f"part 1: {day23.run()}")
    day23 = Day23('./day23.input', part2=True)
    print(f"part 2: {day23.run()}")
