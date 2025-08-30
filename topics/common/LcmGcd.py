def Lcd(a,b):
    if a ==0 and b==0:
        return 0
    
    def Gcd(x,y):
        while y!=0:
            temp = x % y
            x = y
            y = temp
        return x
    return (a // Gcd(a,b))* b
print(Lcd(4,6))