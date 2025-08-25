from math import sqrt

nums=[20,30,40,45]

for num in nums:
    result=[]
    for i in range(1,num//2 + 1):
        if num % i ==0:
            result.append(i)
    result.append(num)
    print(result)


# alternative method for better  time complexity

for num in nums:
    result=[]
    for i in range(1,int(sqrt(num)+1)):
        if num %i ==0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
        result.sort()
        print(result)