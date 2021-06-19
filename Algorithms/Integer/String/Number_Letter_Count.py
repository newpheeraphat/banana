# TODO: Number Letter Counts
""" If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. """

#! Code
from timeit import default_timer

def under_thousands_to_string(n):
    digits_as_string = {
                        0: '',
                        1: 'one',
                        2: 'two',
                        3: 'three',
                        4: 'four',
                        5: 'five',
                        6: 'six',
                        7: 'seven',
                        8: 'eight',
                        9: 'nine',
                        10: 'ten',
                        11: 'eleven',
                        12: 'twelve',
                        13: 'thirteen',
                        14: 'fourteen',
                        15: 'fifteen',
                        16: 'sixteen',
                        17: 'seventeen',
                        18: 'eighteen',
                        19: 'nineteen',
                        20: 'twenty',
                        30: 'thirty',
                        40: 'forty',
                        50: 'fifty',
                        60: 'sixty',
                        70: 'seventy',
                        80: 'eighty',
                        90: 'ninety',
                    }
    as_string = '' 
    # "one thousand" should be the only n>= 1000, se we only consider that 
    if n >= 1000:
        as_string += digits_as_string[n // 1000]
        as_string += " thousand "
        return as_string
    
    # [Number] hundred (and) ___ ** only consider "and" if not a multiple of 100 
    # hundred digit = ((n//10)%10) * 10

    if n >= 100:
        as_string += digits_as_string[n // 100]
        as_string += " hundred "
        n %= 100
        if n != 0: 
            as_string += 'and'
        
    # [Number] hundred and ___ty___
    if n > 20:
        as_string += digits_as_string[n - n % 10]
        as_string += ' '
        as_string += digits_as_string[n % 10]
    
    # [Number] hundred and [<20, one, two, ..., nineteen]
    elif (n % 100) <= 20:
        as_string += digits_as_string[n]
    return as_string

def problem_17():
    # Print Problem Context
    print("Project Euler Problem 17 -- Number Letter Count")

    # Set up variable
    start_time = default_timer()
    totalString = ''

    # Computation Loop -- Retrieve all Number as Strings
    for x in range(1000 + 1):
        totalString += under_thousands_to_string(x)

    # Computation Result (remove spaces and determine length of total String)
    totalString = totalString.replace(' ', '')
    result = len(totalString)

    # Compute Execution Time
    end_time = default_timer()
    execution_time = ( end_time - start_time ) * 1000 

    # Display Results
    print(" Total Characters Used: %d" % result)
    print(" Computation Time: %.3f" % execution_time)
    return

if __name__ == '__main__':
    problem_17()
#! Answer is 21124
