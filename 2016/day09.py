#!/usr/bin/env python3

def expand(input_):
    output = ''
    index = 0
    while True:
        start = input_.find('(', index)
        if start == -1:
            output += input_[index:]
            break
        finish = input_.find(')', index)
        output += input_[index:start]
        marker = input_[start+1:finish]
        len0, repeat = marker.split('x')
        newstring = ''
        for _ in range(int(repeat)):
            newstring += input_[finish+1:finish+1+int(len0)]
        output += newstring
        index = finish + int(len0) + 1
    return output

def expand_part2(input_):
    scores=[1 for _ in range(len(input_))]
    index=0
    score=0
    while index<len(input_):
        if input_[index] != '(':
            score+=scores[index]
            index+=1
        else:
            index_end=input_.find(')', index)
            tokens=input_[index+1:index_end].split('x')
            index=index_end+1
            for n in range(index,index+int(tokens[0])):
                scores[n] *= int(tokens[1])
    return score


def test1():
    assert expand('ADVENT') == 'ADVENT'
    assert expand('A(1x5)BC') == 'ABBBBBC'
    assert expand('(3x3)XYZ') == 'XYZXYZXYZ'
    assert expand('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
    assert expand('(6x1)(1x3)A') == '(1x3)A'
    assert expand('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

    assert expand_part2('(3x3)XYZ') == 9
    assert expand_part2('X(8x2)(3x3)ABCY') == 20
    assert expand_part2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert expand_part2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445
if __name__ == '__main__':
    print("advent of code: day8")
    data = ''.join(open('day09.input').read().strip().split('\n'))
    print(f'part 1: {len(expand(data))}')
    print(f'part 2: {expand_part2(data)}')