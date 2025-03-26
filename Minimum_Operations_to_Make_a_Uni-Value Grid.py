class Solution(object):
    def minOperations(self, grid, x):
        vec = [item for sublist in grid for item in sublist]
        vec.sort()
        print(vec)
        n = len(vec)
        median = vec[n // 2]
        print(median)
        num_of_oper = 0
        for number in vec:
            if (number- median) % x!=0:
                return -1
            else:
                num_of_oper+=abs((number-median)/x)
        return num_of_oper
    
grid = [[2,4],[6,8]]
x = 2
ex = Solution()
print(ex.minOperations(grid, x))



        