#!/usr/bin/env python
import sys
import datetime
import time

def part1(data):
    initial = [int(n) for n in data[0].split()[1:]]
    rules = {}
    for rule in data[1:]:
        rules[rule.split('\n')[0].split()[0]] = [(int(line.split()[0]),int(line.split()[1]),int(line.split()[2])) for line in rule.split('\n')[1:]]
    results = []
    for value in initial:
        for rule in rules:
            value = process_rule(value, rules[rule])
        results.append(value)
    return min(results)

def part2(data):
    start0=time.time()
    start=time.time()
    rules = {}
    for rule in data[1:]:
        rules[rule.split('\n')[0].split()[0]] = [(int(line.split()[0]),int(line.split()[1]),int(line.split()[2])) for line in rule.split('\n')[1:]]
    lowest = 99999999999
    initial = [int(n) for i,n in enumerate(data[0].split()[1:]) if i%2==0]
    ranges = [int(n) for i,n in enumerate(data[0].split()[1:]) if i%2==1]
    total=sum(ranges)
    sofar=0
    print(f"num={len(initial)} ranges={ranges}")
    for n in range(len(initial)):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"round={n} best={lowest} range={ranges[n]} time={int(time.time()-start)} sofar={round(sofar/float(total)*100,1)}% elapsed={int((time.time()-start0)//60)}m{int((time.time()-start0)%60)}s time={ts}")
        start = time.time()
        sofar += ranges[n]
        for r in range(ranges[n]+1):
            value = initial[n] + r
            for rule in rules:
                value = process_rule(value, rules[rule])
            lowest = min(lowest, value)
    return lowest

def process_rule(value, rules):
    for rule in rules:
        if value >= rule[1] and value < rule[1] + rule[2]:
            return rule[0] + (value - rule[1])
    return value

if __name__ == '__main__':
    if len(sys.argv) > 1:
        indata = open(sys.argv[1]).read().strip()
    else:
        indata = sys.stdin.read().strip()
    data = indata.split('\n\n')
    print("day5")
    print(f"part 1: {part1(data)}")
    # todo: part2 takes 1h
    print(f"part 2: {part2(data)}")
