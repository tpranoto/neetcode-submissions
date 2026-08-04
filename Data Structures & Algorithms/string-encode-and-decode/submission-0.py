class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) +"#"+ s
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        i = 0
        result = []

        while i<len(s):
            l_str = ""
            while s[i] != "#" and s[i].isdigit():
                l_str += s[i]
                i+=1

            l = int(l_str)
            i+=1

            result.append(s[i:i+l])
            i+=l

        print(result)

        return result