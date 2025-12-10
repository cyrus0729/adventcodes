import os
txt = open(f"{os.getcwd()}/data.txt").readline().split(',')

import re

REPEATER = re.compile(r"(.+?)\1+$")

t = 0
for x in txt:
    r1,r2 = x.split('-')
    for i in range(int(r1),int(r2)+1):
        i = str(i)
        if REPEATER.match(i):
            t += int(i)
            print(i)
print(t)


