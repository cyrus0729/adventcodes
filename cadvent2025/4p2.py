import os
grid = [
        [int(char) for char in line.strip("\n").replace("@", "1").replace(".", "0")]
        for line in open(f"{os.getcwd()}/data.txt")
    ] # just a map of the entire thing, 1 = roll and 0 = empty

print(f"grid size: {len(grid)}, {len(grid[0])}")

def count(grid):
    valid = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            spaces = [
                [x - 1, y + 1],  # TL
                [x, y + 1],  # TM
                [x + 1, y + 1],  # TR
                [x - 1, y],  # ML
                [x + 1, y],  # MR
                [x - 1, y - 1],  # BL
                [x, y - 1],  # BM
                [x + 1, y - 1],  # BR
            ]

            if grid[x][y] == 0: continue;

            spaces = [grid[pos[0]][pos[1]] for pos in spaces if 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)]
            if sum(spaces) <= 3:
                valid.append([x,y])
    return valid

total = 0

def recursion_woo(grid):
    global total
    if len(count(grid)) == 0:
        return grid
    grid2 = grid
    for x in count(grid):
        grid2[x[0]][x[1]] = 0
        total += 1
    recursion_woo(grid2)
    return None


recursion_woo(grid)
print(total)