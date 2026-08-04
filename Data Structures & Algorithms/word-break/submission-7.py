class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s):True}

        def dfs(idx: int):
            if idx in memo:
                return memo[idx]

            for word in wordDict:
                word_length = len(word)           
                if idx+word_length <= len(s) and s[idx:idx+word_length] == word and dfs(idx+word_length):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False
        
        return dfs(0)
