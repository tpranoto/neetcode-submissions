class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            count=0
            j = i+1
            while j < len(temperatures):
                count+=1
                if temp < temperatures[j]:
                    break
                j+=1
            
            if j < len(temperatures):
                result[i]=count

        return result
                