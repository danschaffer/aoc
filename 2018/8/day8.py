class Node:
    def __init__(self):
        self.metadata = []
        self.children = []

    def add_child(self):
        child = Node()
        self.children += [child]
        return child

    def add_metadata(self, metadata):
        self.metadata += [metadata]

    @property
    def metadata(self):
        return self.metadata

    @property
    def children(self):
        return self.children


def parse(node, inputs):
    if len(inputs) == 0:
        return inputs
    nchildren = inputs[0]
    nmetadata = inputs[1]
    inputs = inputs[2:]
    for _ in range(nchildren):
        child = Node()
        node.children += [child]
        inputs = parse(child, inputs)
    node.metadata = inputs[0:nmetadata]
    return inputs[nmetadata:]

def count(node):
    result = sum(node.metadata)
    for child in node.children:
        result += count(child)
    return result

def value(node):
    result = 0
    if len(node.children) == 0:
        result = sum(node.metadata)
    else:
        for metadata in node.metadata:
            if metadata > 0 and metadata <= len(node.children):
                result += value(node.children[metadata-1])
    return result

# inputs = [int(s) for s in open('./day8-input-test.txt').read().strip().split(" ")]
# root=Node()
# parse(root, inputs)
# print(count(root))
# print(value(root.children[0])) # a = 33
# print(value(root.children[1].children[0])) # d = 99
# print(value(root)) # 33 + 33 + 0

inputs = [int(s) for s in open('./day8-input.txt').read().strip().split(" ")]
root=Node()
parse(root, inputs)
print(count(root))
print(value(root))
