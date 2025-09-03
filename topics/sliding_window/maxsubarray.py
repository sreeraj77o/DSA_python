def max_sub_array(arr,k):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k-1:
            max_sum = max(max_sum,window_sum)
            window_sum -= arr[window_start]
            window_start +=1
        
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Maximum sum of a subarray of size {k} is: {max_sub_array(arr, k)}")
    