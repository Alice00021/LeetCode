def productExceptSelf(nums:list):
    for i in range(len(nums)-1):
        n = len(nums)
        prefix = 1
        postfix = 1
        output = [1] * n
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

print(productExceptSelf([3,8, 12, 7]))