#!/usr/bin/env python

from intcode import Intcode

def test_day9():
    intcode = Intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], verbose=True)
    intcode.run()
    assert intcode.outputs == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

    intcode = Intcode([1102,34915192,34915192,7,4,7,99,0], verbose=True)
    intcode.run()
    assert intcode.outputs == [1219070632396864]

    intcode = Intcode([104,1125899906842624,99], verbose=True)
    intcode.run()
    assert intcode.outputs == [1125899906842624]


def test_day9_solutions():
    data = [int(s) for s in open('./day9.input').read().strip().split(',')]
    intcode = Intcode(data[:], inputs=[1], verbose=False)
    intcode.run()
    assert intcode.outputs == [3345854957]
    intcode = Intcode(data[:], inputs=[2], verbose=False)
    intcode.run()
    assert intcode.outputs == [68938]


if __name__ == '__main__':
    data = [int(s) for s in open('./day9.input').read().strip().split(',')]
    intcode = Intcode(data[:], inputs=[1], verbose=False)
    intcode.run()
    print(f"part 1: {intcode.outputs}")

    intcode = Intcode(data[:], inputs=[2], verbose=False)
    intcode.run()
    print(f"part 2: {intcode.outputs}")
