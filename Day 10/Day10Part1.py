# https://adventofcode.com/2023/day/10

import math, re
from collections import deque

def solve(fileName):
    grid = open(fileName,"r").read().strip().split('\n')
    for r,row in enumerate(grid):
        for c,tile in enumerate(row):
            if tile == "S":
                sc,sr = c,r
                break
        else:   # Allows the break to also apply to the outer loop
            continue
        break

    seen = {(sr,sc)}
    q = deque([(sr,sc)])

    # Go through every element in the queue until it is empty
    while q:
        r,c = q.popleft()
        ch = grid[r][c]
        if r > 0 and ch in "S|LJ" and grid[r-1][c] in "|F7" and (next := (r-1,c)) not in seen:  # Up
            seen.add(next)
            q.append(next)
        elif r < len(grid) - 1 and ch in "S|F7" and grid[r+1][c] in "|LJ" and (next := (r+1,c)) not in seen:  # Down
            seen.add(next)
            q.append(next)
        elif c < len(grid[0]) - 1 and ch in "S-LF" and grid[r][c+1] in "-7J" and (next := (r,c+1)) not in seen:  # Right
            seen.add(next)
            q.append(next)
        elif c > 0 and ch in "S-7J" and grid[r][c-1] in "-LF" and (next := (r,c-1)) not in seen:  # Left
            seen.add(next)
            q.append(next)
    return int(len(seen)/2)     # The dist to the furthest point on the pipe is (total length of loop)/2

#print(solve("Day 10\Day10_UnitTest1.txt"))
#print(solve("Day 10\Day10_UnitTest2.txt"))
print(solve("Day 10\Day10_Input.txt"))