data = {}
ids = []
lines = open('./day3-input.txt').read().split('\n')
for line in lines:
  fields = line.split(' ')
  n = int(fields[0][1:])
  ids += [n]
  coords = fields[2][0:-1].split(',')
  x = int(coords[0])
  y = int(coords[1])
  sizes = fields[3].split('x')
  w = int(sizes[0])
  h = int(sizes[1])
  for w0 in range(w):
    for h0 in range(h):
      spot = f"{x+w0},{y+h0}"
      if spot in data:
        data[spot]['count'] += 1
        data[spot]['members'] += [n]
      else:
        data[spot] = {'count':1, 'members': [n]} 
twoormore = 0
for key in data.keys():
  if data[key]['count'] > 1:
    twoormore += 1
print(f"two or more: {twoormore}")

for id in ids:
  overlap = False
  for key in data.keys():
    if id in data[key]['members'] and len(data[key]['members']) > 1:
      overlap = True
      break
  if not overlap:
    print(f"does not overlap {id}")

