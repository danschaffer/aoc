#!/usr/bin/env python3
import heapq
import sys
class Day19:
    def __init__(self, file):
        self.data = []
        for line in open(file).readlines():
            blueprint = {}
            line = line.strip()
            parts = line.split()
            n = 3
            while n < len(parts) and n < len(parts):
                robot = parts[n]
                costs = []
                n += 3
                while n < len(parts) and parts[n].isnumeric():
                    cost = int(parts[n])
                    name = parts[n+1]
                    if name.endswith('.'):
                        name = name[:-1]
                    costs.append(cost)
                    n += 3
                blueprint[robot] = costs
            self.data.append(blueprint)



    def run_part1(self):
        geodes = 0
        for blueprint in self.data:
            max_geodes = 0
            frontier = []
            visited = set()
            heapq.heappush(frontier,[0, (1,0,0,0,0,0,0,0)])
            while frontier[0][0] < 25:
                #print(f"{frontier[0][0]} {len(frontier)} {max_geodes}")
                time, status = frontier.pop(0)
                num_ore, num_clay, num_obsidian, num_geode, amount_ore, amount_clay, amount_obsidian, amount_geode = status
                if amount_geode < max_geodes - 1:
                    print(f"pruned {time} {status}")
                    continue
                # ore robot
                if amount_ore >= blueprint['ore'][0]:
                    if (num_ore+1,num_clay,num_obsidian, num_geode,amount_ore-blueprint['ore'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode) not in visited:
                        heapq.heappush(frontier,[time+1,(num_ore+1,num_clay,num_obsidian, num_geode,amount_ore-blueprint['ore'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode)])
                        visited.add((num_ore+1,num_clay,num_obsidian, num_geode,amount_ore-blueprint['ore'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode))
                # clay robot
                if amount_ore >= blueprint['clay'][0]:
                    if (num_ore,num_clay+1,num_obsidian, num_geode,amount_ore-blueprint['clay'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode) not in visited:
                        heapq.heappush(frontier,[time+1,(num_ore,num_clay+1,num_obsidian, num_geode,amount_ore-blueprint['clay'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode)])
                        visited.add((num_ore,num_clay+1,num_obsidian, num_geode,amount_ore-blueprint['clay'][0]+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode))
                # obsidian robot
                if amount_ore >= blueprint['obsidian'][0] and amount_clay >= blueprint['obsidian'][1]:
                    if (num_ore,num_clay,num_obsidian+1,num_geode,amount_ore-blueprint['obsidian'][0]+num_ore,amount_clay-blueprint['obsidian'][1]+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode) not in visited:
                        heapq.heappush(frontier,[time+1,(num_ore,num_clay,num_obsidian+1,num_geode,amount_ore-blueprint['obsidian'][0]+num_ore,amount_clay-blueprint['obsidian'][1]+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode)])
                        visited.add((num_ore,num_clay,num_obsidian+1,num_geode,amount_ore-blueprint['obsidian'][0]+num_ore,amount_clay-blueprint['obsidian'][1]+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode))
                # geode robot
                if amount_ore >= blueprint['geode'][0] and amount_obsidian >= blueprint['geode'][1]:
                    if (num_ore,num_clay,num_obsidian,num_geode+1,amount_ore-blueprint['geode'][0]+num_ore,amount_clay+num_clay,amount_obsidian-blueprint['geode'][1]+num_obsidian,amount_geode+num_geode) not in visited:
                        heapq.heappush(frontier,[time+1,(num_ore,num_clay,num_obsidian,num_geode+1,amount_ore-blueprint['geode'][0]+num_ore,amount_clay+num_clay,amount_obsidian-blueprint['geode'][1]+num_obsidian,amount_geode+num_geode)])
                        visited.add((num_ore,num_clay,num_obsidian,num_geode+1,amount_ore-blueprint['geode'][0]+num_ore,amount_clay+num_clay,amount_obsidian-blueprint['geode'][1]+num_obsidian,amount_geode+num_geode))
                heapq.heappush(frontier,[time+1,(num_ore,num_clay,num_obsidian, num_geode,amount_ore+num_ore,amount_clay+num_clay,amount_obsidian+num_obsidian,amount_geode+num_geode)])
            geodes += max_geodes
        return geodes

    def run_part2(self):
        return -1

#def test1():
#    test_day19 = Day19('./day19-test.input')
#    assert test_day19.run_part1() == -1
#    assert test_day19.run_part2() == -1

#def test2():
#    test_day19 = Day19('./day19.input')
#    assert test_day19.run_part1() == -1
#    assert test_day19.run_part2() == -1

if __name__ == '__main__':
    print("advent of code: day19")
    file = './day19.input'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    day19 = Day19(file)
    print(f"part 1: {day19.run_part1()}")
    print(f"part 2: {day19.run_part2()}")
