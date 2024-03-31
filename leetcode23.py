def longestCommonPrefix(strs):
    prefix=strs[0]
    if "" in strs or strs == []:
        return ""
    for i in range(1,len(strs)):
        while(prefix != ""):
            try:
                if str.index(str(strs[i]),prefix) == 0:
                    break
                else:
                    prefix = prefix[:-1]
            except:
                prefix = prefix[:-1]
    return prefix
        

s = ['flower', 'flow', 'flight']
print(longestCommonPrefix(s))   
    