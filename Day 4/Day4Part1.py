# https://adventofcode.com/2023/day/4

import re

def getTotalScore(fileName):
    file = open(fileName,"r")

    sum = 0;    # Variable to store the sum (target value)
    for line in file:
        sum += getGameDetails(line)
    
    file.close()
    print(sum)

def getGameDetails(text):
    # Store both sets of numbers separately
    winningNums = []
    givenNums = []

    # Remove Game# from string
    i = text.find(":")
    text = text[i+2:]

    # Split string between winning and given #s
    game = text.split(' | ')

    # Record winning and given #s
    pattern = re.compile(r'[\d]+')
    matches = pattern.finditer(game[0])
    for match in matches:
        winningNums.append(match.group())
    matches = pattern.finditer(game[1])
    for match in matches:
        givenNums.append(match.group())

    score = getGameScore(winningNums, givenNums)

    return score

def getGameScore(winning, given):
    matches = 0

    for x in given:
        for y in winning:
            if x == y:
                matches += 1

    if matches > 1:
        return pow(2, matches-1)
    else:
        return matches

#getTotalScore("Day 4\Day4_UnitTest.txt")
getTotalScore("Day 4\Day4_Input.txt")