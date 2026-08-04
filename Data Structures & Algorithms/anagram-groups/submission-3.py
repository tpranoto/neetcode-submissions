from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)

        for s in strs:
            letter_counts = [0 for i in range (26)]

            for c in s:
                letter_counts[ord(c)-ord('a')] +=1

            result_map[tuple(letter_counts)].append(s)
        
        result = []
        for _,values in result_map.items():
            result.append(values)

        return result


        
        
        
        
        
        # anagramMap = defaultdict(list)

        # for s in strs:
        #     letters = [0] * 26

        #     for c in s:
        #         c_idx = ord(c) - ord('a')
        #         letters[c_idx] +=1
            
        #     anagramMap[tuple(letters)].append(s)
        
        # result = []
        # for _,val in anagramMap.items():
        #     result.append(val)

        # return result















        # group = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     group[tuple(count].append(s)
        
        # result = []
        # for value in group.values():
        #     result.append(value)

        # return result
