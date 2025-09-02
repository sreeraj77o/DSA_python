def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = []
    i = 0
    while i<cols:
        row = []
        j = 0
        while j<rows:
            row.append(mat[j][i])
            j +=1
        res.append(row)
        i +=1
    return res
print(transpose([[1,2,3],[4,5,6]]))