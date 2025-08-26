def factorial(n):
    if n==0:
        return 1
    else:
        result = n * factorial(n-1)
        print(f"factorial({n}) = {result}")
        return result
        
print(factorial(5))