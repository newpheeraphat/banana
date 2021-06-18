import math
import time
from functools import reduce

def native_str_search(num_list, length):
    num_list_length = len(num_list)
    product_max = 1
    for k in range(num_list_length - length + 1):
        product = 1
        for i in range(length):
            product *= int(num_list[k+i])
        if product > product_max:
            product_max = product
    return product_max

def prod(list):
    return reduce(lambda x, y: int(x) * int(y), list)

def improved_str_search(num_list, length):
    num_length = len(num_list)
    product_max = 0
    break_points = [0]
    # Find all the zeroes in the list that
    for i in range(num_length):
        if num_list[i] == 0:
            break_points.append(i)
    # Iterate over all the intervals between the zeroes
    for i in range(len(break_points)):
        if i == 0:
            start = 0
            stop = break_points[1]
        elif i == len(break_points) -1 :
            start = break_points[-1]
            stop = num_length
        else:
            start = break_points[i] + 1
            stop = break_points[i+1]
        if stop - start >= length:
            interval = num_list[start: stop]
            product = substring_search(interval, length)
            product_max = max(product, product_max)
    return product_max

def substring_search(num_list_sub, length):
    combo = True
    product_max = 1
    for i in range(length-1, len(num_list_sub)):
        # If we are at the start, the end, or have just found
        # A lower value we calculate the whole product
        if i == length-1 or i == len(num_list_sub):
            product = prod(num_list_sub[i-length+1:i+1])
            product_max = max(product, product_max)
        # If the next element is greater than the first element
        # then product is larger is larger, Calculate the new product
        elif num_list_sub[i] > num_list_sub[i-length]:
            if combo:
                product *= float(num_list_sub[i])/max(num_list_sub[i-length],1)
            else:
                product = prod(num_list_sub[i-length+1:i+1])
            product_max = max(product, product_max)
            combo = True
        else:
            combo = False
        # If the next element uis not greater than the first element
        # Set combo t zero and calculate the whole product in the next loop
    return int(product_max)

if __name__ == "__main__":

    n = ("73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450")

    num_list = [int(i) for i in n]
    print(improved_str_search(num_list, 13))
    print(native_str_search(num_list, 13))
