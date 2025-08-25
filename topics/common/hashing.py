m = [1,2,3,4,7,7,6,7,6,8,9,3,2]
n = [2,4,5,6,7,8,1,3,9]

for num in set(m):
    count = 0
    for x in n:
        if x==num:
            count +=1
        
    count = m.count(num)
    print(f"{num}:{count}")



# optimized code

# hashmap1 = dict()
# x = len(m)
# y = len(n)

# for i in range(0,x):
#     hashmap1[m[i]]= hashmap1.get(m[i],0)+1

# for i in range(0,y):
#     hashmap1[n[i]]=hashmap1.get(n[i],0)+1

# print(hashmap1)

hashmap1 = dict()

for num in m:
    hashmap1[num]= hashmap1.get(num,0)+1

for num in n:
    hashmap1[num]=hashmap1.get(num,0)+1

print(hashmap1)



# alternative approach
hashmap2 = dict()

for num in m:
    hashmap2[num] = hashmap2.get(num, 0) + 1

# For each element in n, increment count if it exists in hashmap
for num in n:
    if num in hashmap2:
        hashmap2[num] += 1

print(hashmap2)