from functools import cache

import os
txt = open(f"{os.getcwd()}/data.txt").readlines()

N = len(txt)

for r in range(N):
    for c in range(len(txt[0])-1):
        if txt[r][c] == "S":
            sr,sc = r, c

@cache
def thing(r,c):
    global data
    if r > N-1:
        return 1
    if data[r][c] == "^":
        return thing(r+1,c+1) + thing(r+1,c-1)
    else:
        return thing(r+1,c)

print("running...")
a = thing(sr,sc)
print(a)
print("done!")