Tips
====

### pytest
```
def test1():
    test_day = Day('./day-test.input')
    assert test_day.run_part1() == -1
    assert test_day.run_part2() == -1

# pytest -v *.py
# pytest --durations=0 *.py
```

### parse list int
```
data = [int(line.strip()) for line in open(file).readlines()]

for line in open(file.readlines()):
    line = line.strip()
```

### static method

```
class Test:
  @staticmethod
  def test_static(p1, p2):
    return p1 + p2

if __name__ == '__main__':
  print(Test.test_static(1,2))
```

### memoization

```
from functools import lru_cache
@lru_cache(maxsize = 128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### a star

```
import heapq
def run():
    start=(0,0)
    finish=max(self.data)
    frontier = []
    heapq.heappush(frontier, (0, [(0,0)]))
    visited = set()
    visited.add((0,0))
    while frontier:
        _, moves = heapq.heappop(frontier)
        x,y = moves[-1]
        if (x,y) == finish:
            return self.count(moves)
        for nextmove in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if nextmove not in self.data or nextmove in visited:
                continue
            visited.add(nextmove)
            moves1 = moves[:] + [nextmove]
            heapq.heappush(frontier, (self.count(moves1), moves1))
```