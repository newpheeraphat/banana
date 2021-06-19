def nth_prime(nums):
    counter =2 
    for i in range(3, nums**2, 2):
        j = 1 
        while j*j < i:
            j += 2
            if i % j == 0:
                break
        else:
            counter += 1
        if counter == nums:
            return i 

int1 = int(input())
print(nth_prime(int1))
