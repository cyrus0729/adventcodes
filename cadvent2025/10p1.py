import os
import re

import numpy as np
from z3 import z3

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
    goal_states.append([v for v in re.search(r"\[(.*?)\]", x).group(1)])
    button_combs.append(re.findall(r"\((.*?)\)", x))
    joltage_stuff.append(re.search(r"\{(.*?)\}", x).group(1))

for x in range(len(goal_states)):
    for v in range(len(goal_states[x])):
        if goal_states[x][v] == "#":
            goal_states[x][v] = 1
        elif goal_states[x][v] == ".":
            goal_states[x][v] = 0


print("Goal States:", goal_states)

# convert button combinations to list of ints
for i in range(len(button_combs)):
    button_combs[i] = [list(map(int, v.split(','))) for v in button_combs[i]]

# prepare GF(2) matrices
gf2_matrices = []

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

def solve(input_matrix, target_vector):
    rows = len(input_matrix)
    cols = len(input_matrix[0])

    col_vars = [z3.Bool(f'col_{j}') for j in range(cols)]

    opt = z3.Optimize()

    # add constraint XOR over columns equals target
    for i in range(rows):
        xor_expr = None
        for j in range(cols):
            if input_matrix[i][j] == 1:
                if xor_expr is None:
                    xor_expr = z3.If(col_vars[j], z3.BoolVal(True), z3.BoolVal(False))
                else:
                    xor_expr = z3.Xor(xor_expr, z3.If(col_vars[j], z3.BoolVal(True), z3.BoolVal(False)))
            else:
                pass
        if xor_expr is None:
            opt.add(target_vector[i] == 0)
        else:
            # enforce xor equals target
            opt.add(xor_expr == bool(target_vector[i]))

    # objective: minimize the number of toggled columns
    cost = z3.Sum([z3.If(var, 1, 0) for var in col_vars])
    opt.minimize(cost)

    # Solve
    if opt.check() == z3.sat:
        model = opt.model()
        toggle_list = [1 if z3.is_true(model.evaluate(col_vars[j])) else 0 for j in range(cols)]
        # print("Minimal toggle set (columns):", toggle_list)
        # print("Number of toggles:", sum(toggle_list))
        return toggle_list
    else:
        return -1000

def solve_gf2_systems(vectors, target):
    print(target)
    print(vectors)

    vectors_transpose = vectors.T
    print(vectors_transpose)

    matrix = solve(vectors_transpose,target)
    print(matrix)
    return matrix

t = 0
for x in range(len(gf2_matrices)):
    matrix =  solve_gf2_systems(np.array(gf2_matrices[x]), np.array(goal_states[x]))
    t += sum(matrix)

print(t)
# just make it work for 0 then we can keep going