import os
txt = open(f"{os.getcwd()}/data.txt").readlines()

area = len(txt[0])
currentBeams = [0 for i in range(area)]
currentBeams[area//2] = 1

print(currentBeams)

t = 0

for x in txt:
    for col in range(len(x)):
        if x[col] == '^' and currentBeams[col] == 1:
            currentBeams[col - 1] = 1
            currentBeams[col + 1] = 1
            currentBeams[col] = 0
            t += 1

print(t)