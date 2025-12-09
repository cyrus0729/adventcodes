file = open("D:\\Users\\cyrus\\Desktop\\code stuff\\cadvent\\juan.txt","r").read().splitlines()
left = []
right = []
totaldistance = 0

for i in range(0,1000): # setup the list to actually be correct
    cur = file[i]
    split = cur.split("   ")
    if not split[0].isnumeric() or not split[1].isnumeric():
        continue
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()

print(len(left))
print(len(right))

for i in range(0,1000): # heres where the fun begins
    leftmin = left[i]
    rightmin = right[i]
    d = abs(leftmin-rightmin)
    totaldistance += d

    print(leftmin, rightmin, d,totaldistance)
# not 1669068

print(totaldistance)