from typing import List
def twoSum( nums: List, target):
        i=0; j=1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
print(twoSum([2,7,11,15], 9))

def maximumProduct(nums: List):
    nums.sort()
    max_1, max_2, max_3 = nums[-1], nums[-2], nums[-3]
    min_1, min_2 = nums[0], nums[1]
    
    if min_1 < 0 and min_2 < 0:
        return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)
    else:
        return max_1 * max_2 * max_3
    

print(maximumProduct([-100,-98,-1,2,3,4]))
        
        
        
