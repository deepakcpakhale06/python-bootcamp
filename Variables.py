#!/usr/bin/env python3

# assign values to multiple variables
x, y, z = 1, 2, 3
print(f'x={x} y={y} z={z}')

# One Value to Multiple Variables
a = b = c = "Fish"
print(f'a={a} b={b} c={c}')

# Unpacking
sports = ["Cricket", "Football", "Basketball"]
p, q, r = sports
print(f'p={p}, q={q}, r={r}')

# Change global variables inside function

k = 1


def changek():
    global k
    k += 1
    print(f'Inside function k={k}')

changek()
print(f'Outside function k={k}')

