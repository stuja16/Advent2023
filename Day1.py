# Solves Day 1 by opening/reading file and calling the needed functions to find the sum of all callibration values
def getTotal():
    file = open("Day1_Input.txt","r")
    sum = 0;    # Variable to store the sum (target value)
    for each in file:
        cv = getCallibrationValue(each)
        sum += cv
    print("Sum of all Callibration Values:", sum)   # Print sum to the console
    file.close()

# Get the calibration value for a single token/string
def getCallibrationValue(token):
    return int(getLeadingDigit(token) + getLeadingDigit(token[::-1]))

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