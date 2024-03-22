s = "   fly me   to   the moon  "
def lengthOfLastWord(s):
    s=s.split(" ")
    for i in range(len(s) - 1, -1, -1):  
        if len(s[i]) != 0:  
            return len(s[i]) 
    
print(lengthOfLastWord(s))
