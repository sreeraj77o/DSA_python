n=153
num = n
result = 0
while num>0:
    last_digit = num%10
    nod = len(str(n))
    result += last_digit**nod
    num= num//10

if result == n:
    print(f"{n} is a armstrong")
else:
        print(f"{n} is not a armstrong")

