import math

def min_sub_array(arr,s):
    min_length = math.inf
    window_sum = 0 
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum>=s:
            min_length = min(min_length,window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start +=1

    if min_length ==math.inf:
        return 0 

    return min_length
arr = [2, 1, 5, 2, 3, 2]
s = 7
print(f"Length of the smallest subarray with sum >= {s} is: {min_sub_array(arr, s)}")