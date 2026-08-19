import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n]+=1
        
        heap = []
        for n, freq in freq.items():
            heapq.heappush(heap, (freq,n))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for freq,n in heap:
            result.append(n)
        
        return result