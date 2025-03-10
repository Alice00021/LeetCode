from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        return False if length==len(set(nums)) else True

sol=Solution()
print(sol.containsDuplicate([1,2,3]))