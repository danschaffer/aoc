#!/usr/bin/env python3

class Reindeers:
    def __init__(self):
        self.reindeer = []
        self.results = []
        self.rounds = []

    def run(self, max_time, lines):
        self.parse_lines(lines)
        self.rounds = [0 for _ in range(len(lines))]
        self.results = [0 for _ in range(len(lines))]
        for ct in range(1, max_time):
            for rnum in range(len(self.reindeer)):
                self.results[rnum] = self.calculate(self.reindeer[rnum], ct)
            self.increment_best()

    def parse_lines(self, lines):
        for line in lines:
            self.parse(line)

    def parse(self, line):
        (_, _, _, speed, _, _, flytime, _, _, _, _, _, _, rest, _) = line.split()
        self.reindeer += [(int(speed), int(flytime), int(rest))]

    def calculate(self, reindeer, max_secs):
        (speed, flytime, rest) = reindeer
        flysecs = 0
        secs = 0
        value = 0
        while secs < max_secs:
            value += speed
            flysecs += 1
            secs += 1
            if flysecs == flytime:
                flysecs = 0
                secs += rest
        return value

    def get_best(self):
        return max(self.results)

    def increment_best(self):
        max1 = self.get_best()
        for ct in range(len(self.results)):
            if self.results[ct] == max1:
                self.rounds[ct] += 1
def test1():
    lines = [
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
    ]
    reindeer = Reindeers()
    reindeer.run(1000, lines)
    assert reindeer.get_best() == 1120
    assert max(reindeer.rounds) == 689


def test2():
    lines = [
        'Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.',
        'Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.',
        'Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.',
        'Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.',
        'Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.',
        'Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.',
        'Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.',
        'Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.',
        'Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.'
    ]
    reindeer = Reindeers()
    reindeer.run(2503, lines)
    assert reindeer.get_best() == 2640
    assert max(reindeer.rounds) == 1102

if __name__ == '__main__':
    lines = [
        'Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.',
        'Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.',
        'Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.',
        'Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.',
        'Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.',
        'Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.',
        'Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.',
        'Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.',
        'Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.'
    ]
    reindeer = Reindeers()
    reindeer.run(2503, lines)
    print(f"part 1: {reindeer.get_best()}")
    print(f"part 2: {max(reindeer.rounds)}")
