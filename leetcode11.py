def groupAnagrams(strs):
    result={}
    if strs is None:
        return ""
    if len(strs)==1 and len(strs[0])==1:
        return strs[0]
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]
    return list(result.values())
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))