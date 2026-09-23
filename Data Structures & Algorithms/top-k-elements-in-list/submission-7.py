import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n]+=1

        heap = []

        for n,f in freq.items():      
            heapq.heappush(heap,(f,n))  
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for h in heap:
            result.append(h[1])
        
        return result
