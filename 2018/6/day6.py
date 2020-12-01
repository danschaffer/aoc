lines = open('./day6-input-test.txt').read().strip().split('\n')
xs = []
ys = []

def manhattan(x0, y0, x1, y1):
    return abs(x1-x0) + abs(y1-y0)

def get_edges(l, x, y):
    for n in range(y+1):
        print("".join([str(i) for i in l[n*y:n*y+x]]))
    edges = []
    for n in range(x):
        if l[n] not in edges:
            edges += [l[n]]
        if l[n+(y-1)*x] not in edges:
            edges += [l[n]]
    for n in range(0, x*y, y):
        if l[n] not in edges:
            edges += [l[n]]
        if l[n+x] not in edges:
            edges += [l[n]]
    return edges


def count(l, n):
    result = 0
    for item in l:
        if item == n:
            result += 1
    return result

for line in lines:
    fields = line.split(",")
    x = int(fields[0].strip())
    y = int(fields[1].strip())
    xs += [x]
    ys += [y]
data0=[]
for y in range(max(ys)+1):
    for x in range(max(xs)+1):
        data0 += [[]]
        for n in range(len(xs)):
            d = manhattan(x,y,xs[n],ys[n])
            index = y * (max(xs)+1) + x
            data0[index] += [d]
        min0 = min(data0[index])
        if count(data0[index], min0) > 1:
            data0[index] = -1
        else:
            data0[index] = data0[index].index(min0)


counts = []
for n in range(len(xs)):
    counts += [count(data0, n)]
print(counts)
edges = get_edges(data0, max(xs), max(ys))
for n in range(len(xs)):
    if n in edges:
        counts[n] = 0
print(counts)

print("done")
