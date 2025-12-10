import os
txt = open(f"{os.getcwd()}/data.txt").readline().split(',')

t = 0
for x in txt:
    r1,r2 = x.split('-')
    for i in range(int(r1),int(r2)+1):
        i = str(i)
        if i[:int(len(i)/2)] == i[int(len(i)/2):]:
            t += int(i)
            print(i)
print(t)


