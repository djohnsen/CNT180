# Problem Statement:  "Feet to Inches program".
# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet as an argument
# and returns the number of inches in that many feet.
#
# Use the function in a program that prompts the user to enter a number of feet
# then displays the number of inches in that many feet.
def feet_to_inches(feet):
    inches_per_foot = 12
    inches = feet * inches_per_foot
    return inches

# This time I'll return integer inches and a remainder.
def feet_to_whole_inches(feet):
    inches_per_foot = 12
    inches = feet * inches_per_foot
    remain_inches = inches % inches_per_foot
    int_inches = int(remain_inches)
    dec_inches = remain_inches - int_inches
    fracSixteenth = dec_inches / (1/16)
    answer = int(feet), "feet", int_inches, "and", fracSixteenth, "inches"
    return answer

print("Enter number of feet:")
feet = float(input())
print(feet, "feet converts to", feet_to_whole_inches(feet), ".")


