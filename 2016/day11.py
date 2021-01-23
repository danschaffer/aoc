#!/usr/bin/env python
import copy
import heapq
import itertools
import time
class Day11:
    def __init__(self,file):
        self.cache = set()
        self.state0 = [[],[],[],[]]
        self.names = set()
        for line in open(file).read().strip().split('\n'):
            parts = line.split()
            floor = {'first':0, 'second':1, 'third':2, 'fourth':3}[parts[1]]
            self.state0[floor] = set()
            if parts[-4] == 'and':
                parts = parts[0:-4] + parts[-3:]
            index = 5
            while index < len(parts):
                if parts[index] == 'relevant.':
                    break
                name = parts[index][0:2]
                self.names.add(name)
                if '-' in parts[index]:
                    self.state0[floor].add(name + 'm')
                else:
                    self.state0[floor].add(name + 'g')
                index += 3

    def get_score(self, state):
        return 10 * len(state[3])

    def is_finished(self, state):
        return self.get_score(state) == len(self.names) * 10 * 2

    def is_state_ok(self, state):
        for floor in state:
            if not self.is_floor_ok(floor):
                return False
        return True

    def is_floor_ok(self, floor):
        floor0 = floor.copy()
        has_g = False
        for name in floor0:
            if name.endswith('g'):
                has_g = True
                break
        if not has_g:
            return True
        for name in self.names:
            if name + 'g' in floor0:
                floor0.remove(name + 'g')
                if name + 'm' in floor0:
                    floor0.remove(name + 'm')
        return len(floor0) == 0

    def get_state(self, elevator, state):
        result = f"{elevator}"
        for n in range(len(state)):
            for ele in state[n]:
                result += f"{n}{ele[2:]}"
        return result

    def get_moves(self, elevator, state):
        moves = []
        for move0 in itertools.combinations(list(state[elevator]),2):
            if elevator < 3:
                state0 = copy.deepcopy(state)
                for move in move0:
                    state0[elevator].remove(move)
                    state0[elevator+1].add(move)
                moves.append((elevator+1, state0))
            # if elevator > 0:
            #     state0 = copy.deepcopy(state)
            #     for move in move0:
            #         state0[elevator].remove(move)
            #         state0[elevator-1].add(move)
            #     moves.append((elevator-1, state0))
        for move0 in itertools.combinations(list(state[elevator]),1):
            if elevator < 3:
                state0 = copy.deepcopy(state)
                for move in move0:
                    state0[elevator].remove(move)
                    state0[elevator+1].add(move)
                moves.append((elevator+1, state0))
            if elevator > 0:
                state0 = copy.deepcopy(state)
                for move in move0:
                    state0[elevator].remove(move)
                    state0[elevator-1].add(move)
                moves.append((elevator-1, state0))
        return moves

    def run(self, part2=False):
        self.cache = set()
        if part2:
            for ele in ['el', 'di']:
                self.state0[0].add(ele+'g')
                self.state0[0].add(ele+'m')
                self.names.add(ele)
        self.cache.add(self.get_state(0, self.state0))
        states = []
        heapq.heappush(states, (0, (0,0,self.state0)))
        while len(states):
            point, (elevator, movenum, state) = heapq.heappop(states)
#            print(f"point {point} move {movenum} elevator {elevator} {state}")
            for elevator0, state0 in self.get_moves(elevator, state):
                if not self.is_state_ok(state0):
                    continue
                if self.is_finished(state0):
#                    print(f"{state0}")
                    return movenum + 1
                cache0 = self.get_state(elevator0,state0)
                if cache0 in self.cache:
                    continue
                self.cache.add(cache0)
                heapq.heappush(states, (movenum+1+self.get_score(state0), (elevator0,movenum+1,state0)))

def test1():
    day11 = Day11('./day11-test.input')
    assert day11.is_floor_ok({})
    assert day11.is_floor_ok({'lig'})
    assert day11.is_floor_ok({'lig','lim'})
    assert day11.is_floor_ok({'lig','lim','hyg'})
    assert day11.is_floor_ok({'lig','lim','hym'}) == False
    assert day11.is_floor_ok({'lig','hym'}) == False
    assert day11.is_floor_ok({'lig','lim','hyg','hym'})
    assert day11.get_score({0:{'lig','lim'},1:{}, 2:{}, 3:{}}) == 0
    assert day11.get_score({0:{'lig','lim'},1:{}, 2:{}, 3:{'hyg','hum'}}) == 20
    assert day11.run() == 11

def test2():
    day11 = Day11('./day11.input')
    assert day11.run() == 47
    assert day11.run(part2=True) == 71


if __name__ == '__main__':
    day11 = Day11('./day11.input')
    start = time.time()
    print(f"part 1: {day11.run()} time={round(time.time()-start,2)}s")
    start = time.time()
    print(f"part 2: {day11.run(part2=True)} time={round(time.time()-start,2)}s")
