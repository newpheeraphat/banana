# TODO: Write a Python program to count the number of each character of a given text of a text file.
#! Code
import collections as c 
import pprint 
file_input = input('File Name: ')
with open(file_input, 'r') as info:
    count = c.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)
