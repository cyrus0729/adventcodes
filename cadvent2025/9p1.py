txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()
txt = [(int(a), int(b)) for a, b in [x.strip("\n").split(",") for x in txt]]

import math

max = 0

for one in txt:
    for two in txt:
        if one == two: continue
        xDiff = abs(one[0] - two[0])  # Using absolute value to ignore negatives
        yDiff = abs(one[1] - two[1])
        area = (xDiff + 1) * (yDiff + 1)
        if area > max:
            print(one,two, xDiff, yDiff, area)
            max = area

print(max)
