import math
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

sol=Solution()
print(sol.reverse(-123))