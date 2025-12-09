txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()

a = 50
c = 0

for x in txt:
    cdir = x[0] == "L" and -1 or 1
    for i in range(int(x.strip("\n")[1:])):
        a = (a + cdir) % 100
        if a == 0:
            c += 1


print(c)
