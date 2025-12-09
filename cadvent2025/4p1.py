grid = [
        [int(char) for char in line.strip("\n").replace("@", "1").replace(".", "0")]
        for line in open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt")
    ] # just a map of the entire thing, 1 = roll and 0 = empty

print(f"grid size: {len(grid)}, {len(grid[0])}")

def count(grid):
    total = 0
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
                total += 1

    return total

print(f"total:{count(grid)}")