class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True

        l,r=0,len(s)-1

        while l<=r:
            while l <r and not self.validChar(s[l]):
                l+=1
            while l<r and not self.validChar(s[r]):
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True
        
    
    def validChar(self, c):
        if ord('A')<=ord(c)<=ord('Z'):
            return True
        if ord('a')<=ord(c)<=ord('z'):
            return True
        if ord('0')<=ord(c)<=ord('9'):
            return True
        return False