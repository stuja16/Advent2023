# https://adventofcode.com/2023/day/6

import re

def getWinProduct(fileName):
    times = []
    records = []
    wins = 0

    # Read input from text file
    file = open(fileName,"r")
    timeText = file.readline().replace(" ", "")
    distText = file.readline().replace(" ", "")
    file.close()

    # Search for and log race times and distance records
    pattern = re.compile(r'[\d]+')
    matches = pattern.finditer(timeText)
    for match in matches:
        times.append(int(match.group()))
    matches = pattern.finditer(distText)
    for match in matches:
        records.append(int(match.group()))
    
    # Check each possible length of time for holding down the button
    for i in range(len(times)):
        current = getWinNumbers(times[i],records[i])
        if wins == 0:
            wins = current
        else:
            wins *= current
    
    # Find product of winning options for each race
    print(wins)

# Input (time): Int - total available time to complete the race
# Input (record): Int - previous distance record
# Output: Int - # of distinct time lengths you can hold the button and still win
def getWinNumbers(time, record):
    max = int(time/2) + 1   # Resulting vector is reflexive, so we can halve the cases to check
    wins = 0
    for i in range(1,max):
        if getRaceResults(i,time) > record:
            wins += max - i
            break
    if time % 2 == 0:
        return wins*2 - 1
    return wins*2

# Input (held): Int - racetime spent holding the button down
# Input (total): Int - total available time to complete the race
# Output: Int - total distance travelled during the racetime
def getRaceResults(held, total):
    return (total-held)*held

#getWinProduct("Day 6\Day6_UnitTest.txt")
getWinProduct("Day 6\Day6_Input.txt")