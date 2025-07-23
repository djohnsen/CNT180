#Assignment: Problem Statement:
# 1. Write an if-else statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56.
#    If the speed variable’s value is outside this range, display 'Speed is abnormal'.
print("Enter a value for speed:")
speed = float(input())
if 24 <= speed <= 56: print("Speed is normal")
else: print("Speed is abnormal")

# as a case statement because that came to mind
match speed:
    case num if 24 <= speed <= 56:  #Really didn't save much but maybe this lays out better in some use cases
        print("Speed is normal")
    case _:
        print("Speed is abnormal")


# some extended possibilities that came up when searching for how to use the (fairly new to Python) case construction
# (I have programmed in other languages, recently Ruby, where that was an available branching construct.

# Construct #1
#
# We define an associative array (hash) with keys of (a number range) and values (a or b)
# We remap as a number the 'rng' value, walk the items in the 'cases' hash for each num in 'rng'
# bit fuzzy on that part
#
# cases = {range(1, 21): 'a',
#          range(21, 31): 'b'
#         }
# switch = {num: value for rng, value in cases.items() for num in rng}


# Construct #2
#
# I appreciate that we are defining a new object with the class statement, of type dict (thing to learn about)
# I think that the deal is that it executes an inbuilt function across its own data structure (the hash) when addressed for a key
# The inbuilt function is performing the correct de-referencing of the range we're trying to get into, and returning the value
# stored at that hash key (or an error if out of range)
# I am a little unclear on how the hash is being correctly addressed and assigned in this operation
#
# #
# class Switch(dict):
#     def __getitem__(self, item):
#         for key in self.keys():                 # iterate over the intervals
#             if item in key:                     # if the argument is in that interval
#                 return super().__getitem__(key) # return its associated value
#         raise KeyError(item)                    # if not in any interval, raise KeyError
#
# switch = Switch({
#     range(1, 21): 'a',
#     range(21, 31): 'b'
# })




# 2. Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display
#    the number of calories burned after 10, 15, 20, 25, and 30 minutes.
#
calBurnRate = 4.2
for minute in [10,15,20,25,30]:
    print("The treadmill time is", minute, "minutes and", minute * calBurnRate, "calories have been burned.")
    pass
