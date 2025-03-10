from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j: 
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i

sol=Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2], 2))