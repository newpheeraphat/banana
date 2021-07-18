def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    _sum = 0
    for i in sorted_arr:
        _sum += i
    
    result_min = _sum - sorted_arr[0]
    result_max = _sum - sorted_arr[len(sorted_arr)-1]
    print(result_max, result_min)
    
