import itertools as it

# Part 1
with open("data.txt", "r") as f:
    data = [int(x) for x in f.read().splitlines()]

print(sum(data))  # 459

# Part 2
from collections import defaultdict

d = defaultdict(int)

for x in it.accumulate(it.cycle(data)):
    d[x] += 1
    if d[x] == 2:
        print(x)  # 65474
        break
