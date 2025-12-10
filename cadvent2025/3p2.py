import os
txt = open(f"{os.getcwd()}/data.txt").readlines()

import re

total = 0

def get_biggest_num(inputstr, ind, padding):
    print("args",inputstr,ind,padding)
    if padding == 0:
        nums = list(inputstr[int(ind):])
        return [max(nums), inputstr[int(ind):int(padding)].find(max(nums)) - ind + padding]
    nums = list(inputstr[int(ind):int(padding)])
    returns = [max(nums), inputstr[int(ind):int(padding)].find(max(nums)) + ind]
    print("returns:",returns)
    return returns

for x in txt:
    if x == "" or x == "\n": continue;
    x = x.strip("\n")
    print("inputstr",x)
    big1 = get_biggest_num(x, 0, -12)
    bigs = [big1] # biggest num in str -12 and where it is
    for y in range(1,12): # 12 biggest numbers
        num = get_biggest_num(x, bigs[y-1][1]+1, y-11)
        print("num found:",num)
        if int(num[0]) == -1: break;
        bigs.append(num)
        print("bigs:", bigs)
    total += int(''.join([x[0] for x in bigs]))
    print("total:",total)