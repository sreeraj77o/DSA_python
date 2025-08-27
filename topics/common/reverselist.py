num = [1,2,3,4,4,5,6,6,7,8,9,]

def reverselist(num):
    left = 0
    right = len(num)-1
    while left <=right:
        temp = num[left]
        num[left] = num[right]
        num[right] = temp

        left +=1
        right -=1
reverselist(num)
print(num)
