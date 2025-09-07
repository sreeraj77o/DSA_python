def sumsorted(arr):
    n =len(arr)
    left = 0
    right = n - 1
    result = [0] * n
    result_pointer = n - 1
    # arr.sort()

    while left <= right:
        left_val_sq = arr[left] * arr[left]
        right_val_sq = arr[right] * arr[right]

        if left_val_sq > right_val_sq:
            result[result_pointer] = left_val_sq
            left +=1
        else:
            result[result_pointer] = right_val_sq
            right -= 1
        result_pointer -=1
    return result
arr = [-3,-1,3,2,0]
print(sumsorted(arr))