from matplotlib import pyplot as plt
from scipy import ndimage
import numpy as np
import os

txt = open(f"{os.getcwd()}/data.txt").readlines()
txt = [(int(a), int(b)) for a, b in [x.strip("\n").split(",") for x in txt]] # (x,y)

cols,rows = max(x[0] for x in txt), max(x[1] for x in txt)
print(f"board size: {cols} cols, {rows} rows")
# Initialize the array
bit_array = np.zeros((rows, cols), dtype=np.bool_)

start_node = None
prev = None

def connect_points(arr, start, end):
    sx, sy = start
    ex, ey = end
    min_x, max_x = min(sx, ex), max(sx, ex)
    min_y, max_y = min(sy, ey), max(sy, ey)

    if sx == ex:
        # Vertical line
        for y in range(min_y, max_y + 1):
            arr[y - 1, sx - 1] = True
    elif sy == ey:
        # Horizontal line
        for x_ in range(min_x, max_x + 1):
            arr[sy - 1, x_ - 1] = True

for x in txt:
    bit_array[x[1]-1, x[0]-1] = True
    if prev:
        connect_points(bit_array, prev, x)
    else:
        start_node = x
    prev = x

print("outlining..")

# Connect last node to start node
connect_points(bit_array, prev, start_node)

print("done outliing")

current_score = 0

print("done filling")

def rect_sum(integral, x1, y1, x2, y2):
    total = integral[y2-1, x2-1]
    if x1 > 0:
        total -= integral[y2-1, x1-1]
    if y1 > 0:
        total -= integral[y1-1, x2-1]
    if x1 > 0 and y1 > 0:
        total += integral[y1-1, x1-1]
    return total

integral = np.cumsum(bit_array, axis=0)

for p1 in txt:
    for p2 in txt:

        # Example: Check rectangle (sx, sy, mx, my)
        sx, sy, mx, my = 4, 4, 7, 7  # example rectangle coordinates

        # Calculate total number of bits in the rectangle
        area = (mx - sx) * (my - sy)