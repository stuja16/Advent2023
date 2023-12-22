# https://adventofcode.com/2023/day/10

import math, re
from collections import deque

def solve(fileName):
    # Read in input
    grid = open(fileName,"r").read().strip().split('\n')

    # Search for starting pipe
    for r,row in enumerate(grid):
        for c,tile in enumerate(row):
            if tile == "S":
                sr,sc = r,c
                break
        else:   # Allows the break to also apply to the outer loop
            continue
        break

    seen = {(sr,sc)}
    q = deque([(sr,sc)])
    maybeS = {"|","-","F","7","L","J"}

    # Go through every element in the queue until it is empty
    while q:
        r,c = q.popleft()
        ch = grid[r][c]

        # Use if instead of elif b/c you need to go both directions from the "S" to determine what pipe it is
        if r > 0 and ch in "S|LJ" and grid[r-1][c] in "|F7" and (next := (r-1,c)) not in seen:  # Up
            seen.add(next)
            q.append(next)
            if ch == "S":
                maybeS &= {"|","L","J"} # &= creates the intersection of both sets (& intersects, = assigns)
        if r < len(grid) - 1 and ch in "S|F7" and grid[r+1][c] in "|LJ" and (next := (r+1,c)) not in seen:  # Down
            seen.add(next)
            q.append(next)
            if ch == "S":
                maybeS &= {"|","F","7"}
        if c < len(grid[0]) - 1 and ch in "S-LF" and grid[r][c+1] in "-7J" and (next := (r,c+1)) not in seen:  # Right
            seen.add(next)
            q.append(next)
            if ch == "S":
                maybeS &= {"-","L","F"}
        if c > 0 and ch in "S-7J" and grid[r][c-1] in "-LF" and (next := (r,c-1)) not in seen:  # Left
            seen.add(next)
            q.append(next)
            if ch == "S":
                maybeS &= {"-","7","J"}

    assert len(maybeS) == 1     # "assert" is useful for debugging, throws error if not true
    (s,) = maybeS
    grid = [row.replace("S",s) for row in grid]     # Replace start token with correct pipe
    grid = ["".join(ch if (r,c) in seen else "." for c,ch in enumerate(row)) for r,row in enumerate(grid)]  # Erase pipes not in the loop
    contained = set()   # Set of squares contained within the pipe loop

    # Remember interior squares contained in the pipe loop
    for r,row in enumerate(grid):
        if r == 0 or r == len(grid) - 1:
            continue
        for c,ch in enumerate(row):
            if c == 0 or c == len(grid[0]) - 1:
                continue
            if not ch == ".":
                continue

            pipes, count = "", 0
            for i in range(r+1,len(grid)):  # Checking downward
                if not (p := grid[i][c]) == ".":
                    pipes += p
            count += (pipes := pipes.replace("|","")).count("-") + pipes.count("FJ") + pipes.count("7L")
            if count % 2 == 0:
                continue
            pipes, count = "", 0
            for i in range(c+1,len(row)):  # Checking rightward
                if not (p := grid[r][i]) == ".":
                    pipes += p
            count += (pipes := pipes.replace("-","")).count("|") + pipes.count("FJ") +pipes.count("L7")
            if count % 2 == 0:
                continue
            contained.add((r,c))  

    return len(contained)

#print(solve("Day 10\Day10_UnitTest3.txt"))
#print(solve("Day 10\Day10_UnitTest4.txt"))
print(solve("Day 10\Day10_Input.txt"))