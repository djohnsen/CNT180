#Assignment: Problem Statement:
# 1. Write an if-else statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56.
#    If the speed variable’s value is outside this range, display 'Speed is abnormal'.
print("Enter a value for speed:")
speed = float(input())
if 24 <= speed <= 56: print("Speed is normal")
else: print("Speed is abnormal")

# 2. Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display
#    the number of calories burned after 10, 15, 20, 25, and 30 minutes.
#
calBurnRate = 4.2
for i in [10,15,20,25,30]:
    print("The treadmill time is", i, "minutes and", i * calBurnRate, "calories have been burned.")
    pass
