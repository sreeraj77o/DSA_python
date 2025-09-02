arr = [2, 5, 8, 12, 16, 23]

def binarysearch(arr,target):
    low = 0 
    high = len(arr)-1
    while low <=high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
print(binarysearch(arr,12))
