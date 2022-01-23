#!/usr/bin/env python3

def get_intersection_coordinates(coords0, coords1):
    def get_intersection_range(min0, max0, min1, max1):
        if min1 > max0 or min0 > max1:
            return None
        sorted_vals = sorted([min0, max0, min1, max1])
        return sorted_vals[1], sorted_vals[2]
    this_x, this_X, this_y, this_Y, this_z, this_Z = coords0
    other_x, other_X, other_y, other_Y, other_z, other_Z = coords1
    intersect_xs = get_intersection_range(this_x, this_X, other_x, other_X)
    intersect_ys = get_intersection_range(this_y, this_Y, other_y, other_Y)
    intersect_zs = get_intersection_range(this_z, this_Z, other_z, other_Z)
    all_intersects = [intersect_xs, intersect_ys, intersect_zs]
    return all_intersects if all(all_intersects) else None

class Cuboid:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.hollows = []
        self.coords = (x0, x1, y0, y1, z0, z1)

    def __repr__(self):
        x0, x1, y0, y1, z0, z1 = self.coords
        status = f"cuboid: x: {x0}..{x1} y: {y0}..{y1} z: {z0}..{z1} hollows: {len(self.hollows)} volume: {self.volume()}"
        return status
    
    def remove_intersection(self, other):
        intersection_coords = get_intersection_coordinates(self.coords, other)
        if not intersection_coords:
            return
        x0, x1 = intersection_coords[0][0], intersection_coords[0][1]
        y0, y1 = intersection_coords[1][0], intersection_coords[1][1]
        z0, z1 = intersection_coords[2][0], intersection_coords[2][1]
        for hollow_cube in self.hollows:
            hollow_cube.remove_intersection((x0, x1, y0, y1, z0, z1))
        self.hollows.append(Cuboid(x0, x1, y0, y1, z0, z1))

    def volume(self):
        x0, x1, y0, y1, z0, z1 = self.coords
        result = (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)
        for hollow in self.hollows:
            result -= hollow.volume()
        return result

class Day22:
    def __init__(self, file):
        self.commands = []
        self.cuboids = []
        lines = open(file).read().split('\n')
        for line in lines:
            line = line.strip()
            state,coords=line.split()
            xs,ys,zs=coords.split(',')
            x0,x1=xs[2:].split('..')
            y0,y1=ys[2:].split('..')
            z0,z1=zs[2:].split('..')
            self.commands.append((state, int(x0), int(x1), int(y0), int(y1), int(z0), int(z1)))

    def run(self, part2=False):
        for state,x0,x1,y0,y1,z0,z1 in self.commands:
            if not part2 and (x0 < -50 or x1 > 50 or y0 < -50 or y1 > 50 or z0 < -50 or z1 > 50):
                continue
            for cuboid in self.cuboids:
                cuboid.remove_intersection((x0,x1,y0,y1,z0,z1))
            if state == 'on':
                self.cuboids.append(Cuboid(x0,x1,y0,y1,z0,z1))
        total = 0
        for cuboid in self.cuboids:
            total += cuboid.volume()
        return total

def test1():
    test_day22 = Day22('./day22-test.input')
    assert test_day22.run() == 39
    test_day22 = Day22('./day22-test2.input')
    assert test_day22.run() == 590784
    test_day22 = Day22('./day22-test3.input')
    assert test_day22.run() == 474140

    test_day22 = Day22('./day22-test.input')
    assert test_day22.run(part2=True) == 39
    test_day22 = Day22('./day22-test2.input')
    assert test_day22.run(part2=True) == 39769202357779
    test_day22 = Day22('./day22-test3.input')
    assert test_day22.run(part2=True) == 2758514936282235

def test2():
    test_day22 = Day22('./day22.input')
    assert test_day22.run() == 582644
    test_day22 = Day22('./day22.input')
    assert test_day22.run() == 1263804707062415

if __name__ == '__main__':
    print("advent of code: day22")
    day22 = Day22('./day22.input')
    print(f"part 1: {day22.run()}")
    day22 = Day22('./day22.input')
    print(f"part 2: {day22.run(part2=True)}")
