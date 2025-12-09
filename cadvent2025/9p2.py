from functools import cache

txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()
txt = [(int(a), int(b)) for a, b in [x.strip("\n").split(",") for x in txt]]

print(txt)

cols,rows = max(x[0] for x in txt), max(x[1] for x in txt)

import numpy as np

bit_array = np.zeros((rows, cols), dtype=np.uint8)
print(bit_array)
for x in txt:
    print(x)
    bit_array[x[1]-1, x[0]-1] = 1
print(bit_array)