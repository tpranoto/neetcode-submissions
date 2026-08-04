class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = [0 for i in range(26)]
        t_chars = [0 for i in range(26)]
        
        for i in range (len(s)):
            cur_s = ord(s[i]) - ord('a')
            cur_t = ord(t[i]) - ord('a')
            s_chars[cur_s] +=1
            t_chars[cur_t] +=1
        
        for i in range(len(s_chars)):
            if s_chars[i] != t_chars[i]:
                return False

        return True
        
        
        
        
        
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26
        # for i,c in enumerate(s):
        #     count[ord(c) - ord('a')] +=1
        #     count[ord(t[i]) - ord('a')] -=1
        
        # for c in count:
        #     if c != 0:
        #         return False
        
        # return True


        # return sorted(s) == sorted(t)
        
