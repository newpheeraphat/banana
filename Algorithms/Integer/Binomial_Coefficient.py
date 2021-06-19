# Binomial coefficient
def nck(n, k):
    from math import factorial
    # Function which will return the binomial coefficient
    # of n, k 
    return factorial(n)/ (factorial(k) * factorial(n-k))

print('Number of lattice path is : ' + str(nck(20 + 20, 20)))
