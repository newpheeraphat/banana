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

data_array = sum(newArray)
print(str(data_array)[:10])
