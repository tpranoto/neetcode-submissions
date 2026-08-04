import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        heap = []
        for i,n in enumerate(nums):
            heapq.heappush(heap,(-n,i))

            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])

        return output
