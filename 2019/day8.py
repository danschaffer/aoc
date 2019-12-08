#!/usr/bin/env python

class ImageFormat:
    def __init__(self, wide, tall, data):
        self.wide = wide
        self.tall = tall
        self.data = data
        self.layers = []

    def get_layers(self):
        layersize = self.tall * self.wide
        assert len(self.data) % layersize == 0
        for layer in range(len(self.data) // layersize):
            self.layers += [self.data[layer * layersize:(layer + 1)*layersize]]

    def find_occurrences_in_layers(self, fnd):
        matches = {}
        for layer in range(len(self.layers)):
            matches[layer] = self.find_in_layer(layer, fnd)
        return matches

    def find_in_layer(self, layer, fnd):
        match = 0
        for item in self.layers[layer]:
            if item == str(fnd):
                match += 1
        return match

    def build_image(self):
        image = ''
        for row in range(self.tall):
            for pix in range(self.wide):
                value = ' '
                for layer in range(len(self.layers)):
                    if value == ' ' and self.layers[layer][row * self.wide + pix] in ['0', '1']:
                        value = self.layers[layer][row * self.wide + pix]
                image += value
            image += "\n"
        image1 = image.replace('0', ' ')
        image1 = image1.replace('1', '%')
        return image1

def test1():
    img = ImageFormat(3, 2, '123456789012')
    img.get_layers()
    assert len(img.layers) == 2
    matches = img.find_occurrences_in_layers(0)
    assert matches[0] == 0
    assert matches[1] == 1
    assert img.find_in_layer(0, 1) == 1
    assert img.find_in_layer(1, 2) == 1

def test2():
    img = ImageFormat(2, 2, '0222112222120000')
    img.get_layers()
    img.build_image()

if __name__ == '__main__':
    data = open('./day8.input').read().strip()
    img = ImageFormat(25, 6, data)
    img.get_layers()
    occur = img.find_occurrences_in_layers(0)
    occur1 = sorted(occur.items(), key = lambda kv:(kv[1], kv[0]))
    layer = occur1[0][0]
    print(f"part 1: {img.find_in_layer(layer, 1) * img.find_in_layer(layer, 2)}")
    print(f"part 2:\n{img.build_image()}")
