def findMaxLength(nums):
    count=0
    i=0
    while i < len(nums) - 1:
        if (nums[i] == 1 and nums[i + 1] == 0) or (nums[i] == 0 and nums[i + 1] == 1):
            count += 2
            i += 2  
        else:
            i += 1
    return count
            

print(findMaxLength([0,0,0,1,1,1,0]))
  