def merge(nums1, m, nums2, n):
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()
    return nums1
print(merge([1,2,3,0,0,0],3, [2,5,6], 3))