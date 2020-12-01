lines = open('./test-input.txt').read().strip().split('\n')
data = []
for line in lines:
    x = int(line[10:12].strip())
    y = int(line[14:16].strip())
    xv = int(line[28:30].strip())
    yv = int(line[32:34].strip())
    data += [{'x': x, 'y': y, 'xv': xv, 'yv': yv}]

width = 26
height = 26
for n in range(5):
    points = ['.'*width for _ in range(height)]
    for d in data:
        x0 = d['x'] + n * d['xv']
        y0 = d['y'] + n * d['yv']
        x1 = width/2 + x0
        y1 = height/2 + y0
        if x1 > 0 and x1 < width and y1 > 0 and y1 < height:
            points[y0] = points[y0][0:x0] + '#' + points[y0][x0+1:]
    open(f"out{n}", 'w').write('\n'.join(points))
