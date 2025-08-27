num = [1,2,3,4,5,6,8,6,3,5]
even = []
odd = []
def evenodd(num):
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return 

evenodd(num)
print(f"even:{even},odd:{odd}")

