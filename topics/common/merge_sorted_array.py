a = [1,4,5,6]
b = [2,3,8,7]

def merge_sorted_array(a,b):
    i=0
    j=0
    res = []
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    while i<len(a):
        res.append(a[i])
        i+=1
    while j<len(b):
        res.append(b[j])
        j+=1
    return res

print(merge_sorted_array(a,b))