# Problem Statement:  "Finding the Maximum and Minimum Numbers from a List".
#  Write a program to find the maximum number and minimum number from this list.
#  listA= [ 23, 12, 45, 22, 11, 78, 13, 90, 45, 88, 10, -5, -1 ]

listA= [ 23, 12, 45, 22, 11, 78, 13, 90, 45, 88, 10, -5, -1 ]

listMax = 0
listMin = 0

for element in listA :
    if element > listMax :
        listMax = element
    elif element < listMin :
        listMin = element

print("The list maximum is:", listMax,"and the list minimum is:",  listMin)
