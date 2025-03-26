digits = [1,2,9]
str_digits = map(str, digits)
result = "" .join(str_digits)
print(result)
print(int(result)+1)

class Solution(object):
    def plusOne(self, digits):
        digits = list(map(int, str(int("".join(map(str, [1, 2, 9]))) + 1)))
        return digits

ex = Solution()
digits = [1,2,3]
print(ex.plusOne(digits))