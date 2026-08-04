class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_s = 9999
        for s in strs:
            min_s = min(min_s,len(s))
        
        i = 0
        while i <=min_s:
            count = 0
            for s in strs:
                if strs[0][:i] == s[:i]:
                    count+=1
                else:
                    break
            
            if count != len(strs):
                break
            i+=1
        
        return strs[0][:i-1]
