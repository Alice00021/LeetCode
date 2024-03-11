def sortColors(nums):
    numbers=[0, 0 , 0]
    result=[]
    for i in range(len(nums)):
        numbers[nums[i]]+=1
    for j in range(len(numbers)):
        for i in range(numbers[j]):
            result.append(j)
    return result

def sortColors1( nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums
    
print(sortColors1([2,0,2,1,1,0]))