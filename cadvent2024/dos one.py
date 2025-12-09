file = open("D:\\Users\\cyrus\\Desktop\\code stuff\\cadvent\\asdf.txt").read().splitlines()

totalgood = 0


for i in range(0,len(file)):
    numbers = list(map(int,file[i].split(" ")))
    badinput = 1
    print(numbers)
    if (numbers != sorted(numbers) and numbers != sorted(numbers,reverse=True)):
        print(sorted(numbers),sorted(numbers,reverse=True))
        print("unsorted")
        continue
    for i in range(0,len(numbers)-1):
        currentnum = int(numbers[i])
        nextnum = int(numbers[i+1])
        distance = abs(currentnum-nextnum)
        if distance < 1 or distance > 3:
            print(currentnum,nextnum,distance,"bad")
            break
        print(currentnum,nextnum,distance,"good")
        if i >= len(numbers)-2:
            print("perfect :gladeline:")
            totalgood += 1
            break;
    print("next number!")


print("tgt " + str(totalgood))
        
#not 615

