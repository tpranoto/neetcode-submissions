class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rep_count = {}
        max_freq = 0
        result = 0
        l,r = 0,0

        while r < len(s):
            if s[r] not in rep_count:
                rep_count[s[r]] = 1
            else:
                rep_count[s[r]] +=1

            max_freq = max(max_freq,rep_count[s[r]])
                    
            while ((r-l+1)-max_freq)>k:
                rep_count[s[l]]-=1
                l+=1
            result = max(result,(r-l+1))
            r+=1

        return result


