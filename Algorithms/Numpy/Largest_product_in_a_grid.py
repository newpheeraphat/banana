# import numpy module for matrix operations
from numpy import *

# read the file with martrix of numbers
filename = 'euler11.txt'

# store each line of the file into an array 
with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
    print(array)

# create a new array that converts the number strings into number integer
newArray = []
for i in array:
    j = i.split(' ')       # cut the black space out of the array to list
    k = [int(n) for n in j]  # After that, convert j after change it to list. now, list of j is string We need to convert it to number integer
    newArray.append(k)     # append it to array that we have created it 
print(newArray)

# Convert the array of number of interger to matrix of integer 
problemMatrix = matrix(newArray)
print(problemMatrix)

# set initial(เริ่มต้น) maximum product to be a dummy(จำลอง) number, say 1
maxProd = 1

# search all combinations for matrix product
for i in range(16):
    for j in range(16):
        prod1 = problemMatrix[i, j] * problemMatrix[i+1, j] * problemMatrix[i+2, j] *problemMatrix[i+3, j] 
        if prod1 > maxProd:
            maxProd = prod1
        
        prod2 = problemMatrix[i, j] * problemMatrix[i, j+1] * problemMatrix[i, j+2] * problemMatrix[i, j+3]
        if prod2 > maxProd:
            maxProd = prod2
        
        prod3 = problemMatrix[i, j] * problemMatrix[i+1, j+1] * problemMatrix[i+2, j+2] * problemMatrix[i+3, j+3]
        if prod3 > maxProd:
            maxProd = prod3
        
        prod4 = problemMatrix[19-i, j] * problemMatrix[18-i, j+1] * problemMatrix[17-i, j+2] * problemMatrix[16-i, j+3]
        if prod4 > maxProd:
            maxProd = prod4
print(maxProd)
