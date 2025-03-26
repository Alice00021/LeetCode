class Solution(object):
    def moveZeroes(self, nums):
        if all(x == 0 for x in nums):
            return nums
        j =0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for k in range((len(nums)-j),0, -1):
            nums[len(nums)-k]= 0
        return nums
    
ex = Solution()
print(ex.moveZeroes([0, 1, 0, 3, 12]))
        