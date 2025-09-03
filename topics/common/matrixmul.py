def matrix_mul(a,b):
    r1 = len(a)
    r2 = len(a[0])
    c1 = len(b)
    c2 = len(b[0])
    if r1 != c1:
        return 0 
    res = []
    i = 0
    while i<r1:
        j = 0
        row = []
        while j<c2:
            k = 0
            s = 0
            while k<c1:
                s += a[i][k] * b[k][j]
                k +=1
            row.append(s)
            j+=1
        res.append(row)
        i+=1
    return res
print(matrix_mul([[1,2],[3,4]], [[5,6],[7,8]]))