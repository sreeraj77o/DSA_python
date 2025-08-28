a = [1,2,2,3,5]
b = [2,5,4]

def intersection(a,b):
    seen = {}
    i = 0

    while i<len(b):
        seen[b[i]] = True
        i+=1
    res = []
    i=0
    used = {}
    while i<len(a):
        if a[i] in seen and a[i] not in used:
            res.append(a[i])
            used[a[i]] = True
        i+=1
    return res

print(f"the intersection of each list is: ",intersection(a,b))