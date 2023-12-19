# https://adventofcode.com/2023/day/4

import re

def getTotalScore(fileName):
    file = open(fileName,"r")
    futureCopies = []
    
    sum = 0;    # Variable to store the sum (target value)
    for line in file:
        currentCopies = 1
        for i in reversed(range(len(futureCopies))):
            currentCopies += futureCopies[i][0]
            del(futureCopies[i][0])
            if len(futureCopies[i]) == 0:
                del(futureCopies[i])
        futureCopies = getGameDetails(line, futureCopies, currentCopies)
        sum += currentCopies
        #print("Copies of Current Card:",currentCopies)
    
    file.close()
    print("Sum:",sum)

def getGameDetails(text, copies, cards):
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

    newCopies = []
    for i in range(1,score+1):
        newCopies.append(cards)

    if len(newCopies) != 0:
        copies.append(newCopies)
    #print(copies)
    return copies

def getGameScore(winning, given):
    matches = 0

    for x in given:
        for y in winning:
            if x == y:
                matches += 1

    return matches

#getTotalScore("Day 4\Day4_UnitTest.txt")
getTotalScore("Day 4\Day4_Input.txt")