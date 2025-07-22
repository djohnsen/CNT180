# Assignment: Problem Statement:  "Miles Per Gallon program".
# In the console, the user enters two values: the number of miles that were driven and the gallons of gas that were used.
# Then, the program calculates and displays the miles per gallon.
print("This program calculates the miles driven per gallon - provide miles driven and gallons consumed.")
print("")
print("Enter miles driven")
miles = float(input())
print("Enter gallons consumed")
gallons = float(input())
mpg = miles / gallons
print("The miles per gallon is: ", mpg)