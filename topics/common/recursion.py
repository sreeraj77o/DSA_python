def func(x,n):
    if n==0:
        return 1
    else:
        print(x,end = ", " if n>1 else " \n")
        func(x,n-1)
func(2,5)


# other method
def func2(x,n):
    if x>n:
        return 1
    else:
        print(x,end = ", " if n>x else "\n")
        func2(x+1,n)
func2(1,9)