class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ana1=[0 for _ in range(26)]
        ana2=[0 for _ in range(26)]

        for i in range(len(s)):
            ana1[ord(s[i])-ord('a')]+=1
            ana2[ord(t[i])-ord('a')]+=1

        return ana1 == ana2
        