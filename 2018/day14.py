#!/usr/bin/env python3

def part1(recipes):
    state = [3,7]
    elf0 = 0
    elf1 = 1
    while len(state) < recipes + 10:
#        print(f"{elf0} {elf1} {state}")
        newrecipe = state[elf0] + state[elf1]
        if newrecipe > 9:
            state.append(newrecipe//10)
            state.append(newrecipe%10)
        else:
            state.append(newrecipe)
        elf0 = (elf0 + state[elf0] + 1) % len(state)
        elf1 = (elf1 + state[elf1] + 1) % len(state)
    result = ''.join([str(n) for n in state[recipes:recipes+10]])
    return result

def part1(recipes):
    state = [3,7]
    elf0 = 0
    elf1 = 1
    while len(state) < recipes + 10:
#        print(f"{elf0} {elf1} {state}")
        newrecipe = state[elf0] + state[elf1]
        if newrecipe > 9:
            state.append(newrecipe//10)
            state.append(newrecipe%10)
        else:
            state.append(newrecipe)
        elf0 = (elf0 + state[elf0] + 1) % len(state)
        elf1 = (elf1 + state[elf1] + 1) % len(state)
    result = ''.join([str(n) for n in state[recipes:recipes+10]])
    return result

def part2(score):
    state = '37'
    elf0 = 0
    elf1 = 1
    while score not in state[-7:]:
        state += str(int(state[elf0]) + int(state[elf1]))
        elf0 = (elf0 + int(state[elf0]) + 1) % len(state)
        elf1 = (elf1 + int(state[elf1]) + 1) % len(state)
    return state.index(str(score))

def test1():
    assert part1(5) == '0124515891'
    assert part1(9) == '5158916779'
    assert part1(18) == '9251071085'
    assert part1(2018) == '5941429882'
    assert part1(327901) == '1115317115'

    assert part2('01245') == 5
    assert part2('51589') == 9
    assert part2('92510') == 18
    assert part2('59414') == 2018
    assert part2('327901') == 20229822

if __name__ == '__main__':
    print("advent of code: day14")
    print(f"part 1: {part1(327901)}")
    print(f"part 2: {part2('327901')}")
