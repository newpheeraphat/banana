# TODO: Power digit Sum
""" 215 = 32768 and the sum of its digits is 
    3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 21000? """

def Power_digits_sum(n):
    number = list(str(2**n))         # power number and convert number in string and list
    result = [int(i) for i in number]# convert number in int and sum list 
    return sum(result)

print(Power_digits_sum(15)) # Output will be 26
print(Power_digits_sum(1000)) # Output will be 1366
