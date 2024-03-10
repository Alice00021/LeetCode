import numpy as np
from typing import List

def sumOfUnique(nums):
    result = np.zeros(101)
    unique_sum=0
    i=0
    for i in range(len(nums)):
        result[nums[i]]+=1
    for i in range(len(result)):
        if result[i]==1:
            unique_sum+=i
    return unique_sum

print(sumOfUnique([1,1,1,1,1]))
    
    
