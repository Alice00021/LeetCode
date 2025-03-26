class Solution(object):
    def searchRange(self, nums, target):
        if not nums:  
            return [-1, -1]
    
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right if right >= 0 and nums[right] == target else -1
        
        left = findLeft(nums, target)
        if left == -1:  
            return [-1, -1]
        right = findRight(nums, target)
        
        return [left, right]