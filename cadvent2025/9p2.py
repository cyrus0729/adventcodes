from functools import cache
import os

txt = open(f"{os.getcwd()}/data.txt").readlines()
txt = [(int(a), int(b)) for a, b in [x.strip("\n").split(",") for x in txt]] # (x,y)

cols,rows = max(x[0] for x in txt), max(x[1] for x in txt) 

import numpy as np

bit_array = np.zeros((rows, cols), dtype=np.uint8)

prev = None

@cache
for x in txt:
    print(x)
    bit_array[x[1]-1, x[0]-1] = 1
    
    if prev: # I despise this. Optimize later.
   		if prev[0] == x[0]:  # vertical line
			if prev[1] > x[1]:
            	for i in range(x[1], prev[1]):
					bit_array[x[0], i] = 1
			else:
				for i in range(prev[1], x[1], -1):
					bit_array[x[0], i] = 1
		
		elif prev[1] == x[1]:  # horizontal line
        	if prev[0] > x[0]:
				for i in range(x[0], prev[0]):
                    bit_array[i, x[1]] = 1
			else:
				for i in range(prev[0], x[0], -1):
                	bit_array[i, x[1]] = 1

    prev = x
print(bit_array)

def fillRow(data):
    # this probably doesnt work if theres like a ^V^ formation
    
    first,last = -1,-1
    
    for i in range(len(data)):
        if data[i] == 1:
            if first == -1:
                first = i
            last = i
    
    data[first:last] = 1
    
print(np.apply_along_axis(fillRow,axis=1,arr=bit_array))
filled_array = binary_fill_holes(bit_array).astype(int)
# maybe this will work?
	
    
for p1 in txt:
    for p2 in txt:
        # draw rectangle on seperate array
        # bitwise and and check if any one is zero between the points?
        
