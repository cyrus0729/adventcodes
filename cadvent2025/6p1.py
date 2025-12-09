txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()
# at most 4 rows of numbers + 1 symbol
# numbers about 1-4 digits long with proper paddding

nums = [x.split() for x in txt[0:len(txt)-1]]
exps = txt[len(txt)-1].split()
print(nums)
print(exps)

t=0
for i,x in enumerate(exps):
    t += eval(x.join([v[i] for v in nums]))

print(t)