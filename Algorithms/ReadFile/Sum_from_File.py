from numpy import *
filename = 'eulur13.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
    print(array)

newArray = []
for i in array:
    newArray.append(int(i))   
print(newArray)

"""
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
print(newArray) """

data_array = sum(newArray)
print(str(data_array)[:10])
