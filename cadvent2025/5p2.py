txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()

ranges = []

for x in txt:
    if x == "\n":
        continue
    if "-" in x:
        start, end = map(int, x.split("-"))
        ranges.append([start, end])

ranges.sort(key=lambda r: r[0])
def mergeOverlap(arr):
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

t=0
print(ranges)
print(mergeOverlap(ranges))
for x in mergeOverlap(ranges):
    t += x[1]-x[0]+1


print("total ",t)