class Solution(object):
    def clearStars(self, s):
        result = []
        for i in range(len(s)):
            if s[i] == "*":
                min_char = min(result)
                result.remove(min_char)
            else:
                result.append(s[i])
        return ''.join(result)
    
    def clearStarsResult(self, s):
        result = []
        for char in s:
            if char == "*":
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)
    
ex = Solution()
print(ex.clearStars("bca*de*fg*h*"))
print(ex.clearStars("aaba*")) 

print(ex.clearStarsResult("bca*de*fg*h*"))
print(ex.clearStarsResult("de*"))        

        