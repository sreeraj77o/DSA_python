num = [1,2,3,4]

def is_sorted(num):
    i = 1 
    while i<len(num):
        if num[i]<num[i-1]:
            return False
        i+=1
    return True

print(is_sorted(num))
