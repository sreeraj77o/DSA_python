arr = [1,2,4,5,6]
def missing(arr,n):
    total = 0
    i = 1
    while i<=n:
        total +=i
        i +=1
    i = 0

    while i<len(arr):
        total -= arr[i]
        i+=1
    return total

print(missing(arr,6))