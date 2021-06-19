int1 = int(input())
count = 0 
for j in range(1, int1 + 1):
    if int1 % j == 0:
        count += 1
if count == 2:
    print("is prime")
else:
    print("is not prime")
