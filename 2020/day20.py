#!/usr/bin/env python3
import math
import numpy
class Tile:
    def __init__(self, data):
        lines = data.split('\n')
        self.name = int(lines[0].split()[1][0:-1])
        self.content = numpy.array([list(line) for line in data.split('\n')[1:]])
        self.borders = {
            self.top,
            self.bottom,
            self.left,
            self.right
        }
        self.rotate(2)
        self.borders.update((
            self.top,
            self.bottom,
            self.left,
            self.right
        ))
        self.shared_borders = set()
        self.neighbors = set()
        self.n_neighbors = 0

    def rotate(self,times=1):
        self.content = numpy.rot90(self.content, times)

    def flip(self):
        self.content = numpy.flip(self.content, 1)

    @property
    def top(self):
        return "".join(self.content[0,:])

    @property
    def bottom(self):
        return "".join(self.content[-1,:])

    @property
    def left(self):
        return "".join(self.content[:,0])

    @property
    def right(self):
        return "".join(self.content[:,-1])

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.content])

def load_tiles(file):
    return [Tile(data) for data in open(file).read().split('\n\n')]

def part1(tiles):
    for i, tile in enumerate(tiles[:-1]):
        for other in tiles[i + 1:]:
            shared_borders = tile.borders & other.borders
            if shared_borders:
                tile.neighbors.add(other)
                other.neighbors.add(tile)
                tile.shared_borders.update(shared_borders)
                other.shared_borders.update(shared_borders)
    corner_product = 1
    for tile in tiles:
        tile.n_neighbors = len(tile.neighbors)
        if tile.n_neighbors == 2:
            corner_product *= tile.name
    return corner_product

def part2(tiles):
    tile = None
    for tile in tiles:
        if tile.n_neighbors == 2:
            break
    for _ in range(4):
        if {tile.right, tile.bottom}.issubset(tile.shared_borders):
            break
        tile.rotate()

    tile_map = [[tile]]
    sidelength = int(math.sqrt(len(tiles)))
    for i in range(1, sidelength):
        neighbor = None
        for neighbor in tile.neighbors:
            if tile.right in neighbor.shared_borders:
                break
        for j in range(8):
            if neighbor.left == tile.right:
                break
            neighbor.rotate()
            if j == 4:
                neighbor.flip()
        tile_map[0].append(neighbor)
        tile = neighbor

    for y in range(1, sidelength):
        row = []
        for x in range(sidelength):
            tile = tile_map[y-1][x]
            for neighbor in tile.neighbors:
                if tile.bottom in neighbor.shared_borders:
                    break
            for j in range(8):
                if neighbor.top == tile.bottom:
                    break
                neighbor.rotate()
                if j == 4:
                    neighbor.flip()
            row.append(neighbor)
        tile_map.append(row)

    size = tile.content.shape[0] - 2
    image_size = sidelength * size
    image = numpy.empty(shape=(image_size, image_size), dtype=str)

    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            image[y*size:(y+1)*size, x*size:(x+1)*size] = tile.content[1:-1, 1:-1]

    monster = numpy.array((
        list("                  # "),
        list("#    ##    ##    ###"),
        list(" #  #  #  #  #  #   ")
    ))
    monster_pos = {(x, y) for y, x in zip(*numpy.where(monster == "#"))}
    monster_width = len(monster[0])
    monster_height = len(monster)

    monster_found = False
    for i in range(8):
        all_rough_water_pos = {(x, y) for y, x in zip(*numpy.where(image == "#"))}
        for y in range(image_size - monster_height):
            for x in range(image_size - monster_width):
                cropped = image[y:y+monster_height, x:x+monster_width]
                rough_water_pos = set()
                for cy, row in enumerate(cropped):
                    for cx, char in enumerate(row):
                        if char == "#":
                            rough_water_pos.add((cx, cy))
                if monster_pos.issubset(rough_water_pos):
                    monster_found = True
                    for x_, y_ in monster_pos & rough_water_pos:
                        pos = (x + x_, y + y_)
                        all_rough_water_pos.remove(pos)
        if monster_found:
            break
        image = numpy.rot90(image)
        if i == 4:
            image = numpy.flip(image, 1)
    return len(all_rough_water_pos)

def test1():
    tiles_test1 = load_tiles('./day20-test.input')
    assert part1(tiles_test1) == 20899048083289
    assert part2(tiles_test1) == 273
    tiles_test2 = load_tiles('./day20.input')
    assert part1(tiles_test2) == 104831106565027
    assert part2(tiles_test2) == 2093

if __name__ == '__main__':
    print("advent of code: day20")
    TILES = load_tiles('./day20.input')
    print(f"part 1: {part1(TILES)}")
    print(f"part 2: {part2(TILES)}")
