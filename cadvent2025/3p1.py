import os
txt = open(f"{os.getcwd()}/data.txt").readlines()

import re

total = 0

for x in txt:
    x = x.strip("\n")
    print("inputstr",x)
    big = max(re.findall(r"\d", x[:-1]))
    big2 = max(re.findall(r"\d", x[x.find(big)+1:]))
    print("result:",big,big2)
    total += int(big + big2)
    print("total:",total)
