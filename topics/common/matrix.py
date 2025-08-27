num = [[2,3,4],[2,7,8],[9,8,7]]

rows=len(num)
cols=len(num[0])
def matrix(num):
    for i in range(rows):
        for j in range(cols):
            print(num[i][j],end=" ")
        print()
    return
matrix(num)
print()


# 1st question ,print only upper triangle

def uppermatrix(num):
    for i in range(rows):
        for j in range(cols):
            if i<=j:
                print(num[i][j],end=" ")
            else:
                print("*", end = " ")

        print()
uppermatrix(num)
print()

#2nd question, print lower triangle

def lowermatrix(num):
    for i in range(rows):
        for j in range(cols):
            if i>=j:
                print(num[i][j],end=" ")
            else:
                print("*", end = " ")
        print()

lowermatrix(num)
print()

#3rd question,print only diagonal

def diagonal(num):
    for i in range(rows):
        for j in range(cols):
            if i==j:
                print(num[i][j],end=" ")
            else:
                print("*", end = " ")
        print()
diagonal(num)
print()

#4th question,print opposite diagnoal

def opposite_diagonal(num):
    for i in range(rows):
        for j in range(cols):
            if i + j == cols - 1:
                print(num[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

opposite_diagonal(num)
print()