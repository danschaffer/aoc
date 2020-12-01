boxids = open('./day2-input.txt').read().split('\n')

print("part 1")
twos = 0
threes = 0
for boxid in boxids:
  frequencies = {}
  for id in boxid:
    if id in frequencies:
      frequencies[id] += 1
    else:
      frequencies[id] = 1
  hastwo = False
  hasthree = False
  for key in frequencies:
    if frequencies[key] == 2:
      hastwo = True
    if frequencies[key] == 3:
      hasthree = True
  if hastwo:
    twos += 1
  if hasthree:
    threes += 1
print(f"twos={twos} threes={threes}\nchecksum={twos*threes}")
print("part 2")

def showdiffs(a, b):
  diffs = 0
  first = -1
  for n in range(len(a)):
    if a[n] != b[n]:
      diffs += 1
      if first == -1:
        first = n
  return diffs, first

solutions = []
for n0 in range(len(boxids)):
  for n1 in range(len(boxids)):
    diffs, n = showdiffs(boxids[n0], boxids[n1])
    if diffs == 1:
      answer = boxids[n0][0:n-1] + boxids[n0][n+1:]
      if answer not in solutions:
        solutions += [answer]
        print(answer)
# lujnogabetpmsydyfcovzixaw
