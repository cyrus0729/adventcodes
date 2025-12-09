import re
file = open("D:\\Users\\cyrus\\Desktop\\code stuff\\cadvent\\testcase.txt").readlines()
rules = [x.rstrip("\n") for x in file if re.match("\d\d\|\d\d",x)]
numbers = [x.rstrip("\n") for x  in file if re.match("\d\d,{1}",x)]

bad = False
total = 0

for current in numbers:
    bad = False
    listtouse = current.split(",")
    print(current)
    for i,n in enumerate(listtouse): # current number
        if bad:
            break;
        currentrules = [x for x in rules if re.match(f"{n}\|\d\d",x)] # all the rules
        numberstocheck = [int(x.split("|")[1]) for x in currentrules] # numbers that should be after
        numbersbefore = listtouse[0:i]
        # what im thinking is
        # loop through each one before the current number to check
        # if they exist in numberstocheck
        # fuck
    print("horray")
    total += int(listtouse[int((len(listtouse)-1)/2)])
    
print(total)
                    
                    
                
                