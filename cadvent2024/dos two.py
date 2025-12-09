file = open("D:\\Users\\cyrus\\Desktop\\code stuff\\cadvent\\asdf.txt").read().splitlines()

totalgood = 0

for i in range(0,len(file)):
    numbers = list(map(int,file[i].split(" ")))
    solved = False
    print(numbers)
    for j in range(0,len(numbers)):
        currentlist = list(map(int,file[i].split(" ")))
        removed = currentlist.pop(j)
        print(currentlist)
        if (currentlist != sorted(currentlist) and currentlist != sorted(currentlist,reverse=True)):
            print("unsorted")
            continue
        for k in range(0,len(currentlist)-1):
            currentnum = int(currentlist[k])
            nextnum = int(currentlist[k+1])
            distance = abs(currentnum-nextnum)
            if distance < 1 or distance > 3:
                print(currentnum,nextnum,distance,"bad")
                break
            print(currentnum,nextnum,distance,"good")
            if k >= len(currentlist)-2:
                print("perfect :gladeline:")
                solved = True
                break;
    if solved:
        totalgood += 1
        print("solved, next number!")
    else:
        print("impossible, next number")


print("tgt " + str(totalgood))
        
#not 615

