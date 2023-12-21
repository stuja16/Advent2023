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
    print(text)
    file.close()

    # Sort hands into their rankings based on their strength
    rankings = sorted((scoreHand(hand),*map("J23456789TQKA".index, hand),int(bid)) for hand,bid in text)
    
    # Use rankings to calculate the score
    for rank, (*hand,bid) in enumerate(rankings,1):    # "1" changed start index of enumerate to 1
        sum += bid*rank
    print(sum)

# Input (cards): String - Cards in the current hand
# Output: Int - score of hand by type
def scoreHand(cards):  
    # Create a list of unique cards and their # of instances
    c = Counter(cards)
    counts = [0] if (jokers := c.pop("J", 0)) == 5 else sorted(c.values())
        # pop(key to search for, default value if match not found)
    # Add the jokers to the card that appears the most already
    counts[-1] += jokers

    # Match count to the type of hand
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case 2, 3:
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