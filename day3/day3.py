import re

from collections import Counter


# Part 1

with open("data.txt", "r") as f:
    data2 = f.read().splitlines()

f = lambda x: [int(x) for x in re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', x).groups()]


# Part2
def create_coords2(data):
    ls = []
    d = {}
    seen = set()
    mls = set()
    for s in data:
        idx, offsetx, offsety, width, height = f(s)

        cnt = 0
        tmp_ls = []
        for i in range(offsety, offsety+height):
            tmp_ls.extend([(cnt+x,i) for x in list(range(offsetx,offsetx+width))])
        d[idx] = tmp_ls
        ls.extend(tmp_ls)

        y = mls.intersection(tmp_ls)
        seen.update(y)
        mls.update(tmp_ls)


    print(len(seen))  # 110546

    c = Counter(ls)
    for key, vals in d.items():
        if all(c[x] == 1 for x in vals):
            print("Match", key)  # 819

create_coords2(data2)

