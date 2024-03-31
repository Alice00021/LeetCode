class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return self.myPow(x, n - 1) * x
        else:
            b = self.myPow(x, n / 2)
            return b * b
    
sol=Solution()
print(sol.myPow(7,-5))