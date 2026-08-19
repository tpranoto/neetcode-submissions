class Solution:
    def __init__(self):
        self.sep = "#"

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result+= str(len(s))+self.sep+s
        return result


    def decode(self, s: str) -> List[str]:
        result=[]
        i= 0

        while i < len(s):
            start = i
            while s[i].isdigit() and s[i]!="#":
                i+=1
            s_len=int(s[start:i])
            i+=1
            result.append(s[i:i+s_len])
            i+=s_len
        
        return result
                
