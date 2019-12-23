#!/usr/bin/env python
from intcode import Intcode
class Category6:
    def __init__(self):
        self.data =[3,62,1001,62,11,10,109,2257,105,1,0,1255,2131,1657,1195,2069,1997,1519,639,1127,948,1226,1362,1488,1622,738,1589,2226,2195,884,1729,983,1164,703,1826,1092,1923,1026,1327,1296,1055,1766,1886,1393,843,1954,1797,670,602,1855,779,810,1552,2164,1696,2102,1453,915,2038,571,1424,0,0,0,0,0,0,0,0,0,0,0,0,3,64,1008,64,-1,62,1006,62,88,1006,61,170,1105,1,73,3,65,20102,1,64,1,21002,66,1,2,21101,105,0,0,1106,0,436,1201,1,-1,64,1007,64,0,62,1005,62,73,7,64,67,62,1006,62,73,1002,64,2,132,1,132,68,132,1002,0,1,62,1001,132,1,140,8,0,65,63,2,63,62,62,1005,62,73,1002,64,2,161,1,161,68,161,1101,0,1,0,1001,161,1,169,1002,65,1,0,1102,1,1,61,1102,1,0,63,7,63,67,62,1006,62,203,1002,63,2,194,1,68,194,194,1006,0,73,1001,63,1,63,1105,1,178,21101,0,210,0,106,0,69,1202,1,1,70,1102,0,1,63,7,63,71,62,1006,62,250,1002,63,2,234,1,72,234,234,4,0,101,1,234,240,4,0,4,70,1001,63,1,63,1106,0,218,1106,0,73,109,4,21101,0,0,-3,21101,0,0,-2,20207,-2,67,-1,1206,-1,293,1202,-2,2,283,101,1,283,283,1,68,283,283,22001,0,-3,-3,21201,-2,1,-2,1105,1,263,22101,0,-3,-3,109,-4,2106,0,0,109,4,21101,0,1,-3,21102,0,1,-2,20207,-2,67,-1,1206,-1,342,1202,-2,2,332,101,1,332,332,1,68,332,332,22002,0,-3,-3,21201,-2,1,-2,1106,0,312,21201,-3,0,-3,109,-4,2105,1,0,109,1,101,1,68,358,21001,0,0,1,101,3,68,366,21001,0,0,2,21102,1,376,0,1106,0,436,21201,1,0,0,109,-1,2105,1,0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776,2199023255552,4398046511104,8796093022208,17592186044416,35184372088832,70368744177664,140737488355328,281474976710656,562949953421312,1125899906842624,109,8,21202,-6,10,-5,22207,-7,-5,-5,1205,-5,521,21101,0,0,-4,21102,0,1,-3,21101,0,51,-2,21201,-2,-1,-2,1201,-2,385,470,21002,0,1,-1,21202,-3,2,-3,22207,-7,-1,-5,1205,-5,496,21201,-3,1,-3,22102,-1,-1,-5,22201,-7,-5,-7,22207,-3,-6,-5,1205,-5,515,22102,-1,-6,-5,22201,-3,-5,-3,22201,-1,-4,-4,1205,-2,461,1105,1,547,21102,-1,1,-4,21202,-6,-1,-6,21207,-7,0,-5,1205,-5,547,22201,-7,-6,-7,21201,-4,1,-4,1105,1,529,22101,0,-4,-7,109,-8,2105,1,0,109,1,101,1,68,564,20101,0,0,0,109,-1,2105,1,0,1101,85453,0,66,1101,0,1,67,1101,598,0,68,1102,556,1,69,1102,1,1,71,1102,1,600,72,1105,1,73,1,125,37,271797,1101,0,90599,66,1102,1,4,67,1101,629,0,68,1102,1,302,69,1101,1,0,71,1102,637,1,72,1105,1,73,0,0,0,0,0,0,0,0,5,208578,1101,0,63853,66,1101,0,1,67,1102,666,1,68,1102,1,556,69,1102,1,1,71,1101,0,668,72,1105,1,73,1,-135,27,13873,1101,0,38183,66,1102,2,1,67,1102,1,697,68,1102,302,1,69,1101,0,1,71,1101,0,701,72,1106,0,73,0,0,0,0,29,91961,1101,89491,0,66,1102,3,1,67,1101,730,0,68,1101,302,0,69,1102,1,1,71,1101,736,0,72,1105,1,73,0,0,0,0,0,0,8,163378,1102,3359,1,66,1101,0,6,67,1101,0,765,68,1101,0,302,69,1102,1,1,71,1101,0,777,72,1105,1,73,0,0,0,0,0,0,0,0,0,0,0,0,8,245067,1101,69371,0,66,1101,1,0,67,1102,1,806,68,1102,556,1,69,1102,1,1,71,1102,808,1,72,1105,1,73,1,35,45,192334,1102,69457,1,66,1101,0,2,67,1102,837,1,68,1102,302,1,69,1102,1,1,71,1101,841,0,72,1105,1,73,0,0,0,0,33,167358,1101,0,27893,66,1102,1,6,67,1102,1,870,68,1102,1,253,69,1101,1,0,71,1101,882,0,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,36,38183,1101,0,997,66,1102,1,1,67,1102,1,911,68,1101,556,0,69,1102,1,1,71,1101,0,913,72,1105,1,73,1,160,5,34763,1102,1,1597,66,1102,1,1,67,1101,0,942,68,1102,1,556,69,1102,2,1,71,1102,1,944,72,1105,1,73,1,10,37,362396,5,104289,1102,1,100363,66,1101,0,1,67,1101,0,975,68,1101,556,0,69,1102,1,3,71,1101,0,977,72,1105,1,73,1,3,14,6718,13,32969,2,17601,1101,55469,0,66,1102,1,1,67,1101,1010,0,68,1101,556,0,69,1101,0,7,71,1102,1012,1,72,1106,0,73,1,5,14,16795,2,5867,36,76366,29,183922,37,90599,37,181198,5,69526,1102,1,84961,66,1101,1,0,67,1102,1053,1,68,1102,1,556,69,1101,0,0,71,1101,0,1055,72,1106,0,73,1,1682,1101,91961,0,66,1101,4,0,67,1101,0,1082,68,1102,302,1,69,1102,1,1,71,1101,1090,0,72,1105,1,73,0,0,0,0,0,0,0,0,43,34981,1102,1,2389,66,1102,1,3,67,1101,1119,0,68,1101,302,0,69,1102,1,1,71,1101,1125,0,72,1106,0,73,0,0,0,0,0,0,8,81689,1102,1,81689,66,1101,0,4,67,1101,0,1154,68,1102,253,1,69,1102,1,1,71,1101,0,1162,72,1106,0,73,0,0,0,0,0,0,0,0,1,58391,1102,44089,1,66,1101,0,1,67,1102,1,1191,68,1101,556,0,69,1102,1,1,71,1102,1193,1,72,1105,1,73,1,15,2,11734,1102,1,4999,66,1101,0,1,67,1101,0,1222,68,1102,1,556,69,1102,1,1,71,1102,1224,1,72,1106,0,73,1,225,14,20154,1102,88169,1,66,1102,1,1,67,1102,1253,1,68,1102,556,1,69,1101,0,0,71,1102,1255,1,72,1106,0,73,1,1798,1101,0,20771,66,1102,1,1,67,1101,1282,0,68,1101,0,556,69,1102,1,6,71,1101,1284,0,72,1105,1,73,1,16466,43,69962,24,2389,24,7167,22,89491,22,178982,22,268473,1102,1,40063,66,1102,1,1,67,1102,1323,1,68,1101,0,556,69,1101,0,1,71,1101,1325,0,72,1106,0,73,1,6917,13,98907,1102,13873,1,66,1102,3,1,67,1101,1354,0,68,1101,0,302,69,1101,1,0,71,1101,0,1360,72,1106,0,73,0,0,0,0,0,0,24,4778,1101,0,98689,66,1101,1,0,67,1101,0,1389,68,1102,556,1,69,1101,1,0,71,1102,1,1391,72,1106,0,73,1,19,29,367844,1101,0,23497,66,1102,1,1,67,1102,1,1420,68,1102,556,1,69,1102,1,1,71,1102,1422,1,72,1105,1,73,1,67,41,6819,1101,27259,0,66,1102,1,1,67,1102,1,1451,68,1102,1,556,69,1101,0,0,71,1101,0,1453,72,1105,1,73,1,1466,1102,1,96167,66,1101,3,0,67,1102,1,1480,68,1102,302,1,69,1102,1,1,71,1102,1,1486,72,1105,1,73,0,0,0,0,0,0,33,27893,1102,1,47491,66,1102,1,1,67,1101,0,1515,68,1102,556,1,69,1102,1,1,71,1101,1517,0,72,1106,0,73,1,368,31,129279,1102,1,91691,66,1101,0,1,67,1102,1,1546,68,1102,556,1,69,1101,2,0,71,1101,0,1548,72,1106,0,73,1,227,14,3359,27,41619,1102,1,2273,66,1101,4,0,67,1102,1,1579,68,1102,302,1,69,1101,0,1,71,1101,1587,0,72,1106,0,73,0,0,0,0,0,0,0,0,33,139465,1102,1,85369,66,1102,2,1,67,1102,1,1616,68,1102,1,302,69,1101,1,0,71,1102,1620,1,72,1105,1,73,0,0,0,0,40,138914,1102,32969,1,66,1102,3,1,67,1101,1649,0,68,1101,302,0,69,1102,1,1,71,1101,1655,0,72,1105,1,73,0,0,0,0,0,0,33,83679,1102,1,5867,66,1102,5,1,67,1102,1684,1,68,1102,1,302,69,1101,0,1,71,1101,0,1694,72,1105,1,73,0,0,0,0,0,0,0,0,0,0,33,111572,1101,0,34981,66,1101,2,0,67,1102,1723,1,68,1102,1,302,69,1101,0,1,71,1101,0,1727,72,1105,1,73,0,0,0,0,8,326756,1101,59771,0,66,1102,1,1,67,1101,1756,0,68,1102,556,1,69,1102,4,1,71,1102,1758,1,72,1106,0,73,1,2,31,43093,31,86186,5,139052,5,173815,1102,1753,1,66,1101,1,0,67,1101,0,1793,68,1101,556,0,69,1102,1,1,71,1102,1795,1,72,1106,0,73,1,7741,14,10077,1101,0,82567,66,1101,1,0,67,1102,1,1824,68,1102,556,1,69,1101,0,0,71,1101,0,1826,72,1105,1,73,1,1670,1101,0,8263,66,1102,1,1,67,1101,1853,0,68,1102,1,556,69,1102,0,1,71,1101,1855,0,72,1105,1,73,1,1921,1102,1,9199,66,1102,1,1,67,1102,1,1882,68,1101,556,0,69,1102,1,1,71,1101,1884,0,72,1106,0,73,1,97,2,23468,1102,1,43093,66,1102,4,1,67,1102,1,1913,68,1101,302,0,69,1101,0,1,71,1102,1921,1,72,1105,1,73,0,0,0,0,0,0,0,0,33,55786,1102,1,67957,66,1102,1,1,67,1102,1,1950,68,1101,556,0,69,1102,1,1,71,1102,1,1952,72,1106,0,73,1,-49037,15,85369,1101,0,19183,66,1102,1,1,67,1102,1,1981,68,1102,1,556,69,1102,7,1,71,1101,1983,0,72,1106,0,73,1,1,13,65938,15,170738,40,69457,41,4546,45,96167,2,29335,27,27746,1101,0,34763,66,1101,6,0,67,1101,0,2024,68,1102,302,1,69,1101,0,1,71,1101,2036,0,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,1,116782,1102,17489,1,66,1101,0,1,67,1101,2065,0,68,1101,556,0,69,1101,1,0,71,1102,2067,1,72,1105,1,73,1,11,29,275883,1101,47791,0,66,1102,1,1,67,1101,0,2096,68,1101,556,0,69,1101,2,0,71,1101,2098,0,72,1105,1,73,1,17,41,2273,41,9092,1102,32251,1,66,1101,1,0,67,1102,2129,1,68,1101,0,556,69,1102,0,1,71,1102,1,2131,72,1106,0,73,1,1255,1102,58391,1,66,1102,2,1,67,1101,0,2158,68,1102,351,1,69,1102,1,1,71,1102,1,2162,72,1106,0,73,0,0,0,0,255,20771,1101,70297,0,66,1102,1,1,67,1101,0,2191,68,1101,0,556,69,1101,0,1,71,1102,1,2193,72,1105,1,73,1,839,45,288501,1101,0,13679,66,1102,1,1,67,1101,0,2222,68,1102,556,1,69,1102,1,1,71,1102,2224,1,72,1105,1,73,1,103,31,172372,1101,0,25951,66,1101,0,1,67,1101,2253,0,68,1101,556,0,69,1102,1,1,71,1102,1,2255,72,1106,0,73,1,337,14,13436]
        self.computers = []
        self.memory = {}
        self.natreset = None
        self.natfirst = None

    def initialize(self):
        for n in range(50):
            self.computers += [Computer(self.data, n)]
            self.computers[n].boot()

    def run1(self):
        while True:
            for n in range(50):
                if n not in self.memory or len(self.memory[n]) == 0:
                    x = y = -1
                else:
                    (x, y) = self.memory[n][0]
                    del self.memory[n][0]
                result = self.computers[n].send(x, y)
                while len(result) > 0:
                    address = result[0]
                    x = result[1]
                    y = result[2]
                    result = result[3:]
                    if address not in self.memory:
                        self.memory[address] = []
                    self.memory[address] += [(x,y)]
                if 255 in self.memory:
                    return self.memory[255][0]

    def idle_network(self):
        for n in range(50):
            if n in self.memory and len(self.memory[n]) > 0:
                return False
        return True

    def run(self):
        while True:
            for n in range(50):
                if n not in self.memory or len(self.memory[n]) == 0:
                    x = y = -1
                else:
                    (x, y) = self.memory[n][0]
                    del self.memory[n][0]
                result = self.computers[n].send(x, y)
                while len(result) > 0:
                    address = result[0]
                    x = result[1]
                    y = result[2]
                    result = result[3:]
                    if address not in self.memory:
                        self.memory[address] = []
                    self.memory[address] += [(x,y)]

                if 255 in self.memory:
                    if not self.natfirst:
                        self.natfirst = self.memory[255][0][1]
                        print(f"part 1: {self.natfirst}")
                    if self.idle_network():
                        if len(self.memory[255]) > 1 and self.memory[255][-1][1] == self.natreset:
                            return self.memory[255][-1][1]
                        result = self.computers[0].send(self.memory[255][-1][0], self.memory[255][-1][1])
                        while len(result) > 0:
                            address = result[0]
                            x = result[1]
                            y = result[2]
                            result = result[3:]
                            if address not in self.memory:
                                self.memory[address] = []
                            self.memory[address] += [(x,y)]
                            self.natreset = y

class Computer:
    def __init__(self, data, id):
        self.intcode = Intcode(data)
        self.id = id

    def boot(self):
        self.intcode.inputs = [self.id]
        self.intcode.run()

    def send(self, x, y=0):
        self.intcode.outputs = []
        self.intcode.inputs = [x]
        self.intcode.run()
        if x != -1:
            self.intcode.inputs = [y]
            self.intcode.run()
        return self.intcode.outputs

if __name__ == '__main__':
    cat6 = Category6()
    cat6.initialize()
    print(f"part 2: {cat6.run()}")
