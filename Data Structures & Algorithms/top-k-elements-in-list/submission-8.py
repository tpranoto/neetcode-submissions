import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n]+=1
            else:
                counts[n]=1

        heap = []
        for key,value in counts.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
            
        result = []
        for val in heap:
            result.append(val[1])
        
        return result