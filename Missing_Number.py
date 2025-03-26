class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n+1):
            if i in nums:
                continue
            else:
                return i
        return -1
    
nums = [0,1]
ex = Solution()
print(ex.missingNumber(nums))