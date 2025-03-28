class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()  
        if len(pattern)!= len(words):
            return False   
        dictionary = {}
        for i in range(len(pattern)):
            char = pattern[i]  
            word = words[i]
            if char in dictionary:
                if dictionary[char]!=word:
                    return False
            else:
                if word in dictionary.values():
                    return False
            dictionary[char] = word
        return True
    
ex = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(ex.wordPattern(pattern, s))



        