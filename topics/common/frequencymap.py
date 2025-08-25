nums = [1,2,3,3,2,4,6,8,0,9,6,7,9]

fm= dict()
for i in range(0,len(nums)):
    if nums[i] in fm:
        fm[nums[i]]+=1
    else:
        fm[nums[i]]=1

print(fm)


# alternative method


hashmap= dict()
n= len(nums)
for i in range(0,n):
    hashmap[nums[i]] = hashmap.get(nums[i],0)+1

for key, value in hashmap.items():
    print(f"{key}: {value}")