class Solution(object):
    def findDuplicate(self, nums):
        tortoise = nums[0]
        hear = nums[0]
        while True:
            tortoise = nums[tortoise]
            hear = nums[nums[hear]]
            if hear == tortoise:
                break
        pointer = nums[0]
        pointer2 = tortoise
        while pointer!=pointer2:
            pointer = nums[pointer]
            pointer2 = nums[pointer2]
        return pointer

ex = Solution()
print(ex.findDuplicate([1,3,4,2,2]))
        