""" given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]. """
def jump(nums):
    result=0
    if nums[0]==0:
        return result
    if nums[0]==1:
        return len(nums)-1
    for i in range(len(nums)):
        j=nums[0]
        if 0<=j<=len(nums) and i+j<len(nums):
            i=j; result+=1 
    return result
        
print(jump([2,3,1,1,4]))