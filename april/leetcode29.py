class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool: 
        if len(s1) + len(s2) != len(s3):
            return False
        j, k = 0, 0 
        flag=False
        
        for i in len(s3):
            if s3[i]!=s1[i] and s3[i]!=s2[i]:
                return False
            elif (s3[i]==s1[i] or s3[i]==s2[i]) and flag:
                continue
            elif s3[i]==s1[i] and s3[i]==s2[i]:
                flag=True
                
                
        return True
                
sol=Solution()      
sol.isInterleave("aab", "bbc", "bbcbcb")        
            