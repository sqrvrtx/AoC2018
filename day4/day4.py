
import re

from datetime import datetime
from collections import Counter
from collections import defaultdict

# Part 1
with open("data.txt", "r") as f:
    data = f.read()

f = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M")

vals = sorted((f(x),y) for x,y in re.findall(r'\[(.*)\] (.*)\s', data))
ivals = iter(vals)

regexGuard = re.compile(r'Guard #(\d+) begins')

sleep = defaultdict(int)
minutes_asleep = defaultdict(list)

try:
    ts, action = next(ivals)
    while ivals:

        res = re.search(regexGuard, action)
        if res:
            try:
                idx = res.groups()[0]
            except:
                raise
            ts, action = next(ivals)


        elif action == 'falls asleep':
            ts_start = ts
            ts, action = next(ivals)
            
            # wakes
            ts_stop = ts

            sleep[idx] += (ts_stop.minute - ts_start.minute)
            minutes_asleep[idx].extend(range(ts_start.minute, ts_stop.minute))

            ts, action = next(ivals)

    
except StopIteration:
    pass

guard, seconds = sorted(sleep.items(), key=lambda x: x[1], reverse=True)[0]
most_asleep_minute, freq = Counter(minutes_asleep[guard]).most_common(1)[0]

print("Guard {0}, Most asleep minute {1}".format(guard, most_asleep_minute))
print(most_asleep_minute*int(guard))  # Correct 1: 48680

# Part 2
a, b = sorted([(k, Counter(vals).most_common(1)[0]) for k,vals in minutes_asleep.items()], key=lambda x: x[1][1], reverse=True)[0]
print(int(a)*b[0]) # Correct 2: 94826
