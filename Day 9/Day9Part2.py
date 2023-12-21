# https://adventofcode.com/2023/day/9

# Solution improved with help from the solutions subreddit megathread:
#       https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kcguu6a/

import math, re

def solve(fileName):
    sum = 0

    file = open(fileName,"r").read().strip().split('\n')
    list = [n for n in [re.findall(r'-?\d+', s) for s in file]]
    for s in list:
        sum += predictSequence([int(n) for n in s][::-1])   # Reverse sequence
    return sum

def predictSequence(seq):
    sum = 0
    while not all(s == 0 for s in seq):
        sum += seq[-1]
        newSeq = []
        for i in range(1,len(seq)):
            newSeq.append(seq[i]-seq[i-1])
        seq = newSeq
    return sum

#print(solve("Day 9\Day9_UnitTest.txt"))
print(solve("Day 9\Day9_Input.txt"))