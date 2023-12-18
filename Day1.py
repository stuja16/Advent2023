digitTexts = {("zero", "0"), ("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")}

# Solves Day 1 by opening/reading file and calling the needed functions to find the sum of all callibration values
def getTotal():
    file = open("Day1_Input.txt","r")
    sum = 0;    # Variable to store the sum (target value)
    for each in file:
        cv = getCallibrationValue(each.lower())
        sum += cv
    print("Sum of all Callibration Values:", sum)   # Print sum to the console
    file.close()

# Get the calibration value for a single token/string
def getCallibrationValue(token):
    forward = textToDigit(token)
    backward = forward[::-1]
    return int(getLeadingDigit(forward) + getLeadingDigit(backward))

# Runs through the input one way to add digits before the last char in written numbers
def textToDigit(text):
    modified = True    # Keeps track of whether a numeric digit has been added this round
    while modified:
        modified = False
        # Look for each number
        for num in digitTexts:
            if num[0] in text:
                i = text.find(num[0])
                text = text[:i + len(num[0]) - 1] + num[1] + text[i + len(num[0]) - 1:]
                modified = True
    return text

# Function to analyze the string
def getLeadingDigit(text):
    # Iterate through the input string
    for c in text:
        # Test the character against all possible digits
        for x in range(10):
            if ord(c) - 48 == x:
                # Return the first digit in the string as a char datatype
                return c

getTotal()