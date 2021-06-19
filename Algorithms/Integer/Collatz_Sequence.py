# TODO: Longest Collatz sequence
""" The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million. """

#! Code
# Longest Collatz Sequence under a million
# Function listing collatz sequence for a number

#* Approach 1 (Out of memory)
def collatz(n):
    " Function listing collatz sequence for a positive number"
    coll = [] 
    coll.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2           # Even Number
            coll.append(n)
        else:
            n = (n * 3) + 1   # Odd Number
            coll.append(n)
    return coll

longest = 0 
j = 0 
for i in range(1, 1000000):
    lencoll = len(collatz(i))
    if lencoll > longest:
        longest = lencoll
        j = i
print(j)
#! Answer is 837799
