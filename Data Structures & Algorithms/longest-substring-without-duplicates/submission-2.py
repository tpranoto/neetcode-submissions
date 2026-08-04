class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        buffer = set()
        l,r = 0,0

        longest = 0
        while r <len(s):
            while s[r] in buffer:
                buffer.remove(s[l])
                l+=1
                
            buffer.add(s[r])
            r += 1
            longest = max(longest,r-l)
            
        return longest

            


