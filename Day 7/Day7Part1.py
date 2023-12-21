# https://adventofcode.com/2023/day/7

# Solution improved with help from code by fugelede on Github:
#       https://github.com/fuglede/adventofcode/blob/master/2023/day07/solutions.py

import re
from collections import Counter

def solve(fileName):
    sum = 0

    # Read input from text file
    file = open(fileName,"r")
    text = file.read().strip().split("\n")  # Read in data and split it by line
    text = [line.split() for line in text]  # Seperate hand of cards and bid
    file.close()

    rankings = sorted((scoreHand(hand),*map("23456789TJQKA".index, hand),int(bid)) for hand,bid in text)
    
    for rank, (*_,bid) in enumerate(rankings,1):    # "1" changed start index of enumerate to 1
        sum += bid*rank
    print(sum)

# Input (held): Int - racetime spent holding the button down
# Output: Int - score of hand by type
def scoreHand(cards):    
    # Create a list of unique cards and their # of instances
    c = Counter(cards)
    counts = sorted(c.values())

    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1

#solve("Day 7\Day7_UnitTest.txt")
solve("Day 7\Day7_Input.txt")
#solve("Day 7\Tester.txt")  # https://www.reddit.com/r/adventofcode/comments/18cq5j3/2023_day_7_part_1_two_hints_for_anyone_stuck/