def find_product(sum):
    for a in range(1, sum):
        for b in range(1, sum - a):
            c = sum - a - b 
            if a**2 + b**2 == c**2:
                return a * b * c
            else:
                pass
            # Keep looking! Don't end here 
    print('No such triplet exists!')

print(find_product(1000))
