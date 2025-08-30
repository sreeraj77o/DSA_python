def count(n):
    if n ==0:
        return 0
    if n < 0 :
        n = -n
    count = 0 
    while n>0:
        n//=10
        count +=1
    return count

print(count(12345))