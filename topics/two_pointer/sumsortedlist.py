def sum_sorted(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left,right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

arr = [1,4,6,7,8,9,3]
arr.sort()
target = 4
result = sum_sorted(arr,target)
print(f"the target sum is {target} and the result is {result}")