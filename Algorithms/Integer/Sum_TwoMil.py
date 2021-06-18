import math
def primeNumbers(n):
    A = range(2, n + 1)
    B, C = [], A
    while C[0] <  math.sqrt(n):
        firstElement = C[0]
        B += [firstElement]
        C = [x for x in C if x % firstElement != 0]
    return B + C

_sum = sum(primeNumbers(2000000)) # Sum the prime numbers 
print(_sum)
