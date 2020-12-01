input = open('./day5-input.txt').read()
#input = 'dabAcCaCBAcCcaDA'

def reduce_all(s):
  for n in range(len(s) - 1):
    if s[n].lower() == s[n+1].lower() and (s[n].isupper() and s[n+1].islower() or s[n].islower() and s[n+1].isupper()):
      s = s[0:n] + s[n+2:]
      return s
  return s

def remove(input, ch):
  input1 = ''
  for n in range(len(input)):
    if input[n] != ch.upper() and input[n] != ch:
      input1 += input[n]
  return input1

def part1(input):
  while True:
    print(len(input))
    input1 = reduce_all(input)
    if input == input1:
      break
    input = input1
  print(input)
  print(len(input))

def uniques(s):
  l = []
  for n in range(len(s)):
    if s[n].lower() not in l:
      l += [s[n].lower()]
  return l

def part2(input):
  elements = uniques(input)
  best = len(input)
  print(elements)

  for element in elements:
#    print(element)
    input1 = remove(input, element)
#    print(input1)
    while True:
      input2 = reduce_all(input1)
      print(len(input2))
      if input2 == input1:
        break
      input1 = input2
    if len(input2) < best:
      best = len(input2)
    print(f"element {element} {len(input2)}")
  print(best)

#part1(input) # 10804
print(input)
part2(input)
