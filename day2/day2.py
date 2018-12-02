import itertools as it

from collections import Counter


# Part 1
with open("data.txt", "r") as f:
    data = f.read().splitlines()

cnt3 = 0
cnt2 = 0

for line in data:
    c = dict(Counter(line))
    if 3 in c.values():
        cnt3 += 1

    if 2 in c.values():
        cnt2 += 1

print(cnt2*cnt3)  # 5704

# Part 2
all_combs = []
for i, line in enumerate(data):
    all_combs.append(([''.join(x) for x in list(it.combinations(line,len(line)-1))], i))

for i, line in enumerate(data):
    for combs, j in all_combs:
        for c in combs:
            if c in line and i != j:
                print(c, line, i, j)

# umdryabviapkozistwcnihjqx umdryabviapkozistwcnihjqxg 70 112
# umdryabviapkozistwcnihjqx umdryabviapkozistwcnihjqxd 112 70
