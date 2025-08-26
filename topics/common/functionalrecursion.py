def func(sum,i,n):
    if i>n:
        print(f"final sum: {sum}")
        return 1
    print(f"{sum} + {i} = {sum + i}")
    func(sum+i,i+1,n)
func(0,1,5)

#other methods

def func2(n):
    if n==0:
        return 0
    result = n+func2(n-1)    
    print(f"the sum of {n} is {result}")

    return result

func2(20)