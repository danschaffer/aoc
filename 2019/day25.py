#!/usr/bin/env python
import itertools
import re
import sys
from intcode import Intcode
class Cryostasis:
    def __init__(self, data):
        self.intcode = Intcode(data)

    def run(self, inputs='', verbose=True):
        for input in inputs.split(';'):
            self.intcode.inputs = [ord(ch) for ch in list(input.strip()) + ['\n']]
            self.intcode.run()
            output = ''.join([chr(ch) for ch in self.intcode.outputs])
            self.intcode.outputs = []
            if verbose:
                print(output)
        return output

    def run_interactive(self):
        self.intcode.run()
        while True:
            inp = input('$ ')
            print(f"{inp}\n")
            if inp in ['bye', 'quit']:
                break
            output = self.run(inp)
            if output.find('Analysis complete!') > -1:
                print(f"password is {re.search('[0-9]+', output).group(0)}")
                break

    def collect_all_items(self):
        cryostatis.run()
        cryostatis.run('south;take fixed point;north') # fixed point
        cryostatis.run('west;west;west;take hologram;east;east;east') # hologram
        cryostatis.run('north;take candy cane') # candy cane
        cryostatis.run('north;north;take polygon;south') # polygon
        cryostatis.run('south;west;take antenna')
        cryostatis.run('west;take shell;east;south;take whirled peas;north;east')
        cryostatis.run('north;west;take fuel cell;west')
        cryostatis.run('drop hologram;drop shell;drop whirled peas;drop fuel cell;drop fixed point;drop polygon;drop antenna;drop candy cane')

    def run_checkpoint(self):
        self.collect_all_items()
        items = [
            'whirled peas',
            'fuel cell',
            'fixed point',
            'polygon',
            'antenna',
            'candy cane',
            'hologram',
            'shell'
        ]
        for n in range(1, len(items)):
            items_comb = list(itertools.combinations(items, n))
            for item_set in items_comb:
                for count in range(n):
                    self.run(f"take {item_set[count]}")
                output = self.run("west")
                if output.find('Analysis complete!') > -1:
                    print(f"solution was: {sorted(list(item_set))}")
                    return re.search('[0-9]+', output).group(0)
                for count in range(n):
                    self.run(f"drop {item_set[count]}")

if __name__ == '__main__':
    data = [int(ch) for ch in open('day25.input').read().split(',')]
    cryostatis = Cryostasis(data)
    if len(sys.argv) > 1:
            arg = sys.argv[1]
            if arg == '-manual':
                cryostatis.run_interactive()
            elif arg == '-collect':
                cryostatis.collect_all_items()
                cryostatis.run_interactive()
            else:
                print(f"{sys.argv[0]} -manual -collect")
                sys.exit(1)
    else:
        print(f"part 1: {cryostatis.run_checkpoint()}")
