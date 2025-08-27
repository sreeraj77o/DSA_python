num = [1,2,3,4,4,5,6,9]

def rotate(num,k):
    n=len(num)
    
    if n == 0:
        return num

    k%=n
    i = 0
    while i<k:
        last = num[-1]
        j = n - 1
        while j>0:
            num[j] = num[j-1]
            j-=1
        
        num[0] = last
        i+=1
    return num

rotate(num,5)
print(num)
    


