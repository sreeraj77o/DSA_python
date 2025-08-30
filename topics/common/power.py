def power(x,n):
    result = 1
    i = 0
    while i<n:
        result *=x
        i +=1
    return result
print(power(2,6))