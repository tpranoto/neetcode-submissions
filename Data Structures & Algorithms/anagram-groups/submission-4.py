class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mappings = {}
        for s in strs:
            key = self.getCharsCounts(s)
            if key not in mappings:
                mappings[key] = []
            mappings[key].append(s)

        result = []
        for values in mappings.values():
            result.append(values)
        
        return result


    def getCharsCounts(self,s):
        anagram = [0 for _ in range(26)]

        for c in s:
            anagram[ord(c)-ord('a')] +=1
        
        return tuple(anagram)