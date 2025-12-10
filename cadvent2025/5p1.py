import os
txt = open(f"{os.getcwd()}/data.txt").readlines()

import bisect


ranges = []
ings = []

for x in txt:
    if x == "\n":
        continue
    if "-" in x:
        start, end = map(int, x.split("-"))
        ranges.append((start, end))
    else:
        ings.append(int(x))

ranges.sort(key=lambda r: r[0])
starts = [r[0] for r in ranges]
ends = [r[1] for r in ranges]

t = 0
for x in ings:
    for i in range(len(ranges)):
        if starts[i] <= x <= ends[i]:
            print(f"{x} is in {ranges[i]}")
            t += 1
            break

print(t)