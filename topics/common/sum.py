num = [2,3,4,5,6]

def sum(num):
    total = 0
    i = 0
    while i<len(num):
        total += num[i]
        i += 1
    return total

print(sum(num))

