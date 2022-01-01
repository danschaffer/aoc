#!/usr/bin/env python3
import heapq
import sys
import time
class Day23:
    def __init__(self, file):
        data = {}
        self.best = sys.maxsize
        self.pods = set()
        for y, line in enumerate(open(file).read().split('\n')):
            for x, ch in enumerate(line):
                data[(x,y)] = ch
        self.data= data
        self.goal = ".......AABBCCDD"
        #            012345678901234

#     012345678901
#0    #############
#1    #...........#
#2    ###B#C#B#D###
#3      #A#D#C#A#  
#       #########  

    def print_dict(self, data):
        maxx, maxy = max(data)
        for y in range(maxy+1):
            line = ''
            for x in range(maxx+1):
                if (x,y) in data:
                    line += data[(x,y)]
                else:
                    line += ' '
            print(line)

    def print_str(self, board):
        print("#############")
        print(f"#{board[0]}{board[1]}.{board[2]}.{board[3]}.{board[4]}.{board[5]}{board[6]}#")
        print(f"###{board[7]}#{board[9]}#{board[11]}#{board[13]}###")
        print(f"  #{board[8]}#{board[10]}#{board[12]}#{board[14]}#")
        print("  #########")

    def to_string(self, data):
        return data[(1,1)] + data[(2,1)] + data[(4,1)] + data[(6,1)] + data[(8,1)] + data[(10,1)] + data[(11,1)] + data[(3,2)] + data[(3,3)] + data[(5,2)] + data[(5,3)] + data[(7,2)] + data[(7,3)] + data[(9,2)] + data[(9,3)]

    def to_dict(self, board):
        data = {}
        data[(1,1)] = board[0]
        data[(2,1)] = board[1]
        data[(3,1)] = '.'
        data[(4,1)] = board[2]
        data[(5,1)] = '.'
        data[(6,1)] = board[3]
        data[(7,1)] = '.'
        data[(8,1)] = board[4]
        data[(9,1)] = '.'
        data[(10,1)] = board[5]
        data[(11,1)] = board[6]
        data[(3,2)] = board[7]
        data[(3,3)] = board[8]
        data[(5,2)] = board[9]
        data[(5,3)] = board[10]
        data[(7,2)] = board[11]
        data[(7,3)] = board[12]
        data[(9,2)] = board[13]
        data[(9,3)] = board[14]
        data[(12,1)] = '#'
        data[(12,3)] = '#'
        data[(2,4)] = '#'
        data[(3,4)] = '#'
        data[(4,4)] = '#'
        data[(5,4)] = '#'
        data[(12,4)] = ' '
        return data

    def get_cost(self,item):
        assert item in 'ABCD'
        return {'A':1,'B':10,'C':100,'D':1000}[item]

    def get_move_cost(self, move, board):
        m1, m2 = move
        return (abs(m2[0]-m1[0]) + abs(m2[1]-m1[1])) * self.get_cost(board[m1])

    def get_all_moves(self, board):
        moves = []
        data = self.to_dict(board)
        for pod in self.get_pods(data):
            moves1 = self.get_all_top_moves(data, pod)
            moves2 = self.get_all_room_moves(data, pod)
            moves =  moves + moves1 + moves2
        return moves

    def get_pods(self, board):
        pods = []
        maxx, maxy = max(board)
        for y in range(maxy+1):
            for x in range(maxx+1):
                if (x,y) in board and board[(x,y)] in 'ABCD':
                    pods.append((x,y))
        return pods
          
    def get_all_top_moves(self, board, pod):
        moves = []
        x, y = pod
        if y == 1:
            return []
        type = board[pod]
        num = ord(type) - ord('A')
        dest_x = num * 2 + 3
        if y == 3 and x == dest_x:
            return []
        if y == 2 and x == dest_x and board[(x,3)] == type:
            return []
        if y == 3 and board[(x,2)] != '.':
            return []
        for x1 in [1,2,4,6,8,10,11]:
            if x > x1:
                passed = True
                for x2 in range(x1,x+1):
                    if board[(x2,1)] != '.':
                        passed = False
                        break
                if passed:
                    board1 = board.copy()
                    board1[(x,y)] = '.'
                    board1[(x1,1)] = type
                    moves.append((self.get_cost(type)*((y-1)+x-x1),self.to_string(board1)))
            else:
                passed = True
                for x2 in range(x,x1+1):
                    if board[(x2,1)] != '.':
                        passed = False
                        break
                if passed:
                    board1 = board.copy()
                    board1[(x,y)] = '.'
                    board1[(x1,1)] = type
                    moves.append((self.get_cost(type)*((y-1)+x1-x),self.to_string(board1)))
        return moves        

    def get_all_room_moves(self, board, pod):
        x, y = pod
        if y != 1:
            return []
        type = board[pod]
        num = ord(type) - ord('A')
        dest_x = num * 2 + 3
        if x > dest_x:
            for n in range(dest_x, x):
                if board[n, 1] != '.':
                    return []
        else:
            for n in range(x+1, dest_x):
                if board[n, 1] != '.':
                    return []
        if board[(num * 2 + 3, 3)] == '.' and board[(num * 2 + 3, 2)] == '.':
            board1 = board.copy()
            board1[pod] = '.'
            board1[(num*2+3,3)] = type
            return [(self.get_cost(type) * (abs(x-num*2-3)+2), self.to_string(board1))]
        if board[(num * 2 + 3, 3)] == type and board[(num * 2 + 3, 2)] == '.':
            board1 = board.copy()
            board1[pod] = '.'
            board1[(num*2+3,2)] = type
            return [(self.get_cost(type) * (abs(x-num*2-3)+1), self.to_string(board1))]
        return []

    def get_score(self,board):
        score = 8
        if board[7] == 'A':
            score -= 1
        if board[8] == 'A':
            score -= 1
        if board[9] == 'B':
            score -= 1
        if board[10] == 'B':
            score -= 1
        if board[11] == 'C':
            score -= 1
        if board[12] == 'C':
            score -= 1
        if board[13] == 'D':
            score -= 1
        if board[14] == 'D':
            score -= 1
        return score

    def do_move(self, board, move):
        m1, m2 = move
        cost = self.get_move_cost(move, board)
        print(f"{board[m1]} from {m1} to {m2} {cost}")
        board[m2] = board[m1]
        board[m1] = '.'
        self.print_dict(board)
        return cost

    def solve(self):
        start = self.to_string(self.data)
        frontier = []
        heapq.heappush(frontier,(self.get_score(start),(start,0)))
        while frontier:
            score, (board,cost0)= heapq.heappop(frontier)
            if cost0 >= self.best:
                continue
            if board == self.goal:
                print(f"solution found: {cost0} {len(frontier)} {round(time.time()-self.start,1)}")
                self.best = cost0
            for cost, board1 in self.get_all_moves(board):
                score = self.get_score(board1)
                heapq.heappush(frontier, (score,(board1,cost+cost0)))

def test1():
    day23 = Day23('./day23-test.input')
    day23.solve()
    assert day23.best == 12521

def test2():
    day23 = Day23('./day23.input')
    day23.solve()
    assert day23.best == 18051 # pypy3 1912s

if __name__ == '__main__':
    print("advent of code: day23")
#    day23 = Day23('./day23-test.input')
    day23 = Day23('./day23.input')
    day23.start = time.time()
    day23.solve()
    print(f"part 1: {day23.best} {round(time.time()-day23.start,1)}s")