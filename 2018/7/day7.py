class Node:
    def __init__(self, name):
        self._name = name
        self._children = {}

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        result = []
        names = sorted(self._children.keys())
        for node in names:
            result += [self._children[node]]
        return result

    def add_child(self, node):
        if node.name not in self._children.keys():
            self._children[node.name] = node

def walk(node):
    result = node.name
    for child in node.children:
        result += walk(child)
    return result

lines = open('./day7-input.txt').read().strip().split('\n')
nodes = {}
for line in lines:
    fields = line.split(" ")
    name1 = fields[1]
    name2 = fields[7]
    if name1 not in nodes:
        nodes[name1] = Node(name1)
    if name2 not in nodes:
        nodes[name2] = Node(name2)
    node1 = nodes[name1]
    node2 = nodes[name2]
    node1.add_child(node2)

available = nodes.keys()
for node in nodes.keys():
    for child in nodes[node].children:
        if child.name in available:
            available.remove(child.name)

print(available)
