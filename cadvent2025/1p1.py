txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()

a = 50
c = 0

for x in txt:
    cdir = x[0] == "L" and -1 or 1
    a = (a + int(x.strip("\n")[1:] * cdir) % 100)
    if a == 0:
        c += 1

print(c)
