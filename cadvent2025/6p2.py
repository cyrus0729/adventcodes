import os
txt = open(f"{os.getcwd()}/data.txt").readlines()
# at most 4 rows of numbers + 1 symbol
# numbers about 1-4 digits long with proper paddding

columns = list(zip(*txt))

currentOp = ""
xsum = ""
grandsum = 0
i=0

for x in columns:
    if all([y.isspace() for y in x]): # split point
        currentOp = ""
        i += 1
        print("sum ", i)
        print("summing",grandsum," and ",xsum[:-1])
        grandsum += eval(xsum[:-1])
        xsum = ""
        continue
    if x[len(x)-1] == "*" or x[len(x)-1] == "+":
        currentOp = x[len(x)-1] # either * or +
    xsum = ''.join([y for y in  x[:-1] if y != " "]) + currentOp + str(xsum)
    print("x=",xsum)

grandsum += eval(xsum[:-1])

print("g:", grandsum)

