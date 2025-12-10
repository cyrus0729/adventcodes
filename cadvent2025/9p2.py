from functools import cache
import os

txt = open(f"{os.getcwd()}/data.txt").readlines()
txt = [(int(a), int(b)) for a, b in [x.strip("\n").split(",") for x in txt]] # (x,y)

cols,rows = max(x[0] for x in txt), max(x[1] for x in txt) 

from scipy import ndimage
import numpy as np

bit_array = np.zeros((rows, cols), dtype=np.uint8)

prev = None

@cache
for x in txt:
    print(x)
    bit_array[x[1]-1, x[0]-1] = 1
    
    if prev:
		sx,sy = min(prev[0],x[0]), min(prev[1],x[1])
		mx,my = max(prev[0],x[0]), max(prev[1],x[1])
   		if prev[0] == x[0]:  # vertical line
			for i in range(sy,my):
				bit_array[x[0], i] = 1
		
		elif prev[1] == x[1]:  # horizontal line
			for i in range(sx,mx):
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
filled_array = ndimage.binary_fill_holes(bit_array).astype(int)
# maybe this will work?
	
current_score = 0
    
for p1 in txt:
    for p2 in txt:
      
      sx, sy = min(p1[0],p2[0]), min(p1[1],p2[1])
      mx,my = max(p1[0],p2[0]), max(p1[1],p2[1])
      area = (mx-sx)*(my-sy)
      if area <= current_score:
         continue
      
      bit_array2 = np.zeros((rows,cols), dtype=np.uint8)
      
      for row in range(sy,my):
         for col in range(sx,mx):
            bit_array2[row, col] = 1
      res_arr = np.bitwise_xor(bit_array,bit_array2)
      
      if np.any(res_arr == 1):
         continue
      if area > current_score:
         current_score = area
            
        # draw rectangle on seperate array
        # bitwise xor check if any one exists between the points?