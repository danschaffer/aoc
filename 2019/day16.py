#!/usr/bin/env python

class FFT:
    def __init__(self, input):
        self.phase = [int(n) for n in list(input)]

    def get_pattern(self, element, plen):
        pattern0 = [0, 1, 0, -1]
        pattern = []
        while len(pattern) <= plen:
            for n in range(4):
                pattern += [pattern0[n] for _ in range(element + 1)]
        pattern = pattern[1:]
        pattern = pattern[:plen]
        return pattern

    def apply_phase(self, input, pattern):
        result = 0
        for n in range(len(input)):
            result += input[n] * pattern[n]
        return abs(result) % 10

    def run_phase(self):
        result = []
        phase = self.phase
        self.phase = []
        for n in range(len(phase)):
            pattern = self.get_pattern(n, len(phase))
            result += [self.apply_phase(phase, pattern)]
        self.phase += result
        return result

    def run(self, phases=100, start=0):
        for n in range(phases):
#            print(n)
            self.run_phase()
        answer = self.phase
        return ''.join([str(answer[n]) for n in range(start, 8)])

    def run10k(self, phases=100):
        start = int(''.join([str(self.phase[n]) for n in range(7)]))
        return self.run(100, start)

def dup10k(s):
    out = ""
    for _ in range(10000):
        out += s
    return out

def test_1():
    fft = FFT('12345678')
    assert fft.phase == [1, 2, 3, 4, 5, 6, 7, 8]
    assert fft.get_pattern(0, 8) == [1, 0, -1, 0, 1, 0, -1, 0]
    fft.run_phase()
    assert fft.phase == [4, 8, 2, 2, 6, 1, 5, 8]
    fft.run_phase()
    assert fft.phase == [3, 4, 0, 4, 0, 4, 3, 8]
    fft.run_phase()
    assert fft.phase == [0, 3, 4, 1, 5, 5, 1, 8]
    fft.run_phase()
    assert fft.phase == [0, 1, 0, 2, 9, 4, 9, 8]

def test_2():
    fft = FFT('80871224585914546619083218645595')
    assert fft.run(100) == '24176176'

    fft = FFT('19617804207202209144916044189917')
    assert fft.run(100) == '73745418'

    fft = FFT('69317163492948606335995924319873')
    assert fft.run(100) == '52432133'

if __name__ == '__main__':
    fft = FFT('59775675999083203307460316227239534744196788252810996056267313158415747954523514450220630777434694464147859581700598049220155996171361500188470573584309935232530483361639265796594588423475377664322506657596419440442622029687655170723364080344399753761821561397734310612361082481766777063437812858875338922334089288117184890884363091417446200960308625363997089394409607215164553325263177638484872071167142885096660905078567883997320316971939560903959842723210017598426984179521683810628956529638813221927079630736290924180307474765551066444888559156901159193212333302170502387548724998221103376187508278234838899434485116047387731626309521488967864391')
    print(f"part 1: {fft.run(100)}")
    # fft = FFT(dup10k('59775675999083203307460316227239534744196788252810996056267313158415747954523514450220630777434694464147859581700598049220155996171361500188470573584309935232530483361639265796594588423475377664322506657596419440442622029687655170723364080344399753761821561397734310612361082481766777063437812858875338922334089288117184890884363091417446200960308625363997089394409607215164553325263177638484872071167142885096660905078567883997320316971939560903959842723210017598426984179521683810628956529638813221927079630736290924180307474765551066444888559156901159193212333302170502387548724998221103376187508278234838899434485116047387731626309521488967864391'))
    # print(fft.run10k(100))
