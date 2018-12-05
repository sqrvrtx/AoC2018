import string
import itertools as it

from functools import reduce

# Part 1
with open("data.txt", "r") as f:
    data = f.read()

def fx(c):
    try: 
        return c[:-1]
    except IndexError:
        return []

def fz(c):
    try: 
        return ord(c[-1])
    except IndexError:
        return 0

f = lambda d: len(reduce(lambda x,y: fx(x) if fz(x) == ord(y)+32 or fz(x) == ord(y)-32 else x+y , d))
print(f(data))  # 9562

def shortest_polymer():
    for x, y in zip(string.ascii_lowercase, string.ascii_uppercase):
        data_tmp = data.replace(x,'')
        data_tmp = data_tmp.replace(y,'')

        yield f(data_tmp)

print(min(shortest_polymer()))  # 4934
