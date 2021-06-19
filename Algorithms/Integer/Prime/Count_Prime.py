count_prime = 0
i = 1
while count_prime <= 99:
    count = 0 
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
        count_prime += 1
    i = i + 1
