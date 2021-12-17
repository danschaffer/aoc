#!/usr/bin/env python3
import math
class Day16:
    def __init__(self, message):
        self.bits = ''.join([bin(int(ch,16))[2:].zfill(4) for ch in message])
        self.pointer = 0

    def parse(self):
        packets = []
        while True:
            packets.append(self.parse1())
            if len(self.bits) - self.pointer < 12 and '0' * (len(self.bits)-self.pointer)  == self.bits[self.pointer:]:
                break
        return packets
        
    def parse1(self):
        data = {}
        data['version'] = int(self.bits[self.pointer:self.pointer+3],2)
        data['type'] = int(self.bits[self.pointer+3:self.pointer+6],2)
        self.pointer+=6
        if data['type'] == 4:
            data['value'] = self.parse_literal()
        else:
            data['operators'] = self.parse_operator()
        return data

    def parse_operator(self):
        result = []
        typeid = int(self.bits[self.pointer])
        self.pointer += 1
        if typeid == 0:
            totallength = int(self.bits[self.pointer:self.pointer+15],2)
            self.pointer += 15
            start = self.pointer
            while self.pointer - start < totallength:
                result.append(self.parse1())
        else:
            subpackets = int(self.bits[self.pointer:self.pointer+11],2)
            self.pointer += 11
            for _ in range(subpackets):
                result.append(self.parse1())
        return result

    def parse_literal(self):
        number = ''
        while True:
            number +=self.bits[self.pointer+1:self.pointer+5]
            self.pointer += 5
            if self.bits[self.pointer-5] == '0':
                break
        return int(number,2)

    def versions(self,data):
        result = 0
        for packet in data:
            result += packet['version']
            if 'operators' in packet:
                result += self.versions(packet['operators'])
        return result

    def execute(self, data):
        if data['type'] == 4:
            return data['value']
        elif data['type'] == 0:
            return sum([self.execute(subdata) for subdata in data['operators']])
        elif data['type'] == 1:
            return math.prod([self.execute(subdata) for subdata in data['operators']])
        elif data['type'] == 2:
            return min([self.execute(subdata) for subdata in data['operators']])
        elif data['type'] == 3:
            return max([self.execute(subdata) for subdata in data['operators']])
        elif data['type'] == 5:
            first = self.execute(data['operators'][0])
            second = self.execute(data['operators'][1])
            if first > second:
                return 1
            else:
                return 0
        elif data['type'] == 6:
            first = self.execute(data['operators'][0])
            second = self.execute(data['operators'][1])
            if first < second:
                return 1
            else:
                return 0
        elif data['type'] == 7:
            first = self.execute(data['operators'][0])
            second = self.execute(data['operators'][1])
            if first == second:
                return 1
            else:
                return 0


    def run_part1(self):
        return self.versions(self.parse())

    def run_part2(self):
        return self.execute(self.parse()[0])

def test1():
    assert Day16('8A004A801A8002F478').run_part1() == 16
    assert Day16('620080001611562C8802118E34').run_part1() == 12
    assert Day16('C0015000016115A2E0802F182340').run_part1() == 23
    assert Day16('A0016C880162017C3686B18A3D4780').run_part1() == 31

    assert Day16('C200B40A82').run_part2() == 3
    assert Day16('04005AC33890').run_part2() == 54
    assert Day16('880086C3E88112').run_part2() == 7
    assert Day16('CE00C43D881120').run_part2() == 9
    assert Day16('D8005AC2A8F0').run_part2() == 1
    assert Day16('F600BC2D8F').run_part2() == 0
    assert Day16('9C005AC2F8F0').run_part2() == 0
    assert Day16('9C0141080250320F1802104A08').run_part2() == 1

def test2():
    assert Day16(open('day16.input').read()).run_part1() == 981
    assert Day16(open('day16.input').read()).run_part2() == 299227024091

if __name__ == '__main__':
    print("advent of code: day16")
    print(f"part 1: {Day16(open('day16.input').read()).run_part1()}")
    print(f"part 2: {Day16(open('day16.input').read()).run_part2()}")
