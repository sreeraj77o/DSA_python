nums = [2,3,5,7,8,4,7,9,0]
def func(nums,left,right):
    if left>=right:
        return 1
    nums[left],nums[right] = nums[right],nums[left]
    func(nums,left+1,right-1)

func(nums,0,8)
print(nums)

