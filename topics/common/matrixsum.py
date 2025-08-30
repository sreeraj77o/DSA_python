def matrixsum(a,b):
    rows = len(a)
    cols = len(b[0])
    res = []
    i= 0
    while i<rows:
        row = []
        j = 0
        while j<cols:
            row.append(a[i][j] + b[i][j])
            j+=1
        res.append(row)
        i+=1
    return res

print(matrixsum([[1,2],[2,3]], [[3,4],[4,5]]))