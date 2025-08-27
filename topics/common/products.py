num=[1,4,5,7,8,9]

def products(num):
    total = 1
    i = 0
    while i<len(num):
        total *= num[i]
        i +=1
    return total

print(products(num))