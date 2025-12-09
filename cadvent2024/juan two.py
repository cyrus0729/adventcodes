file = open("D:\\Users\\cyrus\\Desktop\\code stuff\\cadvent\\juan.txt","r").read().splitlines()
left = []
right = []
foundnums = {}
totalsim = 0

for i in range(0,1000): # setup the list to actually be correct
    cur = file[i]
    split = cur.split("   ")
    if not split[0].isnumeric() or not split[1].isnumeric():
        continue
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()

for i in range(0,1000): # heres where the fun begins
    curnum = left[i]
    if curnum in foundnums:
        totalsim += curnum * foundnums.get(curnum)
        continue
    amountfound = right.count(curnum)
    foundnums[curnum] = amountfound
    totalsim += curnum * amountfound
    print(totalsim)
