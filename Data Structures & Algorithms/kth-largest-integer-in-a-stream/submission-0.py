import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        
        for n in nums:
            heapq.heappush(self.data,n)
            if len(self.data) > k:
                heapq.heappop(self.data)

    def add(self, val: int) -> int:
        heapq.heappush(self.data,val)
        if len(self.data) > self.k:
            heapq.heappop(self.data)
        
        return self.data[0]
        
