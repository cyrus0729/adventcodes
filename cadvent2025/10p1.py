import os
import re

import numpy as np

txt = open(f"{os.getcwd()}/data.txt").readlines()

goal_states = []  # list of goal states
button_combs = []  # list of button combinations
joltage_stuff = []  # list of joltage info

# function to get largest number in a string
def largestNumber(in_str):
    l = [int(x) for x in in_str.split() if x.isdigit()]
    return max(l) if l else None

# parse input
for x in txt:
    goal_states.append(re.search(r"\[(.*?)\]", x).group(1))
    button_combs.append(re.findall(r"\((.*?)\)", x))
    joltage_stuff.append(re.search(r"\{(.*?)\}", x).group(1))

print("Goal States:", goal_states)

# convert button combinations to list of ints
for i in range(len(button_combs)):
    button_combs[i] = [list(map(int, v.split(','))) for v in button_combs[i]]

# prepare GF(2) matrices
gf2_matrices = []

# convert it to binary
goal_states = [x.replace('#', '1').replace('.', '0') for x in goal_states]

for i in range(len(button_combs)):
    num_combinations = len(button_combs[i])
    num_goals = len(goal_states[i])  # assuming goal states are sequences
    matrix = []

    for comb in button_combs[i]:
        row = [0] * num_goals
        for x in comb:
            if x < num_goals:
                row[x] = 1
        matrix.append(row)

    gf2_matrices.append(matrix)

import numpy as np


def gauss(vectors, target):
    A = np.array(vectors, dtype=int)
    b = np.array(target, dtype=int)

    n_vectors, n_dim = A.shape

    augmented = np.hstack((A, b.reshape(-1, 1)))

    # Gaussian elimination over GF(2)
    row = 0
    for col in range(n_dim):
        # Find a row with a 1 in current column
        pivot_rows = np.where(augmented[row:, col] == 1)[0]
        if len(pivot_rows) == 0:
            continue  # no pivot in this column
        pivot = pivot_rows[0] + row
        # Swap rows if needed
        if pivot != row:
            augmented[[row, pivot]] = augmented[[pivot, row]]
        # Eliminate below
        for r in range(row + 1, n_vectors):
            if augmented[r, col] == 1:
                augmented[r] = (augmented[r] ^ augmented[row])
        row += 1
        if row >= n_vectors:
            break

    # Back substitution
    solution = np.zeros(n_vectors, dtype=int)
    for i in reversed(range(n_vectors)):
        # Find pivot column
        pivot_cols = np.where(augmented[i, :n_dim] == 1)[0]
        if len(pivot_cols) == 0:
            continue
        pivot_col = pivot_cols[0]
        sum_known = 0
        for j in range(pivot_col + 1, n_dim):
            sum_known ^= (augmented[i, j] & solution[j])
        solution[pivot_col] = augmented[i, -1] ^ sum_known

    # Verify solution
    result = np.zeros(n_dim, dtype=int)
    for idx, vec in enumerate(vectors):
        if solution[idx] == 1:
            result ^= np.array(vec, dtype=int)
    if np.array_equal(result, target):
        # Return indices of vectors used
        indices = [i for i, val in enumerate(solution) if val == 1]
        return indices
    else:
        return None

def solve_gf2_systems(vectors, target):
    target = [int(bit) for bit in target]
    print(target)
    print(vectors)

    for x in range(4):
        goal = [str(v[x]) for v in vectors]
        print('x + '.join(goal),'x = ', target[x])



solve_gf2_systems(gf2_matrices[0], goal_states[0])
# just make it work for 0 then we can keep going