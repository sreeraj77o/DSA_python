arr = [1,2,3,4,5,5,6,2,2]

def remove_element(arr,val):
    write = 0
    i = 0
    while i<len(arr):
        if arr[i]!=val:
            arr[write] = arr[i]
            write +=1
        i+=1
    return arr[:write]

print(remove_element(arr,2))